import csv

import jaydebeapi

def init(movies_csv: str):
    h2_jar = "resources/h2-2.3.232.jar"
    url = "jdbc:h2:~/test"

    conn = jaydebeapi.connect(
        "org.h2.Driver",
        url,
        ["", ""],
        h2_jar,
    )

    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS awards (
    award_year INT,
    title VARCHAR(255),
    studios VARCHAR(255),
    producers VARCHAR(255),
    winner VARCHAR(3)
);""")

    with open(movies_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO movies (award_year, title, studios, producers, winner) VALUES (?, ?, ?, ?, ?)", row)

    cursor.execute("SELECT * FROM movies")
    result = cursor.fetchall()
    print(result)

    cursor.close()
    conn.close()