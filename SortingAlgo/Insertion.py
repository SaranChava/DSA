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

def insertionSort(arr):
    for i in range(len(arr)):
        j=i
        while(j>0):
            if(arr[j]<arr[j-1]):
                temp=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=temp
                j-=1
            else:
                break

    return arr

inputFileName="N:\GitRepo\DSA\Testcases\SortingAlgo.txt"
arr=input(inputFileName)
for ls in arr:
    print(insertionSort(ls))