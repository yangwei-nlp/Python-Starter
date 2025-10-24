"""
https://claude.ai/chat/b432f565-cb86-418a-bcdf-99dd94d17089

open(file, 'r') 配合 for line in f: 并不会一次性加载整个文件到内存！
这是Python文件迭代器的特性：
pythonwith open(log_file_path, 'r', encoding='utf-8') as f:
    for line in f:  # 这是逐行读取，每次只在内存中保留一行
        process(line)
工作原理：

文件对象是迭代器：Python的文件对象实现了迭代器协议
惰性加载：每次循环只读取一行到内存，处理完后才读取下一行
内存占用：只有当前行 + 缓冲区（通常8KB左右）在内存中

与一次性加载的区别：
python# ❌ 这样会超内存（一次性加载）
with open(file, 'r') as f:
    all_lines = f.read()  # 整个文件加载到内存
    # 或
    all_lines = f.readlines()  # 所有行加载到列表

# ✅ 这样不会超内存（逐行读取）
with open(file, 'r') as f:
    for line in f:  # 逐行迭代，内存占用恒定
        process(line)
"""

"""
Question:

2)日志文件中Top N统计
你有一个超大规模的日志文件(假设大小可达几十GB，单机内存无法一次性加载)。
日志2025-08-25 12:00:01,user id-123,action=click,item_id=456
请实现一个Python函数，统计出现次数最多的前K个userid，输出结果为一个列表，如:
[("123"，10500)，(999"，8765),
要求:
1.机器内存有限，无法一次性把整个文件读进内存
2.要求支持并发处理
3.提供具体思路和具体实现代码
"""

# 首先理解最小堆

import heapq

"""
===========================================
最小堆（Min Heap）详细讲解
===========================================

1. 什么是最小堆？
-----------------
最小堆是一种特殊的二叉树结构，满足：
- 父节点的值 ≤ 子节点的值
- 堆顶（根节点）永远是最小值

示例：
        3          <- 堆顶（最小值）
       / \
      5   8
     / \
    9   7

特点：
- 查找最小值：O(1) 时间，直接访问堆顶 heap[0]
- 插入元素：O(log n) 时间
- 删除最小值：O(log n) 时间
"""

print("=" * 60)
print("第一部分：最小堆基本操作演示")
print("=" * 60)

# 创建一个空堆
heap = []

# 插入元素
print("\n1. 依次插入元素: 5, 3, 8, 1, 9")
for num in [5, 3, 8, 1, 9]:
    heapq.heappush(heap, num)
    print(f"   插入 {num} 后，堆内容: {heap}, 堆顶(最小值): {heap[0]}")

# 堆顶永远是最小值
print(f"\n2. 堆顶元素（最小值）: {heap[0]}")

# 弹出最小值
print(f"\n3. 弹出最小值: {heapq.heappop(heap)}")
print(f"   弹出后堆内容: {heap}, 新堆顶: {heap[0]}")

print("\n" + "=" * 60)
print("第二部分：为什么用最小堆找Top K？")
print("=" * 60)

print("""
问题：找出 [3, 5, 1, 8, 9, 2, 7, 10] 中最大的3个数

方法1：排序（不推荐）
- 时间复杂度：O(n*log(n))
- 空间复杂度：O(n)
- 需要对所有数据排序

方法2：最小堆（推荐）✓
- 时间复杂度：O(n*log(k))，k<<n 时效率更高
- 空间复杂度：O(k)，只需要保存k个元素
- 核心思想：维护一个大小为k的最小堆，堆中保存当前最大的k个数
""")


def find_top_k_demo(nums, k):
    """演示用最小堆找Top K的过程"""
    print(f"\n原始数据: {nums}")
    print(f"目标: 找出最大的 {k} 个数\n")

    min_heap = []

    for i, num in enumerate(nums):
        print(f"步骤 {i + 1}: 处理数字 {num}")

        if len(min_heap) < k:
            # 堆未满，直接插入
            heapq.heappush(min_heap, num)
            print(f"   → 堆未满(当前{len(min_heap)}个)，直接插入")
            print(f"   → 堆内容: {sorted(min_heap, reverse=True)}, 堆顶(最小): {min_heap[0]}")
        else:
            # 堆已满，比较堆顶
            if num > min_heap[0]:
                old_min = min_heap[0]
                heapq.heapreplace(min_heap, num)
                print(f"   → {num} > 堆顶{old_min}，替换堆顶")
                print(f"   → 堆内容: {sorted(min_heap, reverse=True)}, 新堆顶(最小): {min_heap[0]}")
            else:
                print(f"   → {num} ≤ 堆顶{min_heap[0]}，不处理")
                print(f"   → 堆内容: {sorted(min_heap, reverse=True)}")
        print()

    # 最终结果按降序排列
    result = sorted(min_heap, reverse=True)
    print(f"最终结果（Top {k}）: {result}")
    return result


# 演示
find_top_k_demo([3, 5, 1, 8, 9, 2, 7, 10], k=3)

