import math

print(math.pi)  # 3.141592653589793
print(len(str(math.pi)))  # 3.141592653589793

print(math.sqrt(25))  # 5.0
# SciPy, numpy, pandas

angle_degree = 30
angle_radians = math.radians(angle_degree)
print(angle_radians)  # 0.5235987755982988

sin_val = math.sin(angle_radians)
print(f"sin({angle_degree}) = {sin_val}")
# sin(30) = 0.49999999999999994

angles = [0, 30, 45, 60, 90]

sin_values = [math.sin(math.radians(a)) for a in angles]
print(sin_values)
# [0.0, 0.49999999999999994, 0.7071067811865476, 0.8660254037844386, 1.0]

for a, s in zip(angles, sin_values):
    print(f"sin({a}) = {s:2f}")
# sin(0) = 0.000000
# sin(30) = 0.500000
# sin(45) = 0.707107
# sin(60) = 0.866025
# sin(90) = 1.000000
