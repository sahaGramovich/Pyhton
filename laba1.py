import math



def to_radians(degrees):
    return degrees * math.pi / 180



def f(x_deg):
    x_rad = to_radians(x_deg)
    cos_x = math.cos(x_rad)
    cos_06x = math.cos(0.6 * x_rad)
    sin_x = math.sin(x_rad)

    term1 = math.exp(cos_x)
    term2 = math.log(cos_06x ** 2 + 1)
    return term1 + term2 * sin_x


def h(x_deg):
    x_rad = to_radians(x_deg)
    cos_x = math.cos(x_rad)
    sin_x = math.sin(x_rad)

    term = (cos_x + sin_x) ** 2 + 2.5
    return -math.log(term) + 10



print("x(градусы)\tf(x)\t\th(x)")
print("-" * 40)

for x in range(-360, 361, 90):
    try:
        f_val = f(x)
        h_val = h(x)
        print(f"{x:4d}\t\t{f_val:8.4f}\t{h_val:8.4f}")
    except:
        print(f"{x:4d}\t\tОшибка вычисления")


print("\nДетальные значения вокруг 0 градусов:")
print("x(градусы)\tf(x)\t\th(x)")
print("-" * 40)
for x in range(-30, 31, 10):
    try:
        f_val = f(x)
        h_val = h(x)
        print(f"{x:4d}\t\t{f_val:8.4f}\t{h_val:8.4f}")
    except:
        print(f"{x:4d}\t\tОшибка вычисления")