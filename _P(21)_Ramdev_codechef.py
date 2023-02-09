l,b = map(int,input().split())
N = int(input())
result = 0
for i in range(0,N):
    L,B = map(int,input().split())
    result += max((L/b)*(B/l),(L/l)*(B/b))

print(int(result))