from openai import OpenAI

# for backward compatibility, you can still use https://api.deepseek.com/v1 as base_url.
client = OpenAI(api_key="sk-5571256aa2734770bff00fee7cea1d6b", base_url="https://api.deepseek.com")


def get_summary_from_text(text: str, summary_length= 100) -> str:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant which generates summary of the given text in {summary_length} words"},
            {"role": "user", "content": f"{text}"},
        ],
        max_tokens=2048,
        temperature=0.7,
        stream=False
    )
    return response.choices[0].message.content


def summarizer(text):
    summary = get_summary_from_text(text)
    return summary, text, len(text.split(' ')), len(summary.split(' '))