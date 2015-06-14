# -*- coding: utf-8 -*-
__author__ = 'Denis Titusov, sescusu@gmail.com'

from fractions import gcd
import sys

def isprime(number):
    max_dev = int(number**0.5+1)
    for i in range(2, max_dev):
        if not number % i:
            return False
    return True

def eulers_loop(number):
    coprime_ints = [1]
    for i in range(2, number):
        if gcd(number, i) == 1:
            coprime_ints.append(i)
    return len(set(coprime_ints))

def count_euler(number):
    if not isinstance(number, int):
        raise TypeError('Euler\'s totient finction could not be called for type: {0} of object {1}'.format(
            type(number), number
        ))
    elif number < 1:
        raise ValueError('Euler\'s function could be called for natural number')
    elif number == 1:
        return 1
    elif isprime(number):
        return number - 1
    for num in range(number-1):
        return eulers_loop(number)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
    else:
        number = int(input('Input number: '))
    print(count_euler(number))
