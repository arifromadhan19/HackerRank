#FIRST WAY
#####################
n = 3
arr = [3, -7, 0]
arr.sort()
result = abs(arr[1] - arr[0])
for i in range(1, n - 1):
    if (abs(arr[i] - arr[i + 1]) < result):
        result = abs(arr[i] - arr[i + 1])
print(result)

#SECOND WAY (NOT EFFICIENCY)
##########################
n = 3
arr = [3, -7, 0]
temp_result = (abs(arr[0])+abs(arr[1]))
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if i > j:
            result = (abs(arr[j])+abs(arr[i]))
            if result <= temp_result:
                temp_result = result
print(temp_result)
