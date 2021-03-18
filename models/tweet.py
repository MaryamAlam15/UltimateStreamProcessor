"""
class to represent a Tweet.
    attributes:
        - tweet text.
        - tweet timestamp.
"""


class Tweet:
    tweet_text = None
    time_stamp = None

    def __init__(self, tweet_value, time_stamp):
        self.tweet_text = tweet_value
        self.time_stamp = time_stamp
