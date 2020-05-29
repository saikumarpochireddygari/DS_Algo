def quicksort(arr,p,r):
    """
    This function is used to perform quicksort algoritm on the array and return
    the sorted array in assencding order
    """
    #test_array= [54, 26, 93, 17, 77, 31, 44, 55]

    q=partion(arr,p,r)
    quicksort(arr,p,q-1)
    quicksort(arr,q+1,r)

def partion(arr,p,r):
    """
    the partion logic
    """
    for j in range(p+1, r+1): #p=0
        #initialising pivot element as per algoritm
        i=p   #0
        pivot = arr[0]

        if arr[j] < pivot:
            i = i + 1
            #swap of two numbers
            arr[i], arr[j] = arr[j], arr[i]

    arr[p], arr[i] = arr[i], arr[p]

    return (i)

if __name__ == '__main__':
    test_array = [54, 26, 93, 17, 77, 31, 44, 55]
    quicksort(test_array, 0, len(test_array)-1 )


















            
