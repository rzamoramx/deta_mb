
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel
from persistance.detadb.DetaDB import DetaDB

db = DetaDB()


def make_topic(topic_name: str) -> bool:
    topic = TopicPersistenceModel(topic_name)
    try:
        result = db.set_topic(topic, topic_name)
        print(f'result make_topic(): {result}')
        return True if result['ts'] > 0 else False
    except Exception as e:
        print(f'Error on make_topic(): {e}')
    return False


def make_subscription(sub_name: str, endpoint: str, topic: str, type_consuming: str) -> bool:
    subs = SubscriptionPersistenceModel(sub_name, topic, type_consuming, endpoint)
    try:
        result = db.set_subs(subs)
        print(f'result make_subscription(): {result}')
        return True if result['ts'] > 0 else False
    except Exception as e:
        print(f'Error on make_subscription(): {e}')
    return False
