import numpy as np
from typing import Dict
from IEProtLib.py_utils.py_mol.PyProtein import PyProtein

def read_file(protein: PyProtein, filename: str) -> Dict:
    protein.load_hdf5(filename)
    return {'AminoChainIDs': protein.aminoChainIds_,
            'AminoPos': protein.aminoPos_,
            'AminoType': protein.aminoType_,
            'AminoNeighbors': protein.aminoNeighs_,
            'AminoNeighborsSIndices': protein.aminoNeighsSIndices_,
            'AminoNeighborsHB': protein.aminoNeighsHB_,
            'AminoNeighborsSIndicesHB': protein.aminoNeighsSIndicesHB_,
            }

def get_num_nodes(file_dict: Dict) -> int:
    return file_dict['AminoPos'].shape[1]

def get_edge_index(file_dict: Dict, includeHB: bool) -> np.ndarray:
    return file_dict['AminoNeighborsHB'] if includeHB else file_dict['AminoNeighbors']

def get_amino_type(file_dict: Dict) -> np.ndarray:
    return file_dict['AminoType'].reshape((-1, 1))

def get_amino_pos(file_dict: Dict) -> np.ndarray:
    return file_dict['AminoPos'].reshape((-1, 3))