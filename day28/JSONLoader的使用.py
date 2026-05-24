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
    text_content=False
)

document=loader.load()
print(document)
