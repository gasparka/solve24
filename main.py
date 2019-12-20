from copy import copy
operators = ['+', '-', '*', '/']

def f(ls):
    if len(ls) == 1:
        try:
            if eval(ls[0]) == 24:
                print(ls[0])
            return
        except ZeroDivisionError:
            pass
    
    # all possible pairs
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i == j:
                continue
            
            a = ls[i]
            b = ls[j]
            for operator in operators:
                newls = copy(ls)
                newls.remove(a)
                newls.remove(b)
                newls.append(f"({a} {operator} {b})")
                f(newls)


def solve24(ls):
    f([str(x) for x in ls])

solve24([1, 5, 7, 10])