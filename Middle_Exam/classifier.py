from ai_agent import ai_classify

def classify_file(filename):
    ext = filename.split('.')[-1].lower()

    if ext in ['jpg', 'jpeg', 'png', 'gif']:
        return "이미지"
    elif ext in ['pdf', 'docx', 'txt']:
        return "문서"
    elif ext in ['py', 'js', 'java']:
        return "코드"
    elif 'report' in filename.lower():
        return "과제"

    return ai_classify(filename)
