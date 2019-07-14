def maxProductAfterCutting_solution(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    products = [0] * (length + 1)
    # 为什么要单独将0123这几个值列出来？
    # 比如长度为6，可以切成2+4和3+3，那么长度为2的那一段并不需要再次切分，因为不切，乘数为2*f(4)，切了为1*f(4)，
    # 同理长度为3的那一段也不需要再次切分，不切，为3*f(3)，切了为2*f(3)
    # 什么意思呢，就是说，当长度为4以下的时候，切分得到的乘积怎么样都会小于长度本身，为了考虑这种特殊情况我们将
    # 它们单独写出来，如下。
    # 其他的任意长度，比如5，乘积得到6，大于5，同理其他任意数，都是不小于长度本身。
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    for i in range(4, length + 1):
        # 外层for循环是需要记录长度为4到length-1子问题的解(动态规划)
        max = 0
        for j in range(1, i // 2 + 1):
            # 里层for循环是在最大的乘积。貌似1个for循环好像只有一刀，但是要知道的是，
            # 我只要切下第一刀，根据之前记录的子问题的解就可以快速得到最大乘积
            # 所以第一刀考虑好就OK了
            product = products[j] * products[i - j]
            if max < product:
                max = product
        products[i] = max

    max = products[length]
    return max


print(maxProductAfterCutting_solution(8))