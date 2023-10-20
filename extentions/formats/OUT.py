
from mocker import Writer
import pandas as pd


class OUT(Writer):

    def __init__(self) -> None:
        super().__init__()

    def output(self, df:pd.DataFrame):
        print(df.to_json(orient='records', lines=True))
    