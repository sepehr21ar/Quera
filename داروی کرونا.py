Shekarestan_cases = int(input())
Shekarestan_die = int(input())

Namakestan_cases = int(input())
Namakestan_die = int(input())


if (Shekarestan_cases - Shekarestan_die) < (Namakestan_cases - Namakestan_die):
    print('Namakestan')
    
elif (Shekarestan_cases - Shekarestan_die) > (Namakestan_cases - Namakestan_die):
    print('Shekarestan')

else:
    print('Equal')