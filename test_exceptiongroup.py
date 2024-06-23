import pytest


def fun():
    raise ExceptionGroup(
        "Group message",
        [
            RuntimeError()
        ]
    )


def test_fun():
    with pytest.raises(ExceptionGroup) as exception_group:
        fun()

    assert exception_group.group_contains(RuntimeError)
    assert not exception_group.group_contains(TypeError)
