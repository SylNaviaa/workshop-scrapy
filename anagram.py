def func():
    word = sorted('racer')
    words_list = ['crazer', 'carer', 'racar', 'caers', 'caers', 'racer']

    for result in words_list:
        if word == sorted(result):
            print(result)

if __name__ == "__main__":
    func()