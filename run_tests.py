import doctest
import os

import pytest


def test():
    pytest.main()


def run_doctest():
    doctest.testfile("README.md")
    for file in os.listdir("tests/"):
        if not file.endswith(".md"):
            continue
        filepath = os.path.join("tests/", file) 
        doctest.testfile(filepath, optionflags=doctest.ELLIPSIS)

