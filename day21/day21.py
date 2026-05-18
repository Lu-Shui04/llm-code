from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.llms.tongyi import Tongyi

example_prompt=PromptTemplate.from_template("正：{work},反：{antonym}")

examples_data=[
    {"work":"大","antonym":"小"},
    {"work":"上","antonym":"下"}
]

few_shot_prompt=FewShotPromptTemplate(
    example_prompt=example_prompt,
    examples=examples_data,
    prefix="告诉我反义词，一下是示例",
    suffix="根据以上的示例，{input_work}的反义词是什么",
    input_variables=['input_work']
)
prompt_text=few_shot_prompt.invoke(input={"input_work":"左"}).to_string()
print(prompt_text)

model=Tongyi(model="qwen-max")
res=model.invoke(input=prompt_text)
print(res)