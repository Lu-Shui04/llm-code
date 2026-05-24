from docx import Document
from langchain_community.document_loaders import JSONLoader

# loader=JSONLoader(
#     file_path="./data/stu.json",
#     jq_schema=".",  # 抽取语法
#     text_content=False,  # 告知JSONLoader我抽取的不是字符串
# )
loader=JSONLoader(
    file_path="./data/stus.json",
    jq_schema=".[].name",
    text_content=False,

    # json_lines=True     
    # json_lines=True -> 告知JSONLoader 这是一个JSONLines文件
    # (每一个都是一个独立的标准的JSON文件),比如：
    # {"name": "张三", "age": 20, "gender": "男"},
    # {"name": "李娜", "age": 22, "gender": "女"},
    # {"name": "王伟", "age": 19, "gender": "男"}
)

document=loader.load()
print(document)
