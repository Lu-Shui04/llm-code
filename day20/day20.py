from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

model=ChatTongyi(model="qwen3-max",streaming=True)

messages=[
    ("system","你是小米智能机器人"),
    ("human","你是谁")
]
res=model.stream(messages)

for chunk in res:
    print(chunk.content,end="",flush=True)