print("\n" + "=" * 60)
print("第三部分：代码逐行解析")
print("=" * 60)

print("""
假设我们有这样的数据：
user_count = {
    "user_1": 10,    # 出现10次
    "user_2": 50,    # 出现50次
    "user_3": 5,     # 出现5次
    "user_4": 30,    # 出现30次
    "user_5": 80,    # 出现80次
}

要找出现次数最多的前3个user_id (k=3)
""")

# 模拟实际场景
user_count = {
    "user_1": 10,
    "user_2": 50,
    "user_3": 5,
    "user_4": 30,
    "user_5": 80,
}
k = 3

print("\n代码执行过程：\n")
print("min_heap = []  # 创建空堆\n")

min_heap = []
step = 0

for user_id, count in user_count.items():
    step += 1
    print(f"{'=' * 50}")
    print(f"循环第 {step} 次: 处理 {user_id}, count={count}")
    print(f"{'=' * 50}")

    if len(min_heap) < k:
        print(f"1. 判断: len(min_heap)={len(min_heap)} < k={k}  → True")
        print(f"2. 执行: heappush(min_heap, ({count}, '{user_id}'))")
        heapq.heappush(min_heap, (count, user_id))
        print(f"3. 结果: min_heap = {min_heap}")
        if min_heap:
            print(f"4. 堆顶（最小值）: {min_heap[0]} → count={min_heap[0][0]}")
    else:
        print(f"1. 判断: len(min_heap)={len(min_heap)} < k={k}  → False")
        print(f"2. 堆已满，检查是否需要替换")
        print(f"3. 当前count={count}, 堆顶count={min_heap[0][0]}")

        if count > min_heap[0][0]:
            print(f"4. 判断: {count} > {min_heap[0][0]}  → True，需要替换")
            old_top = min_heap[0]
            heapq.heapreplace(min_heap, (count, user_id))
            print(f"5. 执行: heapreplace，弹出 {old_top}，插入 ({count}, '{user_id}')")
            print(f"6. 结果: min_heap = {min_heap}")
            print(f"7. 新堆顶: {min_heap[0]} → count={min_heap[0][0]}")
        else:
            print(f"4. 判断: {count} > {min_heap[0][0]}  → False，不替换")
            print(f"5. min_heap 保持不变: {min_heap}")

    print()

print(f"{'=' * 50}")
print("循环结束后的堆状态")
print(f"{'=' * 50}")
print(f"min_heap = {min_heap}")
print(f"\n注意：堆中的元素不是完全有序的，只保证堆顶是最小值")

print(f"\n{'=' * 50}")
print("最后一步：排序输出")
print(f"{'=' * 50}")
print(f"sorted(min_heap, reverse=True) = {sorted(min_heap, reverse=True)}")

result = [(user_id, count) for count, user_id in sorted(min_heap, reverse=True)]
print(f"\n转换为 (user_id, count) 格式:")
for user_id, count in result:
    print(f'  ("{user_id}", {count})')

print("\n" + "=" * 60)
print("第四部分：关键问题解答")
print("=" * 60)

print("""
Q1: 为什么用最小堆而不是最大堆？
A1: 因为我们要找"最大的k个"，用最小堆可以快速淘汰小的值
    - 堆顶是当前k个数中最小的
    - 新来的数如果比堆顶大，就替换堆顶
    - 新来的数如果比堆顶小，说明它肯定不在Top K中，直接忽略

Q2: 为什么是 (count, user_id) 而不是 (user_id, count)？
A2: 因为Python的堆是按元组第一个元素比较的
    - (count, user_id) → 按count比较，符合我们的需求
    - (user_id, count) → 会按user_id比较，错误！

Q3: heapreplace 和 heappop + heappush 有什么区别？
A3: heapreplace 效率更高
    - heapreplace(heap, item): 一次操作，弹出并插入
    - heappop + heappush: 两次操作，先弹出再插入

Q4: 时间复杂度分析？
A4: 假设有n个不同的user_id，找Top k
    - 前k个元素：k次 heappush，O(k*log k)
    - 后n-k个元素：每次比较+可能的heapreplace，O((n-k)*log k)
    - 总时间：O(n*log k)
    - 排序输出：O(k*log k)
    - 总复杂度：O(n*log k)，远优于排序的O(n*log n)

Q5: 空间复杂度？
A5: O(k)，只需要保存k个元素，不管原数据有多大
""")

print("\n" + "=" * 60)
print("第五部分：完整示例")
print("=" * 60)


def find_top_k_users_explained(user_count, k):
    """带详细注释的Top K查找"""

    # 如果总数不超过k，直接返回排序结果
    if len(user_count) <= k:
        return sorted(user_count.items(), key=lambda x: x[1], reverse=True)

    # 创建最小堆
    min_heap = []

    # 遍历所有user_id
    for user_id, count in user_count.items():
        if len(min_heap) < k:
            # 堆未满，直接插入
            # 插入格式：(count, user_id)，按count排序
            heapq.heappush(min_heap, (count, user_id))
        else:
            # 堆已满，判断是否需要替换
            # min_heap[0] 是堆顶（最小元素）
            # min_heap[0][0] 是堆顶的count值
            if count > min_heap[0][0]:
                # 当前count更大，替换堆顶
                heapq.heapreplace(min_heap, (count, user_id))
            # 否则不处理（这个user_id不在Top K中）

    # 将堆中元素按count降序排列
    # sorted默认升序，reverse=True变为降序
    result = [(user_id, count) for count, user_id in sorted(min_heap, reverse=True)]

    return result


