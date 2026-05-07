# print("="*20+"年份判断系统"+"="*20)
# day_year=int(input("请输入年份: "))
# if (day_year % 4==0 and day_year % 100 !=0) or day_year % 400 == 0:
#     print("闰年")
# else:
#     print("不是闰年")

# print("="*20+"登录系统"+"="*20)
# root=input("输入用户名: ")
# password=int(input("输入密码:(3次机会) "))
# count=2

# if root=="admin" and password==123456:
#     print("登录成功")
# elif root=="admin" and password!=123456:
#     while count>0:
#         print(f"密码错误,重新输入密码(剩余{count}次): ")
#         text_password=int(input())
#         if text_password==123456:
#             print("登录成功")
#             break
#         count-=1
#     if count==0:
#         print("密码多次错误, 已锁定🔒")
# else:
#     print("用户不存在")

print("="*20+"成绩分析器"+"="*20)
score1=int(input("课程1成绩: "))
score2=int(input("课程2成绩: "))
score3=int(input("课程3成绩: "))
score4=int(input("课程4成绩: "))
score5=int(input("课程5成绩: "))

#处理逻辑
#平均分
average=float((score1+score2+score3+score4+score5)/5)
#最高分  最低分
if score1 > score2 and score1 >score3 and score1 >score4 and score1 >score5:
    max_score=score1
  
elif score2 >score3 and score2 >score4 and score2 >score5:
    max_score=score2
  
elif score3 >score4 and score3 >score5:
    max_score=score3
   
elif score4 >score5:
    max_score=score4
    
else:
    max_score=score5
    
min_score=min(score1,score2,score3,score4,score5)


#优秀等级函数调用
def get_grad(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "不及格",score

    


print("\n-------成绩分析报告--------")
print(f"平均分: {average}")
print(f"最高分: {max_score}")
print(f"最低分: {min_score}")
print(f"课程1等级: {get_grad(score1)}")
print(f"课程2等级: {get_grad(score2)}")
print(f"课程3等级: {get_grad(score3)}")
print(f"课程4等级: {get_grad(score4)}")
print(f"课程5等级: {get_grad(score5)}")
