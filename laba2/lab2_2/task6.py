def unique_elements(nested_list):
    result = []

    def extract_elements(lst):
        for item in lst:
            if isinstance(item, list):
                extract_elements(item)
            else:
                if item not in result:
                    result.append(item)

    extract_elements(nested_list)
    return result

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(f"Исходный список: {list_a}")
unique = unique_elements(list_a)
print(f"Уникальные элементы: {unique}")

print("\n" + "=" * 50)

test_cases = [
    [1, 2, [3, 4, [5, 1]]],
    [[1, 2], [3, 4], [1, 2]],
    [1, 1, 1, [1, 1]],
    [],
    [1, 2, 3],
    [[[1]], [2], [[1, 2]]]
]
for i, test in enumerate(test_cases, 1):
    print(f"Тест {i}: {test}")
    print(f"Уникальные: {unique_elements(test)}")
    print("-" * 30)