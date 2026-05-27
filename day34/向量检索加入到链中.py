from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

model = ChatTongyi(model="qwen3-max")

prompt = ChatPromptTemplate([
    ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题，参考资料：{context}"),
    ("user", "用户提问：{input}")
])

# 向量库 + 存入知识
vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v4")
)
vector_store.add_texts([
    "减肥就是要少吃多练",
    "减肥期间吃东西很重要，减少油物食物的嗫入多运动",
    "打篮球是好的运动哦"
])

# 把检索操作包装成链的一个环节
def retrieve_context(data: dict) -> dict:
    query = data["input"]
    docs = vector_store.similarity_search(query, 2)
    context = "[" + "".join(d.page_content for d in docs) + "]"
    return {"input": data["input"], "context": context}

# 链: 检索 → 拼提示词 → 调模型 → 解析
chain = RunnableLambda(retrieve_context) | prompt | model | StrOutputParser()

res = chain.invoke({"input": "怎么减肥？"})
print(res)