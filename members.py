from enum import Enum

valid_numbers="1234567890.,"
valid_variable="XYZ"
valid_none="_ "


class MemberType(Enum):

	NUMBER_FLOAT = 1
	#is a cooked number
	
	VARIABLE = 3
	#is a raw number

	OPERATOR = 4
	#do operation between values
	
class Member:
	def __init__(memberType, value):
		self.type=memberType
		self.value=value