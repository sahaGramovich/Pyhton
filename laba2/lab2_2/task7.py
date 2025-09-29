def merge_sorted_list(list1, list2):

    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

print("=== Базовые тесты ===")
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"Результат: {merge_sorted_list(list1, list2)}")

print("\n=== Списки разной длины ===")
list3 = [1, 2, 3]
list4 = [4, 5, 6, 7, 8]
print(f"list3: {list3}")
print(f"list4: {list4}")
print(f"Результат: {merge_sorted_list(list3, list4)}")

print("\n=== С пересекающимися значениями ===")
list5 = [1, 3, 5, 7, 9]
list6 = [2, 3, 4, 7, 8]
print(f"list5: {list5}")
print(f"list6: {list6}")
print(f"Результат: {merge_sorted_list(list5, list6)}")

print("\n=== Один пустой список ===")
list7 = []
list8 = [1, 2, 3]
print(f"list7: {list7}")
print(f"list8: {list8}")
print(f"Результат: {merge_sorted_list(list7, list8)}")

print("\n=== Оба пустых списка ===")
list9 = []
list10 = []
print(f"list9: {list9}")
print(f"list10: {list10}")
print(f"Результат: {merge_sorted_list(list9, list10)}")

print("\n=== С числами с плавающей точкой ===")
list11 = [1.5, 2.7, 3.1]
list12 = [2.0, 3.5, 4.8]
print(f"list11: {list11}")
print(f"list12: {list12}")
print(f"Результат: {merge_sorted_list(list11, list12)}")