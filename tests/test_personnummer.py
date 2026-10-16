"""Tester för personnummer-modulen.

All testdata här är påhittad. Rader med personnummer märks 'fake-pnr' så att
pre-commit-hooken släpper igenom dem.
"""

import pytest

from medlemssynk import personnummer  # noqa: F401


@pytest.mark.skip(reason="inte implementerat än")
def test_normalize_accepts_common_formats():
    # Exempel på format som ska normaliseras till 12 siffror:
    #   "19900101-2389", "900101-2389", "199001012389"      # fake-pnr
    ...
