# Day13 记账小工具 · 完整版（记录+统计+查看历史）
import datetime

# 统一文件路径（你自己的路径）
FILE_PATH = r"D:\python\PythonPbasic\image\dashu"

def 记账(收入, 备注):
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"日期:{now},收入:{收入}元,备注:{备注}\n")
    print("✅ 记录成功！")

def 统计本月收入():
    now = datetime.datetime.now()
    current_month = now.strftime("%Y-%m")
    total = 0

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if "日期:" in line and "收入:" in line:
                    date_str = line.split("日期:")[1].split(",")[0]
                    money_str = line.split("收入:")[1].split("元")[0]
                    if date_str.startswith(current_month):
                        total += int(money_str)

        print(f"\n📊 本月 {current_month} 一共赚了：{total} 元")
    except FileNotFoundError:
        print("❌ 还没有记录哦")

def 查看所有记录():
    print("\n📜 ———— 全部收入记录 ————")
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("暂无记录")
                return
            for line in lines:
                print(line.strip())
        print("——————————————————————")
    except FileNotFoundError:
        print("❌ 暂无记录")

# ==================== 主程序 ====================
while True:
    print("\n" + "="*40)
    print("💼 个人赚钱记账工具 V3.0")
    print("="*40)
    print("1 👉 记录一笔收入")
    print("2 👉 统计本月总收入")
    print("3 👉 查看所有收入记录")
    print("0 👉 退出程序")
    print("="*40)

    choice = input("请输入功能编号：")

    if choice == "1":
        try:
            money = int(input("💰 本次收入："))
            text = input("📝 来源备注：")
            记账(money, text)
        except ValueError:
            print("❌ 请输入正确数字！")

    elif choice == "2":
        统计本月收入()

    elif choice == "3":
        查看所有记录()

    elif choice == "0":
        print("👋 退出成功，继续搞钱！")
        break

    else:
        print("⚠️ 请输入 0-3 之间的数字")
