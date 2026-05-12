def load_students():
    """启动时从文件读取已有账号"""
    try:
        with open("day10/学生信息.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                user, pwd = line.split(" : ", 1)
                student.append({"user": user, "password": pwd})
    except FileNotFoundError:
        pass  # 第一次运行，文件还不存在


def save_student(phone, password):
    """注册时追加写入文件"""
    with open("day10/学生信息.txt", "a", encoding="utf-8") as f:
        f.write(f"{phone} : {password}\n")


student = []

text = "登录数据库样例"
print(f"{text:=^50}")
print("""
      1.注册
      2.登录
      """)

load_students()

while True:
    x = int(input("请选择(1注册,2登录): "))
    if x != 1 and x != 2:
        print("输入有误！")
        continue

    if x == 1:
        while True:
            phone = input("请设置用户名：（手机号）")
            if len(phone) != 11:
                print("手机号有误")
                continue
            while True:
                password = input("请设置密码：（大于6位数字或字母组合）")
                if len(password) < 6:
                    print("密码长度不得小于6位")
                elif " " in password:
                    print("密码不能包含空格")
                else:
                    break
            break
        stu = {"user": phone, "password": password}
        student.append(stu)
        save_student(phone, password)
        print("注册成功！")

    else:
        phone = input("请输入用户名：（手机号）")
        password = input("请输入密码：")
        # 遍历列表逐个比对
        login_ok = False
        for stu in student:
            if stu["user"] == phone and stu["password"] == password:
                login_ok = True
                break
        if login_ok:
            print("登录成功！")
        else:
            print("登录失败！请检查用户名和密码是否正确！")
