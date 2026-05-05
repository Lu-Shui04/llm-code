print("实战: Ai提示词生成器")

start="Ai提示词(prompt)生成器"
print("="*50)
print(f"{start:^50}")
print("="*50)

#收集角色
print("---设定Ai角色---")
role=input("Ai角色(如: python导师/文案助手/代码审核员): ")
style=input("回答风格(如: 简洁/详细/幽默/学术):")
language=input("回答语言(中文/English/中英混合):")

#收集任务信息
print("---设定任务---")
task=input("任务描述(一句话):")
context=input("背景信息:")
constraint=input("限制条件:")

#收集输出要求
print("---输出要求---")
output_format=input("输出格式(如:列表/段落/代码/表格):")
extra=input("其他要求:")

#用f-string拼出一个完整的system prompt
prompt=f"""你是一个{role}。
你的回答风格：{style}。
请用{language}回答。
"""
if context:
    prompt += f"背景信息:{context}"
if constraint:
    prompt += f"注意:{constraint}"

prompt += f"""
用户会给你一个任务，请按照一下要求完成：
任务：{task}
输出格式：{output_format}"""

if extra:
    prompt +=f"{extra}"

print("="*50)
start1="生成的System Prompt: "
print(f"{start1:^50}")
print("="*50)
print(prompt)
print("="*50)
