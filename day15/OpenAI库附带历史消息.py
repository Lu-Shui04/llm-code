from openai import OpenAI

client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是AI助理,回答简洁"},
        {"role":"user","content":"小米家有2条猫"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"小红家有3条狗"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"他们家一共有几条宠物？"}
    ],
    stream=True
)

for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ",
        flush=True
    )