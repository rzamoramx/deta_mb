
class TopicAlreadyExists(Exception):
    def __init__(self, msg="topic already exists"):
        self.__init__(msg)


class SubscriptionAlreadyExists(Exception):
    def __init__(self, msg="subscription already exists"):
        self.__init__(msg)


class CannotUpdateTopic(Exception):
    def __init__(self, msg="cannot update topic, try later"):
        self.__init__(msg)


class TopicNotFound(Exception):
    def __init__(self, msg="topic not found"):
        self.__init__(msg)


class SubscriptionNotFound(Exception):
    def __init__(self, msg="subscription not found"):
        self.__init__(msg)


class CannotUpdateSubscription(Exception):
    def __init__(self, msg="cannot update subscription, try later"):
        self.__init__(msg)