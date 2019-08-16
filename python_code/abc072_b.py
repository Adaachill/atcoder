def print_ans(s):
    """Print substring of s, odd_th char

    Parameters
    --------------
    Examples
    >>> print_ans("a")
    a
    >>> print_ans("ab") 
    a
    >>> print_ans("aibc")
    ab

    """
    for i in range(0,len(s),2):
        print(s[i],end="")

if __name__ == '__main__':
    s = input()
    print_ans(s)

