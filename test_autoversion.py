#!/usr/bin/python3

import re
import autoversion


def test_version_regex():
    regex = autoversion.VERSION_MATCHER

    # Should match.
    assert re.search(regex, "1.2.3") is not None
    assert re.search(regex, "1.2.3b2") is not None
    assert re.search(regex, "1.2.3-build123") is not None
    assert re.search(regex, "1.2.3-build123").group(0) == "1.2.3-build123"
    assert re.search(regex, "release_2_1.2.3") is not None
    assert re.search(regex, "release_2_1.2.3.mender") is not None
    assert re.search(regex, "release_2_1.2.3_mender") is not None
    assert re.search(regex, "release.2_1.2.3_mender") is not None
    assert re.search(regex, "release.2_1.2.3.mender") is not None
    assert re.search(regex, "release.2_1.2.3_2") is not None
    assert re.search(regex, "release.2_master_2") is not None
    assert re.search(regex, "morty") is not None

    # Special case: mender-X.Y.Z
    assert re.search(regex, "mender-1.2.3") is not None
    assert re.search(regex, "mender-1.2.3").group(0) == "mender-1.2.3"
    assert re.search(regex, "something-mender-1.2.3-else") is not None
    assert re.search(regex, "something-mender-1.2.3-else").group(0) == "mender-1.2.3"
    assert re.search(regex, "1.2.3-mender") is not None
    assert re.search(regex, "1.2.3-mender").group(0) == "1.2.3"
    assert re.search(regex, "mender.1.2.3") is not None
    assert re.search(regex, "mender.1.2.3").group(0) == "1.2.3"

    # Should not match.
    assert re.search(regex, "1.2.3.4") is None
    assert re.search(regex, "11.2.3.4") is None
    assert re.search(regex, "1.2.3.14") is None
    assert re.search(regex, "2.1.2.3.4") is None
    assert re.search(regex, "22.1.2.3.4") is None
    assert re.search(regex, "22.11.2.3.4") is None
    assert re.search(regex, "127.0.0.1") is None
    assert re.search(regex, "mortyxxx") is None


def test_minor_versions_regex():
    regex = autoversion.MINOR_VERSIONS_MATCHER

    # Should match.
    assert re.search(regex, "1.2") is not None
    assert re.search(regex, "1.2, 1.3, 1.4").group(0) == "1.2, 1.3, 1.4"
    assert re.search(regex, "something 1.2 else") is not None
    assert re.search(regex, "even 1.2.") is not None

    # Should not match.
    assert re.search(regex, "1.2.3") is None
    assert re.search(regex, "11.2.3.4") is None
    assert re.search(regex, "1.2.3.14, 12.3.1, 123.5.5") is None
    assert re.search(regex, "a.1, 2.c, b.4") is None


test_version_regex()
test_minor_versions_regex()
