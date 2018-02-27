import binascii
source = 'out.txt'
with open(source,'rb') as f:
	content = f.read()
decode = binascii.unhexlify(content)
out = open('./hex.png','wb')
out.write(decode)