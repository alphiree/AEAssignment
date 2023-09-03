## Importing dependencies
import pandas as pd

## Add different transformations and cleaning functions here:
def fill_customer_country(data):
    return data

def fill_gender(data):
    return data

## Creating dictionary for list of functions:
transform_dict = {
    "fill_customer_country":fill_customer_country,
    "fill_gender":fill_gender,
}
## Transform Data Function
def transform_data(data_path):
    """
    Applies all the transformation functions
    """
    print('')
    data = pd.read_csv(data_path)

    try:
        for trans_functions in transform_dict.keys():
            print(f"Applying {trans_functions} function...")
            transform_dict[trans_functions](data)
        

        print("Data Transformation Successful!")
    except Exception as e:
        ## Print Error
        print(f" Data Transformation Error: {e}")
    
    return data



