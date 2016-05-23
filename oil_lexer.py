

from ply import lex, yacc
from lex import TOKEN

#       ####### #     # ####### ######
#       #        #   #  #       #     #
#       #         # #   #       #     #
#       #####      #    #####   ######
#       #         # #   #       #   #
#       #        #   #  #       #    #
####### ####### #     # ####### #     #


class OILLexer():
    # List of token names.
    tokens = (
        'FALSE',
        'TRUE',
        'AUTO',
        'NO_DEFAULT',
        'OIL_VERSION',
        'EQUAL',
        'SEMI',
        'IMPLEMENTATION',
        'IDENT',
        'LBRACE',
        'LBRACKET',
        'RBRACE',
        'RBRACKET',
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
        'TO',
        'COMMA',
        'COLON',
        'OS_TYPE'
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
        'CPU',
        'PLUS',
        'MINUS',
        'DOT',
        'PREFIX'
    )


    t_FALSE                 = r'FALSE'
    t_TRUE                  = r'TRUE'
    t_AUTO                  = r'AUTO'
    t_NO_DEFAULT            = r'NO_DEFAULT'
    t_OIL_VERSION           = r'OIL_VERSION'
    t_EQUAL                 = r'='
    t_SEMI                  = r';'
    t_IMPLEMENTATION        = r'IMPLEMENTATION'
    t_LBRACE                = r'{'
    t_LBRACKET              = r'\['
    t_RBRACE                = r'}'
    t_RBRACKET              = r'\]'
    t_OS                    = r'OS'
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
    t_TO                    = r'\.\.'
    t_COMMA                 = r','
    t_COLON                 = r':'
    t_OS_TYP                = r'OS_TYPE'
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
    t_PLUS                  = r'+'
    t_MINUS                 = r'-'
    t_DOT                   = r'\.'
    t_PREFIX                = r'0x'

    t_IDENT

    # Regular expression rules for simple tokens
    #
    #

    # A regular expression rule with some action code

    def t_COUNT(t):
        r"\d+"
        t.value = int(t.value)
        return t

    def t_error(t):
        raise TypeError("Unknown text '%s'" % (t.value,))

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)