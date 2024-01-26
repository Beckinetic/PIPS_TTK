import numpy as np

# Q2.2P.9 --------------------------------------------------------------------------------------------------------------
# Why?
# Separate modules may help in organizing code into manageable pieces. And by placing functions in modules, we can
# easily reuse them across different programs without copying the code. One other benefit is that separate modules can
# help avoid naming conflicts by segregating functions into different namespaces of different files.
def prime(n):
    """
    Generate the first 'n' prime numbers starting from 2.
    Parameters:
    n (int): A positive integer specifying the number of prime numbers to generate.
    Returns:
    numpy.ndarray: An array of the first 'n' prime numbers.
    Example:
    prime(10)
    array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    """
    try:
        if n < 1:
            raise ValueError('n must be greater than 1')

        prime_list = np.array([2])
        x = 3
        while (len(prime_list) < n):
            for i in prime_list:
                if x % i == 0:
                    # x is not a prime number
                    break
                if i == prime_list[-1]:
                    # x is a prime number, append it to the array
                    prime_list = np.append(prime_list, x)
            x += 1
        return prime_list
    except Exception as e:
        raise Exception(e)

# Q2.2P.10 -------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    assert np.array_equal(prime(1), np.array([2])), "Test failed: prime(1) should return [2]"
    assert prime(10)[-1] == 29, "Test failed: The last element of prime(10) should be 29"
    assert np.array_equal(prime(3), np.array([2, 3, 5])), "Test failed: prime(3) should return [2, 3, 5]"
    assert np.array_equal(prime(5), np.array([2, 3, 5, 7, 11])), "Test failed: prime(5) should return [2, 3, 5, 7, 11]"
    print("Tests passed")