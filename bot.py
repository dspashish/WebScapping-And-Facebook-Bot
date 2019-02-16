from fbchat import Client, log
from fbchat.models import *





username = "ak367576@gmail.com"
password = "ashu367576@bahubali"











class Harvis(Client):
    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        self.markAsRead(author_id)
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))
        msgText = message_object.text
        reply = "Hello"
        if author_id!=self.uid:
            self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)

        self.markAsDelivered(author_id, thread_id)


client = Harvis(username, password)
client.listen()