import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件，确保 API Key 受到保护
load_dotenv()
client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL"),
)
completion = client.chat.completions.create(
    model=os.getenv("MODEL"),  # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁？'}],
)
response = completion.choices[0].message.content
print(response)