import tweepy
import yaml
import logging
from os.path import expanduser


logger = logging.getLogger(__name__)


def load_auth(fn):
    with open(fn) as f:
        auths = yaml.load(f)
    k = np.random.randint(len(auths))
    ak = auths[k]
    auth = tweepy.OAuthHandler(ak['consumer_key'], ak['consumer_secret'])
    auth.set_access_token(ak['access_token'], ak['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

auth_filename = expanduser('~/.twitter_app_credentials.yaml')
api = load_auth(auth_filename)


