from typing import Optional
from sqlmodel import text

def get_query(query_file_path: str):
    with open(query_file_path, 'r', encoding='utf-8') as f :
        query = f.read()
    return text(query)