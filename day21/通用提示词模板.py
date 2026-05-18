from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template=PromptTemplate.from_template(
    "我的朋友姓{lastname},刚生了{gender}儿,你帮我起个名字简单回答。"
)

# 调用.format方法注入信息
# prompt_text=prompt_template.format(lastname="米",gender="男")

# model=Tongyi(model="qwen-max",streaming=True)

# res=model.invoke(input=prompt_text)
# for chunk in res:
#     print(chunk,end="",flush=True)

# 学习链
model=Tongyi(model="qwen-max",streaming=True)

chain=prompt_template | model
res=chain.invoke(input={"lastname":"张","gender":"男"})
for chunk in res:
    print(chunk,end="",flush=True)
