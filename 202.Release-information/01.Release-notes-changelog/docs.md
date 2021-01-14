---
title: Release notes & changelog
taxonomy:
    category: docs
shortcode-core:
    active: false
---

## v1.0.1 
_Released 05.04.2017_

### Notable changes

#### [deployments](https://github.com/mendersoftware/deployments)

* Update artifact description when updating artifact data ([MEN-1093](https://tracker.mender.io/browse/MEN-1093))
* Fix log flag not being set for device deployment after log been uploaded
  ([MEN-1078](https://tracker.mender.io/browse/MEN-1078))

#### [gui](https://github.com/mendersoftware/gui)

* Bugfix: open correct deployment report dialog from dashboard
* Update node modules, add drag+drop artifact, allow edit
  artifact description
* Move user token from local storage to cookie, add react-cookie module ([#217](https://github.com/mendersoftware/gui/pull/217))
* Update node modules, add drag+drop & cookie functionality ([#219](https://github.com/mendersoftware/gui/pull/219))
* Replace artifact upload dialog with drag-and-drop
* Remove cookie when receiving unauthorized response
* Edit artifact description in UI

#### [mender](https://github.com/mendersoftware/mender)

* Fix bug that caused the update not to be retried after failing during
  previous attempt ([#193](https://github.com/mendersoftware/mender/pull/193))

---

## v1.0.0 
_Released 02.20.2017_

---