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
		elif name == '.”':
			return '.”'
		elif name == '...”':
			return '...”'
		elif name == '...':
			return '...'
		elif name == '.':
			return '.'
		elif name == ',”':
			return ',”'
		elif name == ',':
			return ','
		elif name == 'semicolon':
			return ';'
		elif name == '!”':
			return '!”'
		elif name == '?”':
			return '?”'
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
		
		for cnt in range(len(separators)):
			separators[cnt] = self.name2symbol(separators[cnt])
			
		input_file = Files(self.errors)
		input_file.open_file(file_path, 'r' ,enc)
		sep = ''
		wrd = ''
		self.text_elements = []
		last_smb_type = 's'
		smb_cnt = 0
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
			smb_cnt += 1
		if sep != '':
			self.text_elements.append(sep)
		if wrd != '':
			self.text_elements.append(wrd)
			self.text_elements.append('')
		input_file.close_file()
		
	def separator_is_match(self, sep, separators):
		for cnt in range(len(separators)):
			if separators[cnt] in sep:
				# print([sep], separators, cnt)
				return True
		return False
	
	def clear_end_subsentence(self, sep, separators): 		
		for cnt in range(len(separators)):
			if separators[cnt] in sep:
				sep = sep.replace(separators[cnt], '').lstrip(' \t')
				break
		return sep
		
	def remain_end_subsentence(self, sep, separators): 		
		for cnt in range(len(separators)):
			if separators[cnt] in sep:
				sep = separators[cnt]
				break
		return sep
		
	# def combine_subsentences(self, start_subsentence, end_subsentence):
		# subsentence_is_started = False
		# subsentence = ''
		# subsentences = []
		# for cnt in range(1, len(self.text_elements), 2):
			# wrd = self.text_elements[cnt]
			# after_sep = self.text_elements[cnt + 1].replace('\n', '')
			# before_sep = self.text_elements[cnt - 1].replace('\n', '')
			# if subsentence_is_started:
				# subsentence += before_sep + wrd
				# if self.separator_is_match(after_sep, end_subsentence):
					# print(subsentence + self.remain_end_subsentence(after_sep, end_subsentence))
					# subsentence = ''
					# subsentence_is_started = False
					
			# else:
				# subsentence += self.clear_end_subsentence(before_sep, end_subsentence) + wrd
				# subsentence_is_started = True
				# if self.separator_is_match(after_sep, end_subsentence):
					# print(subsentence + self.remain_end_subsentence(after_sep, end_subsentence))
					# subsentence = ''
					# subsentence_is_started = False
					
			
	def combine_subsentences(self, start_subsentence, end_subsentence, end_sentence):
		subsentence_is_started = False
		subsentence = ''
		subsentences = {}
		subsentence_cnt = 0
		wrd_cnt = 0
		for cnt in range(1, len(self.text_elements), 2):
			wrd = self.text_elements[cnt]
			after_sep = self.text_elements[cnt + 1].replace('\n', '')
			before_sep = self.text_elements[cnt - 1].replace('\n', '')
			if subsentence_is_started:
				if self.separator_is_match(wrd, start_subsentence):
					if wrd_cnt > 1:
						subsentences[subsentence_cnt] = {
							'subsentence': subsentence,
							'text_element_idx': cnt - 2 * wrd_cnt + 2,
							'wrd_cnt': wrd_cnt
						}
						# print(wrd_cnt, subsentence)
						subsentence_cnt	+= 1
						subsentence = wrd
						wrd_cnt = 1
					else:
						subsentence += before_sep + wrd
						wrd_cnt += 1
					if self.separator_is_match(after_sep, end_subsentence):
						if wrd_cnt > 1 or self.separator_is_match(after_sep, end_sentence):
							after_sep = self.remain_end_subsentence(after_sep, end_subsentence)
							subsentence += after_sep
							subsentences[subsentence_cnt] = {
								'subsentence': subsentence,
								'text_element_idx': cnt - 2 * wrd_cnt + 2,
								'wrd_cnt': wrd_cnt
							}
							# print(wrd_cnt, subsentence)
							subsentence_cnt	+= 1
							subsentence = ''
							wrd_cnt = 0
							subsentence_is_started = False
				else:
					subsentence += before_sep + wrd
					wrd_cnt += 1
					if self.separator_is_match(after_sep, end_subsentence):
						if wrd_cnt > 1 or self.separator_is_match(after_sep, end_sentence):
							after_sep = self.remain_end_subsentence(after_sep, end_subsentence)
							subsentence += after_sep
							subsentences[subsentence_cnt] = {
								'subsentence': subsentence,
								'text_element_idx': cnt - 2 * wrd_cnt + 2,
								'wrd_cnt': wrd_cnt
							}
							# print(wrd_cnt, subsentence)
							subsentence_cnt	+= 1
							subsentence = ''
							wrd_cnt = 0
							subsentence_is_started = False
					
			else:
				subsentence += self.clear_end_subsentence(before_sep, end_subsentence) + wrd
				wrd_cnt += 1
				subsentence_is_started = True
				if self.separator_is_match(after_sep, end_subsentence):
					if wrd_cnt > 1 or self.separator_is_match(after_sep, end_sentence):
						after_sep = self.remain_end_subsentence(after_sep, end_subsentence)
						subsentence = subsentence + after_sep
						subsentences[subsentence_cnt] = {
							'subsentence': subsentence,
							'text_element_idx': cnt - 2 * wrd_cnt + 2,
							'wrd_cnt': wrd_cnt
						}
						# print(wrd_cnt, subsentence)
						subsentence_cnt	+= 1
						subsentence = ''
						wrd_cnt = 0
						subsentence_is_started = False
			
		##################################
		for _idx in subsentences:
			# if subsentences[_idx]['text_element_idx'] < 643 and subsentences[_idx]['text_element_idx'] > 599: 
			if subsentences[_idx]['wrd_cnt'] < 2:
				if not self.separator_is_match(self.text_elements[subsentences[_idx]['text_element_idx'] - 1], end_sentence):
					subsentence_is_started = False
					wrd_cnt = 0
					subsentence = ''
					start_cnt = subsentences[_idx - 1]['text_element_idx']
					wrd_length = subsentences[_idx - 1]['wrd_cnt'] + subsentences[_idx]['wrd_cnt']
					stop_cnt = start_cnt + wrd_length * 2
					for cnt in range(start_cnt, stop_cnt, 2):
						wrd = self.text_elements[cnt]
						after_sep = self.text_elements[cnt + 1].replace('\n', '')
						before_sep = self.text_elements[cnt - 1].replace('\n', '')
						if subsentence_is_started:
							subsentence += before_sep + wrd
							wrd_cnt += 1
						else:
							subsentence += self.clear_end_subsentence(before_sep, end_subsentence) + wrd
							wrd_cnt += 1
							subsentence_is_started = True
						
					after_sep = self.remain_end_subsentence(after_sep, end_subsentence)
					subsentence = subsentence + after_sep
					subsentences[_idx] = {
						'subsentence': subsentence,
						'text_element_idx': cnt - 2 * wrd_cnt + 2,
						'wrd_cnt': wrd_cnt
					}
					subsentences[_idx-1] = subsentences[_idx]
					# print(subsentences[_idx-1]['text_element_idx'], subsentences[_idx-1]['wrd_cnt'], subsentences[_idx-1]['subsentence'])	
					# print(subsentences[_idx]['text_element_idx'], subsentences[_idx]['wrd_cnt'], subsentences[_idx]['subsentence'])	
						
		for _idx in subsentences:
			print(_idx, subsentences[_idx]['text_element_idx'], subsentences[_idx]['wrd_cnt'], subsentences[_idx]['subsentence'])	
		
	def parse_text(self, settings):
		if self.errors.error_occured:
			return None
			
		file_path = settings['input']['file_path']
		enc = settings['input']['encoding']
		word_common_separators = settings['params']['word_common_separators']
		start_subsentence = settings['params']['start_subsentence']
		end_subsentence = settings['params']['end_subsentence']
		end_sentence = settings['params']['end_sentence']
		
		for cnt in range(len(end_subsentence)):
			end_subsentence[cnt] = self.name2symbol(end_subsentence[cnt])
			
		for cnt in range(len(end_sentence)):
			end_sentence[cnt] = self.name2symbol(end_sentence[cnt])
		
		self.split_text(file_path, enc, word_common_separators)
		self.combine_subsentences(start_subsentence, end_subsentence, end_sentence)
		# print(self.text_elements)
		