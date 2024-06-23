import pytest


def fun():
    raise SystemExit()


def test_mytest():
    with pytest.raises(SystemExit):
        fun()
