def matrixPattern(n):
    arr=[[0 for i in range(n)]for j in range(n)]
    p=1
    for k in range(n):
        j=k
        i=0
        while(j>=0):
            arr[i][j]=p
            p+=1
            i=i+1
            j=j-1
        for k in range(1,n,1):
            i=k
            j=n-1
            f=k
            while(j>=f):
                arr[i][j]=p
                p+=1
                i=i+1
                j=j-1
            for i in range(0,n,1):
                for j in range(0,n,1):
                    print(arr[i][j],end=" ")
if __name__=='__main__':
    n=3
    matrixPattern(n)

