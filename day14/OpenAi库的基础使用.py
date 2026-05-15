from openai import OpenAI
import os
# 获取client对象，OpenAi类对象
client = OpenAI(
    base_url="http://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一个python编程专家，并且不说废话简单回答"},
        {"role":"assistant","content":"好的。"},
        {"role":"user","content":"帮我写一个python输出1-10的代码"}
    ]
)

# 处理结果
print(response.choices[0].message.content)