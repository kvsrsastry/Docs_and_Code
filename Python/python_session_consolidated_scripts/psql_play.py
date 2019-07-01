import psycopg2

host = 'tt-db.juniper.net'
user = 'readonly'
password = 'readonly'
dbname = 'systest_live'

try:

 connect_str = "host={} user={} password= {} dbname={}".format(host,user,password,dbname)
 print(connect_str)
 conn = psycopg2.connect(connect_str)

except Exception as e:
 print(e)

else:
 cursor = conn.cursor()
 for tid in (72974,29452,81960,96760):
  cursor.execute("select * from test where test_id = {}".format(tid))
  for record in cursor.fetchall():
   print(record)

 cursor.close()
 conn.close()


