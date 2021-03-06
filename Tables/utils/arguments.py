import argparse

parser = argparse.ArgumentParser(description="Kafka consumer inserting data to PostgreSQL")
parser.add_argument('-b_ip', '--bootstrap_ip', default='localhost')
parser.add_argument('-b_p', '--bootstrap_port', default='9092')
parser.add_argument('-t', '--topic', default='sql-insert')
parser.add_argument('-db_ip', '--database_ip', default='localhost')
parser.add_argument('-db_p', '--database_port', default='5432')
parser.add_argument('-db', '--database_name', default='kafkaConsumer')
parser.add_argument('-user', '--username', default='postgres')
parser.add_argument('-pass', '--password', default='')

args = parser.parse_args()

BOOTSTRAP_SERVER_ADDR = f"{args.bootstrap_ip}:{args.bootstrap_port}"

TOPIC_NAME = args.topic

DB_CONN_URL = \
    f'postgresql+psycopg2://{args.username}:{args.password}@{args.database_ip}:{args.database_port}/{args.database_name}'

