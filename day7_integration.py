# ============================================================
# Day 7：第一周整合练习 —— 饭卡消费数据分析
# 目标：把 pandas + Git 串起来，完成 读入 → 清洗 → 统计 → 导出
# ============================================================
import pandas as pd

# 1. 读入数据
cards = pd.read_csv("cards.csv")
trans = pd.read_csv("transactions.csv")

# 2. 数据清洗（检查空值）
print("=== 饭卡表空值检查 ===")
print(cards.isnull().sum())
print("\n=== 消费记录表空值检查 ===")
print(trans.isnull().sum())

# 3. 合并两表（对应 SQL 的 JOIN）
merged = pd.merge(trans, cards, on="card_id", how="left")

# 4. 分组统计（对应 SQL 的 GROUP BY）
# 各食堂总消费
by_canteen = merged.groupby("location")["amount"].sum().reset_index()
by_canteen.columns = ["食堂", "总消费"]
print("\n=== 各食堂总消费 ===")
print(by_canteen)

# 各餐次平均消费
by_meal = merged.groupby("meal_type")["amount"].mean().reset_index()
by_meal.columns = ["餐次", "平均消费"]
print("\n=== 各餐次平均消费 ===")
print(by_meal)

# 各学院总消费（降序）
by_dept = (
    merged.groupby("department")["amount"]
    .sum()
    .reset_index()
    .sort_values("amount", ascending=False)
)
by_dept.columns = ["学院", "总消费"]
print("\n=== 各学院总消费（降序）===")
print(by_dept)

# 5. 导出结果 CSV
by_canteen.to_csv("day7_canteen.csv", index=False, encoding="utf-8-sig")
by_dept.to_csv("day7_department.csv", index=False, encoding="utf-8-sig")
print("\n已导出 day7_canteen.csv 和 day7_department.csv")
