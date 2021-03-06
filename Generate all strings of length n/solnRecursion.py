def rangeToList(k):
    result = []
    for i in range(1, k):
        result.append(str(i))
    return result


def baseKStrings(n, k):
    if n == 0:
        return []
    if n == 1:
        return rangeToList(k)
    return [x+y for x in baseKStrings(1, k) for y in baseKStrings(n-1, k)]


print(*baseKStrings(3, 3), sep="\n")
