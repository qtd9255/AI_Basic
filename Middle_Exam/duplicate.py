import hashlib
import os

def get_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        if os.path.isfile(path):
            h = get_hash(path)
            if h in hashes:
                duplicates.append((f, hashes[h]))
            else:
                hashes[h] = f

    return duplicates
