# A program that computes a factorial of a given number
# It receives user input

def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)

x = float(input())
print(fact(x))
