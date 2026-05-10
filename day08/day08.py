"""
基于字典的学生信息管理系统
功能：
1. 添加学生信息
2. 删除学生信息
3. 修改学生信息
4. 查询学生信息
5. 显示所有学生信息
学生信息包括：姓名、年龄、性别、学号
6.退出系统
"""
# 学生列表
students = []

# 添加学生信息 1
def add_student(): 
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    gender = input("请输入学生性别：")
    sid = input("请输入学生学号：")
    stu = {"姓名": name, "年龄": age, "性别": gender, "学号": sid}
    students.append(stu)
    print("学生信息添加成功！")
    

# 显示所有学生信息 5
def show_students():
    if not students:
        print("暂无学生信息")
        
    else:
        for stu in students:
            print(f"姓名: {stu['姓名']}, 年龄: {stu['年龄']}, 性别: {stu['性别']}, 学号: {stu['学号']}")
            
# 删除学生信息 2
def delete_student():
    sid = input("请输入要删除的学生学号:")
    for stu in students:
        if stu['学号'] == sid:
            students.remove(stu)
            print("学生信息删除成功！")
            return
    print("未找到该学生信息！") 

# 修改学生信息 3
def modify_student():
    sid = input("请输入要修改的学生学号:")
    for stu in students:
        if stu['学号'] == sid:
            stu['姓名'] = input(f"请输入新的学生姓名({stu['姓名']}):") or stu['姓名']
            stu['年龄'] = input(f"请输入新的学生年龄({stu['年龄']}):") or stu['年龄']
            stu['性别'] = input(f"请输入新的学生性别({stu['性别']}):") or stu['性别']
            stu['学号'] = input(f"请输入新的学生学号({stu['学号']}):") or stu['学号']
            print("学生信息修改成功！")
            return
    print("未找到该学生信息！")


# 查询学生信息 4
def query_student():
    sid = input("请输入要查询的学生学号:")
    for stu in students:
        if stu['学号'] == sid:
            print(f"姓名: {stu['姓名']}, 年龄: {stu['年龄']}, 性别: {stu['性别']}, 学号: {stu['学号']}")
            return
    print("未找到该学生信息！")

while True:
    print("\n欢迎使用学生信息管理系统")
    print("1. 添加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("6. 退出系统")
    choice = input("请输入您的选择(1-6):")
    if choice == '1':
        print()
        add_student()
        print()
    elif choice == '5':
        show_students()
        print()
    elif choice == '6':
        print("退出系统，再见！")
        break
    elif choice == '2':
        delete_student()
        print()
    elif choice == '3':
        modify_student()
        print()
    elif choice == '4':
        query_student()
        print()
    else:
        print("无效的选择，请重新输入！")
