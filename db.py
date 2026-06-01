import psycopg2

with psycopg2.connect(
    host="dpg-d7ng4fe7r5hc73aqr48g-a.frankfurt-postgres.render.com",
    database="trieda",
    user="trieda_user",
    password="CU76wt1voH4NyVoSvtaSeeyJyRKloMoN",
    port=5432
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT NOW();")
        print(cur.fetchone())