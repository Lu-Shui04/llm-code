from openai import OpenAI
import json

client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"       
)

# 示例数据
example_data={
    '是':[
        ("我最近在学Python","编程入门其实不难"),
        ("今天气温38度","外面热得不行"),
        ("我想学做大模型应用","RAG技术有点难学")
    ],
    '不是':[
        ("今天早上下雨了","我喜欢吃冰淇淋"),
        ("我买了新玩具","小明喜欢小红")
    ]
}
# 输入数据
questions=[
    ("周一我要开学了","我不喜欢吃蔬菜"),
    ("我在学习大模型应用开发","大模型RAG技术有点难学"),
    ("我每天在敲代码","我的编程能力提升了不少")
]
messages=[
    {"role":"system","content":"你是一个文本相似度专家，按照判断两个句子意思是不是一样回答是或不是,下面有示例"}
]

for key,value in example_data.items():
    for v in value:
        messages.append(
            {"role":"user","content":f"句子1：[{v[0]}] 句子2：[{v[1]}]"}
        )
        messages.append(
            {"role":"assistant","content":key}
        )

for q in questions:
    response=client.chat.completions.create(
        model="qwen3-max",
        messages=messages+[{"role":"user","content":f"句子1：[{q[0]}],句子2：[{q[1]}]"}]
    )
    print(response.choices[0].message.content)