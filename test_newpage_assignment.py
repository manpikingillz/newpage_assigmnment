import pytest

from newpage_assignment import SitesData


@pytest.fixture
def sites_data():
    '''Returns a SitesDat instance with dataframe'''
    return SitesData(
        file_path='Test Excel.xlsx',
        sheet_name='Sheet2'
    )

def test_number_of_sites(sites_data):
    sites_data.number_of_sites()
    assert sites_data.number_of_sites() == 8

def test_days_count_between_dates(sites_data) -> int:
    start_date = sites_data.dataframe.iloc[0,0]
    end_date = sites_data.dataframe.iloc[1,0]
    delta = end_date - start_date
    assert delta.days == 1

def test_convert_dataframe_to_excel(sites_data, output_file):
    transformed_data = sites_data.transform_data()
    transformed_data.to_excel(output_file, index=False)