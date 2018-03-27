import pytest
from linked_list import LinkedList as LL


def test_insert_first_node(empty_ll):
    """test to insert first node"""
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_insert_two_nodes(empty_ll):
    """test to insert two nodes, new node is inserted at head"""
    empty_ll.insert(2)
    empty_ll.insert(1)
    assert empty_ll.head.val == 1


def test_insert_iterable():
    assert LL([1, 2, 3, 4])._size == 4


def test_find_none(empty_ll):
    """test to search an empty list"""
    assert empty_ll.find(1) is False


def test_find(small_ll):
    """test to find in list"""
    assert small_ll.find(1) is True


def test_not_found(small_ll):
    """test to not find in list"""
    assert small_ll.find(5) is False


def test_length_empty(empty_ll):
    """test length of empty list"""
    assert len(empty_ll) == 0


def test_length(small_ll):
    """test length of list"""
    assert len(small_ll) == 4


def test_check_valid_iterable():
    """check if iterable valid"""
    with pytest.raises(TypeError) as err:
        LL(2)

    assert str(err.value) == 'Invalid iterable'


def test_append_to_end_empty(empty_ll):
    """test if appends to empty list"""
    empty_ll.append(2)
    assert empty_ll.head.val == 2


def test_append_to_end(small_ll):
    """test if appends to end of list"""
    small_ll.append(5)
    assert len(small_ll) == 5
    assert small_ll.head._next._next._next._next.val == 5


def test_insert_after(small_ll):
    """test if inserts after value"""
    small_ll.insert_after(2, 8)
    assert len(small_ll) == 5
    assert small_ll.head._next._next._next.val == 8


def test_insert_after_end(small_ll):
    """test if inserts after value"""
    small_ll.insert_after(1, 9)
    assert len(small_ll) == 5
    assert small_ll.head._next._next._next._next.val == 9
