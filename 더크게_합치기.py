def solution(a, b):
    A = str(a) + str(b)
    B = str(b) + str(a)
    if int(A) >= int(B):
        answer = int(A)
    else:
        answer = int(B)
    return answer