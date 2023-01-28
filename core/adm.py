
from persistance.TopicPersistenceModel import TopicPersistenceModel
from persistance.SubscriptionPersistenceModel import SubscriptionPersistenceModel
from persistance.detadb.DetaDB import DetaDB

db = DetaDB()


def manage_subscription_enable_disable(sub_name: str, can_consume: bool):
    sub_i = db.get_subscription(sub_name)
    sub_i.can_consume = can_consume
    db.upd_subscription(sub_name, sub_i)


def manage_topic_enable_disable(topic: str, can_produce: bool, can_consume: bool):
    topic_i = db.get_topic(topic)
    topic_i.can_consume = can_consume
    topic_i.can_produce = can_produce
    db.upd_topic(topic, topic_i)


def make_topic(topic_name: str):
    """save topic to db, throw an exception if key already exists"""
    db.set_topic(TopicPersistenceModel(topic_name), topic_name)


def make_subscription(sub_name: str, endpoint: str, topic: str, type_consuming: str):
    """save subscription to db, throw an exception if key already exists"""
    db.set_subs(SubscriptionPersistenceModel(sub_name, topic, type_consuming, endpoint))
