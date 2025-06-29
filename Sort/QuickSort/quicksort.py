def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        # 获取分区点位置
        pivot_index = partition(arr, low, high)

        # 递归排序左右数组
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,high)

def partition(arr, low, high):
    # 选择最左侧元素为基准
    pivot = arr[low]
    i = low + 1

    for j in range(low + 1,high + 1):
        # 将小于基准的元素移动到左边
        if arr[j] < pivot:
            # 交换元素
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # 将基准元素放到正确的位置
    arr[low], arr[i-1] = arr[i-1], arr[low]
    return i - 1

# 测试
arr = [10, 7, 8, 9, 1, 5]
print("排序前：", arr)
quick_sort(arr)
print("排序后：", arr)