max = 0
while True:
    a=int(input('Masukan Bilangan :'))
    if max < a:
        max = a
    if a == 0:
        break
print('\n Bilangan Terbesar Adalah :', max)