import openai
import os
import pandas as pd
import json 
# Assign OpenAI API Key from environment variable
df_csv = pd.read_csv("test.csv",encoding = "utf_8")
print(df_csv)
openai.api_key = ''
messages = []
system_msg = "プロンプト内にあるデータフレームを基に質問に答えて,\
    データフレームは複数の商品の詳細情報である.\
    「～はありますか」という問いには「～件」有りますと回答."
messages.append({"role": "system", "content": system_msg})
df_json = df_csv.to_dict(orient="records")
messages.append(df_json)
print("Say hello to your new assistant!")
while input != "quit()":
    message = input ("🙋 Human: ")
    messages.append ({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.8,
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("---\n🤖 Riley: " + reply + "\n---")

