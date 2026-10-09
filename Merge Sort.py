def merge_sort(arr):
    if len(arr)>1:
        leftarr = arr[:len(arr)//2]
        rightarr = arr[len(arr)//2:]

        merge_sort(leftarr)
        merge_sort(rightarr)

        i=0
        j=0
        k=0
        
        while i<len(leftarr) and j<len(rightarr):
            if leftarr[i]<rightarr[j]:
                arr[k]=leftarr[i]
                i+=1
            else:
                arr[k]=rightarr[j]
                j+=1
            k+=1

        while i<len(leftarr):
            arr[k]=leftarr[i]
            i+=1
            k+=1
        while j<len(rightarr):
            arr[k]=rightarr[j]
            j+=1
            k+=1
        


arr = [3,8,6,9,4,1,2,5,7]
merge_sort(arr)
print(arr)
