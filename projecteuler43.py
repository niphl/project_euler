d = {0:17, 1:13, 2:11, 3:7, 4:5, 5:3, 6:2}
totalSum = 0
def addPan(nums,n):
    global totalSum
    if nums == '':
        totalSum += int(n)
        return
    if len(n) >= 3:
        k = d[len(n)-3]
        if int(n[:3])%k != 0:
            return
    for i in nums:
        m = i + n
        reducedNums = nums.replace(i,'')
        addPan(reducedNums, m)
    return
addPan('0123456789','')
print(totalSum)