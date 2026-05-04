# -*- coding: utf-8 -*-
"""Day 2 实战：个人信息卡片生成器"""

print("=" * 40)
print("  个人信息卡片生成器")
print("=" * 40)

# 收集信息（input 拿到的都是字符串，该转的转）
name = input("请输入你的姓名：")
age = int(input("请输入你的年龄："))
height = float(input("请输入你的身高（米）："))
city = input("请输入你所在的城市：")
target = input("请输入你的学习目标：")

# 计算
birth_year = 2026 - age
height_cm = height * 100
target_length = len(target)

# 输出卡片
print("\n" + "=" * 40)
print(f"个人信息卡片")
print("-" * 40)
print(f"""
姓名：{name}
年龄：{age} 岁（{birth_year} 年出生）
身高：{height} 米（{height_cm:.0f} 厘米）
城市：{city}
目标：{target}
目标长度：{target_length} 个字符
""")
print("=" * 40)

