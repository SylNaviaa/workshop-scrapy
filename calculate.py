def func():

    val = ['nothing', '8', '1']
    total = 0

    for i in val:
        try:
            total += int(i)
        except ValueError:
            pass
    print(total)


if __name__ == "__main__":
    func()