from datetime import datetime
import pandas as pd
# Read input_refresh_template sheet, Analytics Template for Exercise.xlsx
# Generate output file (as shown in output_31_days_report, but for all sites)

'''
    To be submitted:
    ----------------------------------------------------------------
    a. Final working code in Python
    b. Input file
    c. Generated output file
    d. README.md file, with these contents
        - Purpose of the project (brief introduction)
        - Expected input and output
        - Installation steps
          > create virtual env, python3.10 -m venv venv
          > install pandas -> pip3 install pandas openpyxl
        - Instructions to run the project
        - Instructions to run tests
        - Use cases and edge cases covered in the code
        - Known limitations (if any)
        - Assumptions made -> add these in README.md or in code comments
    e. Unit Tests written in pytest with maximum possible code coverage.
'''


'''
    Work to be done
    ---------------------------------------------------------------
    input_refresh_template DATA:
    - Start date -> A1
    - end date -> A2
    - Metrices for each site:
        a. Page Views
        b. Unique Visitors
        c. Total Time Spent
        d. Visits
        e. Average Time Spent on Site
    - Ability process more than or less than the given 100
    - Follow all the standard python coding practices to make th code readible and maintainable
'''



'''
   Read A1
   Read A2

   Site 1
      Row (Start on row 4)
        - page views, 1 to 31
        - unique visitors, 1 to 31
        - total time spent, 1 to 31
        - visits, 1 to 31
        - Average time to spent on site, 1 to 31
      Next Row (4 rows from the previous Row)
       - page views, 1 to 31
        - unique visitors, 1 to 31
        - total time spent, 1 to 31
        - visits, 1 to 31
        - Average time to spent on site, 1 to 31

    Next Row (4 rows from the previous Row)
       ....

   Format of File to be produced
   ---------------------------
    Day of Month | Date      | Site ID | Page Views | Unique Visitors | Total Time Spent | Visits | Average Time Spent on Site
        1        |2021/01/01 |  Site 1 | 6          |  4              | 11               | 4      |      0.1
        2        |2021/01/02 |  Site 1 | 4          |  2              | 14               | 2      |      0.1
        .
        .
        1        |2021/01/01 |  Site 2 | 4          |  2              | 5                | 2      |      0
        2        |2021/01/01 |  Site 2 | 5          |  3              | 6                | 3      |      0.1
'''

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


df = pd.read_excel(
            io='Test Excel.xlsx',
            sheet_name='Sheet2',
            engine='openpyxl',
            header=None
        )
sites_data = SitesData(
    dataframe=df
)
sites_data.convert_dataframe_to_excel('Output.xlsx')




