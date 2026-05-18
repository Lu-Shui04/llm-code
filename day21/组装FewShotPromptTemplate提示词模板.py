from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate

# 通用提示词模板
example_template=PromptTemplate.from_template(
    "单词：{work},反义词：{antonym}"
    )

# 示例数据
example_data=[
    {"work":"大","antonym":"小"},
    {"work":"上","antonym":"下"}
]

# FewShot提示词模板对象
few_shot_prompt=FewShotPromptTemplate(
    example_prompt=example_template,
    examples=example_data,
    prefix="给出给定词的反义词，有如下示例",
    suffix="基于示例告诉我：{input_work}的反义词是什么",
    input_variables=['input_work']
)

# 获得最终提示词
prompt_text=few_shot_prompt.invoke(input={"input_work":"左"}).to_string()
print(prompt_text) 
