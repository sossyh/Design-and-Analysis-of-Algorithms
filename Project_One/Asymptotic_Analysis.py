import math

def compute_sum(a, b, n):
    """
    This function calculates the sum of individual elements of two arrays a, and b by iterating with sizes based on sqrt(2) and sqrt(3).

    Parameters:
        a is (list of int or float) - list of numbers
        b is (list of int or float) - list of numbers
        n is (int/float) - Upper bound for iteration (most importantly if the sizes of the two arrays are not equal)

    Returns:
        float: The sum or total
    """
    summ = 0
    j = 5
    while j < n / 2:
        k = 5
        while k < n:
            summ += a[j] * b[k]
            k = int(k * math.sqrt(2))  # ensure integer index
        j = int(j * math.sqrt(3))      # ensure integer index
    return summ
