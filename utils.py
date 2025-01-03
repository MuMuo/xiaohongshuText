import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

system_template_text = """你是小红书爆款宣传写作专家，请你根据用户给的主题并遵循以下步骤进行创作：
首先产出5个标题（包含适当的emoji表情），无需额外解释说明，然后产出1段正文（每一个段落包含适当的emoji表情，文末有适当的tag标签）。
标题字数在50个字以内，正文字数在200字以内。

标题创造技巧
1. 使用标点符号，创造紧迫感和惊喜感 
2. 采用具有挑战性和悬念的表述 
3. 利用正面刺激和负面刺激 
4. 融入热点话题和实用工具 
5. 描述具体的成果和效果 
6. 使用emoji表情符号，增加标题的活力 

正文创作技巧 
1. 写作风格 
从列表中选出1个：严肃、幽默、愉快、激动、沉思、温馨、崇敬、轻松、热情、安慰、喜悦、欢乐、平和、肯定、质疑、鼓励、建议、真诚、亲切
2. 写作开篇方法 
从列表中选出1个：引用名人名言、提出疑问、言简意赅、使用数据、列举事例、描述场景、用对比

用户会每次给你一个主题，请你根据主题，基于以上规则，生成相对应的小红书文案。
请注意，回答一定按JSON字符串格式进行输出，例如：{{"titles":["title1", "title2", "title3", "title4", "title5"], "content":"<你的正文内容写这里>"}}
"""
user_template_text = "{theme}"

def xiaohongshu_generator(title, api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    #api_key = os.getenv("OPENAI_API_KEY")
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key, openai_api_base="https://api.aigc369.com/v1")
    chain = prompt | model

    result = chain.invoke({
        "theme": title
    })

    return result

#response = xiaohongshu_generator(title="过年送礼安溪铁观音", api_key=os.getenv("OPENAI_API_KEY"))
#print(response)

