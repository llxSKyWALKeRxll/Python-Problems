def checkArraySorted(A):
    if len(A)==1:
        return True
    return A[0] <= A[1] and checkArraySorted(A[1:])

if __name__=="__main__":
    A = [1,5,8,16,16,16,21,31,45]
    print(checkArraySorted(A))
