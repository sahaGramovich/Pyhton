import pytest
from .functions import (
    count_words,
    find_unique,
    is_palindrome,
    are_anagrams,
    combine_dicts,
)

def test_count_words_normal():
    assert count_words("Hello world") == 2
    assert count_words("One two three four") == 4


def test_count_words_empty():
    assert count_words("") == 0


def test_count_words_invalid():
    with pytest.raises(TypeError):
        count_words(123)

def test_find_unique_basic():
    assert find_unique([1, 2, 2, 3, 4, 4]) == [1, 3]


def test_find_unique_all_unique():
    assert find_unique([1, 2, 3]) == [1, 2, 3]


def test_find_unique_invalid():
    with pytest.raises(TypeError):
        find_unique("not a list")

def test_is_palindrome_true():
    assert is_palindrome("madam")
    assert is_palindrome("racecar")
    assert is_palindrome(121)
    assert is_palindrome("A man a plan a canal Panama")


def test_is_palindrome_false():
    assert not is_palindrome("python")
    assert not is_palindrome(123)

def test_are_anagrams_true():
    assert are_anagrams("listen", "silent")
    assert are_anagrams("evil", "vile")
    assert are_anagrams("Dormitory", "Dirty room")


def test_are_anagrams_false():
    assert not are_anagrams("hello", "world")


def test_are_anagrams_invalid():
    with pytest.raises(TypeError):
        are_anagrams(10, "abc")

def test_combine_dicts_basic():
    assert combine_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def test_combine_dicts_overwrite():
    assert combine_dicts({"a": 1}, {"a": 99}) == {"a": 99}


def test_combine_dicts_invalid():
    with pytest.raises(TypeError):
        combine_dicts("not dict", {})