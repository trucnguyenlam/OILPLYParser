from ply import lex
from ply.lex import TOKEN


class OILLexer():
    def __init__(self):
        self.filename = ''
        self.last_token = None

    # List of token names.
    keywords = (
        'FALSE',
        'TRUE',
        'AUTO',
        'NO_DEFAULT',
        'OIL_VERSION',
        'IMPLEMENTATION',
        'OS',
        'TASK',
        'COUNTER',
        'ALARM',
        'RESOURCE',
        'EVENT',
        'ISR',
        'MESSAGE',
        'COM',
        'NM',
        'APPMODE',
        'IPDU',
        'UINT32',
        'INT32',
        'UINT64',
        'INT64',
        'FLOAT',
        'ENUM',
        'STRING',
        'BOOLEAN',
        'WITH_AUTO',
        'OS_TYPE',
        'TASK_TYPE',
        'COUNTER_TYPE',
        'ALARM_TYPE',
        'RESOURCE_TYPE',
        'EVENT_TYPE',
        'ISR_TYPE',
        'MESSAGE_TYPE',
        'COM_TYPE',
        'NM_TYPE',
        'APPMODE_TYPE',
        'IPDU_TYPE',
        'CPU'
    )

    keyword_map = {}
    for keyword in keywords:
        keyword_map[keyword] = keyword

    tokens = keywords + (
        'EQUAL',
        'SEMI',
        'LBRACE',
        'LBRACKET',
        'RBRACE',
        'RBRACKET',
        'TO',
        'COMMA',
        'COLON',
        'PLUS',
        'MINUS',
        'IDENT',
        'STRING_LITERAL',
        'CONST_DEC',
        'CONST_HEX',
        'FLOATING_CONSTANT'
        )

    # Regular expression rules for simple tokens
    t_OS_TYPE               = r'OS_TYPE'
    t_TASK_TYPE             = r'TASK_TYPE'
    t_COUNTER_TYPE          = r'COUNTER_TYPE'
    t_ALARM_TYPE            = r'ALARM_TYPE'
    t_RESOURCE_TYPE         = r'RESOURCE_TYPE'
    t_EVENT_TYPE            = r'EVENT_TYPE'
    t_ISR_TYPE              = r'ISR_TYPE'
    t_MESSAGE_TYPE          = r'MESSAGE_TYPE'
    t_COM_TYPE              = r'COM_TYPE'
    t_NM_TYPE               = r'NM_TYPE'
    t_APPMODE_TYPE          = r'APPMODE_TYPE'
    t_IPDU_TYPE             = r'IPDU_TYPE'
    t_CPU                   = r'CPU'
    t_FALSE                 = r'FALSE'
    t_TRUE                  = r'TRUE'
    t_AUTO                  = r'AUTO'
    t_NO_DEFAULT            = r'NO_DEFAULT'
    t_OIL_VERSION           = r'OIL_VERSION'
    t_IMPLEMENTATION        = r'IMPLEMENTATION'
    t_TASK                  = r'TASK'
    t_COUNTER               = r'COUNTER'
    t_ALARM                 = r'ALARM'
    t_RESOURCE              = r'RESOURCE'
    t_EVENT                 = r'EVENT'
    t_ISR                   = r'ISR'
    t_MESSAGE               = r'MESSAGE'
    t_COM                   = r'COM'
    t_NM                    = r'NM'
    t_APPMODE               = r'APPMODE'
    t_IPDU                  = r'IPDU'
    t_UINT32                = r'UINT32'
    t_INT32                 = r'INT32'
    t_UINT64                = r'UINT64'
    t_INT64                 = r'INT64'
    t_FLOAT                 = r'FLOAT'
    t_ENUM                  = r'ENUM'
    t_STRING                = r'STRING'
    t_BOOLEAN               = r'BOOLEAN'
    t_WITH_AUTO             = r'WITH_AUTO'
    t_OS                    = r'OS'
    t_EQUAL                 = r'='
    t_SEMI                  = r';'
    t_LBRACE                = r'\{'
    t_LBRACKET              = r'\['
    t_RBRACE                = r'\}'
    t_RBRACKET              = r'\]'
    t_TO                    = r'\.\.'
    t_COMMA                 = r','
    t_COLON                 = r':'
    t_PLUS                  = r'\+'
    t_MINUS                 = r'-'

    simple_escape = r"""([a-zA-Z._~!=&\^\-\\?'"])"""
    decimal_escape = r"""(\d+)"""
    hex_escape = r"""(x[0-9a-fA-F]+)"""
    bad_escape = r"""([\\][^a-zA-Z._~^!=&\^\-\\?'"x0-7])"""

    escape_sequence = r"""(\\("""+simple_escape+'|'+decimal_escape+'|'+hex_escape+'))'
    # string literals (K&R2: A.2.6)
    string_char = r"""([^"\\\n]|"""+escape_sequence+')'
    string_literal = '"'+string_char+'*"'
    identifier          = r'[a-zA-Z_$][0-9a-zA-Z_$]*'
    # Number
    hex_prefix          = r'0x'
    hex_digits          = r'[0-9a-fA-F]+'
    hex_constant        = hex_prefix + hex_digits
    decimal_constant    = r'''(0)|([1-9][0-9]*)'''
    # float
    floating_constant   = r'''([0-9]+\.[0-9]+)([eE][-+]?[0-9]+)?'''
    # String

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore  = ' \t'

    # A regular expression rule with some action code
    @TOKEN(string_literal)
    def t_STRING_LITERAL(self, t):
        return t

    @TOKEN(identifier)
    def t_IDENT(self, t):
        t.type = self.keyword_map.get(t.value, 'IDENT')
        return t

    @TOKEN(floating_constant)
    def t_FLOATING_CONSTANT(self, t):
        return t

    @TOKEN(hex_constant)
    def t_CONST_HEX(self, t):
        return t

    @TOKEN(decimal_constant)
    def t_CONST_DEC(self, t):
        return t

    def t_error(self, t):
        raise TypeError("Unknown text (%s)" % (t.value,))

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(object=self, **kwargs)

    def input(self, text):
        self.lexer.input(text)

    def token(self):
        self.last_token = self.lexer.token()
        return self.last_token