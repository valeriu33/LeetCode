import copy

towers = [["@", "*", "."], [], []]


def move(from_t: int, to_t: int):
    print("Moving from tower", from_t, "to", to_t)
    towers[to_t - 1].append(towers[from_t - 1].pop())
    aux = copy.deepcopy(towers)

    for i in range(3):
        aux[i].reverse()
        print(i, end="  ")
        while aux[i]:
            print(aux[i].pop(), end=" ")
        print()
    print("\n\n")


def hanoi(n: int, from_t: int, through_t: int, to_t: int):
    print("1  @ * .\n2\n3\n\n\n")
    if n == 0:
        pass
    else:
        hanoi(n - 1, from_t, to_t, through_t)
        move(from_t, to_t)
        hanoi(n - 1, through_t, from_t, to_t)
