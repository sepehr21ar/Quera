mouse, trap = list(map(int, input().split()))

if mouse < trap:
    print((trap - mouse)*"R")
elif mouse > trap:
    print((mouse - trap)*"L")
else:
    print('Saal Noo Mobarak!')