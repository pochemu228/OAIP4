def template(z, y, x):
    if z + y > x and z + x > y and y + x > z:
        print('Периметр: {z + y + x}')
        p = (z + y + x) / 2
        print(f'Площадь: {(p * (p * z) * (p - y) * (p - x)) ** 0.5}'
        f'\nРавнобедренный: {"да" if z == y or z == x or y == x else "нет"}'
        f'\nРавносторонний: {"да" if z == y == x else "нет"}')

    else:
        print('None')

template(5, 4, 5)
