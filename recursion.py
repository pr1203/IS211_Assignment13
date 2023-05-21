def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    if s1 < s2:
        return -1
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])


if __name__ == '__main__':
    print("The 9th element is {}.".format(fibonacci(9)))
    print("The greatest common divisor of 164 and 348 is {}.".format(gcd(164, 348)))
    print("The result of str1 to str2 is {}.".format(compareTo("thisistr1", "thisIsstr2")))
