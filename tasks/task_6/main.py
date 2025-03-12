def second_largest(arr):
    unique_arr=list(set(arr))
    unique_arr.sort(reverse=True)
    return unique_arr[1] if len(unique_arr)>1 else None


print(second_largest([13,11,10,1,2,3,39]))