def input(input_file):
    arr=[]
    try:
        f=open(input_file,'r')
        lines=f.readlines()
        for line in lines:
            arr.append(list(map(int,line.strip().split(','))))
        f.close()
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
    return arr

def selectionSort(arr):
    for i in range(len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[min]>arr[j]):
                min=j
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp
    return arr

inputFileName="N:\GitRepo\DSA\Testcases\SortingAlgo.txt"
arr=input(inputFileName)
print("Selection Sort")
for ls in arr:
    print(selectionSort(ls))