import csv

import jaydebeapi

def get_conn():
    h2_jar = "resources/h2-2.3.232.jar"
    url = "jdbc:h2:~/test"

    conn = jaydebeapi.connect(
        "org.h2.Driver",
        url,
        ["", ""],
        h2_jar,
    )
    return conn

def init(movies_csv: str):
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS awards")
    cursor.execute("""CREATE TABLE IF NOT EXISTS awards (
    award_year INT,
    title VARCHAR(255),
    studios VARCHAR(255),
    producers VARCHAR(255),
    winner VARCHAR(3)
);""")

    with open(movies_csv, newline='', encoding='utf-8') as csvfile:
        total = 0
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            total = total + 1
            cursor.execute("INSERT INTO awards (award_year, title, studios, producers, winner) VALUES (?, ?, ?, ?, ?)",
                           row)

    cursor.close()
    conn.commit()
    conn.close()

def get_dados():
    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute("""
       with intervalos as (
    select producers, AWARD_YEAR, LAG(AWARD_YEAR, 1, null) over (partition by PRODUCERS order by AWARD_YEAR) as anterior,
            AWARD_YEAR - LAG(AWARD_YEAR, 1, null) over (partition by PRODUCERS order by AWARD_YEAR) as diferenca
           from awards
           where winner = 'yes'
)
select 'min' as descricao, i.PRODUCERS, i.AWARD_YEAR, i.anterior, i.diferenca
    from intervalos i
where i.diferenca = (select min(diferenca) from intervalos)
union all
select 'max' as descricao, i.PRODUCERS, i.AWARD_YEAR, i.anterior, i.diferenca
    from intervalos i
where i.diferenca = (select max(diferenca) from intervalos)
        """)
        result = cursor.fetchall()

        if len(result) == 0:
            return [],[]

        min = [x[1:] for x in filter(lambda x: x[0] == 'min', result)]
        max = [x[1:] for x in filter(lambda x: x[0] == 'max', result)]

        return min, max
    finally:
        cursor.close()
        conn.close()

