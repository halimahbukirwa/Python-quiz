# A program that accepts a sequence of comma-separated numbers
# Generates a list and a tuple which contains every number

lists = []

nums = (input())

l = nums.split(",")
t = tuple(l)

for i in l:
    
    lists.append(i)
    
print(lists)
print(t)
