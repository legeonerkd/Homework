#nums = [1,2,5,2,3]
#target = 2
#indexes = [i for i, x in enumerate(sorted(nums)) if x == target]
#print(indexes)
#candyType = [6,6,6,6]
#new = []
#for candy in candyType:
#    if candy not in new:
#        new.append(candy)
#if len(new) >= (len(candyType)//2):
#    print(len(candyType)//2)
#print(len(new))
#arrr = [17,18,5,4,6,1]
#print(max(arrr[2:]))
nums = [12,345,2,6,7896]
count = 0
for num in nums:
    if len(str(num))%2 == 0:
        count += 1
print(count)