def generate_preview(files, classifier, renamer):
    preview = []

    for f in files:
        category = classifier(f)
        new_name = renamer(f)

        preview.append({
            "original": f,
            "category": category,
            "new_name": new_name
        })

    return preview
