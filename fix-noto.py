## 
##
## Requires:
##     pip install fonttools

import sys

from fontTools.ttLib import TTFont

exact_family_name = 'Noto Sans CJK JP'

weights = [
	'Thin',
	'Light',
	'DemiLight',
	'Regular',
	'Medium',
	'Bold',
	'Black',
]

for weight in weights:
	font = TTFont('src/NotoSansCJKjp-' + weight + '.otf')
	namerecord_list = font["name"].names
	
	for record in namerecord_list:
		if record.nameID == 1:
			record.string = exact_family_name
	
	output_path = 'dest/NotoSansCJKjp-' + weight + '.otf'
	try:
		font.save(output_path)
	except Exception as e:
		sys.stderr.write('ERROR: unable to write "' + output_path + '"')
		sys.exit(1)
