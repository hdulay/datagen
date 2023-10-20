from mocker import Schema
import json
import jsonschema as js
import pandas as pd


class JSON(Schema):
    def gen(self, schema:str, limit):
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

            if is_array:
                raise AttributeError("not yet supported")

            for x in self.keys:
                # d = self.dimensions[x]
                rec[x] = self.ID()

            for x in self.dimensions:
                rec[x['name']] = getattr(self, x['dataType'].upper())()

            for x in self.metrics:
                rec[x['name']] = getattr(self, x['dataType'].upper())()

            for x in self.datetimes:
                rec[x['name']] = self.EPOC()
            records.append(rec)

        return records
