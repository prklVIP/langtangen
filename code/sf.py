from math import pi, sin

def S(t, n, T):
    return 4 / pi * sum(sin(2 * (2*i - 1) * pi * t / T) / (2*i - 1) for i in range(1, n + 1))

def f(t, T):
    return 1 if 0 < t < T/2 else -1 if T/2 < t < T else 0

def test():
    print("   n |  alpha |    error ")
    print("-----+--------+----------")
    T = 2*pi
    for n in 1, 3, 5, 10, 30, 100:
        for alpha in 0.01, 0.25, 0.49:
            t = alpha * T
            error = f(t, T) - S(t, n, T)
            print(f" {n:3} | {alpha:6} | {error:8.4f}")

if __name__ == '__main__':
     import argparse
     parser = argparse.ArgumentParser()
     parser.add_argument('-n', type=int, default=20, metavar='n')
     parser.add_argument('-alpha', type=int, default=0.2, metavar='alpha')
     parser.add_argument('-T', type=int, default=2*pi, metavar='T')
     args = parser.parse_args()
     t = args.alpha * args.T
     error = f(t, args.T) - S(t, args.n, args.T)
     print(f"error = {error:8.4f}")
