from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

model=ChatTongyi(model="qwen3-max", streaming=True)

messages=[
    ("system","你是诗人家"),
    ("human","写一首幽默诗"),
    ("ai","我不想回答!"),
    ("human","不要生成诗，告诉我你为什么不想回答？")
]
res=model.stream(input=messages)

for chunk in res:
    print(chunk.content,end="",flush=True)