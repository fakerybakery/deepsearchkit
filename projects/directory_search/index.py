import txtai
from txtai.embeddings import Embeddings
from tqdm import tqdm
import mimetypes
import textract
import os
embeddings = Embeddings({
    "path": "sentence-transformers/all-MiniLM-L6-v2"
})
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
    if mimetypes.guess_type(path)[0] == 'text/plain':
        with open(path, 'r') as f:
            return f.read()
    else:
        try:
            return textract.process(path).decode()
        except:
            return ''
start_dir = 'example_dir'
data = []
for file in list_files(start_dir):
    text = get_text_from_doc('example_dir/attn_all_you_need.pdf').strip()
    if text:
        data.append(text)
embeddings.index(tqdm(data, total=len(data)))
embeddings.save('index')