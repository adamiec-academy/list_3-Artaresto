def is_perfect(n):
    a = 0
    if n < 6:
        return False
    for i in range(1, n):
        if (n % i) == 0:
            a = a + i
    if a == n:
        return True

def get_perfect_numbers(n):
    result = []
    a = n
    while len(result) != n: 
        for _ in range(a+1):
            if is_perfect(a) == True and a not in result:
                result.append(a)
            else:
                a += 1
    return result
