# 导入字符串解析器包和JSON解析器包
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.output_parsers import JsonOutputParser
# 导入通用提示词模板包
from langchain_core.prompts import PromptTemplate
# 导入聊天大模型包
from langchain_community.chat_models.tongyi import ChatTongyi

# 创建字符串和JSON解析器对象
str_parser=StrOutputParser()
json_parser=JsonOutputParser()

model=ChatTongyi(model="qwen3-max",streaming=True)

# 不要忘记.from_template
# 第一个提示词模板
first_prompt=PromptTemplate.from_template(
    "我的邻居姓{lastname},生了{gender}儿，帮我起名，并封装到JSON格式返回给我"
    "要求key是name，value就是起的名字，请严格遵守格式要求"
)

# 第二个提示词模板
second_prompt=PromptTemplate.from_template(
    "姓名{name},请帮我解析含义"
)

# 创建链
chian=first_prompt | model | json_parser | second_prompt | model | str_parser

res=chian.invoke({"lastname":"王","gender":"女"})
print(res)

