# -*- coding: utf-8 -*

from modules.common_1_0.Errors import *
from modules.common_1_0.Files import *
from modules.common_1_0.IniParser import *

class Tests:
	def __init__(self):
		self.errors = Errors()
		self.spaces = ' ' * 70;
	
	def res_ok(self, test_title):
		print('\t' + test_title + self.spaces[:-len(test_title)] + ': OK')
	
	def res_fail(self, test_title):
		print('\t' + test_title + self.spaces[:-len(test_title)] + ': FAIL')
		self.errors.print_errors()
		exit()
	
	def test_Files(self):
		print('Tests.test_Files()')
		file = Files(self.errors)
		
		file_path = 'data/tests/files/file_for_reading.txt'
		#open_file() for reaing
		test_title = 'open_file() for reaing'
		file.open_file(file_path)
		if file.handler != None:
			self.res_ok(test_title)
		else:		
			self.res_fail(test_title)

		#read_line()
		test_title = 'read_line()'
		line = file.read_line()
		line = file.read_line()
		if line == 'ab, cd, ef,\n':
			self.res_ok(test_title)
		else:
			self.res_fail(test_title)

		file.close_file()
		
		file_path = 'data/tests/files/file_for_writing.txt'
		#open_file() for writing
		test_title = 'open_file() for writing'
		file.open_file(file_path, 'w')
		if file.handler != None:
			self.res_ok(test_title)
		else:		
			self.res_fail(test_title)

		#write_line()
		test_title = 'write_line()'
		line = 'a, b, c,'
		file.write_line(line)
		file.close_file()
		
		file.open_file(file_path)
		line = file.read_line()
		if line == 'a, b, c,\n':
			self.res_ok(test_title)
		else:
			self.res_fail(test_title)
		
		file.close_file()
		
		
		
		