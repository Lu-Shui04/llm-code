from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model=ChatTongyi(model="qwen3-max")
str_parser=StrOutputParser()

Prompt=ChatPromptTemplate.from_messages(
    [
        ("system","请根据历史记录回答问题"),
        MessagesPlaceholder("chat_history"),
        ("human","请回答一下问题,{input}")
    ]
)

story={}
def get_history(session_id):
    if session_id not in story:
        story[session_id]=InMemoryChatMessageHistory()
    return story[session_id]

base_chian=Prompt | model | str_parser

conversations_chain=RunnableWithMessageHistory(
    base_chian,
    get_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

if __name__=="__main__":
    session_config={
        "configurable":{
            "session_id":"user001"
        }
    }
    res=conversations_chain.invoke({"input":"小米有2只猫"},session_config)
    print("第1次：",res)

    res=conversations_chain.invoke({"input":"小啊有5只猫"},session_config)
    print("第2次：",res)

    res=conversations_chain.invoke({"input":"总共多少猫"},session_config)
    print("第3次：",res)