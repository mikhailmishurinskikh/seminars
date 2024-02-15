def qsort(array):
    try:
        if len(array) < 2: return array
        pivot = array[0]
        right = [i for i in array[1:] if i >= pivot]
        left = [i for i in array[1:] if i < pivot]
        return qsort(left) + [pivot] + qsort(right)
    except TypeError: return 'error'

