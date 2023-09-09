Note: This project is still a work-in-progress. It works, but it doesn't have many features yet. Please suggest features, report problems (bugs should go in Issues), or just say hi in Discussions!

![PyPI - Downloads](https://img.shields.io/pypi/dm/deepsearchkit)

# :mag: DeepSearchKit

A small, fast, and easy package that allows easy semantic searching using :brain: artificial intelligence. It is based on and similar to the closed-source DeepSearch system.

## :computer: Installation

You can install the latest stable version from the registry:

```
pip3 install deepsearchkit
```

You can install the very latest version directly from the Git repository, however certain features may not work:

```
pip3 install git+https://github.com/fakerybakery/deepsearchkit
```

## :white_check_mark: Features

 * CPU, CUDA, and MPS support (enhanced GPU acceleration)!
 * Simple usage

## :newspaper: Usage

Documentation is available [here](DOCUMENTATION.md).

## :thought_balloon: Todo

- [ ] Integrate DeepSearch into DeepSearchKit
  - [ ] Open-source DeepSearch
- [ ] Add Web Interface (from DeepSearch)
- [ ] Add document search demo
  - [ ] Add document chat demo
- [ ] Add upsert feature ([txtai#251](https://github.com/neuml/txtai/issues/251))
- [ ] Add more data support, e.g. parquet, MySQL/hosted DBs
- [ ] Custom prompt/data format for multiple columns in JSON
- [ ] Custom progress callback for indexing
- [ ] Make some example projects
  - [ ] Chat with a folder using open-sourced conversational models
  - [ ] Search an entire directory
- [ ] Allow easy publishing with a `.dskpkg` file - compressed DeepSearchKit package that includes the index, the data, and some attributes (name, author, license, etc)
  - [ ] Maybe in the future: "DSK Hub" - hub for DSK packages

## :memo: Credits

We would like to thank the authors of the following open source projects:

 * [sentence-transformers](https://github.com/UKPLab/sentence-transformers)
 * [txtai](https://github.com/neuml/txtai)

## :briefcase: Disclaimer/Agreement (Read BEFORE you contribute!)

In every new issue/PR, make sure to include "I agree to the disclaimer!"

By using/contributing to this software, you agree to the [agreement](DISCLAIMER.md).
