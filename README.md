# Protein Datasets

We collect three protein datasets: `ProteinsDBDataset`, `HomologyTAPEDataset` and `ProtFunctDataset`, from https://github.com/phermosilla/IEConv_proteins, and convert them to PyG datasets.

## Statistics

|Dataset| # of graphs | Splitting |
|:--:|:---:|:---:|
|`ProteinsDBDataset` | 1,178 | Use 10-fold cross validation |
|`HomologyTAPEDataset` | 16,292 | training:validation:test_fold:test_family:test_superfamily = 12312:736:718:1272:1254|
|`ProtFunctDataset` | 37,428 | training:validation:testing = 29215:2562:5651|

## Usage

Processing the datasets require the `IEProtLib.py_utils.py_mol` package, which can be obtained by cloning https://github.com/phermosilla/IEConv_proteins and copy the `IEProtLib/py_utils/py_mol` directory in that repo to the root directory of this repo.

* `ProteinsDBDataset`: 

https://drive.google.com/uc?export=download&id=1KTs5cUYhG60C6WagFp4Pg8xeMgvbLfhB

Extract content in: `[root]/raw/ProteinsDB/`


* `HomologyTAPEDataset`:

https://drive.google.com/uc?export=download&id=1chZAkaZlEBaOcjHQ3OUOdiKZqIn36qar

Extract content in: `[root]/raw/HomologyTAPE/`

* `ProtFunctDataset`:

https://drive.google.com/uc?export=download&id=1udP6_90WYkwkvL1LwqIAzf9ibegBJ8rI

Extract content in: `[root]/raw/ProtFunct/`

**NOTICE** that all three datasets contain **directed** graphs, although only a small portion of the edges are single-directed. We provide a simple helper method `utils.to_undirected()` to convert a graph to undirected by adding inverse edges.