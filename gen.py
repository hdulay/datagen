#!/usr/bin/env python
import json
import random
import string
import typer
import time
import importlib
from importlib import import_module
from extentions import formats
from extentions import schemas
from pathlib import Path

class Format:
    def output(self, records:dict): str

class Schema:

    def gen(self, schema:str, formatter:Format, limit:int) -> []:dict

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


def load_format(name:str, path:str="extentions.formats"):
    return load(name, path).output

def load_schema(name:str, path:str="extentions.schemas"):
    return load(name, path).gen

app = typer.Typer()
@app.command()
def mock(schema_file:str="schemas/pinot.json", schema_type:str="Pinot", format:str="CSV", limit:int=100):
    """
    Generate data
    """
    f = open(schema_file, "r")
    schema = f.read()

    formatter = load_format(format)
    generator = load_schema(schema_type)
    cols, records = generator(schema, formatter, limit)

    print(cols)
    for r in records:
        print(r)

if __name__ == "__main__":
    app()
