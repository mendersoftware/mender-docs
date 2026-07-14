---
title: Update an ESP32-S3 with a Raspberry Pi
taxonomy:
    category: docs
---

This section walks through a complete System update on **real hardware**, and
shows how Mender Orchestrator can update a Component that **does not run Mender**
at all. A **Raspberry Pi 5** runs Mender Orchestrator as the System Device, and
an **Espressif ESP32-S3-DevKitC** connected to it over USB is a Component that
the Raspberry Pi flashes over serial. By the end, you will deploy a single
Manifest that updates both the Raspberry Pi's root filesystem and the ESP32-S3's
firmware in one coordinated deployment.

## How this differs from the microcontroller Get started

In [Get started &rarr; Microcontroller](../../../01.Get-started/07.Microcontroller-preview/docs.md)
the ESP32-S3 runs the `mender-mcu` client and talks to the Mender Server
**directly** over WiFi. It is its own [micro tier](../../../02.Overview/17.Device-tiers/docs.md)
device.

Here the roles are different:

* The **Raspberry Pi 5** is the only device that talks to the Mender Server. It
  runs the Mender Client and Mender Orchestrator, and uses the
  [system tier](../../../02.Overview/17.Device-tiers/docs.md).
* The **ESP32-S3** is a passive [Component](../../01.Overview/docs.md#components).
  It has no connection to the Mender Server. The Raspberry Pi flashes it over USB
  serial through an [Interface](../../04.Interface-protocol/docs.md).

The two setups are architecturally opposite, so the ESP32-S3 firmware here does
**not** include the `mender-mcu` client. We reuse only the Zephyr development
environment from the microcontroller Get started to build a plain firmware image.

The System we build looks like this:

| Component | `component_type` | Interface | Role |
|-----------|------------------|-----------|------|
| Raspberry Pi 5 | `raspberrypi5` | `rootfs-image` | System Device, runs Orchestrator |
| ESP32-S3 | `esp32s3` | `esp32` | Firmware flashed over USB serial |

## Prerequisites

* A **Raspberry Pi 5** prepared and connected to hosted Mender, following
  [Prepare a Raspberry Pi device](../../../01.Get-started/01.Preparation/01.Prepare-a-Raspberry-Pi-device/docs.md).
  Keep an SSH session to the device open, and note the login user and IP address.
* An **ESP32-S3-DevKitC** board and a USB cable.
* A **Zephyr development environment** on your workstation, set up as in
  [Prepare an ESP32-S3 with Zephyr](../../../01.Get-started/07.Microcontroller-preview/01.Prepare-an-esp32-s3-with-Zephyr/docs.md).
  We reuse the `west` workspace to build firmware, but we do not flash the board
  from the workstation.
* The [mender-artifact](../../../12.Downloads/01.Workstation-tools/docs.md#mender-artifact)
  tool on your workstation.

## Step 1 - Install Mender Orchestrator on the Raspberry Pi

On the Raspberry Pi (over SSH), download and install the
`mender-orchestrator-core` and `mender-orchestrator-support` Debian packages by
following the
[Debian family installation instructions](../../05.Installation/02.Debian-family/docs.md).
Use the **arm64** packages for the Raspberry Pi 5.

Next, tell the Mender Client that this device runs in the system tier. Edit
`/etc/mender/mender.conf` and set the `DeviceTier` option to `system`:

```json
{
  "DeviceTier": "system"
}
```

Restart the Mender Client so the change takes effect:

```bash
sudo systemctl restart mender-updated
```

Confirm the device's built-in device type, which we use later as the
`component_type` of the System Device:

```bash
cat /var/lib/mender/device_type
```

For a Raspberry Pi 5 this reads `device_type=raspberrypi5`.

Accept the device in Mender Server.

## Step 2 - Install the ESP32 Interface on the Raspberry Pi

The `esp32` Interface, which flashes firmware over USB serial with `esptool.py`,
ships in the `mender-orchestrator-demo` package.

Install the demo package on the Raspberry Pi by following the
[Debian family installation instructions](../../05.Installation/02.Debian-family/docs.md#demo-package-optional).
It installs the `esp32` Interface into
`/usr/share/mender-orchestrator/interfaces/v1/`, along with a demo Topology that
we edit in the next step.

!!! The demo package is intended for evaluation and is not appropriate for
!!! production devices. We use it here as a convenient way to obtain the `esp32`
!!! Interface and a starting Topology.

The Interface depends on `esptool.py` and `jq`. Install `jq` from the
distribution, and install `esptool` from PyPI:

```bash
sudo apt-get update
sudo apt-get install -y python3-pip jq
sudo pip3 install --break-system-packages 'esptool<5'
```

!! Install `esptool` from PyPI, **not** from the distribution's `esptool`
!! package. The Debian and Ubuntu package omits the stub flasher data files (for
!! example `stub_flasher_32s3.json`), so flashing fails with
!! `FileNotFoundError: [Errno 2] No such file or directory: '.../stub_flasher_32s3.json'`.
!! The PyPI package includes them. If the `esptool` package is already installed,
!! remove it first with `sudo apt-get remove -y esptool`.

!!! The Interface calls `esptool.py`. Pinning to `esptool<5` keeps that command
!!! name available; esptool 5.x renames it to `esptool`. Confirm the PyPI build
!!! is the one on the `PATH` with `command -v esptool.py` (it should resolve to
!!! `/usr/local/bin/esptool.py`, ahead of `/usr/bin`). If you use esptool 5.x,
!!! create a symlink: `sudo ln -s "$(command -v esptool)" /usr/local/bin/esptool.py`.

Now connect the ESP32-S3 to the Raspberry Pi with a USB cable, using the port
labeled **UART** on the DevKitC. Find the serial device it registers as:

```bash
ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null
```

The UART bridge usually appears as `/dev/ttyUSB0`. The Interface reads a mapping
from instance IDs to serial devices in `/etc/mender-orchestrator/esp32-devices.conf`.
Create it, mapping the instance `esp32-1` to the port you found:

```bash
sudo mkdir -p /etc/mender-orchestrator
echo "esp32-1=/dev/ttyUSB0" | sudo tee /etc/mender-orchestrator/esp32-devices.conf
```

`esp32-1` is the instance ID. It is passed to the Interface through
`interface_args` in the Topology, which is how the Interface knows which physical
board to flash.

## Step 3 - Edit the Topology

The [Topology](../../03.Topology/docs.md) describes the Components of the System.
The demo package installed a sample Topology at
`/data/mender-orchestrator/topology.yaml` describing a mock System: a `gateway`
System Device and two mock `rtos` Components. Replace its contents to describe
our real System instead - a Raspberry Pi 5 System Device and one ESP32-S3
Component:

```bash
sudo tee /data/mender-orchestrator/topology.yaml > /dev/null << 'EOF'
api_version: "mender/v1"
kind: "topology"
system_type: "rpi5-esp32-system"

components:
  - component_type: raspberrypi5
    interface: rootfs-image

  - component_type: esp32s3
    interface: esp32
    interface_args: ["esp32-1"]
EOF
```

Compared to the demo Topology, this sets our own `system_type`, renames the
System Device's `component_type` to match the Raspberry Pi's built-in
`device_type` (`raspberrypi5`), and replaces the two mock `rtos` Components with a
single `esp32s3` Component:

* The **System Device** uses `component_type: raspberrypi5` (matching the
  device's built-in `device_type` from Step 1) and the built-in `rootfs-image`
  Interface.
* The **ESP32-S3** uses `component_type: esp32s3`, the `esp32` Interface, and
  passes `esp32-1` as the instance ID so the Interface resolves the correct
  serial port from `esp32-devices.conf`.

## Step 4 - Build the ESP32-S3 firmware

On your **workstation**, activate the Zephyr environment you set up in the
prerequisites:

```bash
source ~/zephyrproject/.venv/bin/activate
```

The board's only onboard LED is an addressable WS2812 RGB LED driven over I2S, so
we base the firmware on Zephyr's `led_strip` sample. Copy it out of the Zephyr
tree into your `west` workspace so you can edit it. It ships with the devicetree
overlay and configuration for this board, so the LED works out of the box:

```bash
cd ~/mender-mcu-workspace
cp -r zephyr/samples/drivers/led/led_strip esp32-component-fw
```

!! The onboard RGB LED's data pin differs by ESP32-S3-DevKitC-1 hardware
!! revision, and the Zephyr sample overlay's default changed with it (GPIO38 up
!! to Zephyr 4.2, GPIO48 from 4.4). If, after flashing, the LED stays dark
!! **but** the serial console (view it with `west espressif monitor` on your
!! workstation, or `picocom -b 115200 /dev/ttyUSB0` on the Raspberry Pi) reports
!! the strip as `ready` with no update errors, the data is being clocked out to
!! the wrong pin. Edit
!! `esp32-component-fw/boards/esp32s3_devkitc_procpu.overlay` and switch the
!! `pinmux` line between `I2S0_O_SD_GPIO38` and `I2S0_O_SD_GPIO48`, then rebuild.

Replace the sample's `src/main.c` with a minimal application that lights the LED
a solid color. It logs over the serial console and refreshes the LED in a loop,
which makes troubleshooting easy. Open
`~/mender-mcu-workspace/esp32-component-fw/src/main.c` and replace its contents
with:

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/led_strip.h>
#include <zephyr/logging/log.h>

LOG_MODULE_REGISTER(component_fw, LOG_LEVEL_INF);

#define STRIP_NODE       DT_ALIAS(led_strip)
#define STRIP_NUM_PIXELS DT_PROP(DT_ALIAS(led_strip), chain_length)

static const struct device *const strip = DEVICE_DT_GET(STRIP_NODE);
static struct led_rgb pixels[STRIP_NUM_PIXELS];

int main(void)
{
	/* Firmware version 1 lights the LED yellow.
	 * For version 2, set green instead: { .r = 0x00, .g = 0x20, .b = 0x00 }. */
	const struct led_rgb color = { .r = 0x20, .g = 0x20, .b = 0x00 };

	if (!device_is_ready(strip)) {
		LOG_ERR("LED strip %s is not ready", strip->name);
		return 0;
	}
	LOG_INF("LED strip %s ready, %d pixel(s)", strip->name, STRIP_NUM_PIXELS);

	for (size_t i = 0; i < STRIP_NUM_PIXELS; i++) {
		pixels[i] = color;
	}

	while (1) {
		int rc = led_strip_update_rgb(strip, pixels, STRIP_NUM_PIXELS);
		if (rc) {
			LOG_ERR("failed to update strip: %d", rc);
		}
		k_sleep(K_SECONDS(1));
	}
	return 0;
}
```

Build the firmware for the ESP32-S3:

```bash
cd ~/mender-mcu-workspace/esp32-component-fw
west build -p always -b esp32s3_devkitc/esp32s3/procpu .
```

The build produces a directly bootable image at `build/zephyr/zephyr.bin`. Copy
it to a working directory for the next step:

```bash
mkdir -p ~/esp32-orchestrator && cp build/zephyr/zephyr.bin ~/esp32-orchestrator/
cd ~/esp32-orchestrator
```

!!! You do not need to flash from your workstation for the deployment - the
!!! Raspberry Pi flashes the ESP32-S3 as part of the update, so we only need the
!!! firmware binary. It is worth sanity-checking the firmware first, though:
!!! connect the board to your workstation, run `west flash` and then
!!! `west espressif monitor`, and confirm the LED lights yellow and the log shows
!!! the strip `ready`. This isolates firmware problems from the deployment
!!! pipeline before you wrap the binary in an Artifact.

## Step 5 - Create the Component Artifacts

Now create the Mender Artifacts. Run these commands on your **workstation**, in
the working directory that holds `zephyr.bin`.

### ESP32-S3 firmware Artifact

Wrap the firmware in a `module-image` Artifact of type `esp32` (the Interface
name):

```bash
INTERFACE=esp32
COMPONENT_TYPE=esp32s3
VERSION=esp32-v1

mender-artifact write module-image \
  --type $INTERFACE \
  --compatible-types $COMPONENT_TYPE \
  --artifact-name $VERSION \
  --file zephyr.bin \
  --output-path $VERSION.mender
```

`mender-artifact` automatically records the version as
`rootfs-image.esp32.version=esp32-v1` in the Artifact, derived from the payload
type (`esp32`) and the Artifact name. The `esp32` Interface reports the same
`rootfs-image.esp32.version` field through its `Provides` query, so the
Orchestrator can tell which firmware a Component runs and skip it when it is
already up to date.

### Raspberry Pi system Artifact

Create a root filesystem Artifact for the System Device with the `mender-artifact`
snapshot feature, which reads the live filesystem over SSH. Replace the values
with those of your Raspberry Pi:

```bash
IP_ADDRESS=<your-raspberry-pi-ip>
PORT=22
DEVICE_TYPE=raspberrypi5
USER=<your-raspberry-pi-user>

mender-artifact write rootfs-image \
    --file ssh://"${USER}@${IP_ADDRESS}" \
    --compatible-types "${DEVICE_TYPE}" \
    --artifact-name rpi5-v1 \
    --output-path rpi5-v1.mender \
    --ssh-args="-p ${PORT}" \
    --ssh-args="-o UserKnownHostsFile=/dev/null" \
    --ssh-args="-o StrictHostKeyChecking=no"
```

!!! Your device is temporarily frozen during snapshot creation to ensure
!!! consistency. This may take several minutes depending on the root filesystem
!!! size.

## Step 6 - Create the Manifest and its Artifact

The [Manifest](../../02.Manifest/docs.md) defines the target state of the whole
System: which Artifact each Component type should run, and in what order they should be installed.
On your **workstation**, create the Manifest file:

```bash
cat > manifest-v1.yaml << 'EOF'
api_version: "mender/v1"
kind: "manifest"
name: "system-v1"
system_types_compatible: ["rpi5-esp32-system"]

component_types:
  raspberrypi5:
    artifact_name: rpi5-v1
    update_strategy:
      order: 10

  esp32s3:
    artifact_name: esp32-v1
    update_strategy:
      order: 20
EOF
```

The `order` values install the Raspberry Pi root filesystem first (order 10), and
the ESP32-S3 firmware second (order 20). Every `component_type` in the Topology
must have a matching entry in the Manifest.

Turn the Manifest into a Mender Artifact with `mender-orchestrator-manifest-gen`.
If you do not have the generator yet, install it as described in
[Create a Manifest Artifact](../../02.Manifest/01.Manifest-Artifact/docs.md#installation):

```bash
mender-orchestrator-manifest-gen \
    --artifact-name system-v1 \
    --output-path system-v1.mender \
    --system-type rpi5-esp32-system \
    manifest-v1.yaml
```

## Step 7 - Upload the Artifacts and deploy

Upload the three Artifacts you created to hosted Mender. Go to the **Software**
section and upload:

* `rpi5-v1.mender` - the Raspberry Pi root filesystem
* `esp32-v1.mender` - the ESP32-S3 firmware
* `system-v1.mender` - the Manifest

Then deploy the Manifest:

1. In hosted Mender, go to the **Devices** section and find your Raspberry Pi 5.
2. From **Device actions**, select **Create a deployment for this device**.
3. Choose the `system-v1` Release and start the deployment.

## Step 8 - Verify the result

Once the deployment reaches **Finished**, check the installed versions directly
on the Raspberry Pi:

```bash
sudo mender-orchestrator show-provides
```

You should see the Raspberry Pi reporting `rpi5-v1` and the ESP32-S3
Component reporting `rootfs-image.esp32.version=esp32-v1`, listed under its
component ID. You can also see this information under the Raspberry Pi's **Software**
tab in hosted Mender.

Most importantly, **look at the ESP32-S3 board**: its onboard RGB LED is now lit
**yellow**. Unlike `show-provides`, which reflects the Orchestrator's bookkeeping on
the Raspberry Pi, the LED is proof that the new firmware is actually running on
the device itself.

## Deploy a second version and watch the LED change

To see an update land on the device, build a version 2 that lights the LED a
different color, and deploy it through a new Manifest.

On your **workstation**, edit `~/mender-mcu-workspace/esp32-component-fw/src/main.c`
and change the color from yellow to green:

```c
	const struct led_rgb color = { .r = 0x00, .g = 0x20, .b = 0x00 };
```

Rebuild and copy the new binary to your Artifact working directory:

```bash
cd ~/mender-mcu-workspace/esp32-component-fw
west build -b esp32s3_devkitc/esp32s3/procpu .
cp build/zephyr/zephyr.bin ~/esp32-orchestrator/
cd ~/esp32-orchestrator
```

Create the version 2 firmware Artifact:

```bash
VERSION=esp32-v2
mender-artifact write module-image \
  --type esp32 \
  --compatible-types esp32s3 \
  --artifact-name $VERSION \
  --file zephyr.bin \
  --output-path $VERSION.mender
```

Create a version 2 Manifest. The Raspberry Pi keeps `rpi5-v1` (nothing to
do there, so it is not reinstalled), and only the ESP32-S3 moves to
`esp32-v2`:

```bash
cat > manifest-v2.yaml << 'EOF'
api_version: "mender/v1"
kind: "manifest"
name: "system-v2"
system_types_compatible: ["rpi5-esp32-system"]

component_types:
  raspberrypi5:
    artifact_name: rpi5-v1
    update_strategy:
      order: 10

  esp32s3:
    artifact_name: esp32-v2
    update_strategy:
      order: 20
EOF

mender-orchestrator-manifest-gen \
    --artifact-name system-v2 \
    --output-path system-v2.mender \
    --system-type rpi5-esp32-system \
    manifest-v2.yaml
```

Upload `esp32-v2.mender` and `system-v2.mender` to hosted Mender,
then deploy the `system-v2` Release to your Raspberry Pi as before.
When the deployment finishes, the ESP32-S3's LED turns from **yellow to green** -
the update is visible on the device.
