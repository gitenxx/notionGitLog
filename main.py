import settings

import os
from notion.client import NotionClient
from tools import TextHandler
from git_tools import git_init, git_add

from git import Repo

client = NotionClient(token_v2=settings.TOKEN_V2)

page = client.get_block(settings.LINK)
page_title = page.title.strip()
page_id = page.id

block_content = client.get_record_data(table='block', id=page_id)['content']

if not os.path.exists('text'):
    os.makedirs('text')
os.chdir('text')
path = os.getcwd()

git_init(path, page_title)

f = open(f"{page_title}.txt","w+")

for i in block_content:
    try:
        text = client.get_record_data('block', i)['properties']['title']
        clean_text = []
        TextHandler.removeNestings(text, clean_text)
        f.write(''.join(clean_text) + '\r\n')
    except KeyError:
        continue   
f.close()

git_add(path, f"{page_title}.txt")

# TODO add callback (currently unavailable)
# TODO I actually don't like names "tools" and "git_tools", maybe need to rename it later
