def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] >arr[j + 1]:
                arr[j], arr [j+1] = arr[j+1], arr[j]
    return arr

# 如果是已经排序好的数组，则可以进行以下优化
def optimized_bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        swaaped = False
        
        for j in range(n - i - 1):
            if arr[j] >arr[j + 1]:
                arr[j], arr [j+1] = arr[j+1], arr[j]
                swaaped = True
                
        # 如果没有进行交换操作，排序完成
        if not swaaped:
            break
    return arr
