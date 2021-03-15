# program that checks the numbers that are divible by seven
#but not divisible by 5
#in the range of 2000 and 3200 both inclusive

nums = []

for num in range(2000,3201):
    if (num%7==0) and (num%5!=0):
        nums.append(num)
    else:
        pass

print(nums) 