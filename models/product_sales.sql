{{ config(materialized='table') }}
with product_sales as(
select city,state,sum(NA_SALES) na_sales,sum(global_sales) global_sales from PROD.product group by 1,2)
select * from product_sales

