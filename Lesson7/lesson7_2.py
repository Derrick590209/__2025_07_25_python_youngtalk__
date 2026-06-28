#寫這程式的目的是希望將來執行時是輸入 python lesson7_2.py --name "你的名字  然後跑出你的名字是:Derrick"

import argparse 
parser = argparse.ArgumentParser(description="要求使用者輸入姓名") 
#ArgumentParser是一個物件 class
#第一個實體名稱叫parser 用來控制argparse.ArgumentParser的實體
#實體名稱裡面有兩個東西1.實體屬性 2.實體方法()== add_argument()

parser.add_argument("name", help="請輸入姓名")
# 使用實體方法的步驟是:實體名稱.實體方法  例: parser.add_argument()
# name是位置的引數名稱(位置的參數),help是說明文字,會在使用者輸入python lesson7_2.py -h時顯示
# add_argument()輸出是None,所以不需要用變數去接收
#最後輸入python leeson7_2.py -h 會跑出positional arguments(位置的引述名稱)叫做name,說明寫:請輸入姓名


args = parser.parse_args()
#parse_args是第二個實體方法,輸出是Namespace物件(實體),裡面有一個屬性叫name,值是使用者輸入的姓名
#args是第二個實體名稱,用來控制parser.parse_args()的實體

type(args) #<class 'argparse.Namespace'>



print(f"你的名字是: {args.name}")