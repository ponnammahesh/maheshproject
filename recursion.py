def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

result = fact(3)
print(result)

#Let's walk through the calculation for fact(3):

#(fact(3) calls fact(2) → return 3 * fact(2)
#fact(2) calls fact(1) → return 2 * fact(1)
#fact(1) calls fact(0) → return 1 * fact(0) = 1 (base case)
#Now the function begins returning values:

#fact(1) returns 1 * 1 = 1
#fact(2) returns 2 * 1 = 2
#fact(3) returns 3 * 2 = 6)