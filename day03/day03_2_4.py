print(""""2.4 替换与分割""")

#替换
text="今天学了python,python很有趣！"
print(text.replace("python","小米"))
print(text.replace("python","小米",1))

#分割
text1="周一:python,周二:web,周三:API"
parts=text1.split(",")
print(parts)

#再分割
for i in parts:
    day,task=i.split(":")
    print(f"{day}-->{task}")
    