import config

def lambda_handler(event, context):
    query = "SELECT * FROM players"

    conn = config.make_conn()

    result = config.fetch_data(conn, query)
    conn.close()

    print result

lambda_handler(1, 1)