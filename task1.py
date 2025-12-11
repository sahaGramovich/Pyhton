def count_words(sentence: str) -> int:
    """Возвращает количество слов в предложении."""
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    return len(sentence.split())


def find_unique(items: list) -> list:
    """Возвращает элементы, которые встречаются только один раз."""
    if not isinstance(items, list):
        raise TypeError("Input must be a list")

    result = []
    for item in items:
        if items.count(item) == 1:
            result.append(item)
    return result


def is_palindrome(value) -> bool:
    """Проверяет, является ли строка или число палиндромом."""
    s = str(value).lower().replace(" ", "")
    return s == s[::-1]


def are_anagrams(str1: str, str2: str) -> bool:
    """Проверяет, являются ли строки анаграммами."""
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")

    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())


def combine_dicts(d1: dict, d2: dict) -> dict:
    """Возвращает новый словарь, содержащий пары из двух словарей в порядке следования."""
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise TypeError("Both inputs must be dictionaries")

    new_dict = {}
    new_dict.update(d1)
    new_dict.update(d2)
    return new_dict