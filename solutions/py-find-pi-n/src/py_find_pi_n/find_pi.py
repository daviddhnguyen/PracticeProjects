from decimal import Decimal, getcontext

def find_pi(n):
    # Set precision a few digits higher than n for accuracy
    if n>50:
        return "Error too many digits; enter 50 or less!"

    getcontext().prec = n + 2

    # Chudnovsky algorithm constants
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, n):
        M = (M * (K**3 - 16*K)) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    # Return as string, trimming the extra digits
    return str(pi)[:n+2]  # 1 digit before the decimal + n digits after