count, killed = list(map(int, input().split()))
year = int(input())
for i in range(year):
    count+=count
    count -= killed
print(count)
