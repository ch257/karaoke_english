# -*- coding: utf-8 -*

from modules.common.Files import *

class TextParser:
	def __init__(self, errors):
		self.errors = errors
		
	def name2symbol(self, name):
		if self.errors.error_occured:
			return None
			
		if name == 'space':
			return ' '
		elif name == 'tab':
			return '\t'
		elif name == 'n':
			return '\n'
		elif name == '.':
			return '.'
		elif name == ',':
			return ','
		elif name == 'semicolon':
			return ';'
		elif name == '!':
			return '!'
		elif name == '?':
			return '?'
		elif name == ':':
			return ':'
		elif name == "'":
			return "'"
		elif name == "’":
			return "’"
		elif name == '"':
			return '"'
		elif name == "“":
			return "“"
		elif name == '”':
			return '”'
		else:
			self.errors.raise_error('Unknown symbol name ' + name)
		return None
		
	def parse(self, file_path, enc, params):
		if self.errors.error_occured:
			return None
		
		separators = params['separators']
		for cnt in range(len(separators)):
			separators[cnt] = self.name2symbol(separators[cnt])
			
		input_file = Files(self.errors)
		input_file.open_file(file_path, 'r' ,enc)
		sep = ''
		wrd = ''
		text_elements = []
		last_smb_type = 's'
		while not self.errors.error_occured:
			smb = input_file.read_smb(1)
			if smb == '':
				break
			else:
				if smb in separators:
					if last_smb_type == 'l':
						text_elements.append(wrd)
						wrd = ''
					sep += smb
					last_smb_type = 's'
				else:
					if last_smb_type == 's':
						text_elements.append(sep)
						sep = ''
					wrd += smb
					last_smb_type = 'l'
		if sep != '':
			text_elements.append(sep)
		if wrd != '':
			text_elements.append(wrd)
			text_elements.append('')
		
		print(text_elements)
			
			
			
		input_file.close_file()
		
		# test_file_r = Files(self.errors)
		# test_file_w = Files(self.errors)
		# test_file_r.open_file('data/in/test_r.txt', 'r')
		# test_file_w.open_file('data/in/test_w.txt', 'w')
		# smb = test_file_r.read_smb(1)
		# print(smb == '\n')
		# test_file_w.write_line(smb)
		# test_file_r.close_file()
		# test_file_w.close_file()
		
			
		# print(separators)