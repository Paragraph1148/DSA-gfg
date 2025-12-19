# def is_power_of_other(x, y):
#     if x == 1:
#         return y == 1
#     pow = 1
#     while pow < y:
#         pow *= x
#     return pow == y

# print(is_power_of_other(10, 1))
# print(is_power_of_other(1, 20))
# print(is_power_of_other(2, 128))
# print(is_power_of_other(2, 30))


import math

def _pow_limit(base: int, exp: int, limit: int):
    """Return base**exp if ≤ limit, otherwise None (early stop)."""
    result = 1
    while exp:
        if exp & 1:
            result *= base
            if result > limit:
                return None
        exp >>= 1
        if exp:
            base *= base
            if base > limit:
                return None
    return result

def isPower(x: int, y: int) -> bool:
    # ----- trivial bases -------------------------------------------------
    if x == 0:      return y == 0
    if x == 1:      return y == 1
    if x == -1:     return y == 1 or y == -1
    if y < 0 and x > 0: return False   # positive base cannot give negative power

    ax, ay = abs(x), abs(y)

    # Upper bound for exponent k: 2**k ≤ y  →  k ≤ log2(y)
    k_max = math.floor(math.log2(ay)) + 1
    lo, hi = 1, k_max

    while lo <= hi:
        mid = (lo + hi) // 2
        power = _pow_limit(ax, mid, ay)
        if power is None:               # ax**mid > ay
            hi = mid - 1
            continue
        if power == ay:
            # sign must match when x or y are negative
            if (x < 0) != (y < 0):
                return mid % 2 == 1     # odd exponent needed
            return True
        if power < ay:
            lo = mid + 1
        else:   # should not happen because _pow_limit caps at limit
            hi = mid - 1
    return False

print(isPower(10, 1))
print(isPower(1, 20))
print(isPower(2, 128))
print(isPower(2, 30))