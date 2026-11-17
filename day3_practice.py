# Day 3 练习：pandas 分组与合并（饭卡管理版）
# 数据集：cards.csv（饭卡表）、transactions.csv（消费记录表）
# 重点：groupby（分组聚合）、merge（多表合并）、sort_values（排序）

import pandas as pd

# 读数据
cards = pd.read_csv("cards.csv")
trans = pd.read_csv("transactions.csv")

print("=== 饭卡表 ===")
print(cards)
print()

print("=== 消费记录表（前5条）===")
print(trans.head())
print()


# ============================================================
# 练习 1：groupby 分组统计（重点！）
# ============================================================

# 例 1：按餐次分组，求每餐次的总消费金额
# 类比 SQL: SELECT meal_type, SUM(amount) FROM trans GROUP BY meal_type
total_by_meal = trans.groupby("meal_type")["amount"].sum()
print("=== 各餐次总消费 ===")
print(total_by_meal)
print()

# 例 2：按食堂分组，求每个食堂的消费笔数
count_by_loc = trans.groupby("location")["trans_id"].count()
print("=== 各食堂消费笔数 ===")
print(count_by_loc)
print()

# TODO 1：按餐次分组，求每餐次的平均消费金额（用 mean）
avg_by_meal = trans.groupby("meal_type")["amount"].mean()
print("=== 各餐次平均消费 ===")
print(avg_by_meal)

# TODO 2：按卡号分组，求每张饭卡的总消费金额
# 提示: groupby("card_id")["amount"].sum()
total_by_card = trans.groupby("card_id")["amount"].sum()
print("=== 各饭卡总消费 ===")
print(total_by_card)

# TODO 3：按食堂分组，同时求总消费、笔数、平均消费
# 提示: .agg(["sum", "count", "mean"])
stats = trans.groupby("location")["amount"].agg(["sum", "count", "mean"])
print("=== 各食堂多维度统计 ===")
print(stats)


# ============================================================
# 练习 2：sort_values 排序
# ============================================================
# 把各餐次总消费按金额从高到低排序
sorted_meal = total_by_meal.sort_values(ascending=False)
print("=== 各餐次消费排名（降序）===")
print(sorted_meal)
print()


# ============================================================
# 练习 3：merge 多表合并（重点！对应 SQL 的 JOIN）
# 把消费记录和饭卡信息合并，就能知道每笔消费是哪个学院的学生
# ============================================================
merged = pd.merge(trans, cards, on="card_id")
print("=== 合并后（消费记录 + 学生信息）前5条 ===")
print(merged.head())
print()

# TODO 4：合并后，按学院分组，求每个学院的总消费
# 提示: merged.groupby("department")["amount"].sum()
total_by_dept = merged.groupby("department")["amount"].sum()
print("=== 各学院总消费 ===")
print(total_by_dept)

# TODO 5：合并后，按学生姓名分组，求每个学生的总消费，再从高到低排序
# 提示: groupby("student_name")["amount"].sum() 然后 .sort_values(ascending=False)
consume_rank = merged.groupby("student_name")["amount"].sum().sort_values(ascending=False)
print("=== 学生消费排名 ===")
print(consume_rank)


# ============================================================
# 综合练习：用代码回答业务问题
# ============================================================
# 问题：哪个学院的学生在二食堂消费最多？
# 提示：
#   1. 先筛选 location == "二食堂" 的记录
#   2. 再按学院分组求和
#   3. 排序取第一
result = merged[merged["location"] == "二食堂"].groupby("department")["amount"].sum().sort_values(ascending=False).head(1)
print("=== 二食堂消费最多的学院 ===")
print(result)