#풀이1
def solution(n):
    odd_list = []
    even_list = []
    for i in range(1, n+1):
        if n % 2 == 1:
            if i % 2 == 1:
                odd_list.append(i)
                answer = sum(odd_list)
        else:
            if i % 2 == 0:
                even_list.append(i**2)
                answer = sum(even_list)
    return answer

#풀이2
def solution(n):
    answer = 0
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            answer += i
    else:
        for i in range(2, n+1, 2):
            answer += (i**2)
    return answer