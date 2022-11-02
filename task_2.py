def fibonacci_sequence(n):
    result = []
    a = n
    while len(result) != n:
            if n == 1: 
                result.append(0)
            elif n == 2:
                result.append(0)
                result.append(1)
            elif n > 2:
                result.append((a - 1) + (a - 2))
                a+=1
    return result
