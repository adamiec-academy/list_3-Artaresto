def fibonacci_sequence(n):
    result = []
    while len(result) != n:
            if n == 1: 
                result.append(0)
            elif n == 2 or len(result) == 0:
                result.append(0)
                result.append(1)
                if n > 2:
                    result.append(1)
            else:
                result.append(result[-1] + result[-2])
    return result
