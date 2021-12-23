#!/usr/bin/python3
if __name__ == "__main__":

    import calculator_1 as f
    a = 10
    b = 5
    print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}".format(a, b,f.add(a, b),a, b, f.sub(a, b), a, b, f.mul(a, b), a, b, f.div(a, b)))
