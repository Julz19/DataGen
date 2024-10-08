# Datagen

This repository contains simple code to get started with generating high-quality synthetic data using LLMs provided documentation.

-----
### Getting Started

1. Clone the repo from git and cd into it
```bash
git clone https://github.com/Julz19/DataGen.git
cd DataGen
```

2. Install the dependencies
```bash
pip install -r requirements.txt
```

3. Run the main.py script to get started the fastest and begin generating an example dataset for Mojo Code using the contained documents.json file
```bash
python main.py
```
-----

**NOTE:** The current state of the script **DOES NOT** handle output parsing situations, meaning user and assistant completions will contain '<user></user>', '<assistant></assistant>' tags within them. o ensure a proper clean generation, please handle this parsing and cleaning accordingly.

This is **NOT** meant to be used in production applications and instead is to be seen as more of a starting point for beginners or as a research point into synthetic data generation.
