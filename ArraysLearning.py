import numpy as np
nlist=[1,2,3]
narr=np.array([1,2,3])
#print(narr.dtype)

an_arr = np.array([1, 2, 3], dtype=np.float64)
#print(an_arr.dtype)

tw_arr=np.array([[1,2,3],[4,5,6]])
#print(tw_arr.ndim)
#print(tw_arr)

tr_arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(tr_arr[1][0][0])
print(tr_arr[1,0,0])
#print(tr_arr.ndim)
#print(tr_arr)
#print(tr_arr.shape)
#print(an_arr.shape)
#print(tw_arr.shape)

a = np.ones((2, 3),dtype=np.int32)
arrange_fun=np.arange(0,100,10,dtype=float)
#print(arrange_fun)

a = np.ones((2, 3),dtype=np.int32)
linspace_fun=np.linspace(1,5,5,endpoint=False,dtype=int)
#print(linspace_fun)

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b=a[1:,1:].copy()
print(b)
b[0,0]=2
print(b)
print(a.sum())


if __name__=='__main__':
    N,M=list(map(int,input().split()))
    arr=[]
    for _ in range(N):
        lst=list(map(int,input().split()))
        arr.append(lst)
    print(arr)