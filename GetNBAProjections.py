import config

def lambda_handler(event, context):
    query = """SELECT	pp.team_abbrev, pp.playerid, pp.player_name, dk.position, pp.min, pp.pts_per_min, CAST(pp.game_date AS VARCHAR(10))
                FROM	draftkings dk JOIN playerprojections pp ON (REPLACE(dk.name, '.', '') = REPLACE(player_name, '.', '') AND upper(dk.team) = team_abbrev AND dk.game_date = pp.game_date)
                WHERE	pp.gameid IN (SELECT gameid FROM games WHERE date(game_date) = '%s')
				ORDER BY pp.proj_pts DESC""" % event['game_date']

    conn = config.make_conn()

    result = config.fetch_data(conn, query)
    conn.close()

    return result

### Testing ###

#event = {"game_date": "04/10/2018"}

#lambda_handler(event, 1)