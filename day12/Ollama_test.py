import ollama

# 查看有哪些模型
print("模型列表：")
print(ollama.list())

print("\n" + "=" * 40)

# 查看模型详情
print("deepseek-r1:1.5b 信息：")
print(ollama.show('deepseek-r1:1.5b'))

print("\n" + "=" * 40)

while True:
    prompt = input("你想问什么：")
    response = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=[{"role": "user", "content": prompt}]
    )
    print("模型回复：")
    print(response['message']['content'])
    print()
