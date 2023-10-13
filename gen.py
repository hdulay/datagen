#!/usr/bin/env python
import json
import random
import string
import typer
import time
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

class CSV(Format):
    def output(self, record:dict):
        keys = record.keys()
        return f"{','.join(str(x) for x in keys)}", f"{','.join(str(record[x]) for x in keys)}"

class Pinot(Schema):
    def gen(self, schema:str, formatter, limit):
        s:dict = json.loads(schema)
        self.schema_name = s['schemaName']
        self.dimensions = s['dimensionFieldSpecs']
        self.metrics = s['metricFieldSpecs']
        self.datetimes = s['dateTimeFieldSpecs']
        self.keys = s['primaryKeyColumns']

        records = []
        for i in range(limit):
            rec = {}
            is_array = bool(x["singleValueField"] if "singleValueField" in s.keys() else False)
            for x in self.dimensions:
                rec[x['name']] = getattr(self, x['dataType'].upper())()

            for x in self.metrics:
                rec[x['name']] = getattr(self, x['dataType'].upper())()

            for x in self.datetimes:
                rec[x['name']] = self.EPOC()

            for x in self.keys:
                # d = self.dimensions[x]
                rec[x] = self.ID()

            cols, rf = formatter(rec)
            records.append(rf)

        return cols, records


formats = {
    "csv": CSV().output
}
schemas = {
    "pinot": Pinot().gen
}

app = typer.Typer()
@app.command()
def mock(schema_file:str, schema_type:str="pinot", format:str="csv", limit:int=100):
    """
    Generate data
    """
    f = open(schema_file, "r")
    schema = f.read()

    formatter = formats[format]
    generator = schemas[schema_type]
    cols, records = generator(schema, formatter, limit)

    print(cols)
    for r in records:
        print(r)

if __name__ == "__main__":
    app()
