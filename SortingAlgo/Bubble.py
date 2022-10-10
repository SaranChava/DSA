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

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[i]>arr[j]):
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
    return arr

inputFileName="N:\GitRepo\DSA\Testcases\SortingAlgo.txt"
arr=input(inputFileName)
for ls in arr:
    print(bubbleSort(ls))