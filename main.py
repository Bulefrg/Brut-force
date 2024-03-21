import string
from itertools import product
from time import time
from numpy import loadtxt
import hashlib
import itertools
import numpy as np

def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
    return False


def bruteforce(password, max_nchar=8):
    """Password brute-force algorithm.
    Parameters
    ----------
    password : string
        To-be-found password.
    max_nchar : int
        Maximum number of characters of password.
    Return
    ------
    bruteforce_password : string
        Brute-forced password
    """
    print('1) Comparing with most common passwords / first names')
    common_pass = loadtxt('probable-v2-top12000.txt', dtype=str)
    common_names = loadtxt('middle-names.txt', dtype=str, usecols=0)
    cp = [c for c in common_pass if c == password]
    cn = [c for c in common_names if c == password]
    cnl = [c.lower() for c in common_names if c.lower() == password]

    if len(cp) == 1:
        print('\nPassword:', cp)
        return cp
    if len(cn) == 1:
        print('\nPassword:', cn)
        return cn
    if len(cnl) == 1:
        print('\nPassword:', cnl)
        return cnl

    print('2) Digits cartesian product')
    for l in range(1, 9):
        generator = product(string.digits, repeat=int(l))
        print("\t..%d digit" % l)
        p = product_loop(password, generator)
        if p is not False:
            return p

    print('3) Digits + ASCII lowercase')
    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)
        generator = product(string.digits + string.ascii_lowercase,
                            repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            return p

    print('4) Digits + ASCII lower / upper + punctuation')
    # If it fails, we start brute-forcing the 'hard' way
    # Same as possible_char = string.printable[:-5]
    all_char = string.digits + string.ascii_letters + string.punctuation

    for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)
        generator = product(all_char, repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            return p

    # If all methods fail, fallback to bruteforce_attack
    attempts, guess = bruteforce_attack(password)
    if guess:
        print(f"Password cracked in {attempts} attempts. The password is {guess}.")
        return guess
    else:
        print(f"Password not cracked after {attempts} attempts.")
        return None


def bruteforce_attack(password_hash):
    chars = np.array(list(string.printable.strip()))
    attempts = 0
    for length in range(1, 9):  # Assuming maximum length of 8 for the password
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            if guess_hash == password_hash:
                return (attempts, guess)
    return (attempts, None)


start = time()

password = input("Enter the password to crack: ")
bruteforce(password)
end = time()
print('Total time: %.2f seconds' % (end - start))
