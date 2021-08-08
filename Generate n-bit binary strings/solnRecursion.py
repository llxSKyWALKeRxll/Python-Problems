def binaryStrings(n):
    if n==0: return []
    if n==1: return ["0", "1"]
    return [digit + binaryString for digit in binaryStrings(1) for binaryString in binaryStrings(n-1)]

print(*binaryStrings(15), sep="\n")