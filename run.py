import json
from kafka import KafkaConsumer


from Tables.utils import db
from Tables.utils.arguments import BOOTSTRAP_SERVER_ADDR, TOPIC_NAME


db.create_table()
task_table = list(db.Base._decl_class_registry.values())[0]

consumer = KafkaConsumer(TOPIC_NAME,
                         bootstrap_servers=[BOOTSTRAP_SERVER_ADDR],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    new_task = task_table(**message.value)
    db.insert(new_task)
