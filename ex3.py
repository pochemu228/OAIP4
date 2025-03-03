def func_table(f, x_max, y_max):
    for y in range(y_max + 1):
        table = []
        for x in range(x_max + 1):

            value = eval(f, {'x': x, 'y': y})
            table.append(str(value))
        print("\t".join(table))

func_table("x ** 2 + y", 3, 5)
