
from gen import Writer
import numpy as np
import pandas as pd
from avro.schema import parse
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

class AVRO(Writer):

    def __init__(self) -> None:
        super().__init__()

    def output(self, df:pd.DataFrame):
        schema_parsed = parse(json.dumps(schema_dict))
        
        with open('data.avro', 'wb') as out:
            writer(out, parsed_schema, records)
