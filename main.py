import streamlit as st
from utils import xiaohongshu_generator
import json

st.title("爆款小红书AI写作助手")
with st.sidebar:
    api_key = st.text_input("请输入OpenAi API秘钥", type="password")

theme = st.text_input("请输入想要创作的主题")
submit = st.button("开始写作")

if submit:
    if not api_key:
        #st.info("将使用默认api_key")
        #api_key = os.getenv("OPENAI_API_KEY")
        st.info("请输入你的openai_api秘钥")
        st.stop()
    if not theme:
        st.info("请输入主题")
        st.stop()

    with st.spinner("AI正在创作中..."):
        result = xiaohongshu_generator(theme, api_key)

    result_dict = json.loads(result.content)

    if "ai_response" in st.session_state:
        st.session_state["ai_response"].append(result_dict)
        st.session_state["theme"].append(theme)
    else:
        st.session_state["ai_response"] = [result_dict]
        st.session_state["theme"] = [theme]

    st.divider()
    column1, column2 = st.columns(2)
    with column1:
        i=1
        for title in result_dict["titles"]:
            st.markdown("##### 小红书标题"+str(i))
            i = i + 1
            st.write(title)

    with column2:
        st.markdown("##### 小红书正文")
        st.write(result_dict["content"])

    if len(st.session_state["theme"]) >1:
       for i in range(len(st.session_state["theme"])-2,-1,-1):
           text = st.session_state["theme"][i]
           ai_res = st.session_state["ai_response"][i]

           st.divider()
           st.chat_message("human").write(text)
           column1, column2 = st.columns(2)
           with column1:
               i = 1
               for title in ai_res["titles"]:
                   st.markdown("##### 小红书标题" + str(i))
                   i = i + 1
                   st.write(title)

           with column2:
               st.markdown("##### 小红书正文")
               st.write(ai_res["content"])
