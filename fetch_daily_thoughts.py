#!/usr/bin/env python
# coding: utf-8

# In[68]:


import glob
from datetime import datetime as dt
__obsidian_path__ ="/mnt/c/Users/ryano/Google Drive/Obsidian/Big_vault/Ryan's Brain/"
def make_obs_link(name):
    return """![[{name}]]""".format(name=name)
def parse_file(filename):
    return make_obs_link(filename.replace(__obsidian_path__,'').replace('.md',''))
files = list(filter(lambda x:x!=make_obs_link(dt.now().strftime('%Y%m%d')),map(
    parse_file,glob.glob(__obsidian_path__+ "*" + dt.now().strftime('%Y%m%d') + "*"))))
daily_file = __obsidian_path__ + '/'+ dt.now().strftime('%Y%m%d') +'.md'
with open(daily_file,'r') as f:
    existing = (f.read())
to_write = filter(lambda x:x not in existing,files)
with open(daily_file,'a') as f:
    for filename in to_write:
        f.write(filename+ '\n')

