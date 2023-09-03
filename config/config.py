## Changing the folder_alias to my last name and initials
folder_alias = "LUPAGUE_RMJM"

##=====================================##
## Database Details
environment = "prod"
host = "company1@country.co"
database = "platform_prod"
user = "analytics"
password = "securepassword"

## Table name
table_name = "events"
##=====================================##
## Folder Details
reports_folder = "reports"
data_folder = "data"
##=====================================##
## Datatypes of the table
datatypes = {
    "transaction_id": "INT",
    "purchase_price": "FLOAT",
    "product_value": "FLOAT",
    "product_name": "VARCHAR(255)",
    "first_name": "VARCHAR(255)",
    "last_name": "VARCHAR(255)",
    "email": "VARCHAR(255)",
    "gender": "VARCHAR(255)",
    "customer_country": "VARCHAR(255)",
    "client_country": "VARCHAR(255)",
}
