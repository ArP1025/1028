# Day 2 练习：list 和 dict + 文件读写
# 目标：能写出「词频统计」程序

# ============================================================
# 热身 1：list 基本操作
# ============================================================
nums = [10, 20, 30, 40, 50]

# 1. 打印第 1 个元素（索引 0）
print(nums[0])   # 期望: 10

# 2. 打印最后 1 个元素（用负数索引，-1 表示最后一个）
# TODO: 取消注释并填写
print(nums[-1])   # 期望: 50

# 3. 用 append 加一个数 60，然后打印整个列表
# TODO: 在这里写一行 append，然后 print(nums)
nums.insert(5,60)
print(nums)
# 4. 用 for 循环打印列表里每个数（每个一行）
# TODO: 写一个 for 循环
for num in nums:
    print(num)


# ============================================================
# 热身 2：dict 基本操作
# ============================================================
scores = {"语文": 85, "数学": 92, "英语": 78}

# 1. 打印数学成绩
print(scores["数学"])   # 期望: 92

# 2. 新增一科「物理」成绩 88
scores["物理"] = 88

# 3. 用 for 循环打印所有科目和成绩，格式如「语文: 85」
# 提示: for k, v in scores.items():
for k,v in scores.items():
  print(f"{k}:{v}")


# ============================================================
# 热身 3：用 dict 计数（这是词频统计的核心）
# 给你一个列表 ["a", "b", "a", "c", "a", "b"]，
# 统计每个字母出现几次，结果应该是 {"a": 3, "b": 2, "c": 1}
# ============================================================
def count_items(items):
    result = {}    # 空字典
    for item in items:
        if item in result:              # 如果这个字母已经在字典里
            result[item] = result[item] + 1   # 次数 +1
        else:                            # 如果不在
            result[item] = 1             # 设为 1
    return result

# 测试：
print(count_items(["a", "b", "a", "c", "a", "b"]))
# 期望: {'a': 3, 'b': 2, 'c': 1}


# ============================================================
# 练习：词频统计（Day 2 最终目标）
# 步骤：
#   1. 准备一个文本文件 poem.txt（我已帮你建好，里面有几行中文）
#   2. 用 open() 读取文件内容
#   3. 把内容按空格或换行拆成单词列表（中文就按字符拆，简单起见）
#   4. 用热身 3 的方法统计每个字出现次数
#   5. 按出现次数从多到少排序，打印前 10 个
# ============================================================
def word_frequency(filename):
    # 1. 读文件
    f = open(filename, "r", encoding="utf-8")
    text = f.read()
    f.close()

    # 2. 拆成字符（中文按字统计最简单）
    # 提示：text 本身就是一个字符串，可以直接 for char in text 遍历
    # 但要跳过空格和换行符
    chars = []
    for ch in text:
        if ch not in [" ", "\n", "，", "。", "！"]:   # 跳过空格、换行、标点
            chars.append(ch)

    # 3. 统计（复用热身 3 的逻辑）
    count = {}
    for ch in chars:
        if ch in count:
            count[ch] = count[ch] + 1
        else:
            count[ch] = 1

    # 4. 排序：按出现次数从高到低
    # sorted 的 key 参数指定按什么排序，reverse=True 表示降序
    sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)

    # 5. 打印前 10 个
    print("出现次数最多的前 10 个字：")
    for char, num in sorted_chars[:10]:
        print(f"{char}: {num}")

# 测试：
word_frequency("poem.txt")
