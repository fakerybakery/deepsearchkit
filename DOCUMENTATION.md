# Documentation

Thank you for using DeepSearchKit! If you prefer some examples, please check out the `demo_index.py` file (a demo of indexing data), and the `demo_search.py` file (a demo of searching data). Simplified examples at bottom.

## Important Notes

**Please read these before using DeepSearchKit! Make sure you've read these notes before reporting bugs! Thank you!**

* You need to load the SAME data *both for searching AND indexing*. You may encounter errors if you load different data for searching and indexing.
* We may introduce **breaking changes** in the future. Make sure to specify the version in your package dependencies.
  * If you share indexed data, **make sure to specify the version of DeepSearchKit it has been tested on** 

## Get Started

### Import DSK

```python
from deepsearchkit import DSK
```

### Create new DSK object

Create a new object with the default model, [`sentence-transformers/all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). This model allows for commercial use.

```python
dsk = DSK()
```

Custom model ID:

```python
dsk = DSK(path="sentence-transformers/all-MiniLM-L6-v2")
```

Low memory mode (disables several crucial features, only slightly decreases memory usage depending on dataset size):

```python
dsk = DSK(lowMem=True)
```

### Load data

#### JSON

```python
dsk.loadJSON(filename="file_path.json", column_names=["title", "description"])
```

Usage:

```
loadJSON(filename: String "The file name", column_names: Array(String) "The column names in the JSON")
```

#### CSV

Make sure you remove the header row.

```python
dsk.loadCSV(filename="file_path.csv", column_index=[1, 2])
```

Usage:

```
loadCSV(filename: String "The file name", column_names: Array(Int) "The index IDs in the CSV")
```

### Index

This method allows you to index your data.

```python
dsk.index()
```

You can show a progress bar in the console as well:

```python
dsk.index(progress=True)
```

### Save index

You can save the index to a folder:

```python
dsk.saveIndex(directory="directory")
```

You can also compress the file:

```python
dsk.saveIndex(directory="file.tar.xz")
```

It will be automatically compressed if the `directory` attribute ends with `tar.gz`, `tar.bz2`, `tar.xz`, or `zip`. `tar.xz` should be most efficient.

### Load from saved index

```python
dsk.loadIndex(directory="directory")
```

### Search

This will return rows from the dataset.

```python
dsk.search(query="machine learning")
```

Specify number of results:

```python
dsk.search(query="machine learning", num_results=5)
```

### Search + return indices

This will return the indices of rows in the dataset.

```python
dsk.searchIndices(query="machine learning", num_results=5)
```

Specify number of results:

```python
dsk.searchIndices(query="machine learning", num_results=5)
```

## Examples

Adapted/simplified from `demo_index.py` and `demo_search.py`.

### Index data

```python
from deepsearchkit import DSK
dsk = DSK()
dsk.loadJSON(filename="demo_data.json", column_names=["title", "content"])
dsk.index(progress=True)
dsk.saveIndex(directory="index_directory")
```

### Search data

You must index data first for this to work.

```python
from deepsearchkit import DSK
dsk = DSK()
dsk.loadJSON(filename="demo_data.json", column_names=["title", "content"])
dsk.loadIndex(directory="index_directory")
results = dsk.search(query="machine_learning")
print("Search Results:")
for i, result in enumerate(results, start=1):
    print(f"{i}. {result[1]}:\n{result[2]}\n")
```



Documentation Copyright 2023. All rights reserved.
