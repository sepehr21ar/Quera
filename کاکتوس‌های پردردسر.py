groups = int(input())

group_members = list(map(int,input().split()))
for i in group_members :
    # print(i)
    if  i > 3 and groups<=100:
        print('*')
    else:
        print('*' * i)
