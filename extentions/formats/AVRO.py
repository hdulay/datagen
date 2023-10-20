
from mocker import Writer
import json
import numpy as np
import pandas as pd
from avro.schema import parse, Schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

class AVRO(Writer):

    def __init__(self) -> None:
        super().__init__()

    def output(self, df:pd.DataFrame):

        with DataFileWriter(open(self.avro_data_file, "wb"),
                            DatumWriter(),
                            self.schema) as writer:
            writer.append({'name': 'Prague',
                           "year": 2020,
                           "population": 1324277,
                           "area": 496})
            writer.append({'name': 'Berlin',
                           "year": 2019,
                           "population": 3769495,
                           "area": 891})
            writer.append({'name': 'Vienna',
                           "year": 2018,
                           "population": 1888776,
                           "area": 414})
        
