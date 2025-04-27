def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] 
    return arr

arr = [19,78,95,88,64,12,336,4458,415,77]
print("排序前：",arr)
bubble_sort(arr)
print("排序后：",arr)