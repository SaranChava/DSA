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

def factorial(n):
    while(n>0):
        return n*factorial(n-1)
    return 1

inputFileName="/Users/saran/GoaldotIO/DSA/Testcases/factorial.txt"
arr=input(inputFileName)
for ls in arr:
    print(factorial(ls[0]))