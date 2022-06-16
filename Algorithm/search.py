import os

# 递归实现
def binary_search(num, l, start, end):  # 二分法查找，成功返回索引值，否则返回-1
    if start <= end:
        mid = (start + end) // 2        # 算出中间值
        if l[mid] == num:
            return mid
        elif l[mid] < num:
            start = mid + 1
            return binary_search(num, l, start, end)
        else:
            end = mid - 1
            return binary_search(num, l, start, end)
    else:
        return -1



if __name__ == '__main__':
    
    list_demo=[1,5,8,7,9,19,41,53,321]
    rs = binary_search(9,list_demo,0,len(list_demo))
    print(rs)
    c = -5//2
    print(c)
    