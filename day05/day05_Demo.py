print("----------列表与数据容器-----------")
# my_list=[1,2,3,4,5]
# names=["小米","华为","vivo","oppo"]
# mixed=[1,"小米",3.14,True]
# fruits=["苹果","葡萄","香蕉","橘子"]
# print(fruits[0])
# print(f"{fruits[1]}")
# print(fruits[2])
# print(fruits[3])
# print(fruits[-1])
# print(fruits[-3])
# print("-----------")
# print(len(fruits))
tasks=["安装Python","装vscode"]

#=======增========
tasks.append("写代码")

tasks.insert(1,"休息一下")
print(tasks)

tasks.extend(["复习","睡觉"])
print(tasks)

#======删=======
tasks.remove("休息一下")
print(tasks)
del tasks[0]
print(tasks)
last=tasks.pop(1)
print(last)
print(tasks)
tasks[1]="小米"
print(tasks)
print(tasks.index("小米"))
print(tasks.count("9999"))
print("小米" in tasks)

