n, k, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range (q):
    m = int(input())
    i = (m - k) % n
    print(a[i])
##i/p:
3 2 3
1 2 3
0
1
2
##o/p:
2
3
1
