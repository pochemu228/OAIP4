def main():
    def horse2(place):
        letters = 'abcdefgh'
        numeral = '12345678'

        col = place[0]
        row = int(place[1])

        result = []

        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i * j) == 2:
                    new_col = letters.find(col) + i
                    new_row = row + j

                    if 0 <= new_col < len(letters) and 1 <= new_row <= len(numeral):
                        result.append(letters[new_col] + str(new_row))

        return result

    place = input("Введите положение коня (например, f2): ")
    possible_moves = horse2(place)
    print(f'Ходы коня из места {place}: {possible_moves}')

if __name__ == '__main__':
    main()
