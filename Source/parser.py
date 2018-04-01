################################################
# Sample Prompt File
################################################
from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("-f", "--file", metavar="FILE", dest="file", help="Specifies raw file transmission")
parser.add_option("-i", "--image", metavar="IMAGE", dest="image", help="Specifies PNG file transmission")
parser.add_option("-c", "--chat", action="store_true", dest="chat", help="Specifies text input from user in console")
(options, args) = parser.parse_args()

if options.file:
    f = open(options.file,'r')
    print f.read()
elif options.image:
    os.startfile(options.image)
elif options.chat:
    send = raw_input("Enter Message: ")
    print(send)
