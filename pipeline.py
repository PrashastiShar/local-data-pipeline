import duckdb
import requests
import time

print("Downloading dataset...")
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
response = requests.get(url)
with open("covid_data.csv", "wb") as f:
    f.write(response.content)
print("Dataset downloaded successfully.")

print("Connecting to DuckDB...")
# DuckDB can query the CSV file directly!
con = duckdb.connect()

query = """
    SELECT location, MAX(total_deaths) as max_deaths, MAX(people_vaccinated) as max_vaccinated
    FROM 'covid_data.csv'
    WHERE continent IS NOT NULL
    GROUP BY location
    ORDER BY max_deaths DESC
    LIMIT 5;
"""

print("Running serverless SQL query...")
start_time = time.time()
result = con.execute(query).fetchall()
end_time = time.time()

print(f"\nQuery executed in {end_time - start_time:.4f} seconds.")
print("\nTop 5 Locations by Deaths:")
for row in result:
    print(f"Location: {row[0]} | Deaths: {row[1]} | Vaccinated: {row[2]}")
