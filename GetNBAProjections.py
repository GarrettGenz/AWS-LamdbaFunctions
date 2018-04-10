import config

def lambda_handler(event, context):
    query = """SELECT	team_abbrev, playerid, player_name, min, pts_per_min, CAST(game_date AS VARCHAR(10))
                FROM	playerprojections
                WHERE	gameid IN (SELECT gameid FROM games WHERE date(game_date) = '4/09/2018')"""

    conn = config.make_conn()

    result = config.fetch_data(conn, query)
    conn.close()

    print result

lambda_handler(1, 1)