from math import factorial


def choose(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def main():
    # Every path from top left to bottom right consists of precisely 20 'right'
    # movements and precisely 20 'down' movements. Any arrangements of these 40
    # movements is a valid path to the bottom, and each arrangement is
    # characterised by the position of the 20 'right' movements within the list
    # of 40, so there are 40 choose 20 routes.
    return choose(40, 20)
    # 137846528820
