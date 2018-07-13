def sqrt(A):
    if A == 0:
        return 0
    high = A
    low = 1
    while high >= low:
        mid = (high+low)/2
        if mid**2  == A:
            return mid
        elif mid**2 > A:
            high = mid - 1
        elif mid**2 < A:
            low = mid + 1
    return high
if __name__ == "__main__":
    A = int(input())
    print sqrt(A=A)