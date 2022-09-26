from datetime import datetime
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
import io
import mock

from sites_data import SitesData


@pytest.fixture
def sites_data():
    date1 = datetime.strptime('2021-01-01', '%Y-%m-%d')
    date2 = datetime.strptime('2021-01-02', '%Y-%m-%d')

    df = pd.DataFrame({
        'column1': [
            date1, date2, 'Site ID', 'Site 1',
            None, None, 'Site 2', None, None, 'Site 3'
        ],
        'column_pageviews_1': [
            None, 'Page Views', date1, '6',
            'Page Views', date1, '4',
            'Page Views', date1, '4',
        ],
        'column_page_views_2': [
            None, 'Page Views', date2, '4',
            'Page Views', date2, '5',
            'Page Views', date2, '4',
        ],
        'column_unique_vistors_1': [
            None, 'Unique Visitors', date1, '4',
            'Unique Visitors', date1, '2',
            'Unique Visitors', date1, '2',
        ],
        'column_unique_vistors_2': [
            None, 'Unique Visitors', date2, '2',
            'Unique Visitors', date2, '3',
            'Unique Visitors', date2, '2',
        ],
        'column_total_time_spent_1': [
            None, 'Total Time Spent', date1, '11',
            'Total Time Spent', date1, '5',
            'Total Time Spent', date1, '8',
        ],
        'column_total_time_spent_2': [
            None, 'Total Time Spent', date2, '14',
            'Total Time Spent', date2, '6',
            'Total Time Spent', date2, '8',
        ],
        'column_visits_1': [
            None, 'Visits', date1, '4',
            'Visits', date1, '2',
            'Visits', date1, '2',
        ],
        'column_visits_2': [
            None, 'Visits', date2, '2',
            'Visits', date2, '3',
            'Visits', date2, '2',
        ],
        'column_average_time_spent_on_site_1': [
            None, 'Average Time Spent on Site', date1, '0.1',
            'Average Time Spent on Site', date1, '0',
            'Average Time Spent on Site', date1, '0.1',
        ],
        'column_average_time_spent_on_site_2': [
            None, 'Average Time Spent on Site', date2, '0.1',
            'Average Time Spent on Site', date2, '0.1',
            'Average Time Spent on Site', date2, '0.1',
        ],
        })

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)

    xlsx_dataframe = pd.read_excel(output, sheet_name='sheet1', engine='openpyxl')
    xlsx_dataframe.columns = range(df.shape[1])

    return SitesData(dataframe=xlsx_dataframe)


def test_number_of_sites(sites_data):
    # Test case to test that number of sites is correct'
    sites_data.number_of_sites() == 3


def test_days_count_between_dates(sites_data):
    # Test case to test days count between dates
    start_date = sites_data.dataframe.iloc[0,0]
    end_date = sites_data.dataframe.iloc[1,0]
    delta = end_date - start_date
    assert delta.days == 1

def test_transform_data(sites_data):
    # Test case to test that data will be transformed correctly.
    date1 = '2021-01-01'
    date2 = '2021-01-02'

    expected_transformed_dataframe = pd.DataFrame({
                'Day of Month': [1,2,1,2,1,2],
                'Date': [date1, date2, date1, date2, date1, date2],
                'Site ID': ['Site 1', 'Site 1', 'Site 2', 'Site 2', 'Site 3', 'Site 3'],
                'Page Views': ['6','4','4','5','4','4'],
                'Unique Visitors': ['4','2','2','3','2','2'],
                'Total Time Spent': ['11', '14', '5', '6', '8', '8'],
                'Visits': ['4','2','2','3','2','2'],
                'Average Time Spent on Site': ['0.1','0.1','0','0.1','0.1','0.1']
            })

    assert_frame_equal(expected_transformed_dataframe.reset_index(drop=True), sites_data.transform_data().reset_index(drop=True))
