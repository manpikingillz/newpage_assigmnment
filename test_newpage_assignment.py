import pytest
import pandas as pd
import io

from newpage_assignment import SitesData


@pytest.fixture
def sites_data():
    '''Returns a SitesDat instance with dataframe'''
    df = pd.DataFrame({
        'column1': [
            '2021/01/01', '2021/01/31', 'Site ID', 'Site 1',
            None, None, 'Site 2', None, None, 'Site 3'
        ],
        'column_pageviews_1': [
            None, 'Page Views', '2021/01/01', '6',
            'Page Views', '2021/01/01', '4',
            'Page Views', '2021/01/01', '4',
        ],
        'column_page_views_2': [
            None, 'Page Views', '2021/01/02', '4',
            'Page Views', '2021/01/02', '5',
            'Page Views', '2021/01/02', '4',
        ],
        'column_unique_vistors_1': [
            None, 'Unique Visitors', '2021/01/01', '4',
            'Unique Visitors', '2021/01/01', '2',
            'Unique Visitors', '2021/01/01', '2',
        ],
        'column_unique_vistors_2': [
            None, 'Unique Visitors', '2021/01/02', '2',
            'Unique Visitors', '2021/01/02', '3',
            'Unique Visitors', '2021/01/02', '2',
        ],
        'column_total_time_spent_1': [
            None, 'Total Time Spent', '2021/01/01', '11',
            'Total Time Spent', '2021/01/01', '5',
            'Total Time Spent', '2021/01/01', '8',
        ],
        'column_total_time_spent_2': [
            None, 'Total Time Spent', '2021/01/02', '14',
            'Total Time Spent', '2021/01/02', '6',
            'Total Time Spent', '2021/01/02', '8',
        ],
        'column_visits_1': [
            None, 'Visits', '2021/01/01', '4',
            'Visits', '2021/01/01', '2',
            'Visits', '2021/01/01', '2',
        ],
        'column_visits_2': [
            None, 'Visits', '2021/01/02', '2',
            'Visits', '2021/01/02', '3',
            'Visits', '2021/01/02', '2',
        ],
        'column_average_time_spent_on_site_1': [
            None, 'Average Time Spent on Site', '2021/01/01', '0.1',
            'Average Time Spent on Site', '2021/01/01', '0',
            'Average Time Spent on Site', '2021/01/01', '0.1',
        ],
        'column_average_time_spent_on_site_2': [
            None, 'Average Time Spent on Site', '2021/01/02', '0.1',
            'Average Time Spent on Site', '2021/01/02', '0.1',
            'Average Time Spent on Site', '2021/01/02', '0.1',
        ],
        })

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)
        writer.save()

    xlsx_data = pd.read_excel(output, engine='openpyxl', header=None, index_col=None)
    print(xlsx_data)

    # print(xlsx_data)
    return SitesData(dataframe=df)
    # print(xlsx_data)
    # pd.testing.assert_frame_equal(xlsx_data, df)

# def test_tranform_data(sites_data):
#     print(sites_data.dataframe)

def test_number_of_sites(sites_data):
    sites_data.number_of_sites()
    # assert sites_data.number_of_sites() == 3

# def test_days_count_between_dates(sites_data) -> int:
#     start_date = sites_data.dataframe.iloc[0,0]
#     end_date = sites_data.dataframe.iloc[1,0]
#     delta = end_date - start_date
#     assert delta.days == 1

# def test_convert_dataframe_to_excel(sites_data, output_file):
#     transformed_data = sites_data.transform_data()
#     transformed_data.to_excel(output_file, index=False)