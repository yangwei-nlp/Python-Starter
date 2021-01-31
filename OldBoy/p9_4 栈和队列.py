# 记住原则，栈：后进先出；队列：先进先出。在编程中，我们常常用到这两个简单的原则来帮助我们解决复杂的问题。

# 检测括号是否有效
def bracket_match(s):
    """
    检查括号是否有效
    """
    stack = []
    d = {'{':'}', '(': ')', '[': ']'}
    for cha in s:
        if cha in ['(', '[', '{']:
            stack.append(cha)
        elif cha == d[stack[-1]]:
            # 消掉，如[]
            stack.pop()
        elif not stack:
            # 来了个反括号，如]
            return False
        else:
            # 符号不匹配，如[)
            return False
    return True if not stack else False

print(bracket_match("()()[]{}{}()"))
print(bracket_match("()([)[]{}{}()"))



# 教科书写法 P141
def check_parens(text):
    parens = "({["
    all_parens = "({[]})"
    opp_parens = {'(': ')', '[': ']', '{': '}'}

    def paren_generator(text):
        # 生成括号和其位置
        text_len = len(text)
        i = 0
        while True:
            while i < text_len and text[i] not in all_parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    
    stack = []
    for pr, i in paren_generator(text):
        if pr in parens:
            stack.append(pr)
        elif not stack:
            return False
        elif opp_parens[stack.pop()] != pr:
            return False
    return True if not stack else False



print(check_parens("()())(){(}{}()[]"))
print(check_parens("()()(){}{}()[]["))
print(check_parens("()()(){}{}()[][]"))
