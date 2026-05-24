from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter":",",  # 指定分隔符(默认是,)
        #"quotechar":'"',  # 指定带有分隔符文本的引号包围是单引号还是双引号
        # 如果数据有表头就不使用fieldnames
        "fieldnames":['name','age','性别','其他']
    },
    encoding="utf-8"  # 指定编码
)

# 批量加载.load() -> [Document,Document,...]
# documents=loader.load()

# # print(documents)
# for document in documents:
#     print(document)


# 懒加载 .lazy_load()
for documen in loader.lazy_load():
    print(documen)

# 内存足够大批量加载，不然 懒加载
