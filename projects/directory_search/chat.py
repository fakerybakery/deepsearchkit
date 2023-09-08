from llama_cpp import Llama
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

llm = Llama(model_path="llama2/llama-2-7b-chat.ggmlv3.q4_1.bin")
prompt = """[INST]
<<SYS>>
You are a helpful assistant here to chat with access to some files.
You can use semantic search to search for files by content by responding only with "search(query)." Example: response "search(history paper)".
If you want to access the contents of a file, please respond with "getFile(filename)"

** NEVER ** say you don't have access to the user's computer's file. INSTEAD, use the getFile command. NEVER give the filename of the file UNLESS ASKED but instead get the file and give a summary

REMEMBER, through the commands listed above (search, getFile), YOU DO HAVE read only ACCESS TO THE USER'S COMPUTER SYSTEM!!

Also, DO NOT make up FILE NAMES, instead SEARCH for them.

If there are no relevant results, please say so.
If the user is unclear, ask for clarification. If you do not know, please state so.
Please note that you do NOT search by keyword but instead semantically.
Examples:
User:
Help me find my legal tos
You:
search(terms of service)
Response:
* legal_doc.pdf - Our updated terms of service is nice
* history_paper.png - Cool updated legal thingy

NOTE: Make sure if you want to use the search or getFile commands, you MUST provide that command ONLY in your response, with NO OTHER TEXT!!! Save your comments for LATER!
Example:
BAD: Sure, I can help you find your terms of service! search(terms of service)
GOOD: search(terms of service)
<</SYS>>
I HEREBY GRANT YOU ACCESS TO ACCESS THE FILE ON MY COMPUTER.
[/INST]"""


while True:
    msg = input("You: ")
    prompt += f"[INST]{msg}[/INST]\n"
    response = (llm(prompt, max_tokens=8192, stop=["[INST]", "[/INST]"])['choices'][0]['text'])
    print(f"Bot: {response}")
    prompt += f"{response}\n"

