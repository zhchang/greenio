#!/usr/bin/pypy
from server.simple_server import SimpleServer
from protocol.packet import PacketHandler
import gc

gc.disable()
SimpleServer('0.0.0.0',7777,PacketHandler).serve()
