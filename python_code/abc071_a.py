def print_ans(x,a,b):
    """Print min(abs(x-a),abs(x-b))

    Parameters
    --------------

    Examples
    ------------
    >>> print_ans(3,0,1)
    B
    >>> print_ans(3,2,5)
    A
    >>> print_ans(2,5,9)
    A
    """
    #print(min(abs(x-a),abs(x-b)))
    if min(abs(x-a),abs(x-b)) == abs(x-b):
      print("B")
    else:
      print("A")




if __name__ == '__main__':
    x,a,b = map(int,input().split())
    print_ans(x,a,b)
