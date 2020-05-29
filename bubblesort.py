def bubbleSort(arr):
    """
    This function is used to sort the array adcending order
    """
    #Test array = [ 3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]

    for i in range(0,len(arr)):
        for j in range (0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    return (arr)

if __name__ == "__main__":
    arr=[3,44,38,5,47,15,36,26,27,2,46,4,19,50,48,1]
    print(bubbleSort(arr))
