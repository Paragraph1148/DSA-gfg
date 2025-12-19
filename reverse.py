def reverse(num):
    rev = 0
    while num > 0:
        a = num % 10
        rev = rev * 10 + a
        num //= 10        
    return rev
n = 2364
print(reverse(n))