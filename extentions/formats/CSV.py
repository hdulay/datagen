
from mocker import Writer
import pandas as pd

class CSV(Writer):

    def __init__(self) -> None:
        super().__init__()

    def output(self, df:pd.DataFrame):
        df.to_csv(f'data.csv')