# 测试
test_data = {
    "user_1": 100,
    "user_2": 500,
    "user_3": 50,
    "user_4": 300,
    "user_5": 800,
    "user_6": 200,
    "user_7": 150,
}

print("\n测试数据:")
for uid, cnt in sorted(test_data.items(), key=lambda x: x[1], reverse=True):
    print(f"  {uid}: {cnt}次")

print("\nTop 3 结果:")
top_3 = find_top_k_users_explained(test_data, 3)
for uid, cnt in top_3:
    print(f'  ("{uid}", {cnt})')




# 最终答案

import heapq
from collections import defaultdict
import re


def find_top_k_users(log_file_path, k, chunk_size=1024 * 1024):
    """
    统计日志文件中出现次数最多的前K个user_id

    思路：
    1. 使用哈希表(字典)统计每个user_id的出现次数
    2. 逐行读取文件，避免一次性加载到内存
    3. 使用最小堆维护Top K结果，降低空间复杂度

    参数：
    - log_file_path: 日志文件路径
    - k: 返回前k个user_id
    - chunk_size: 每次读取的字节数(默认1MB)

    返回：
    - 列表，格式为[(user_id, count), ...]，按count降序排列
    """

    # 第一步：统计每个user_id的出现次数
    user_count = defaultdict(int)

    # 使用正则表达式提取user_id
    pattern = re.compile(r'user_id=(\d+)')

    print("开始统计user_id出现次数...")

    # 逐行读取文件
    with open(log_file_path, 'r', encoding='utf-8') as f:
        line_count = 0
        for line in f:
            # 提取user_id
            match = pattern.search(line)
            if match:
                user_id = match.group(1)
                user_count[user_id] += 1
                line_count += 1

                # 每处理100万行打印一次进度
                if line_count % 1000000 == 0:
                    print(f"已处理 {line_count} 行...")

    print(f"统计完成，共处理 {line_count} 行，发现 {len(user_count)} 个不同的user_id")

    # 第二步：使用最小堆找出Top K
    # 如果user_id总数小于等于k，直接返回所有结果
    if len(user_count) <= k:
        result = sorted(user_count.items(), key=lambda x: x[1], reverse=True)
        return result

    # 使用最小堆维护Top K
    # 堆中元素格式：(count, user_id)
    min_heap = []

    for user_id, count in user_count.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (count, user_id))
        else:
            # 如果当前count大于堆顶元素，替换堆顶
            if count > min_heap[0][0]:
                heapq.heapreplace(min_heap, (count, user_id))

    # 第三步：将结果按count降序排列
    result = [(user_id, count) for count, user_id in sorted(min_heap, reverse=True)]

    return result


def find_top_k_users_optimized(log_file_path, k):
    """
    优化版本：如果内存极度受限，可以使用分治+外部排序

    思路：
    1. 按user_id的哈希值分片，将日志分成多个小文件
    2. 对每个小文件分别统计Top K
    3. 合并所有小文件的Top K结果

    这个版本适用于user_id种类极多的场景
    """
    pass  # 根据实际需求实现


# 使用示例
if __name__ == "__main__":
    # 示例1：处理真实日志文件
    log_file = "access.log"  # 替换为你的日志文件路径
    k = 10  # 查找出现次数最多的前10个user_id

    try:
        top_k_users = find_top_k_users(log_file, k)

        print(f"\n出现次数最多的前{k}个user_id：")
        for user_id, count in top_k_users:
            print(f'("{user_id}", {count})')

    except FileNotFoundError:
        print(f"文件 {log_file} 不存在")
        print("\n使用测试数据进行演示...")

        # 示例2：生成测试数据
        test_file = "test_log.txt"

        # 生成测试日志
        import random

        with open(test_file, 'w', encoding='utf-8') as f:
            # 模拟日志：某些user_id出现频率更高
            user_ids = [str(i) for i in range(1, 101)]  # 100个不同的user_id
            weights = [1] * 90 + [10] * 10  # 前90个权重为1，后10个权重为10

            for i in range(10000):  # 生成1万条日志
                user_id = random.choices(user_ids, weights=weights)[0]
                log_line = f"2025-08-25 12:00:01, user_id={user_id}, action=click, item_id=456\n"
                f.write(log_line)

        print(f"已生成测试文件：{test_file}")

        # 统计Top 10
        top_k_users = find_top_k_users(test_file, 10)

        print(f"\n出现次数最多的前10个user_id：")
        for user_id, count in top_k_users:
            print(f'("{user_id}", {count})')
