
from mocker import Writer
import pandas as pd


class JSON(Writer):

    def __init__(self) -> None:
        super().__init__()

    def output(self, df:pd.DataFrame):
        df.to_json(f'data.json', orient='records', lines=True)
    