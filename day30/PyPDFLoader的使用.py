from langchain_community.document_loaders import PyPDFLoader

# 快速读取pdf文件，提取文字
loader=PyPDFLoader(
    file_path="./data/pdf1.pdf",
    # mode="page",    # 默认是page模式，每个页面生成一个Document文档对象
    mode="single",    # single模式，不管有多少页，只返回1个Document对象
    # password="123456"  对加密的pdf需要填写密码
)

i=0
for doc in loader.lazy_load():
    i += 1
    print(doc)
    print("="*20,i)