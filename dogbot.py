
import tracery
import mastodon
import future
import requests
import requests_oauthlib
import twitter
import os
from mastodon import Mastodon
from tracery.modifiers import base_english

#Create a dog
rules = {
    'origin': "#adj# #dog#",
    'adj': ["smol","little","tiny","smol af","heckin smol","widdle","larg","huge","ginormo","XL","mystical","mysterious","sage","clever","soft as heck","sleepy","speepy","snuggly","energetic","hungie","playful","aloof","stealth","secret","wise","demanding","independent","squishy","puffy","tongue-out","dancing","roly-poly","medium-sized","scholarly","vacuum-shy","loyal","upside-down","fab","fabulous","marvelous","proper","super","just a great","my favorite","flower hat","sweater-wearing","boopable","bleppy","mlem","stylish","fashion","whoa what a great","such a good dang","confident","skittish","bouncy","spoopy","smart","precious","important","dang that's a good","om nom nomming","brand hecking new","just hecking got borned","graceful","gentle","quality","fancy"],
    'dog': ["dog","puppy","puppo","pup","puplet","borker","borkling","borklet","borkadoodle","borklord","bab","pupperoo","borkaroo","boofer","floof","fluffball","puffball","floofball","floofpoof","floofer poofer","fluff","baby","boy","girl","doggo","doge","doglet","dogling","doggeroo","corg","sheeb","sammy","corglet","booplet","Frenchie","puggo","Pom","flopper","woofer","booflord","pup-pup-pupper","dog-dog-doglet","grumbly-bumbly","sniffer","nosy-nose","canine","doodle","noodle","Lab bab","dogge"]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print (grammar.flatten("#origin#")) # prints, e.g., "Hello, world!"
post = (grammar.flatten("#origin#"))
'''
#Twitter credentials
api = twitter.Api(consumer_key= (os.environ['consumer_key']),
                      consumer_secret=(os.environ['consumer_secret']),
                      access_token_key=(os.environ['access_token']),
                      access_token_secret=(os.environ['access_token_secret']))

#Mastodon credentials
'''
# Register app - only once!
'''
Mastodon.create_app(
     'dogbot',
      to_file = 'dogbot_clientcred.txt'
)
'''

# Log in - either every time, or use persisted

mastodon = Mastodon(client_id = 'dogbot_clientcred.txt', debug_requests = True)
mastodon.log_in(
    'kelly.n.sweeney+listofdogs@gmail.com',
    'klwyPd2I6L3zQMqPR0tW',
    to_file = 'dogbot_usercred.txt'
)

'''
# Create actual instance
mastodon = Mastodon(
    client_id = (os.environ['m_client_id']),
    access_token = (os.environ['m_access_token']),
    client_secret = (os.environ['m_client_secret'])
)
mastodon.toot(post)
'''



#Post to Twitter
