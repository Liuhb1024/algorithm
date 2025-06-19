def cocktail_sort(arr):
    """
    鸡尾酒排序的基本实现
    """
    n = len(arr)
    left = 0
    right = n - 1
    
    while left < right:
        # 从左到右，将最大元素移到右边
        for i in range(left, right):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] == arr[i+1],arr[i]
        right -= 1
        
        # 从右到左，将最小元素移动到左边
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] == arr[i - 1], arr[i]
            left += 1
            
    return arr

def cocktail_sort_optimized(arr):
    """
    优化的鸡尾酒排序，增加提前终止条件
    """
    n = len(arr)
    left = 0
    right = n - 1
    
    while left < right:
        swapped = False
        
        # 从左到右扫描
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        right -= 1
        
        # 如果没有发生交换，说明已经有序
        if not swapped:
            break
            
        # 从右到左扫描
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        left += 1
        
        # 如果没有发生交换，说明已经有序
        if not swapped:
            break
    
    return arr

# 可视化版本
def cocktail_sort_verbose(arr):
    """
    带详细输出的鸡尾酒排序，便于理解过程
    """
    n = len(arr)
    left = 0
    right = n - 1
    round_num = 1
    
    print(f"初始数组: {arr}")
    
    while left < right:
        print(f"<br />第{round_num}轮:")
        
        # 从左到右
        print(f"  从左到右扫描 (范围: {left} 到 {right})")
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print(f"    交换 {arr[i+1]} 和 {arr[i]}: {arr}")
        right -= 1
        
        # 从右到左
        print(f"  从右到左扫描 (范围: {right} 到 {left})")
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                print(f"    交换 {arr[i]} 和 {arr[i-1]}: {arr}")
        left += 1
        
        print(f"  第{round_num}轮结束: {arr}")
        round_num += 1
    
    return arr

# 测试用例
test_arrays = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 2, 4, 6, 1, 3],
    [1, 2, 3, 4, 5],  # 已排序
    [5, 4, 3, 2, 1],  # 逆序
    [42]              # 单元素
]

for i, arr in enumerate(test_arrays):
    print(f"<br />测试{i+1}: {arr}")
    sorted_arr = cocktail_sort_optimized(arr.copy())
    print(f"排序后: {sorted_arr}")