import json

# 字典
d={
    'name':'小米',
    'age':20,
    'gender':'男'
}
s=json.dumps(d,ensure_ascii=False) # 将字典转换成json字符串，ensure_ascii=False可以让中文正常显示
print(s)

# 列表
l=[
    {'name':'张三','age':25,'gender':'男'},
    {'name':'李四','age':30,'gender':'女'}, 
]

s=json.dumps(l,ensure_ascii=False) # 将列表转换成json字符串，ensure_ascii=False可以让中文正常显示
print(s)

print("-"*50)
json_str='{"name": "小米", "age": 20, "gender": "男"}'
res_dict=json.loads(json_str) # 将json字符串转换成字典，json.loads()函数可以将json字符串转换成python对象，这里是字典
print(res_dict)
print(res_dict['name'])
