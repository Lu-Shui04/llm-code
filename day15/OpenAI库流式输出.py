from openai import OpenAI

# 1.获取client对象，OpenAI类对象
client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是python专家"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"输出1-10的数字，使用python编写代码"}
    ],
    stream=True
)

# 处理结果
# print(response.choices[0].message.content)
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ",
        flush=True
        )