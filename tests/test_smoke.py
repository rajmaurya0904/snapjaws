"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import snapjaws


def test_version_is_set() -> None:
    assert snapjaws.__version__
