def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): list to print elements from.
        x (int): number of elements of my_list to print.

    Returns:
         number of elements printed.
    """
    ap = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            ap += 1
        except IndexError:
            break
    print("")
    return (ap)

