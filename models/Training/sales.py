import snowflake.snowpark.functions as F
def model (dbt,session):
  

  df_sql = session.sql("select * from prod.product")
  df_filtered = df_sql.filter(df_sql["REGION"] == 'West')
  df=df_filtered.group_by("STATE").agg(F.sum(F.col('GLOBAL_SALES')).alias("GLOBAL_SALES"))

  return df