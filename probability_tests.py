import math
import random

def jacobi_symbol(a, n):
    if n <= 1 or n % 2 == 0:
        return 0

    a = a % n
    res = 1

    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                res = -res

        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res

        a = a % n

    if n == 1:
        return res
    return 0


def fermat_primality_test(N, s):
    for _ in range(s):
        a = random.randint(1, N - 1)
        d = math.gcd(a, N)
        if d > 1:
            return "составное"

        if pow(a, N - 1, N) != 1:
            return "составное"

    return "неизвестно (вероятно простое)"


def solovay_strassen_test(N, s):
    if N % 2 == 0:
        return "составное"

    for _ in range(s):
        a = random.randint(2, N - 1)
        d = math.gcd(a, N)
        if d > 1:
            return "составное"

        jacobian = jacobi_symbol(a, N) % N
        val = pow(a, (N - 1) // 2, N)

        if val != jacobian:
            return "составное"

    return "неизвестно (вероятно простое)"


def miller_rabin_test(N, s):
    if N % 2 == 0:
        return "составное"

    t = 0
    u = N - 1
    while u % 2 == 0:
        t += 1
        u //= 2

    for _ in range(s):
        a = random.randint(1, N - 1)
        d = math.gcd(a, N)
        if d > 1:
            return "составное"

        r_0 = pow(a, u, N)

        if r_0 == 1 or r_0 == N - 1:
            continue

        is_composite = True
        curr_r = r_0
        for k in range(1, t):
            curr_r = pow(curr_r, 2, N)
            if curr_r == N - 1:
                is_composite = False
                break

        if is_composite:
            return "составное"

    return "неизвестно (вероятно простое)"