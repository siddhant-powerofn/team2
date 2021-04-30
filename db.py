import psycopg2

#ESTABLISHING CONNECTION
conn = psycopg2.connect(database="test_siddhant", user = "siddhant", password = "QWERTY123", host = "35.210.16.114", port = "5432")
print(conn)
print("Open database successfully")


cur = conn.cursor()