def lam3():
    def makeAdd(n):
        def addX(x):
            return x + n

        return addX


def lam31():
    makeAdd = lambda n: lambda x: x + n

    add_5 = makeAdd(5)
    print(add_5(5))


def lam1():
    """
    Создать список, в котором каждый элемент – кортеж из двух чисел.
    Отсортировать данный список по убыванию вторых элементов кортежей.
    """
    from operator import itemgetter
    n = 5
    a = [(n - i, i) for i in range(n)]
    print(a)
    # print(sorted(a, key=lambda tup: tup[1], reverse=True))
    print(sorted(a, key=itemgetter(1), reverse=True))


def lam2():
    """
    Отсортируйте список слов по убыванию длины слова.
    """
    words = "один два шесть восемь"
    list_words = words.split()
    print(list_words)
    print(sorted(list_words,
                 key=lambda w: len(w),
                 reverse=True))


# if __name__ == "__main__":
#     words = "один два шесть восемь"
#     for word in gen1(words):
#         print(word)

def gen1(words):
    listW = words.split()
    for word in listW:
        yield word


# def gen2(start, step):
#     # for i in range(start, step):
#     i = start
#     while True:
#         arg = yield i
#         if arg != None:
#             i = int(arg[0])
#             step = int(arg[1])
#         i += step
#
#
# if __name__ == "__main__":
#     step = 10
#     a = gen2(10, step)
#     while True:
#         l = a.send(None)
#         print(l)
#         if l > 100:
#             break
#     step += 5
#     print("--" * 6)
#     print(a.send((10, step)))
#     print("--" * 6)
#     while True:
#         l = a.send(None)
#         print(l)
#         if l > 200:
#             break


def my_random(x0: int = 1, a: int = 23, m: int = 3, c: int = 4):
    """
    Xn1 = (a * Xn + c) % m
    :param x0:
    :param a:
    :param m:
    :param c:
    :return:
    """
    while True:
        xn1 = (a * x0 + c) % m
        yield xn1
        x0 = xn1

if __name__ == "__main__":
    rnd = my_random()
    for _ in range(20):
        l=rnd()
        print(l)