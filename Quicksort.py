def Quicksort(L, H: int):
    global arr
    if L >= H: return None
    tmp = arr[(L + H) // 2]
    i = L
    j = H
    while i < j:
        while arr[i] < tmp: i += 1
        while arr[j] > tmp: j -= 1
        if i <=j:
            if i<j:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
            i += 1
            j -= 1
    Quicksort(L,j)
    Quicksort(i,H)

f = open("input.txt")
n = int(f.readline())
arr = list(map(int,f.readline().split()))
f = open("output.txt", "w")

Quicksort(0,n-1)
for i in range(n):
    f.write(str(arr[i]) + ' ')