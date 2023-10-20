
from mocker import Writer
import pandas as pd


class parquet(Writer):

    def __init__(self) -> None:
        super().__init__()

    def output(self, df:pd.DataFrame):
        df.to_parquet('data.parquet')

    