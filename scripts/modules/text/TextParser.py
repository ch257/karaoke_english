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
		elif name == 'semicolon':
			return ';'
		elif name == '.':
			return '.'
		elif name == ',':
			return ','
		elif name == '!':
			return '!'
		elif name == '?':
			return '?'
		elif name == ':':
			return ':'
		else:
			self.errors.raise_error('Unknown symbol name ' + name)
		return None
		
	def parse(self, file_path, enc, params):
		if self.errors.error_occured:
			return None
		
		separators = params['separators']
		for cnt in range(len(separators)):
			separators[cnt] = self.name2symbol(separators[cnt])
			
		print(separators)