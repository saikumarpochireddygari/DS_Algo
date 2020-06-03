def selectionsort(arr):
    """
    This function is used to perform selection sort on array and return
    a sorted ascending array
    """
    #test array = [10, 8, 1, 40, 20, 7]
    #test array = [10, 1, 40, 20, 7]
    #test_array = []
    #test_array = [2]
    if len(arr) == 0:
        return ("The given array is empty please enter an array of atleast size one")

    elif len(arr) == 1:
        return ("The given array is already sorted here is the entered array: {}".format(arr))

    else:
        for i in range(len(arr)):
            index_of_ele=i
            for j in range(i+1 , len(arr)):
                if arr[j] <= arr[index_of_ele]:
                    index_of_ele = j
            arr[i], arr[index_of_ele] = arr[index_of_ele], arr[i]
        return (arr)


if __name__ == '__main__':
    test_array = [10, 8, 1, 40, 20, 7]
    test_array_one = [10]
    test_array_two = []
    print(selectionsort(test_array))
    print(selectionsort(test_array_one))
    print(selectionsort(test_array_two))
