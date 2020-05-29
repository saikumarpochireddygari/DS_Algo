
def insertionSort(arr):
  """
  This Function is Used to perform Insertion sort agorithm on the given array and sort the array in the \n
   ascending order.
  """
  myArray = arr 

  if myArray == [ ]:
        return ("Empty array is passed")
  elif len(myArray) == 1:
        return (myArray)
  else:
    for j in range (1,len(myArray)):
      key = myArray[j]
      i=j-1
      while (i >= 0) & (key < myArray[i]):
         
          myArray[i+1] = myArray[i]
          i = i-1
      myArray[i+1] = key
    return(myArray)

if __name__ == "__main__":
    testarr1 = [3,7,2,10,29,1]
    testarr2 = [2]
    testarr3 = [ ]
    print(insertionSort(testarr1))


