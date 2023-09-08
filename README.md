# DeepSearchKit

A small, fast, and easy package that allows easy semantic searching using artificial intelligence. It is based on and similar to the closed-source DeepSearch system.

## Installation

You can install the latest stable version from the registry:

```
pip3 install deepsearchkit
```

You can install the very latest version directly from the Git repository, however certain features may not work:

```
pip3 install git+https://github.com/fakerybakery/DeepSearchKit
```

## Features

 * CPU, CUDA, and MPS support (enhanced GPU acceleration)!
 * Simple usage

## Usage

Documentation is available [here](DOCUMENTATION.md).

## Todo

- [ ] Integrate DeepSearch into DeepSearchKit
  - [ ] Open-source DeepSearch
- [ ] Add Web Interface (from DeepSearch)
- [ ] Add document search demo
  - [ ] Add document chat demo
- [ ] Add upsert feature ([txtai#251](https://github.com/neuml/txtai/issues/251))
- [ ] Add more data support, e.g. parquet
- [ ] Custom prompt/data format for multiple columns in JSON
- [ ] Custom progress callback for indexing
- [ ] Make some example projects
  - [ ] Chat with a folder using open-sourced conversational models
  - [ ] Search an entire directory
- [ ] Allow easy publishing with a `.dskpkg` file - compressed DeepSearchKit package that includes the index, the data, and some attributes (name, author, license, etc)
  - [ ] Maybe in the future: "DSK Hub" - hub for DSK packages

## Credits

We would like to thank the authors of the following open source projects:

 * [sentence-transformers](https://github.com/UKPLab/sentence-transformers)
 * [txtai](https://github.com/neuml/txtai)

## Disclaimer

By using/contributing to this software, you agree to the [disclaimer](DISCLAIMER.md).