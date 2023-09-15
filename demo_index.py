from deepsearchkit import DSK
dsk = DSK()
dsk.loadJSON(filename="demo_data.json", column_names=["title", "content"])
dsk.index(progress=True)
dsk.saveIndex(directory="index_directory")
print("Data indexed and saved to 'index_directory'.")
