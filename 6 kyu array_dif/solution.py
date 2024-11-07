def array_diff(a:list[int], b:list[int]) -> list:
    deleted_array = [num for num in a if num not in b]
    return deleted_array

dt = array_diff([1,2,2,2,3],[2])
print(dt)