from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

vector_store=InMemoryVectorStore(
    embedding=DashScopeEmbeddings()
)

loader=CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source"      #指定本条数据的来源是哪里
)

documents=loader.load()
# print(documents[1])

# 向量存储的 新增，删除，检索
vector_store.add_documents(
    documents=documents,    #被添加的文档，类型list[Document]
    ids=["id"+str(i) for i in range(1,len(documents)+1)]
)

# 删除 传入[id,id,...]
vector_store.delete(["id1","id3"])

# 检索
result=vector_store.similarity_search(
    "如何正确切分数据",
    2
)

print(result)