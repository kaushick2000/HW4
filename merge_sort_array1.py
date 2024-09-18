def merge_two_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

def merge_k_arrays(arrays):
    if not arrays:
        return []

    result = arrays[0]
    for i in range(1, len(arrays)):
        result = merge_two_arrays(result, arrays[i])

    return result
input1 = 3
n=4
arrays1 = [1, 3, 5, 7]
arrays2 = [2, 4, 6, 8]
arrays3 = [0, 9, 10, 11]
first_set = [arrays1, arrays2, arrays3]

input2 = 3
n=3
array1 = [1,3,7]
array2 = [2,4,8]
array3 = [9,10,11]
second_set = [array1, array2, array3]
print(merge_k_arrays(first_set))
print(merge_k_arrays(second_set))