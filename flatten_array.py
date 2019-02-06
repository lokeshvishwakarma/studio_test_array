def flatten(element, flat_arr=None):
    """
    This method takes nested array as a parameter and
    returns as flattened version of it.
    :element : list
    example:    element=[1,[2,3,[4],5,[6]]]
                output = [1,2,3,4,5,6]
    """
    if flat_arr == None:
        flat_arr = []
    
    if not isinstance(element, list):
        flat_arr.append(element)
    else:
        for item in element:
            flatten(item, flat_arr)
    return flat_arr

in_list = [1,[2,3,[4],5,[6]]]
print(flatten(in_list))