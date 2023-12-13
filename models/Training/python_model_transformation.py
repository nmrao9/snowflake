from  snowflake.snowpark.functions import sum
def model(dbt,session):
    
    dbt.config(materialized="table")
    Store=dbt.ref("store_tbl_2023")
    Store_Sales=dbt.ref("store_sales_tbl_2023")
    
    final_df = (
        Store
        .join(Store_Sales, Store_Sales.SS_STORE_SK == Store.S_STORE_SK, 'Inner')
        .group_by(Store.S_STORE_NAME,Store.S_COUNTY)
            .agg(sum(('SS_SALES_PRICE')).alias('SALES_PRICE')))

    return final_df