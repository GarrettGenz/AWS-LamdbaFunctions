import config

def lambda_handler(event, context):
    config.connect_to_db()

lambda_handler(1,1)