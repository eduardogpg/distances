import csv
from typing import Dict
from typing import List


class openTsv:
    def open_tsv_file(self, path: str, delimiter='\t') -> List[Dict[str, str]]:
        if path is not None:
            file = open(path)
            return list(csv.DictReader(file, delimiter=delimiter))
        else:
            print('no hay path por favor ingrese uno')
