from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system","你是一个诗人，可以作诗"),
        MessagesPlaceholder("xiaomi"),
        ("human","请再来一首")
    ]
)

xiaomi_data=[
    ("human","你来写一首诗"),
    ("ai","床前明月光，凝是地上霜，举头望明月，低头思故乡"),
    ("human","再来一个"),
    ("ai","没问题")
]

model=ChatTongyi(model="qwen3-max",streaming=True)

chain=chat_prompt_template | model

# res=chain.invoke({"xiaomi":xiaomi_data})
# print(res.content)
res=chain.stream({"xiaomi":xiaomi_data})
for chunk in res:
    print(chunk.content,end="",flush=True)

