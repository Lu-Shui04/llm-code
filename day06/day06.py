# 1. 创建简历字典
print("="*30)
resume = {
    "name": "小米",
    "age": 22,
    "school": "新疆工程学院",
    "skills": ["Python", "API调用", "AI应用开发"],
    "expected_salary": 12000
}

# 2. 直接打印整个字典
print("--- 原始数据 ---")
print(resume)

# 3. (进阶) 格式化打印，让简历更好看
print("\n--- 我的个人简历 ---")
print(f"姓名：{resume['name']}")
print(f"年龄：{resume['age']}")
print(f"学校：{resume['school']}")
print(f"技能：{'、'.join(resume['skills'])}")  # 将列表转为字符串
print(f"期望薪资：{resume['expected_salary']}")