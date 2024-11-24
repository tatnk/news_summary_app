from openai import OpenAI

def summarize_text(text):
    client = OpenAI()
    response = client.chat.completions.create(
        messages=[
        {"role": "system", "content": "あなたは丁寧で具体的な回答をするアシスタントです。"},
        {"role": "user", "content": f"このニュース記事を要約してください。記事の内容：{text}"}
    ],
        model="gpt-4o-mini"
    )
    return response.choices[0].message.content.strip()