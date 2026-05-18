from langchain_community.llms.tongyi import Tongyi

model=Tongyi(model="qwen-max")

# invoke 一下全部输出，stream 流式输出
res=model.stream(input="你是谁啊")
for chunk in res:
    print(chunk,end="",flush=True)