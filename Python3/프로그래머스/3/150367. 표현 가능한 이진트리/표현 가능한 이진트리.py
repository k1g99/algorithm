def check(a, b, n):
    mid = (a + b) // 2

    if (b - a) <= 3:
        if(n[mid]) == "1":
            return True

    if(n[mid]) == "1":
        return (check(a, mid, n) and check(mid + 1, b, n))

    else: # "0"
        z = "0" * (b - a)
        if(n[a:b] == z):
            return True
        else:
            return False


def add_zeros(str):
    sl = len(str)
    twos = 2
    for i in range(10):
        if(sl < twos):
            break
        twos *= 2
    twos -= 1
    # print(twos)
    
    z = "0" * (twos - sl)
    
    return z + str

def solution(numbers):
    answer = []
    for n in numbers:
        b = bin(n)
        bb = b[2:]
        
        l = add_zeros(bb)
        # print(l)
        
        if(check(0, len(l), l)):
            answer.append(1)
        else:
            answer.append(0)
        
    
    # print(check(0,3, "010"))
    # print(check(0,7, "1011111"))
    # print(check(0,7, "0001111"))

    
    return answer
