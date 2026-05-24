from operator import length_hint

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader=TextLoader("./data/Python基础语法.txt",encoding="utf-8")

docs=loader.load()

# print(docs)
# print("长度是："+str(len(docs)))  # [Document]对象

splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,     #分段最大字符数
    chunk_overlap=50,   #分段之间允许重叠的字符数
    #文本自然段落分割的依据符号
    separators=["\n\n","\n","。","！","？",".","!","?"," ",""],
    length_function=len  #统计字符的依据函数
)

split_docs=splitter.split_documents(docs)
print("切成了", len(split_docs), "块")
for doc in split_docs:
    print("="*20)
    print(doc)
    print("="*20)
