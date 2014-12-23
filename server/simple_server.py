import asyncore_epoll as asyncore
from greenlet import greenlet
import socket
from protocol.packet import PacketIO,PacketHandler 
import resource
import time

class SimpleServer(asyncore.dispatcher):
    def __init__(self,host,port,handler_type):
        asyncore.dispatcher.__init__(self)
        self.glet = greenlet(self.routine)
        self.handler_type = handler_type
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host,port))
        self.listen(5)
        resource.setrlimit(resource.RLIMIT_NOFILE,(65535,65535))

    def handle_accept(self):
        pair = self.accept()
        #print time.time()
        socket,addr = pair
        handler = self.handler_type(socket,self)
        handler.glet.switch()


    def routine(self):
        asyncore.loop(poller=asyncore.epoll_poller)

    def serve(self):
        self.glet.switch()

