def solve():
    cmd = input()
    arr_len = int(input())
    arr_str = input()
    dir = True

    # 여기서 일단 arr_len보다 cmd에서 'D'가 더 많으면 error출력하고 끝
    count_D = cmd.count('D')
    if(count_D>arr_len):
        print('error')
        return
    elif(count_D == arr_len):
        print('[]')
        return

    if(arr_str == '[]'):
        print(arr_str)
        return 

    arr = arr_str[1:-1]
    arr = list(map(int, arr.split(",")))
    # print(arr)

    start = 0
    end = len(arr)

    for c in cmd:
        if(c == 'R'):
            dir = not dir
        elif(c == 'D'):
            if(dir):
                start += 1
            else:
                end -= 1
    
    if(dir):
        print('['+','.join(map(str, arr[start:end]))+']')
    else:
        print('['+','.join(map(str, reversed(arr[start:end])))+']')


N = int(input())
for _ in range(N):
    solve()