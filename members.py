from enum import Enum

valid_numbers="1234567890.,"
valid_operators="+-*/^"
valid_parentheses="()"
parentheses_closing=")"
valid_none="_ "


class MemberType(Enum):

	NUMBER_FLOAT = 1
	#is a cooked number
	
	VARIABLE = 3
	#is a raw number

	OPERATOR = 4
	#do operation between values
	
	PARENTHESE = 5
	#do priority
	
	UNIT = 6
	#is unit letter

	NOTHING = 0
	
#class Member:
#	def __init__(self, memberType, value):
#		self.type=memberType
#		self.value=value