"""2.3 查找与判断"""

text = "哈喽小米 晚上吃了米什么饭？"
print(text.startswith("小米"))  # 判断是否以"小米"开头 → False
print(text.endswith("什么饭？"))  # 判断是否以"什么饭？"结尾 → True
print("小米" in text)            # 判断"小米"是否在字符串中 → True
print(text.find("小米"))         # 查找"小米"的位置，从0开始 → 2
print(text.find("你好"))         # 查找"你好"，找不到返回 → -1
print(text.count("米"))          # 统计"米"出现的次数 → 2