from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

model=ChatTongyi(model="qwen3-max",streaming=True)
prompt=PromptTemplate.from_template(
    "我邻居姓{lastname},刚生了{gender}儿，给我起名"
)
# ai的回答是aimessage，所以需要字符串解析器来转换字符串
# 再传给下个model
parser=StrOutputParser()  #字符串解析器
chain=prompt | model | parser | model | parser

res=chain.invoke({"lastname":"张","gender":"女"})
print(res)
