from ai_agent import ai_rename

def should_rename(filename):
    keywords = ['img', 'final', 'copy', 'v1', 'v2']
    return any(k in filename.lower() for k in keywords)


def get_new_name(filename):
    if should_rename(filename):
        return ai_rename(filename)
    return filename
