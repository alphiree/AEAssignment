## Importing Configuration Details
from config.config import database, datatypes, table_name

## Importing dependencies
import datetime
from dateutil.relativedelta import relativedelta

## Database Information
column_definition = ",\n".join(
    f"{column_name} {column_type}" for column_name, column_type in datatypes.items()
)
column_tuple = ", ".join(datatypes.keys())

## Initializing Base Queries
month_beggining = datetime.date.today().replace(day=1)
month_end = month_beggining + relativedelta(day=31)

EVENTS = f"""
CREATE TABLE IF NOT EXISTS {database}.{table_name} (
{column_definition}
)
INSERT INTO {database}.{table_name} ({column_tuple})
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# FINANCE_QUERY = f"""
# WITH TRANSACTIONS AS (
#     SELECT * FROM {database}.{table_name}
# )

# SELECT
#     CUSTOMER_COUNTRY,
#     SUM(PRODUCT_VALUE) AS TOTAL_VALUE
# FROM TRANSACTIONS
# WHERE TRANSACTION_DATE BETWEEN {month_beggining} AND {month_end}
# """

# MARKETING_QUERY = f"""
# WITH TRANSACTIONS AS (
#     SELECT * FROM {database}.{table_name}
# )

# SELECT
#     CUSTOMER_COUNTRY,
#     COUNT(ID) AS TOTAL_TRANSACTIONS
# FROM TRANSACTIONS
# WHERE TRANSACTION_DATE BETWEEN {month_beggining} AND {month_end}
# """

# I modified the 2 sample queries. The default queries somehow does not work on my end
# Note: There is also no transaction date column on the given dataframe

FINANCE_QUERY = f"""
WITH TRANSACTIONS AS (
    SELECT * FROM {table_name}
)
SELECT
    CUSTOMER_COUNTRY,
    SUM(PRODUCT_VALUE) AS TOTAL_VALUE
FROM TRANSACTIONS
GROUP BY
    CUSTOMER_COUNTRY
"""

MARKETING_QUERY = f"""
WITH TRANSACTIONS AS (
    SELECT * FROM {table_name}
)

SELECT
    CUSTOMER_COUNTRY,
    COUNT(transaction_id) AS TOTAL_TRANSACTIONS
FROM TRANSACTIONS
GROUP BY
    CUSTOMER_COUNTRY
"""

# {name}_QUERY = f"""


# """


