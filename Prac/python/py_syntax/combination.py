def nCr(arr, r):
    n = len(arr)
    if (n == r):
        return [arr]
    if (r == 1):
        return [[x] for x in arr]
    # nCr => for 로 1개씩 지정 -> 나머지는 다시 c'C(r-1)
    ans = []
    for i, a in enumerate(arr):
        sub_nCr = nCr(arr[i+1:], r - 1)
        sub_nCr = [[a] + x for x in sub_nCr]
        ans += sub_nCr

    return ans


print(nCr([1,2,3,4,5], 5))
print(nCr([1,2,3,4,5], 1))
print(nCr([1,2,3,4,5], 3))
