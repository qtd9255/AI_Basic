from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ai_classify(filename):
    prompt = f"""
    파일명을 보고 카테고리 하나 선택:
    [과제, 문서, 이미지, 코드, 기타]

    파일명: {filename}
    """

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content.strip()


def ai_rename(filename):
    prompt = f"""
    파일명을 더 의미있게 변경하세요.

    규칙:
    - 영어 소문자
    - 공백 대신 _
    - 확장자 유지

    파일명: {filename}
    """

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content.strip()
