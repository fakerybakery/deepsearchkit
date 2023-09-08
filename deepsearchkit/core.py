import txtai
from txtai.embeddings import Embeddings
import json
import csv
from tqdm import tqdm
from .error_handler import *
class DSK:
    _data = []
    _dat = []
    _lowMem = False
    _embeddings = None
    _hasIndex = False
    def __init__(self, path: str = "sentence-transformers/all-MiniLM-L6-v2", lowMem: bool = False):
        """
        Create a DeepSearchKit object.

        Args:
            path (str): The path to the pre-trained model (locally or on Hugging Face Hub).
            lowMem (bool): Low-memory mode. Only slightly decreases memory usage, depending on data size.
        """
        self._lowMem = lowMem
        self._embeddings = Embeddings({
            "path": path
        })

    def loadCSV(self, filename: str, column_index: [int]):
        """
        Load CSV data into DeepSearchKit.

        Args:
            filename (str): The path to the CSV file.
            column_index (list of int): A list of column indices to extract data from.
        """
        with open('output.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                r = ""
                for i in column_index:
                    r += f"{row[i]}\n"
                self._data.append(r)
                if self._lowMem == False:
                    self._dat.append(row)

    def loadJSON(self, filename: str, column_names: [str]):
        """
        Load JSON data into DeepSearchKit.

        Args:
            filename (str): The path to the JSON file.
            column_names (list of str): A list of column names to extract data from the JSON objects.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
                r = ""
                for column_name in column_names:
                    r += f"{item.get(column_name, '')}\n"
                self._data.append(r)
                if self._lowMem == False:
                    self._dat.append(list(item.values()))

    def index(self, progress: bool = False):
        """
        Index the loaded data.

        Args:
            progress (bool): If True, display indexing progress using TQDM.
        """
        if len(self._data) == 0:
            raise DSKUndefinedVariableError('No data loaded has been loaded')
        if not self._embeddings:
            raise DSKUndefinedVariableError('No embedding model has been specified. This should usually be done automatically, so please create an Issue on DeepSearchKit source code. Make sure to include the full traceback and your source code.')
        if len(self._data) == 0:
            raise DSKEmptyDataError('Your data is empty. Please debug your code. If this issue persists, please create an Issue on DeepSearchKit source code. Make sure to include the full traceback and your source code.')
        datalen = len(self._data)
        if progress:
            self._embeddings.index(tqdm(self._data, total=datalen))
        else:
            self._embeddings.index(self._data)
        self._hasIndex = True

    def saveIndex(self, directory: str):
        """
        Save the index to a directory.

        Args:
            directory (str): The directory where the index should be saved.
        """
        if self._hasIndex == False:
            raise DSKUnindexedError('You do not have a loaded index. Check our documentation for details.')
        self._embeddings.save(directory)

    def loadIndex(self, directory: str):
        """
        Load an index from a directory.

        Args:
            directory (str): The directory from which the index should be loaded.
        """
        self._embeddings.load(directory)
        self._hasIndex = True

    def searchIndices(self, query: str, num_results: int = 5):
        """
        Search the embeddings for matching results and returns the indices of matching results.

        Args:
            query (str): The search query.
            num_results (int): The number of results to retrieve.

        Returns:
            list: A list of indices of matching results.
        """
        if self._hasIndex == False:
            raise DSKUnindexedError('You do not have a loaded index. Check our documentation for details.')
        res = self._embeddings.search(query, num_results)
        return [r[0] for r in res]
    
    def search(self, query: str, num_results: int = 5):
        """
        Search the embeddings for matching results and returns the data of matching results.

        Args:
            query (str): The search query.
            num_results (int): The number of results to retrieve.

        Returns:
            list: A list of the data of matching results.
        """
        if self._lowMem:
            raise DSKFeatureNotSupportedError("Data not stored on low-memory mode. Disable low-memory mode to enable this feature.")
        if self._hasIndex == False:
            raise DSKUnindexedError('You do not have a loaded index. Check our documentation for details.')
        res = self._embeddings.search(query, num_results)
        return [self._dat[r[0]] for r in res]


    def getData(self):
        """
        Get the loaded data.

        Returns:
            list: The loaded data.
        """
        if self._lowMem:
            raise DSKFeatureNotSupportedError("Data not stored on low-memory mode. Disable low-memory mode to enable this feature.")
        return self._dat
