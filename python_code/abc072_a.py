def print_ans(X,t):
    """Print max(X-t,0)

    Parameters
    --------------

    Examples
    ------------
    >>> print_ans(3,0)
    3
    >>> print_ans(3,2)
    1
    >>> print_ans(2,5)
    0
    """
    print(max(0,X-t))

if __name__ == '__main__':
    X,t = map(int,input().split())
    print_ans(X,t)
