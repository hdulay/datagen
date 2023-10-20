#!/usr/bin/env python
import random
import string
import typer
import time
import pandas as pd

class Writer:
    def output(self, df:pd.DataFrame):
        pass

class Schema:

    def gen(self, schema:str, limit:int) -> []:
        pass

    def STRING(self) -> str: 
        return ''.join(random.choices(string.ascii_uppercase, k=10))
    
    def ID(self) -> str: 
        return ''.join(random.choices(string.ascii_uppercase, k=3))
    
    def INT(self) -> int: 
        return ''.join(random.choices(string.digits, k=5))
    
    def LONG(self): 
        return ''.join(random.choices(string.digits, k=10))
    
    def EPOC(self):
        return round(time.time() * 1000)


def load(name:str, path:str):
    mod = __import__(path, fromlist=[name])
    inst = getattr(getattr(mod, name), name)
    return inst()

def load_writer(name:str, path:str="extentions.formats") -> Writer:
    return load(name, path).output

def load_schema(name:str, path:str="extentions.schemas"):
    return load(name, path).gen

app = typer.Typer()
@app.command()
def mock(schema_file:str, schema_type:str, format:str="JSON", output_file:str="output", limit:int=100):
    """
    Generate data

    --format other options are CSV, AVRO, protobuf
    """
    f = open(schema_file, "r")
    schema = f.read()

    generator = load_schema(schema_type)
    records = generator(schema, limit)

    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    df = pd.DataFrame.from_records(records)
    writer = load_writer(format)
    writer(df)
    

if __name__ == "__main__":
    app()
