print("="*20+"年份判断系统"+"="*20)
day_year=int(input("请输入年份: "))
if (day_year % 4==0 and day_year % 100 !=0) or day_year % 400 == 0:
    print("闰年")
else:
    print("不是闰年")

print("="*20+"登录系统"+"="*20)
root=input("输入用户名: ")
password=int(input("输入密码:(3次机会) "))
count=2

if root=="admin" and password==123456:
    print("登录成功")
elif root=="admin" and password!=123456:
    while count>0:
        print(f"密码错误,重新输入密码(剩余{count}次): ")
        text_password=int(input())
        if text_password==123456:
            print("登录成功")
            break
        count-=1
    if count==0:
        print("密码多次错误, 已锁定🔒")
else:
    print("用户不存在")




