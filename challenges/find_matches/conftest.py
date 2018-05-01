from .k_tree import KTree as KT
import pytest


@pytest.fixture
def large_tree():
    tree = KT()
    tree.insert(10, None)
    tree.insert(2, 10)
    tree.insert(2, 10)
    tree.insert(3, 2)
    tree.insert(12, 3)
    tree.insert(13, 3)
    return tree


@pytest.fixture
def small_tree():
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    return tree