score = 85
if score >= 85:
    print("合格")
print("="*20+"2.3"+"="*20) #分行循序来
balance=50
price=100
if balance>=price:
    print("购买成功")
    balance=balance-price
else:
    print("余额不足")
    print(f"还差{price-balance}元")
print("="*20+"2.3"+"="*20) #分行循序来

if score >=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else:
    grade="F"
print(f"成绩等级：{grade}")

print("="*20+"2.5"+"="*20) #分行循序来
judge="python" in "我在学python"
print(judge)

age=19
has_ticket=True
is_adult=age>=18
print(is_adult)

if is_adult and has_ticket:
    print("请进")

print("="*20+"2.3"+"="*20) #分行循序来

submitted=True
if score>=60 and score<=100 and submitted:
    print("有效成绩")

is_admin=False
is_vip=True
if is_admin or is_vip:
    print("享受优先服务")

#day=input("今天星期几：")
#if day=="6" or day=="7":
#    print("周末愉快")
#else:
#    print("上班日子宝贝")

is_banned=False
if not is_banned:
    print("可以发言")
if not (age<18):
    print("成年")

my_list=[]
if len(my_list)>0 and my_list[0]=="小米":
    pass

age=25
ticket=True
ticket_vip=False
if age>18:
    if ticket:
        if ticket_vip:
            print("vip专属通道")
        else:
            print("普通通道")
    else:
        print("请先购票")
else:
    print("未成年需陪同家长")

if age>=18 and ticket and  ticket_vip:
    print("vip")
else:
    print("不是vip")
