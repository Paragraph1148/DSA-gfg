# def closest_number(n, m):
#     closest = 0
#     min_difference = float('inf')
#     for i in range(n - abs(m), n + abs(m) + 1):
#         if i % m == 0:
#             difference = abs(n - i)
#             if difference < min_difference or (difference == min_difference and abs(i) > abs(closest)):
#                 closest = i
#                 min_difference = difference
#     return closest

# n = -19
# m = 4
# print(closest_number(n, m))

def closest_number(n, m):
    q = int(n / m)
    n1 = m * q
    if (n * m) > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)
    if abs(n - n1) < abs(n - n2):
        return n1
    return n2

n = 19
m = 4
print(closest_number(n, m))
n = -19
m = 4
print(closest_number(n, m))