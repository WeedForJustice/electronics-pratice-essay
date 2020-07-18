from fbchat import Client
from fbchat.models import *

# User login
client = Client('chengxuanjhe@gmail.com', "G`!)Z';g@7q{k!(J")

# Recipient
thread_id = '100010233364189'
message = '喵'
sticker = Sticker('209575325899636') # Fox with a bat sticker

for i in range(100):
    client.send(
        Message(text=message * i),
        thread_id
    )

client.logout()