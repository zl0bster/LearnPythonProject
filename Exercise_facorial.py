def factorial1(n: int):
    assert n > 0
    if n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factFab():
    cacheDict = {1: 1}

    def factorial2(n: int):
        def factorialCount(n: int,
                           firstVal=1,
                           cachVal=1):
            result = cachVal
            for i in range(firstVal, n + 1):
                result *= i
                if not (i in cacheDict):
                    cacheDict[i] = result
            return result

        assert n > 0
        if n == 1:
            return 1
        if n in cacheDict:
            return cacheDict[n]
        else:
            startVal = max(cacheDict)
            cachedVal = cacheDict[startVal]
            return factorialCount(n,
                                  startVal,
                                  cachedVal)

    factorial2.dct = cacheDict
    return factorial2


if __name__ == "__main__":
    for val in range(12, 15):
        print(val, factorial1(val))
    fx = factFab()
    for val in range(12, 15):
        print(val, fx(val))
    print("-" * 12)
    print(fx.dct)
