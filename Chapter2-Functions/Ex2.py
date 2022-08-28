from math import factorial
def pascal_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

        # for new line
        print()
pascal_triangle(5)