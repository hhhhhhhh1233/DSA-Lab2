import random

def SmallestThreeSmart(arr):
    if len(arr) == 3:
        return sorted(arr)
    x, y, z = SmallestThreeSmart(arr[:-1])
    return sorted([x,y,z,arr[-1]])[:-1]

def SmallestThree(arr):
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]
    if len(arr) == 3:
        x, y = SmallestThree(arr[:-1])
        if arr[2] < y:
            if arr[2] < x:
                return arr[2],x,y
            else:
                return x,arr[2],y
        else:
            return x,y,arr[2]
    x, y, z = SmallestThree(arr[:-1])
    if arr[-1] < z:
        if arr[-1] < y:
            if arr[-1] < x:
                return arr[-1], x, y
            else:
                return x, arr[-1], y
        else:
            return x, y, arr[-1]
    else:
        return x, y, z

def SmallestThreeNoRecur(arr):
    if arr[0] > arr[1]:
        x, y = arr[0], arr[1]
    else:
        x, y = arr[1], arr[0]

    if arr[2] > y:
        z = arr[2]
    elif arr[2] > x:
        y, z = z, arr[2]
    elif arr[2] < x:
        x, y, z = arr[2], x, y

    for i in arr[3:]:
        if i < z:
            if i < y:
                if i < x:
                    x, y, z = i, x, y
                else:
                    x, y, z = x, i, y
            else:
                x, y, z = x, y, i
        else:
            x, y, z = x, y, z

    return x,y,z    
  
for i in range(10):
    testArr = []
    for j in range(10):
        testArr.append(random.randint(0,30))
    print(f"Arr: {testArr}\nSmallestThree: {SmallestThree(testArr)}\n")


