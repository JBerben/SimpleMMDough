#!/usr/bin/python3
import hashlib
import pickle
import requests
from lxml import html
import textwrap

global SAVED_KEY_OBJ

# Previous key, which needs to be sent straight after POST
SAVED_KEY = ''

# CTF landing page with flag needing to be md5 hashed
URL = ""
req = requests.session()

def saveKey(emdee):
    f = open('store.pckl', 'wb')
    pickle.dump(emdee, f)
    f.close()

def loadKey():
    f = open('store.pckl', 'rb')
    SAVED_KEY_OBJ = pickle.load(f)
    print(SAVED_KEY_OBJ)
    f.close()

print(SAVED_KEY)

# Fetch the landing page
r = req.get(url = URL)
page_content = r.content
print(page_content)
print(page_content)
emdee_five_key = html.fromstring(page_content)
emdee_uid = ''

# Debug
for sel in emdee_five_key.xpath("/html/body/h3"):
    
    if sel.text:
        s = sel.text.strip()
        emdee_uid = textwrap.fill(s, width = 50)

hashed_emdee_object = hashlib.md5(emdee_uid.encode())
hashed_emdee = hashed_emdee_object.hexdigest()

DATA = {'hash': hashed_emdee}
resp = req.post(url = URL, data = DATA)
print(resp.text)

page_content = resp.content
emdee_five_key = html.fromstring(page_content)
emdee_uid = ''

# Debug
for sel in emdee_five_key.xpath("/html/body/h3"):
    
    if sel.text:
        s = sel.text.strip()
        emdee_uid = textwrap.fill(s, width = 50)

hashed_emdee_object = hashlib.md5(emdee_uid.encode())
hashed_emdee = hashed_emdee_object.hexdigest()

DATA = {'hash': hashed_emdee}
resp = req.post(url = URL, data = DATA)
print(resp.text)