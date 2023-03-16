import streamlit as st
import openai
import os


def setup_openai_api():
    openai.api_key = "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"

 
  
def get_user_input() -> str:
    return st.text_area("質問", value="OpenAIとOpen AIの違いは？")

def main():
    setup_openai_api()  # OpenAI APIキーを設定する

    system_text = "アシスタントAI"
    user_text = get_user_input()  # ユーザーの入力を取得する
    is_generate_clicked = st.button("回答")

    if is_generate_clicked:
        response = generate_response(system_text, user_text)  # OpenAIに問い合わせを送信し、応答を取得する
        display_response(response)  # OpenAIから受け取った応答を表示する
        
def display_response(response: openai.api_resources.Completion):
    for message in response.choices:
        text = message.text
        st.text(text)

# OpenAIに問い合わせを送信し、応答を取得する関数
def generate_response(system_text: str, user_text: str) -> openai.api_resources.Completion:
    response = openai.Completion.create(
    model='text-davinci-003',
    prompt=user_text,
    temperature=0, # ランダム性の制御[0-1]
    max_tokens=1000, # 返ってくるレスポンストークンの最大数
    top_p=1.0, # 多様性の制御[0-1]
    frequency_penalty=0.0, # 周波数制御[0-2]：高いと同じ話題を繰り返さなくなる
    presence_penalty=0.0 # 新規トピック制御[0-2]：高いと新規のトピックが出現しやすくなる
    )
    return response

if __name__ == "__main__":
    main()