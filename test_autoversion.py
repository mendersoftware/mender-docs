#!/usr/bin/python3

import re
import autoversion

def test_version_regex():
    regex = autoversion.VERSION_MATCHER

    # Should match.
    assert re.search(regex, "1.2.3") is not None
    assert re.search(regex, "release_2_1.2.3") is not None
    assert re.search(regex, "release_2_1.2.3.mender") is not None
    assert re.search(regex, "release_2_1.2.3_mender") is not None
    assert re.search(regex, "release.2_1.2.3_mender") is not None
    assert re.search(regex, "release.2_1.2.3.mender") is not None
    assert re.search(regex, "release.2_1.2.3_2") is not None
    assert re.search(regex, "release.2_master_2") is not None
    assert re.search(regex, "morty") is not None

    # Should not match.
    assert re.search(regex, "1.2.3.4") is None
    assert re.search(regex, "11.2.3.4") is None
    assert re.search(regex, "1.2.3.14") is None
    assert re.search(regex, "2.1.2.3.4") is None
    assert re.search(regex, "22.1.2.3.4") is None
    assert re.search(regex, "22.11.2.3.4") is None
    assert re.search(regex, "127.0.0.1") is None
    assert re.search(regex, "mortyxxx") is None

test_version_regex()
