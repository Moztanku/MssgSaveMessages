#!/usr/bin/env python3
from fbchat import Client
from fbchat.models import *
import getpass
import urllib.request
from datetime import datetime

login = input('Email: ')
password = getpass.getpass(prompt='Password: ')
threadIds = ['',''] #Put here thread IDs of people who you want save messages from.
                    #You can get them easily, 

class SaveMessages(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if(thread_id == client.uid):
            if(message_object.text=="Stop"):
                client.stopListening()
        if(thread_id in threadIds):
            author_name = client.fetchUserInfo(message_object.author)[message_object.author].name
            message_time = datetime.utcfromtimestamp(int(message_object.timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')
            tmp_file = open("{}.txt".format(author_name),"a")
            tmp_file.write("{}:\n".format(author_name))
            tmp_file.write("'{}'\n".format(message_object.text))
            tmp_file.write("{}\n".format(message_time))
            print("{}:".format(author_name))
            print("'{}'".format(message_object.text))
            print("{}".format(message_time))
            if(message_object.attachments):
                y = 0
                for x in message_object.attachments:
                    urllib.request.urlretrieve(x.large_preview_url,"{} [{}].{}".format(message_object.timestamp,y,x.original_extension))
                    y+=1
                tmp_file.write("    *\n")
                print(" *")
            tmp_file.write("---------------------------------\n")
            print("---------------------------------")
            tmp_file.close()
client = SaveMessages(login,password)
client.listen()
client.logout()
