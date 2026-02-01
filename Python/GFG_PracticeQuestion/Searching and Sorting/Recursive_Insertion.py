# Pick element arr[i] and isnert it into sorted sequence arr[0...i-1]


def insertionSort(arr, n):
    if n<=1:
        return
    insertionSort(arr,n-1)
    last = arr[n-1]
    j = n-2
    while(j>=0 and arr[j] > last):
        arr[j+1] = arr[j]
        j = j-1
        arr[j+1] = last
if __name__ == '__main__':
    A = [-7,11,6,0,-3,5,10,2]
    n = len(A)
    insertionSort(A,n)
    print(A)

#------------------------------------------