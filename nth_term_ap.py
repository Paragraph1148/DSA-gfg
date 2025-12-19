# def nth_term_of_ap(a1, a2, n):
#     nth_term = a1
#     diff = a2 - a1
#     for i in range(1, n):
#         nth_term += diff
#     return nth_term

# a1 = 2
# a2 = 3
# n = 17987278398
# print(nth_term_of_ap(a1, a2, n))

def nth_term_of_ap(a1, a2, n):
    nth_term = a1 + (n - 1) * (a2 - a1)
    return nth_term
a1 = 2
a2 = 3
n = 17987278398
print(nth_term_of_ap(a1, a2, n))