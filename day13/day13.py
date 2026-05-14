import streamlit as st
import time

st.title("🎈 小米智能机器人")
st.write("小米开发")
st.divider()

# 初始化对话记录（只执行一次）
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 先显示历史对话记录
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# 接收用户输入
prompt = st.chat_input("输入你的问题：")
if prompt:
    # 存入并显示用户消息
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # 模拟思考
    with st.spinner("正在思考..."):
        time.sleep(2)
        response = "小米在开发中，敬请期待！☺️"

    # 存入并显示机器人回复
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
