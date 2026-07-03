import argparse

# 1. 建立解析器（可以加上程式的描述）
parser = argparse.ArgumentParser(description="這是一個示範 argparse 的工具")

# 2. 新增參數
# 位置參數（Positional Argument）- 必填
parser.add_argument("name", type=str, help="請輸入你的名字")

# 選用參數（Optional Argument）- 選填，通常以 - 或 -- 開頭
parser.add_argument("-a", "--age", type=int, default=18, help="輸入你的年齡（預設為 18）")

# 3. 解析參數
args = parser.parse_args()

# 4. 使用參數
print(f"嗨，{args.name}！你今年 {args.age} 歲。")