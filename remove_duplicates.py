def remove_duplicates(array):
    if not array:
        return array

    unique_list = []
    last_element = None

    for element in array:
        if element != last_element:
            unique_list.append(element)
            last_element = element

    return unique_list

array1 = [2, 2, 2, 2, 2]
print(remove_duplicates(array1))  

array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(array2))