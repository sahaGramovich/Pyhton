def flatten_list(lst):
    i = 0
    while i < len(lst):

        if type(lst[i]) == list:

            flatten_list(lst[i])

            j = 0
            while j < len(lst[i]):
                lst.insert(i + j, lst[i][j])
                j += 1

            lst.pop(i + j)

        else:

            i += 1

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print(f"Исходный список: {list_a}")
flatten_list(list_a)
print(f"Сглаженный список: {list_a}")

print("\n" + "="*40)

test_cases = [
    [1, [2, [3, [4]]]],
    [[], 1, [], 2, [[3]]],
    [1, 2, 3],
    [[1, 2], [3, 4], [5]],
    []
]

for i, test in enumerate(test_cases, 1):
    print(f"Тест {i} до: {test}")
    flatten_list(test)
    print(f"Тест {i} после: {test}")
    print("-" * 20)