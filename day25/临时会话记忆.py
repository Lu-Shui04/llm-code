from click import prompt
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model=ChatTongyi(model="qwen3-max",streaming=True)

# Prompt=PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题。对话历史：{chat_history},用户问题：{input},请回答"
# )
Prompt=ChatPromptTemplate.from_messages(
    [
         ("system","你需要根据会话历史回应用户问题。"),
         MessagesPlaceholder("chat_history"),
         ("human","请回答一下问题,{input}")

    ]
)

# 字符串解析器
str_parser=StrOutputParser()

def print_prompt(full_prompt):
    print("="*10,full_prompt.to_string(),"="*10)
    return full_prompt

# 创建基础链
base_chain= Prompt | print_prompt |model | str_parser #提示词给模型，模型的输出字符串解析器解析成字符串

# 创建一个字典存储历史对话
store={}  #key就是session_id,value就是InMemoryChatMessageHistory类对象

# 实现通过会话id获取InMemoryChatMessageHistory
def get_history(session_id):
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()
    return store[session_id]

# 创建一个新的链，对原有的链增强功能:自动附加历史消息
conversations_chain=RunnableWithMessageHistory(
    # 需要四个参数
    base_chain,     #被增强的原有的chain
    get_history,    #通过会话id获取InMemoryChatMessageHistory
    input_messages_key="input", #表示用户输入在模板中的占位符
    history_messages_key="chat_history" #表示用户输入在模板中的占位符
)


if __name__=='__main__':
    session_config={
        "configurable":{
            "session_id":"user001"
        }
    }

    res=conversations_chain.invoke({"input":"小明有2条狗"},session_config)
    print("第1次执行：",res)

    res=conversations_chain.invoke({"input":"小张有3只猫"},session_config)
    print("第2次执行：",res)

    res=conversations_chain.invoke({"input":"总共多少个宠物"},session_config)
    print("第3次执行：",res)
