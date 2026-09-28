# setup.py
import duckdb

# Connect to a persistent database file
con = duckdb.connect("sales_database.duckdb")

# Create a view or table inside this database
con.sql("CREATE TABLE IF NOT EXISTS auto_sales AS SELECT * FROM read_csv_auto('query_data/auto_sales.csv')")

# Close the connection when done writing so another file can access it
con.close()
print("Database created and closed successfully.")