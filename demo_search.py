from deepsearchkit import DSK
dsk = DSK()
dsk.loadJSON(filename="demo_data.json", column_names=["title", "content"])
dsk.loadIndex(directory="index_directory")
while True:
    results = dsk.search(query=input("> "), num_results=5)
    print("Search Results:")
    for i, result in enumerate(results, start=1):
        print(f"{i}. {result[1]}:\n{result[2]}\n")
