# in this file : Some enum-like used.

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


replace_shortcuts = {
    #syntax
# "from": "to",
    #shortcut
    "**": "^",
}

replace_const = [
    #constants
    ("siπ", "3"),
    ("SIPI", "3"),
    ("sipi", "3"),
    ("siPI", "3"),
    ("SIpi", "3"),
    ("sie", "3"),
    ("SIE", "3"),

    ("PI", "π"),
    ("pi", "π"),
    ("pI", "π"),
    ("Pi", "π"),
    ("π", "3.14159265358979323846"),

    #("E", "𝑒"),
	("e", "𝑒"),
    ("𝑒", "2.71828182845904523536"),
]

replace_writte = {
    #letters
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eigth":"8",
    "nine":"9",
    "ten":"10",
}


pow_to_digits = {
	"⁰":"0",
	"¹":"1",
	"²":"2",
	"³":"3",
	"⁴":"4",
	"⁵":"5",
	"⁶":"6",
	"⁷":"7",
	"⁸":"8",
	"⁹":"9",
	"⁻":"-",
	"˙":".",
}
