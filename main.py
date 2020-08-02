import settings

import os
from notion.client import NotionClient
from tools import TextHandler

client = NotionClient(token_v2=settings.TOKEN_V2)

page = client.get_block(settings.LINK)
page_title = page.title
page_id = page.id

block_content = client.get_record_data(table='block', id=page_id)['content']

if not os.path.exists('text'):
    os.makedirs('text')
os.chdir('text')
f= open(f"{page_title}.txt","w+")

for i in block_content:
    try:
        text = client.get_record_data('block', i)['properties']['title']
        clean_text = []
        TextHandler.removeNestings(text, clean_text)
        f.write(''.join(clean_text) + '\r\n')
    except KeyError:
        continue
f.close()

# TODO add callback (currently unavailable)
