import txtai
import json
from txtai.embeddings import Embeddings
from tqdm import tqdm
import mimetypes
import subprocess
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
embeddings.load('index')

files = []
with open('data.json', 'r') as f:
    files = json.load(f)

while True:
    res = embeddings.search(input("Query: "), 2)
    for r in res:
        file = files[r[0]]
        print(file)