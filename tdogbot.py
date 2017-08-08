
import tracery
import future
import requests
import requests_oauthlib
import tweepy
import os
import boto3
from tracery.modifiers import base_english

#Create a dog
rules = {
    'origin': "#adj# #dog#",
    'adj': ["smol","little","tiny","smol af","heckin smol","widdle","larg","huge","ginormo","XL","mystical","mysterious","sage","clever","soft as heck","sleepy","speepy","snuggly","energetic","hungie","playful","aloof","stealth","secret","wise","demanding","independent","squishy","puffy","tongue-out","dancing","roly-poly","medium-sized","scholarly","vacuum-shy","loyal","upside-down","fab","fabulous","marvelous","proper","super","just a great","my favorite","flower hat","sweater-wearing","boopable","bleppy","mlem","stylish","fashion","whoa what a great","such a good dang","confident","skittish","bouncy","spoopy","smart","precious","important","dang that's a good","om nom nomming","brand hecking new","just hecking got borned","graceful","gentle","quality","fancy","extremely pettable"],
    'dog': ["dog","puppy","puppo","pup","puplet","borker","borkling","borklet","borkadoodle","borklord","bab","pupperoo","borkaroo","boofer","floof","fluffball","puffball","floofball","floofpoof","floofer poofer","fluff","baby","boy","girl","doggo","doge","doglet","dogling","doggeroo","corg","sheeb","sammy","corglet","booplet","Frenchie","puggo","Pom","flopper","woofer","booflord","pup-pup-pupper","dog-dog-doglet","grumbly-bumbly","sniffer","nosy-nose","canine","doodle","noodle","Lab bab","dogge","pood","poodle doodle","poodleroo","poodle noodle","husky","husko","saluki","borkmaster","snoot boy","snoot girl","pupball"]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

#Twitter credentials
class TwitterAPI:
    """
    Class for accessing the Twitter API.
    Requires API credentials to be available in environment
    variables. These will be set appropriately if the bot was created
    with init.sh included with the heroku-twitterbot-starter
    """
    def __init__(self):
        consumer_key = os.environ.get('consumer_key')
        consumer_secret = os.environ.get('consumer_secret')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = os.environ.get('access_token')
        access_token_secret = os.environ.get('access_token_secret')
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        """Send a tweet"""
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet(grammar.flatten("#origin#"))
    time.sleep(10800)