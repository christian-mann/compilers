T = [
	"program",
	"id",
	"var",
	"array",
	"num",
	"of",
	"integer",
	"real",
	"procedure",
	"begin",
	"end",
	"assignop",
	"if",
	"then",
	"else",
	"while",
	"do",
	"call",
	"relop",
	"addop",
	"mulop",
	"not",
	"",
	"(",
	")",
	";",
	".",
	",",
	":",
	"[",
	"]",
	"+",
	"-",
	"..",
]

V = [
	"programSymb",
	"identifier_list",
	"declarations",
	"type",
	"standard_type",
	"subprogram_declarations",
	"subprogram_declaration",
	"subprogram_head",
	"arguments",
	"parameter_list",
	"compound_statement",
	"optional_statements",
	"statement_list",
	"statement",
	"variable",
	"procedure_statement",
	"expression_list",
	"expression",
	"simple_expression",
	"term",
	"factor",
	"sign"
]

S = "programSymb"

P = [
	("programSymb", "program id ( identifier_list ) ; declarations subprogram_declarations compound_statement .".split()),
	("identifier_list", "id".split()),
	("identifier_list", "identifier_list , id".split()),
	("declarations", "declarations var id : type ;".split()),
	("declarations", [""]),
	("type", ["standard_type"]),
	("type", "array [ num .. num ] of standard_type".split()),
	("standard_type", ["integer"]),
	("standard_type", ["real"]),
	("subprogram_declarations", "subprogram_declarations subprogram_declaration ;".split()),
	("subprogram_declarations", [""]),
	("subprogram_declaration", "subprogram_head declarations subprogram_declarations compound_statement".split()),
	("subprogram_declaration", "subprogram_head declarations compound_statement".split()),
	("subprogram_head", "procedure id arguments ;".split()),
	("arguments", "( parameter_list )".split()),
	("arguments", [""]),
	("parameter_list", "id : type".split()), 
	("parameter_list", "parameter_list ; id : type".split()),
	("compound_statement", "begin optional_statements end".split()),
	("optional_statements", "statement_list".split()),
	("optional_statements", [""]),
	("statement_list", "statement".split()),
	("statement_list", "statement_list ; statement".split()),
	("statement", "variable assignop expression".split()),
	("statement", "procedure_statement".split()),
	("statement", "compound_statement".split()),
	("statement", "if expression then statement else statement".split()),
	("statement", "while expression do statement".split()),
	("statement", "if expression then statement".split()),
	("variable", "id".split()),
	("variable", "id [ expression ]".split()),
	("procedure_statement", "call id".split()),
	("procedure_statement", "call id expression_list".split()),
	("expression_list", "expression".split()),
	("expression_list", "expression_list , expression".split()),
	("expression", "simple_expression".split()),
	("expression", "simple_expression relop simple_expression".split()),
	("simple_expression", "term".split()),
	("simple_expression", "sign term".split()),
	("simple_expression", "simple_expression addop term".split()),
	("term", "factor".split()),
	("term", "term mulop factor".split()),
	("factor", "id".split()),
	("factor", "id [ expression ]".split()),
	("factor", "num".split()),
	("factor", "( expression )".split()),
	("factor", "not factor".split()),
	("sign", ["+"]),
	("sign", ["-"])
]

if S not in V:
	print "S = %s not in V!" % S
for lhs,rhs in P:
	if lhs not in V:
		print "'%s' not in V!" % lhs
	for w in rhs:
		if w not in T and w not in V:
			print "'%s' not in T!" % w
		if ' ' in w:
			print "improperly split?"
