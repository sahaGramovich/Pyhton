def merge_dicts(dict_a, dict_b):
    for key, value in dict_b.items():
        if key in dict_a:

            if isinstance(dict_a[key], dict) and isinstance(value, dict):
                merge_dicts(dict_a[key], value)
            elif isinstance(dict_a[key], list) and isinstance(value, list):
                dict_a[key].extend(value)
            elif isinstance(dict_a[key], set) and isinstance(value, set):
                dict_a[key].update(value)
            elif isinstance(dict_a[key], tuple) and isinstance(value, tuple):
                dict_a[key] = dict_a[key] + value
            else:
                dict_a[key] = value
        else:
            dict_a[key] = value

dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

print("До слияния:")
print("dict_a =", dict_a)
print("dict_b =", dict_b)

merge_dicts(dict_a, dict_b)

print("\nПосле слияния:")
print("dict_a =", dict_a)
print("dict_b =", dict_b)