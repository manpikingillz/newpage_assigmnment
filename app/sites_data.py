from datetime import datetime
import pandas as pd


class SitesData:
    def __init__(
        self,
        dataframe: pd.DataFrame
    ):
        self.dataframe = dataframe

    def transform_data(self) -> pd.DataFrame:
        row_counter = 0
        sites_count = self.number_of_sites()
        sites = []

        for _ in range(1, sites_count+1):
            row_counter+=1
            site_header_dict = self.dataframe.iloc[row_counter].to_dict()

            row_counter+=1
            site_date_dict = self.dataframe.iloc[row_counter].to_dict()

            row_counter+=1
            site_numbers_dict = self.dataframe.iloc[row_counter].to_dict()

            site_mame = site_numbers_dict[0]

            del site_header_dict[0]
            del site_date_dict[0]
            del site_numbers_dict[0]

            days_count = self.days_count_between_dates()

            days_of_month = [date.day for date in site_date_dict.values()]
            dates = [date.strftime("%Y-%m-%d") for date in site_date_dict.values()]

            transformed_data = pd.DataFrame({
                'Day of Month': days_of_month[:days_count],
                'Date': dates[:days_count],
                'Site ID': [site_mame]*days_count,
                'Page Views': list(site_numbers_dict.values())[:days_count],
                'Unique Visitors': list(site_numbers_dict.values())[days_count:days_count*2],
                'Total Time Spent': list(site_numbers_dict.values())[days_count*2:days_count*3],
                'Visits': list(site_numbers_dict.values())[days_count*3:days_count*4],
                'Average Time Spent on Site': list(site_numbers_dict.values())[days_count*4:days_count*5]
            })

            sites.append(transformed_data)
        return pd.concat(sites)

    def number_of_sites(self) -> int:
        column_items = list(self.dataframe.iloc[3:,0])
        cols = [str(site) for site in column_items if str(site)!='nan']
        return len(cols)

    def days_count_between_dates(self) -> int:
        start_date = self.dataframe.iloc[0,0]
        end_date = self.dataframe.iloc[1,0]

        delta = end_date - start_date
        return delta.days + 1

    def convert_dataframe_to_excel(self, output_file: str) -> None:
        transformed_data = self.transform_data()
        transformed_data.to_excel(output_file, index=False)







