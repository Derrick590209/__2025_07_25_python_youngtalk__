import argparse

parser = argparse.ArgumentParser(description="讓使用者輸入姓名")
parser.add_argument("-n", "--name", type=str,help="姓名")
args = parser.parse_args()

if not args.name: #沒有輸入是None,所以not args.name是True
    name = input("請輸入姓名: ")
else:
    name=args.name

print(f"您的姓名是 {name}!")

