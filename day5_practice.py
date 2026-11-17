# Day 5 练习：SQL 入门（饭卡管理版）
# 用 Python 自带的 sqlite3，无需安装数据库
# 重点：SELECT / WHERE / GROUP BY / JOIN

import sqlite3

# 连接数据库（文件形式，会在当前目录生成 mealcard.db）
conn = sqlite3.connect("mealcard.db")
cur = conn.cursor()

# ========== 建表并插入数据（这段不用改，运行一次即可）==========
cur.execute("DROP TABLE IF EXISTS cards")
cur.execute("DROP TABLE IF EXISTS transactions")

cur.execute("""
CREATE TABLE cards (
    card_id TEXT PRIMARY KEY,
    student_name TEXT,
    department TEXT,
    balance REAL,
    status TEXT
)
""")

cur.execute("""
CREATE TABLE transactions (
    trans_id TEXT PRIMARY KEY,
    card_id TEXT,
    amount REAL,
    meal_type TEXT,
    location TEXT,
    trans_date TEXT
)
""")

cards_data = [
    ("C001", "张小明", "计算机学院", 128.50, "正常"),
    ("C002", "李小红", "人工智能学院", 86.00, "正常"),
    ("C003", "王小强", "数学学院", 245.30, "正常"),
    ("C004", "赵小芳", "外国语学院", 15.00, "正常"),
    ("C005", "钱小刚", "物理学院", 320.80, "正常"),
    ("C006", "孙小丽", "计算机学院", 0.00, "冻结"),
    ("C007", "周小杰", "人工智能学院", 189.60, "正常"),
    ("C008", "吴小燕", "数学学院", 67.20, "正常"),
]
trans_data = [
    ("T001", "C001", 8.50, "早餐", "一食堂", "2024-03-01"),
    ("T002", "C001", 15.00, "午餐", "一食堂", "2024-03-01"),
    ("T003", "C002", 12.00, "午餐", "二食堂", "2024-03-01"),
    ("T004", "C003", 18.50, "晚餐", "一食堂", "2024-03-01"),
    ("T005", "C001", 6.00, "早餐", "二食堂", "2024-03-02"),
    ("T006", "C002", 16.00, "午餐", "一食堂", "2024-03-02"),
    ("T007", "C004", 10.00, "午餐", "二食堂", "2024-03-02"),
    ("T008", "C003", 9.00, "早餐", "一食堂", "2024-03-02"),
    ("T009", "C005", 22.00, "晚餐", "二食堂", "2024-03-02"),
    ("T010", "C001", 14.50, "午餐", "二食堂", "2024-03-03"),
    ("T011", "C002", 7.50, "早餐", "一食堂", "2024-03-03"),
    ("T012", "C003", 13.00, "午餐", "二食堂", "2024-03-03"),
    ("T013", "C005", 20.00, "晚餐", "一食堂", "2024-03-03"),
    ("T014", "C001", 11.00, "晚餐", "一食堂", "2024-03-03"),
    ("T015", "C002", 19.00, "晚餐", "二食堂", "2024-03-03"),
    ("T016", "C007", 12.50, "午餐", "一食堂", "2024-03-03"),
    ("T017", "C008", 8.00, "早餐", "二食堂", "2024-03-03"),
    ("T018", "C003", 17.00, "午餐", "一食堂", "2024-03-04"),
    ("T019", "C001", 9.50, "早餐", "一食堂", "2024-03-04"),
    ("T020", "C005", 15.50, "午餐", "二食堂", "2024-03-04"),
]

cur.executemany("INSERT INTO cards VALUES (?,?,?,?,?)", cards_data)
cur.executemany("INSERT INTO transactions VALUES (?,?,?,?,?,?)", trans_data)
conn.commit()
print("数据库已创建，饭卡表和消费表已导入数据\n")


# 辅助函数：执行 SQL 并打印结果（不用改）
def run_sql(sql, title=""):
    if title:
        print(f"=== {title} ===")
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print()


# ============================================================
# 练习 1：SELECT 基本查询
# ============================================================
# 查所有饭卡
run_sql("SELECT * FROM cards", "所有饭卡")

# TODO 1：只查姓名和学院两列
# 提示: SELECT student_name, department FROM cards
# run_sql("???", "姓名和学院")


# ============================================================
# 练习 2：WHERE 条件筛选
# ============================================================
# 例：查一食堂的所有消费
run_sql("SELECT * FROM transactions WHERE location = '一食堂'", "一食堂的消费")

# TODO 2：查金额大于 15 元的消费记录
# 提示: WHERE amount > 15
# run_sql("???", "超过15元的消费")

# TODO 3：查计算机学院的学生
# 提示: WHERE department = '计算机学院'
# run_sql("???", "计算机学院的学生")


# ============================================================
# 练习 3：GROUP BY 分组（对应 pandas 的 groupby）
# ============================================================
# 例：按餐次分组，求每餐次总消费
# 对比 pandas: trans.groupby("meal_type")["amount"].sum()
run_sql("SELECT meal_type, SUM(amount) FROM transactions GROUP BY meal_type",
        "各餐次总消费")

# TODO 4：按食堂分组，求每个食堂的消费笔数（用 COUNT）
# 提示: SELECT location, COUNT(*) FROM transactions GROUP BY location
# run_sql("???", "各食堂消费笔数")

# TODO 5：按卡号分组，求每张卡的总消费，按金额降序排列
# 提示: ORDER BY SUM(amount) DESC
# run_sql("???", "各饭卡总消费（降序）")


# ============================================================
# 练习 4：JOIN 多表查询（对应 pandas 的 merge）
# ============================================================
# 例：把消费记录和饭卡信息连起来
# 对比 pandas: pd.merge(trans, cards, on="card_id")
run_sql("""
    SELECT t.trans_id, c.student_name, t.amount, t.meal_type
    FROM transactions t
    JOIN cards c ON t.card_id = c.card_id
    LIMIT 5
""", "消费记录 + 学生姓名（前5条）")

# TODO 6：查每个学院的总消费
# 提示: JOIN 后 GROUP BY department，SUM(amount)
# run_sql("???", "各学院总消费")

# TODO 7（综合）：查二食堂消费最多的学院（排序取第一）
# 提示: WHERE location='二食堂' GROUP BY department ORDER BY SUM(amount) DESC LIMIT 1
# run_sql("???", "二食堂消费最多的学院")

conn.close()
