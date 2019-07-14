# 斐波那契数列
def f(n):
    """递归解法"""
    if n < 1:
        return 0
    elif n < 2:
        return 1
    else:
        return f(n-1) + f(n-2)


def f_2(n):
    """非递归解法"""
    priori2 = 0
    priori1 = 1
    if n == 0:
        return priori2
    elif n == 1:
        return priori1
    else:
        for i in range(1, n):
            temp = priori1
            priori1 = priori1 + priori2
            priori2 = temp
        return priori1


# 青蛙跳台阶问题(解法同上面一模一样)
def jump_nums(n):
    """递归解法"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return jump_nums(n-1) + jump_nums(n-2)


# 青蛙变态跳问题
def niupi_jump(n):
    """递归解法"""
    if n == 1:
        return 1
    else:
        num = 1
        for i in range(1, n):
            num += niupi_jump(i)
        return num


def niupi_jump2(n):
    """数学归纳法"""
    return 2**(n-1)
