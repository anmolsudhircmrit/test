# Import libraries
from sshtunnel import SSHTunnelForwarder
import pymysql

  # SSH (ec2_public_dns, ec2_user, pem_path, remote_bind_address=(rds_instance_access_point, port))
with SSHTunnelForwarder(('ec2-54-249-131-81.ap-northeast-1.compute.amazonaws.com'), ssh_username="ubuntu", ssh_pkey="~/Desktop/Home/key.pem", remote_bind_address=('database-1.czjqbvwtsf5g.ap-northeast-1.rds.amazonaws.com', 3306)) as tunnel:
    print("****SSH Tunnel Established****")

    db = pymysql.connect(
        host='127.0.0.1', user="admin",password="Anmol123",
        port=tunnel.local_bind_port, database="test"
    )
      # Run sample query in the database to validate connection
    try:
          # Print all the databases
        with db.cursor() as cur:
              # Print all the tables from the database
            cur.execute('SHOW TABLES FROM test')
            for r in cur:
                print(r)

              # Print all the data from the table
            cur.execute('SELECT * FROM person')
            for r in cur:
                print(r)
    finally:
        db.close()

print("YAYY!!")