from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage ,AIMessage ,SystemMessage

model=ChatTongyi(model="qwen3-max")

messages=[
    SystemMessage(content="你是三国时代的唐人。"),
    HumanMessage(content="接我的诗[天不佑我]"),
    AIMessage(content="[心上挥剑]"),
    HumanMessage(content="[今时不胜仗],下一句是："),

]

# 调用stream流式输出
res=model.stream(input=messages)

# 聊天模型需要通过.content来获取内容
for chunk in res:
    print(chunk.content,end="",flush=True)