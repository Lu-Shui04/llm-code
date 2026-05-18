from langchain_community.embeddings import DashScopeEmbeddings

# 创建模型对象,不传model默认是 text-embedding-v1
model=DashScopeEmbeddings()

# 不用invoke stream
# embed_query，embed_documents
print(model.embed_query("我叫小米")) #单次转换向量
print(model.embed_documents(["你好","哈哈"])) #批量转换向量
 
#  langchain通用提示词模板