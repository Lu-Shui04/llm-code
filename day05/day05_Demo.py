# # # # print("----------列表与数据容器-----------")
# # # # # my_list=[1,2,3,4,5]
# # # # # names=["小米","华为","vivo","oppo"]
# # # # # mixed=[1,"小米",3.14,True]
# # # # # fruits=["苹果","葡萄","香蕉","橘子"]
# # # # # print(fruits[0])
# # # # # print(f"{fruits[1]}")
# # # # # print(fruits[2])
# # # # # print(fruits[3])
# # # # # print(fruits[-1])
# # # # # print(fruits[-3])
# # # # # print("-----------")
# # # # # print(len(fruits))
# # # # tasks=["安装Python","装vscode"]

# # # # #=======增========
# # # # tasks.append("写代码")

# # # # tasks.insert(1,"休息一下")
# # # # print(tasks)

# # # # tasks.extend(["复习","睡觉"])
# # # # print(tasks)

# # # # #======删=======
# # # # tasks.remove("休息一下")
# # # # print(tasks)
# # # # del tasks[0]
# # # # print(tasks)
# # # # last=tasks.pop(1)
# # # # print(last)
# # # # print(tasks)
# # # # tasks[1]="小米"
# # # # print(tasks)
# # # # print(tasks.index("小米"))
# # # # print(tasks.count("9999"))
# # # # print("小米" in tasks)

# # # tasks=["学Python","学web","学API","学RAG","学Agent"]
# # # for task in tasks:
# # #     print(f"已完成: {task}")
# # # #带编号遍历
# # # for i,task in enumerate(tasks):
# # #     print(f"第{i+1}步: {task}")
    
# # # print("===================")
# # # for i,task in enumerate(tasks):
# # #     print(f"第{i+1}步: {task}")

# # # for task in tasks:
# # #     if "web" in task:
# # #         print(f"已完成：{task}")
# # #     else:
# # #         print(f"未完成: {task}")


# # nums=[0,1,2,3,4,5,6,7,8,9]
# # print(nums[::-1])
# # print(nums[0:10:2])
# # print(nums[-5:])#取最近5条

# nums=[5,2,8,1,9,3]
# #排序 升序
# # nums.sort()
# # print(nums)
# #降序
# # nums.sort(reverse=True)
# # print(nums)
# # print(sorted(nums))#不改变原列表
# # print(nums)

# # nums.reverse()#反转列表
# # print(nums)

# squares=[x**2 for x in range(1,6)]
# print(squares)

# a=[1,2,3]
# b=a
# b.append(4)
# print(a)
# print(b)
# c=a[:2]
# print(c)
# c.append(5)
# print(c)

a=[1,2,3]
b=a.copy()
b.append(5)
print(a)
print(b)
