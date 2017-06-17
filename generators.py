def chain(iterable_one, iterable_two):
    for element in iterable_one:
        yield element
    for element in iterable_two:
        yield element


def compress(iterable, mask):
    assert len(mask) == len(iterable)
    for element, bit in zip(iterable, mask):
        if bit:
            yield element


def cycle(iterable):
    while True:
        for element in iterable:
            yield element


if __name__ == "__main__":
    print("First task:\n")

    print(list(chain(range(0, 4), range(4, 8))))
    print("-------------------------------\nSecond task:\n")

    print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
    print("-------------------------------\nThird task:\n")

    endless = cycle(range(0, 10))
    for i in range(25):
        print(next(endless))

        # Uncomment next two lines for an infinite loop

        # for item in endless:
        #   print(item)
