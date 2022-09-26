## Purpose of the Project
This project's purpose is to transform data provided in an excel document, to a report

## Expected input and output
- The expected input is an excel document with a sheet that contains that needs to be transformed.
- The output is an excel document with transformed data.

## Installation steps
- Ensure Python 3.10 is installed on your computer. Confirm by executing `python3.10 --version`
- Extract provided zip folder or clone the repo https://github.com/manpikingillz/newpage_assigmnment.git. Either way, you will end up with a directory `newpage_assigmnment`
- Change directory to `newpage_assigmnment` by executing `cd newpage_assigmnment`
- Create virtual environment `python3.10 -m venv venv`
- Activate virtual environment `source venv/bin/activate`. Once in the virtual environment, executing `python --version` should show `python 3.10.x`
- Install project dependencies - `pip install -r requirements.txt`
- To run the app, execute the command `python run.py`
- To run the tests, execute - `pytest`

## Use cases and edge cases covered in the code.
- The code is able to read the `input_refresh_template` sheet of `Analytics Template for Exercise.xlsx` and generate the output into another file `Output Report.xlsx` with transformed data.
- The code allows for flexible number of sites. Original file has 100, but we can have less or more sites and we will still be fine.
## Known limitations
- Columns won't be flexible. We will only work with provided columns. Adding new columns will mean modifying the code to accomodate the changes

## Assumptions made
- The format of the input file will not change.
- `start datE`e will be in the first column, first row (A1). `end date` will always be the first column, second row (A2)
- The date range (`start date` to `end date`) must be covered for `Page Views`, `Unique Visitors`, `Total Time Spent`, `Visits`, `Average Time Spent on Site` e.g if `start date` is `2022-09-01` and `end date` is `2022-09-30`, `Page Views` must have data reprensation for all the dates from `2022-09-01` to `2022-09-30`
- Sites are flexible i.e We can have varying number of sites.
