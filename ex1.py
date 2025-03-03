def horse2(position):
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

    x = ord(position[0]) - ord("a")
    y = int(position[1]) - 1

    total_moves = []

    for move in moves:
        new_x = x + move[0]
        new_y = y + move[1]

        if 0 <= new_x < 8 and 0 <= new_y < 8:
            new_position = chr(new_x + ord("a")) + str(new_y + 1)
            total_moves.append(new_position)

    return total_moves

def main():
    print(horse2("a3"))

if __name__ == "__main__":
    main()
