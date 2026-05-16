from openai import OpenAI
# 获取client对象，OpenAI类对象
client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# 模型加消息列表
response=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是python专家"},
        {"role":"assistant","content":"好"},
        {"role":"user","content":"帮我写输出1-10"}
    ],
    stream=True  #流式输出
)

for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ", #每个段落空格分开
        flush=True #刷新输出
        )
    
    """
    遇到了三个问题：
    1.在写response时,messages的's'忘记写了，导致代码报错
    2.在写content时,写成conteent了,(多了一个e)导致代码报错
    3.chunk.choices[0].delta.content不熟练,想不起来
    """