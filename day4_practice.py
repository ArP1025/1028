# Day 4 练习：数据导出 + 简单图表
# 数据：cards.csv、transactions.csv（和 Day 3 一样）
# 重点：to_csv/to_excel 导出、多条件筛选、matplotlib 柱状图和饼图

import pandas as pd
import matplotlib.pyplot as plt

# 解决中文显示问题（必须加，否则图表里的中文会变成方块）
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

cards = pd.read_csv("cards.csv")
trans = pd.read_csv("transactions.csv")
merged = pd.merge(trans, cards, on="card_id")


# ============================================================
# 练习 1：导出数据到文件
# ============================================================
# 把各学院总消费算出来
dept_total = merged.groupby("department")["amount"].sum().sort_values(ascending=False)
print("=== 各学院总消费 ===")
print(dept_total)
print()

# 导出到 CSV（不写索引）
# TODO 1：把下面这行的注释去掉，运行后看 e:\shixi 目录下有没有生成 dept_total.csv
dept_total.to_csv("dept_total.csv", encoding="utf-8-sig")
print("已导出 dept_total.csv")

# 导出到 Excel（需要 openpyxl 库，如果报错就先 pip install openpyxl）
# TODO 2：取消注释，尝试导出 Excel
dept_total.to_excel("dept_total.xlsx")
print("已导出 dept_total.xlsx")


# ============================================================
# 练习 2：多条件筛选
# ============================================================
# 例：筛选出「金额大于 15 元」且「在一食堂」的消费记录
# 注意：多个条件用 & 连接，每个条件要用括号包起来
big_ones = merged[(merged["amount"] > 15) & (merged["location"] == "一食堂")]
print("=== 一食堂单笔超过15元的消费 ===")
print(big_ones[["student_name", "amount", "meal_type"]])
print()

# TODO 3：筛选出「午餐」且「金额大于 10 元」的记录，打印姓名和金额
# 提示: (merged["meal_type"] == "午餐") & (merged["amount"] > 10)
lunch_big =  (merged["meal_type"] == "午餐") & (merged["amount"] > 10)
print(lunch_big[["student_name", "amount"]])


# ============================================================
# 练习 3：柱状图（bar chart）
# 展示各学院的总消费
# ============================================================
dept_total = merged.groupby("department")["amount"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 4))              # 设置图的大小
plt.bar(dept_total.index, dept_total.values)   # 柱状图：x=学院名, y=金额
plt.title("各学院总消费")               # 标题
plt.xlabel("学院")                       # x轴标签
plt.ylabel("消费金额（元）")             # y轴标签
plt.xticks(rotation=30)                  # x轴文字旋转30度，避免重叠
plt.tight_layout()                       # 自动调整布局
plt.savefig("dept_bar.png")              # 保存图片
print("已保存柱状图 dept_bar.png")
plt.show()  # 想弹窗看就取消注释


# ============================================================
# 练习 4：饼图（pie chart）
# 展示各餐次消费占比
# ============================================================
meal_total = trans.groupby("meal_type")["amount"].sum()

plt.figure(figsize=(6, 6))
plt.pie(meal_total.values,
        labels=meal_total.index,        # 标签：餐次名
        autopct="%.1f%%")               # 显示百分比，保留1位小数
plt.title("各餐次消费占比")
plt.tight_layout()
plt.savefig("meal_pie.png")
print("已保存饼图 meal_pie.png")
