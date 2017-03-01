#! /usr/bin/python

import message_pb2
import sys

# This function fills in a Person message based on user input.
def PromptForAddress(msgg):
  msgg.id = int(raw_input("Enter msgg ID number: "))
  msgg.name = raw_input("Enter name: ")
  msgg.email = raw_input("Enter email address (blank for none): ")
  msgg.fullmessage = raw_input("Enter full message (blank for none): ")


# Main procedure:  Reads the entire address book from a file,
#   adds one msgg based on user input, then writes it back out to the same
#   file.
if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "MESSAGE_BOOK_FILE"
  sys.exit(-1)

message_book = message_pb2.Inbox()

try:
  f = open(sys.argv[1], "rb")
  message_book.ParseFromString(f.read())
  f.close()
except IOError:
  print sys.argv[1] + ": Could not open file.  Creating a new one."

# Add an address.
PromptForAddress(message_book.msgg.add())

# Write the new address book back to disk.
f = open(sys.argv[1], "wb")
f.write(message_book.SerializeToString())
f.close()
