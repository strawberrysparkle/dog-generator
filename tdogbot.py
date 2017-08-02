
import tracery
import future
import requests
import requests_oauthlib
import twitter
import os
import boto3
from tracery.modifiers import base_english

#Create a dog
rules = {
    'origin': "#adj# #dog#",
    'adj': ["smol","little","tiny","smol af","heckin smol","widdle","larg","huge","ginormo","XL","mystical","mysterious","sage","clever","soft as heck","sleepy","speepy","snuggly","energetic","hungie","playful","aloof","stealth","secret","wise","demanding","independent","squishy","puffy","tongue-out","dancing","roly-poly","medium-sized","scholarly","vacuum-shy","loyal","upside-down","fab","fabulous","marvelous","proper","super","just a great","my favorite","flower hat","sweater-wearing","boopable","bleppy","mlem","stylish","fashion","whoa what a great","such a good dang","confident","skittish","bouncy","spoopy","smart","precious","important","dang that's a good","om nom nomming","brand hecking new","just hecking got borned","graceful","gentle","quality","fancy"],
    'dog': ["dog","puppy","puppo","pup","puplet","borker","borkling","borklet","borkadoodle","borklord","bab","pupperoo","borkaroo","boofer","floof","fluffball","puffball","floofball","floofpoof","floofer poofer","fluff","baby","boy","girl","doggo","doge","doglet","dogling","doggeroo","corg","sheeb","sammy","corglet","booplet","Frenchie","puggo","Pom","flopper","woofer","booflord","pup-pup-pupper","dog-dog-doglet","grumbly-bumbly","sniffer","nosy-nose","canine","doodle","noodle","Lab bab","dogge"]
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

#Twitter credentials
api = twitter.Api(consumer_key= (os.environ['consumer_key']),
                      consumer_secret=(os.environ['consumer_secret']),
                      access_token_key=(os.environ['access_token']),
                      access_token_secret=(os.environ['access_token_secret']))

#Post to Twitter
status = api.PostUpdate(grammar.flatten("#origin#"))
print(status.text)