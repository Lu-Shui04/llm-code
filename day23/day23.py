from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

str_parser=StrOutputParser()
json_parser=JsonOutputParser()

model=ChatTongyi(model="qwen3-max")

first_prompt=PromptTemplate.from_template(
    "我的邻居姓{lastname},生了{gender}儿，帮我起名，并封装到JSON格式返回给我"
    "要求key是name，value就是起的名字，请严格遵守格式要求"
)

second_prompt=PromptTemplate.from_template(
    "姓名{name},请帮我解析含义"
)
chain=first_prompt | model | json_parser | second_prompt | model | str_parser

res=chain.invoke({"lastname":"王","gender":"男"})
print(res)
