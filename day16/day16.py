from openai import OpenAI

client=OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 示例数据
example_data={
    '新闻报道':'近日，某地发生了一起交通事故，造成多人受伤。事故发生在市中心的十字路口，一辆汽车与一辆摩托车相撞。目击者称，汽车闯红灯导致了这起事故。目前，伤者已被送往医院接受治疗，警方正在调查事故原因。',
    '社交媒体':'今天在社交媒体上，某明星发布了一条动态，宣布将推出自己的新专辑。粉丝们纷纷表示期待，并在评论区留言支持。这条动态很快就获得了数万点赞和转发，成为当天的热门话题。',
    '科学研究':'最近的一项科学研究发现，某种新型材料具有优异的导电性能，可能在未来的电子设备中得到广泛应用。研究人员通过实验验证了这种材料的性能，并发表了相关论文。这一发现为电子技术的发展带来了新的可能性。',
    '不清楚':'今天天气真好，适合出去走走。',
    '不清楚_2':'这首歌真好听，单曲循环了一整天。',
    '不清楚_3':'小明喜欢小红'
}

# 分类列表
example_types=['新闻报道','社交媒体','科学研究']

# 提问数据
question=[
    "近日，国家统计局发布最新经济数据显示，今年前三季度国内生产总值同比增长5.2%，经济运行保持稳中向好态势。专家分析称，消费和出口是拉动增长的主要动力，预计全年经济增长目标有望实现。",
    "今天去了这家网红咖啡馆打卡，环境真的太棒了！拍照超出片📷 咖啡口感也很不错，推荐大家都来试试～下次还要带闺蜜一起来！",
    "一项发表在《自然》杂志上的医学研究表明，通过基因编辑技术可以精准修复某些遗传性疾病的致病突变。研究团队在小鼠实验中取得了显著成果，为未来人类遗传病的治疗提供了全新思路。",
    "小明喜欢小新哦"
]

messages=[
    {"role":"system","content":f"你是文本分类专家，将文本分类为{example_types}。注意：如果文本不属于前三个类别，就归类为'不清楚'。"}
]

for key,vlaue in example_data.items():
    messages.append({"role":"user","content":vlaue})
    messages.append({"role":"assistant","content":key})


for q in question:
    response=client.chat.completions.create(
        model="qwen3-max",
        messages=messages+[{"role":"user","content":f"按照示例回答这段文本的分类：{q}"}]
    )
    print(response.choices[0].message.content)