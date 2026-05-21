from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda

model=ChatTongyi(model="qwen3-max",streaming=True)
str_parser=StrOutputParser()

first_prompt=PromptTemplate.from_template(
    "我的邻居姓{lastname},生了{gender}儿，帮我起名，仅告知我名字，不要额外信息"
)
second_prompt=PromptTemplate.from_template(
     "姓名{name},请帮我解析含义"
)
# 函数的入参：AImessage -> dict(字典) ({"name":"xxx"})
my_func=RunnableLambda(lambda ai_msg:{"name":ai_msg.content})

chain=first_prompt|model|my_func|second_prompt|model|str_parser
for chunk in chain.stream({"lastname":"张","gender":"女"}):
    print(chunk,end="",flush=True)