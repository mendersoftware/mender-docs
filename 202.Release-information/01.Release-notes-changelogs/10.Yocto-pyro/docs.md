---
title: Release notes & changelogs for Yocto Project meta-mender/pyro
taxonomy:
    category: docs
---

## pyro-v2017.11

_Released 11.13.2017_

* Add Mender 1.3.0b1 recipe.
* Upstream image has grown significantly, increase to 608MB sdimg.
  The noticably non-round number is to make sure the calculated rootfs
  size is divisible by the partition alignment.
