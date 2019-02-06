def flatten(nested_arr):
    """
    This method takes nested array as a parameter and
    returns as flattened version of it.
    :nested_arr : list
    example:    nested_arr=[1,[2,3,[4],5,[6]]]
                output = [1,2,3,4,5,6]
    """
    flat_arr = []
    for item in nested_arr:
        if type(item) == type(list()):
            flat_arr.extend(flatten(item))
        else:
            flat_arr.append(item)
    return flat_arr
