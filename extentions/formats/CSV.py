
from gen import Format


class CSV(Format):

    def __init__(self) -> None:
        super().__init__()

    def output(self, record:dict):
        keys = record.keys()
        return f"{','.join(str(x) for x in keys)}", f"{','.join(str(record[x]) for x in keys)}"
    
