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

#Dis

def bubbleSortRecursion(arr,n):
    return 0

inputFileName="N:\GitRepo\DSA\Testcases\SortingAlgo.txt"
arr=input(inputFileName)
for ls in arr:
    print(bubbleSortRecursion(ls,0))