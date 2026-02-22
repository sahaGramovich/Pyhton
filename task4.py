import numpy as np
from scipy import integrate

# пример 1: определённый интеграл ∫ sin(x^2) dx от 0 до 2
f = lambda x: np.sin(x ** 2)
res1, err1 = integrate.quad(f, 0, 2)
print(f"Определённый интеграл ∫ sin(x²) dx от 0 до 2 = {res1:.4f}")

# пример 2: двойной интеграл ∫∫ (x² + y²) dx dy по [0,1]x[0,1]
g = lambda y, x: x ** 2 + y ** 2
res2, err2 = integrate.dblquad(g, 0, 1, lambda x: 0, lambda x: 1)
print(f"Двойной интеграл ∫∫ (x² + y²) dxdy по [0,1]x[0,1] = {res2:.4f}")
