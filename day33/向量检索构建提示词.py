from altair import PredicateComposition
from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from openai import vector_stores

model=ChatTongyi(model="qwen3-max")
prompt=ChatPromptTemplate(
    [
        ("system","以我提供的已知参考资料为主，简洁和专业的回答用户问题，参考资料：{context}"),
        ("user","用户提问：{input}")
    ]
)

vector_store=InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v4")
)

# 准备资料 (向量库的数据)
# add_texts 传入一个list[str]
vector_store.add_texts(["减肥就是要少吃多练","减肥期间吃东西很重要，减少油物食物的嗫入多运动","打篮球是好的运动哦"])

input_text="怎么减肥？"

# 检索向量库
result=vector_store.similarity_search(input_text,2)
# print(result)
reference_text="["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"
print(reference_text)

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt 
 
# chain
chain=prompt|print_prompt|model|StrOutputParser()

res=chain.invoke({"input":input_text,"context":reference_text})
print(res)