# -*- coding: utf-8 -*

from modules.common.Errors import *
from modules.common.IniParser import *
from modules.text.TextParser import *

class Parser:
	def __init__(self):
		self.errors = Errors()
		self.ini_encoding = 'utf-8'
		self.ini_parser = IniParser(self.errors)
		self.settings = {}
	
	def read_settings(self, args):
		if len(args) < 2:
			self.errors.raise_error('No ini file path')
		else:
			encoding = self.ini_encoding
			if len(args) > 2:
				encoding = args[2]
				
			ini_file_path = args[1]
			self.ini_parser.read_ini(args[1], encoding)
	
	def set_params(self, args):
		self.read_settings(args)
		self.settings['input'] = {}
		self.settings['output'] = {}
		self.settings['params'] = {}
		self.settings['input']['file_path'] = self.ini_parser.get_param('input', 'file_path')
		self.settings['input']['encoding'] = self.ini_parser.get_param('input', 'encoding')
		self.settings['params']['separators'] = self.ini_parser.get_param('params', 'separators', param_type='str_array', sep='\\')
		
		
	def main(self, args):
		self.set_params(args)
		# print(self.settings)
		text_parser = TextParser(self.errors)

		input_file_name = self.settings['input']['file_path']
		enc = self.settings['input']['encoding']
		params = self.settings['params']
		text_parser.parse(input_file_name, enc, params)
		
		if self.errors.error_occured:
			self.errors.print_errors()
		else:
			print('OK\n')