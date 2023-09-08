import txtai
from txtai.embeddings import Embeddings
from tqdm import tqdm
import mimetypes
import textract
import os
import json
embeddings = Embeddings({
    "path": "sentence-transformers/all-MiniLM-L6-v2"
})
txtext = (
    '.txt', '.csv', '.log', '.md', '.markdown', '.rst', '.html', '.json', '.xml', '.yaml', '.yml', '.ini', '.cfg', '.conf', '.bat', '.sh', '.c', '.cpp', '.h', '.java', '.py', 'mdown'
)

def isPlainTxt(path: str):
    if mimetypes.guess_type(path)[0] == 'text/plain':
        return True
    for ext in txtext:
        if path.endswith(ext):
             return True
    return False
def list_files(start_dir):
    file_list = []
    for root, _, files in os.walk(start_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if not file.startswith('.'):
                file_list.append(file_path)
    return file_list

def get_text_from_doc(path: str):
    if not os.path.isfile(path):
        return ''
    if isPlainTxt(path):
        with open(path, 'r') as f:
            return f.read()
    else:
        try:
            return textract.process(path).decode()
        except:
            return ''

start_dir = 'example_dir'
data = []
files = []
for file in list_files(start_dir):
    text = get_text_from_doc(file).strip()
    if text:
        data.append(text)
        files.append(file)

with open('data.json', 'w') as f:
    json.dump(files, f)

embeddings.index(tqdm(data, total=len(data)))
embeddings.save('index')