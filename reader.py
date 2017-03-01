#! /usr/bin/python

import message_pb2
import sys

# Iterates though all people in the Inbox and prints info about them.
def ListMessages(message_book):
  for msgg in message_book.msgg:
    print "Person ID:", msgg.id
    print "  Name:", msgg.name
    print "  Email:", msgg.email
    print "  Message:", msgg.fullmessage
#    if msgg.HasField('email'):
#      print "  E-mail address:", msgg.email
#    if msgg.HasField('fullmessage'):
#      print "  Message:", msgg.fullmessage

# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.
if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "MESSAGE_BOOK_FILE"
  sys.exit(-1)

message_book = message_pb2.Inbox()

# Read the existing address book.
f = open(sys.argv[1], "rb")
message_book.ParseFromString(f.read())
f.close()

ListMessages(message_book)
