import pandas as pd
from app.sites_data import SitesData


df = pd.read_excel(
            io='Analytics Template for Exercise.xlsx',
            sheet_name='input_refresh_template',
            engine='openpyxl',
            header=None
        )
sites_data = SitesData(
    dataframe=df
)
sites_data.convert_dataframe_to_excel('Output Report.xlsx')