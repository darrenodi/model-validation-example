from rdkit import Chem
import numpy as np
import pandas as pd

def get_inchikey(smiles):
    inchikeys = []
    for values in smiles:
        if isinstance(values, str) and not pd.isnull(values):
            mol = Chem.MolFromSmiles(values)
            if mol is not None:
                inchikey = Chem.inchi.MolToInchiKey(mol)
            else:
                inchikey = None
        else:
            inchikey = None
        inchikeys.append(inchikey)ls
    return inchikeys