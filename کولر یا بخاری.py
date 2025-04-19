days = int(input())
target = ""
degree= list(map(int, input().split()))
for i in degree:
    if i > 15:
        print("cooler")
    elif i <= 15:
        print("heater")
