def print_ans(s):
    """Print substring of s, odd_th char
    >>> print_ans([1])
    1
    >>> print_ans([1,4])
    1
    >>> print_ans([0,3,4,5])
    3
    >>> print_ans([1,2,3,2,5,6])
    4
    
    """
    b = list(set(s))
    ans = 1
    """TLE 
    for i in range(b[0],b[-1]+1):
        ans = max(b.count(i)+b.count(i+1)+b.count(i+2),ans)
    """
    
    for i in range(len(b)):
        ans = max(ans,s.count(b[i])+s.count(b[i]+1)+s.count(b[i]+2))
    print(ans)

if __name__ == '__main__':
    N = input()
    a = list(map(int,input().split()))
    print_ans(a)

