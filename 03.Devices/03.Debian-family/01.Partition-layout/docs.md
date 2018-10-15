---
title: Partition layout
taxonomy:
    category: docs
---

Original layout of partition should be modified to fulfill Mender needs. The [mender-convert](https://github.com/mendersoftware/mender-convert?target=_blank) tool provides for modification of the partition layout. Restructuring of partition layout should be done as the first step. It can be done by executing the following command:

```bash
        ./mender-convert raw-disk-image-create-partitions  \
                --raw-disk-image <PATH-TO-RAW-DISK-IMAGE>  \
                --mender-disk-image <MENDER-IMAGE-NAME>    \
                --device-type <beaglebone | raspberrypi3>  \
                --data-part-size-mb <DATA-PART-SIZE-IN-MB>
```


