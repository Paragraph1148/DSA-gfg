# def sum_of_digits(num):
#     sum = 0
#     for _ in range(len(str(num))):
#         dig = num % 10
#         sum += dig
#         num //= 10
#     return sum

def sum_of_digits(num):
    sum = 0
    for ch in str(num):
        sum += int(ch)
    return sum
n = 12345
print(sum_of_digits(n))
