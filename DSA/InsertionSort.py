def insertion_sort(arr):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            if key<arr[j]:
                arr[j+1]=arr[j]
                j-=1
        arr[j+1]=key

    return arr    


if __name__ == '__main__':
    arr=[3,5,1,2,9,8,4]
    insertion_sort(arr)
    print(arr)    

