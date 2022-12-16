import pytest
from .. import main


def test_make_file():
    """`
    make sure that the file saves properly and uses default ext or explicitly
    defined ext.
    This will run two assertions; First will create a new file, and second will
        read existing file and save with same ext.

    """

    result = main.Manage("with_ext.py")
    assert result.name() == "with_ext.py"
    print("Passed first")
    result = main.Manage("with_ext.py")
    assert result.name() == "with_ext.py"

    result = main.Manage("without_ext")
    assert result.name() == "without_ext.txt"
    result = main.Manage("without_ext")
    assert result.name() == "without_ext.txt"