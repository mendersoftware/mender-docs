---
title: File Transfer
taxonomy:
    category: docs
---

File Transfer is a Mender add-on providing the functionality of transferring
files on and off any accepted device.

## Mender File Transfer vs FTP and SFTP

From the caller's perspective, File Transfer offers a simple HTTP API to `GET`
and `PUT` files. On a device `mender-connect` handles requests from the backend
and provides data to reply to the HTTP calls. The implementation does not relay
on any third-party software installed on a device, and in that sense has no relation
to FTP or SFTP. Although feature-wise it provides similar functionalities.

## Controlling the uploads and downloads

You can use the File Transfer feature to upload and download anything to and from a device.
In itself it gives a great power, but may require a certain degree of control.
[The Limits](../90.Mender-Connect/docs.md#limits-configuration) configuration section allows you
to restrict many aspects of the file transfer process. We designed it to give you full control over what
you can do, while at the same time providing a way to introduce restrictions for environments where limiting
is crucial.

## Limitations

### Multiple parallel file transfer sessions to the same device

Currently, the File Transfer does not support parallel uploads or downloads.
Please make sure you are not running multiple sessions at the same time 
for the same device.

## Further reading

* For a detailed list of the configuration options please refer to the
[mender-connect configuration reference](../90.Mender-Connect/docs.md#file-transfer-configuration).
* You can find the mender-connect installation steps for Yocto-based projects,
and for Debian family,
in the [customize with Yocto](../../05.Operating-System-updates-Yocto-Project/05.Customize-Mender/docs.md),
and [customize with Debian](../../04.Operating-System-updates-Debian-family/03.Customize-Mender/docs.md)
respectively.
