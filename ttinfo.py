import sys

from fontTools.ttLib import TTFont

print(sys.argv[1])
print('')

font = TTFont(sys.argv[1])
namerecord_list = font["name"].names

for record in namerecord_list:
	print(record.nameID, end=': ')
	print(record.string.decode('latin-1'))
