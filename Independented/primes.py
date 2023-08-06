from math import sqrt, exp
from numpy import log
from time import time
import matplotlib.pyplot as plt

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]
XLNXES = []
DIFFES = []
NUM = 1000


def is_prime(n):
    sqn = sqrt(n)
    for i in PRIMES:
        if i > sqn:
            PRIMES.append(n)
            return True
        if n % i == 0: return False


i = PRIMES[-1] + 2
while len(PRIMES) < NUM:
    is_prime(i)
    i += 2

stt = time()
for i in range(0, NUM):
    x = i + 1
    XLNXES.append(x * log(x))
    ca = PRIMES[i] - XLNXES[i]
    # print(ca)
    DIFFES.append(ca)
    # if ca < 0: raise Exception(f'at {i + 1}th prime, predicted minimum is bigger than the prime!\n{PRIMES[i]} < {XLNXES[i]}')
# print(time() - stt)

'''for i in DIFFES:
    print(f'{round(i, 2)}')'''

plt.plot(PRIMES)
plt.plot(XLNXES)
plt.plot(DIFFES)
plt.show()
