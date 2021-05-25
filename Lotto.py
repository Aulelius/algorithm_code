def solve(a, index, lotto):
    // 조건문 로또 번호의 갯수가 6개인 경우 출력한다.
    if len(lotto) == 6:
        print(' '.join(map(str,lotto)))
        return
        
        
    // 기본이 길이의 갯수와 일치하는 경우     
    if index == len(a):
        return
    solve(a, index+1, lotto+[a[index]])
    solve(a, index+1, lotto)

while True:
    n, *a = list(map(int,input().split()))
    if n == 0:
        break
    solve(a, 0, [])
    print()
