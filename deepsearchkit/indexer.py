import txtai
from txtai.embeddings import Embeddings
from tqdm import tqdm
from .error_handler import *
class DSKIndexer:
    """Low(er)-level indexer from DSK"""
    _embeddings = None
    _hasIndexed = False
    def __init__(self, path: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self._embeddings = Embeddings({
            "path": path
        })
    def index(self, data: [str], progress: bool = False):
        datalen = len(data)
        if progress:
            self._embeddings.index(tqdm(self._data, total=datalen))
        else:
            self._embeddings.index(self._data)
        self._hasIndexed = True
    def save(self, directory: str):
        if self._hasIndexed == False:
            raise DSKUnindexedError('Not indexed yet')
        self._embeddings.save(directory)