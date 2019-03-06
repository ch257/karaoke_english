# -*- coding: utf-8 -*

from modules.common.Files import *

class TextParser:
	def __init__(self, errors):
		self.errors = errors
		self.text_elements = [];
		
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
		
	def split_text(self, file_path, enc, separators):
		if self.errors.error_occured:
			return None
		
		separators
		for cnt in range(len(separators)):
			separators[cnt] = self.name2symbol(separators[cnt])
			
		input_file = Files(self.errors)
		input_file.open_file(file_path, 'r' ,enc)
		sep = ''
		wrd = ''
		self.text_elements = []
		last_smb_type = 's'
		while not self.errors.error_occured:
			smb = input_file.read_smb(1)
			if smb == '':
				break
			else:
				if smb in separators:
					if last_smb_type == 'l':
						self.text_elements.append(wrd)
						wrd = ''
					sep += smb
					last_smb_type = 's'
				else:
					if last_smb_type == 's':
						self.text_elements.append(sep)
						sep = ''
					wrd += smb
					last_smb_type = 'l'
		if sep != '':
			self.text_elements.append(sep)
		if wrd != '':
			self.text_elements.append(wrd)
			self.text_elements.append('')
		input_file.close_file()
		
	def parse_text(self, settings):
		if self.errors.error_occured:
			return None
		
		file_path = settings['input']['file_path']
		enc = settings['input']['encoding']
		separators = settings['params']['separators']
		
		self.split_text(file_path, enc, separators)
		for cnt in range(1, len(self.text_elements), 2):
			print(self.text_elements[cnt])
		