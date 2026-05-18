from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.llms.tongyi import Tongyi

# 示例模板
example_template=PromptTemplate.from_template(
    "单词：{work}，反义词：{antonym}"
)

# 示例的动态数据注入
example_data=[
    {"work":"大","antonym":"小"},
    {"work":"上","antonym":"下"}
]

few_shot_template=FewShotPromptTemplate(
    example_prompt=example_template,  #示例数据的模板
    examples=example_data,        #示例的数据（用来动态输入数据，格式list套字典）
    prefix="告知我单词的反义词，我提供一下示例",          #示例之前的提示词
    suffix="根据以上的示例，{input_work}反义词是什么",         #示例之后的提示词
    input_variables=["input_work"]    #声明在前缀或后缀中所需要注入的变量名
)

prompt_text=few_shot_template.invoke(input={"input_work":"左"}).to_string()

model=Tongyi(model="qwen-max",streaming=True)

res=model.invoke(input=prompt_text)
print(res)