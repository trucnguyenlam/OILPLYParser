from ply import yacc
from oil_lexer import OILLexer
import oil_ast

class OILParser():
    def __init__(self):
        self.oillexer = OILLexer()
        self.oillexer.build()
        self.tokens = self.oillexer.tokens
        self.oilparser = yacc.yacc(module=self, start='File')

    def parse(self, text, filename='', debuglevel=0):
        self.oillexer.filename = filename
        return self.oilparser.parse(input=text, lexer=self.oillexer, debug=debuglevel)

    def p_File(self, p):
        """ File : OilVersion ImplementationDefinition ApplicationDefinition
        """
        p[0] = oil_ast.File(p[1], p[2], p[3])

    def p_OilVersion(self, p):
        """ OilVersion : OIL_VERSION EQUAL Version Description SEMI
        """
        p[0] = oil_ast.OilVersion(p[3], p[4])

    def p_Version(self, p):
        """ Version : String """
        p[0] = p[1]

    def p_ImplementationDefinition(self, p):
        """ ImplementationDefinition :  IMPLEMENTATION Name LBRACE ImplementationSpecList RBRACE Description SEMI
        """
        p[0] = oil_ast.ImplementationDefinition(p[2], p[4], p[6])

    def p_ImplementationSpecList(self, p):
        """ ImplementationSpecList : ImplementationSpec
                                   | ImplementationSpecList ImplementationSpec
        """
        p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

    def p_ImplementationSpec(self, p):
        """ ImplementationSpec : Object LBRACE ImplementationList RBRACE Description SEMI
        """
        p[0] = oil_ast.ImplementationSpec(p[1], p[3], p[5])

    def p_Object(self, p):
        """ Object : OS
                   | TASK
                   | COUNTER
                   | ALARM
                   | RESOURCE
                   | EVENT
                   | ISR
                   | MESSAGE
                   | COM
                   | NM
                   | APPMODE
                   | IPDU
        """
        p[0] = p[1]

    def p_ImplementationList(self, p):
        """ ImplementationList : empty
                               | ImplementationDef
                               | ImplementationList ImplementationDef
        """
        if p[1] is None:
            p[0] = []
        else:
            p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

    def p_ImplementationDef(self, p):
        """ ImplementationDef : ImplAttrDef
                              | ImplRefDef
        """
        p[0] = p[1]

    def p_ImplAttrDef(self, p):
        """ ImplAttrDef : UINT32    AutoSpecifier NumberRange   AttributeName MultipleSpecifier DefaultNumber Description SEMI
                        | INT32     AutoSpecifier NumberRange   AttributeName MultipleSpecifier DefaultNumber Description SEMI
                        | UINT64    AutoSpecifier NumberRange   AttributeName MultipleSpecifier DefaultNumber Description SEMI
                        | INT64     AutoSpecifier NumberRange   AttributeName MultipleSpecifier DefaultNumber Description SEMI
                        | FLOAT     AutoSpecifier FloatRange    AttributeName MultipleSpecifier DefaultFloat  Description SEMI
                        | ENUM      AutoSpecifier Enumeration   AttributeName MultipleSpecifier DefaultName   Description SEMI
                        | STRING    AutoSpecifier               AttributeName MultipleSpecifier DefaultString Description SEMI
                        | BOOLEAN   AutoSpecifier BoolValues    AttributeName MultipleSpecifier DefaultBool   Description SEMI
        """
        if len(p) == 9:     # Not STRING case
            p[0] = oil_ast.ImplAttrDef(p[1], p[2], p[3], p[4], p[5], p[6], p[7])
        else:               # STRING
            p[0] = oil_ast.ImplAttrDef(p[1], p[2], None, p[3], p[4], p[5], p[6])


    def p_ImplParameterList(self, p):
        """ ImplParameterList   : empty
                                | LBRACE ImplDefList RBRACE
        """
        if p[1] is None:
            p[0] = []        # empty list
        else:
            p[0] = p[2]

    def p_ImplDefList(self, p):
        """ ImplDefList         : empty
                                | ImplementationDef ImplDefList
        """
        if p[1] is None:
            p[0] = []
        else:
            p[0] = p[2] + [p[1]]

    def p_AutoSpecifier(self, p):
        """ AutoSpecifier       : empty
                                | WITH_AUTO
        """
        p[0] = p[1]

    def p_NumberRange(self, p):
        """ NumberRange         : empty
                                | LBRACKET Number TO Number RBRACKET
                                | LBRACKET NumberList RBRACKET
        """
        if p[1] is None:
            p[0] = p[1]
        elif len(p) == 4:
            p[0] = oil_ast.NumberRange(1, None, None, p[2])
        else:
            p[0] = oil_ast.NumberRange(0, p[2], p[4], numberList=[])

    def p_NumberList(self, p):
        """ NumberList          : Number
                                | NumberList COMMA Number
        """
        p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]


    def p_DefaultNumber(self, p):
        """ DefaultNumber       : empty
                                | EQUAL Number
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """
        if p[1] is None:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_Description(self, p):
        """ Description         : empty
                                | COLON String
        """
        if p[1] is None:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_FloatRange(self, p):
        """ FloatRange          : empty
                                | LBRACKET Float TO Float RBRACKET
        """
        if p[1] is None:
            p[0] = p[1]
        else:
            p[0] = oil_ast.FloatRange(p[2], p[4])


    def p_DefaultFloat(self, p):
        """ DefaultFloat        : empty
                                | EQUAL Float
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """
        if p[1] is None:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_Enumeration(self, p):
        """ Enumeration         : LBRACKET EnumerationList RBRACKET
        """
        p[0] = oil_ast.Enumeration(p[2])


    def p_EnumerationList(self, p):
        """ EnumerationList     : Enumerator
                                | EnumerationList COMMA Enumerator
        """
        p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

    def p_Enumerator(self, p):
        """ Enumerator          : Name Description
                                | Name ImplParameterList Description
        """
        if len(p) == 3:
            p[0] = oil_ast.Enumerator(p[1], [], p[2])
        else:
            p[0] = oil_ast.Enumerator(p[1], p[2], p[3])

    def p_BoolValues(self, p):
        """ BoolValues          : empty
                                | LBRACKET TRUE ImplParameterList Description COMMA FALSE ImplParameterList Description RBRACKET
        """
        if p[1] is None:
            p[0] = p[1]
        else:
            p[0] = oil_ast.BoolValues(p[3], p[4], p[7], p[8])

    def p_DefaultName(self, p):
        """ DefaultName         : empty
                                | EQUAL Name
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """
        if p[1] is None:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_DefaultString(self, p):
        """ DefaultString       : empty
                                | EQUAL String
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """
        if p[1] is None:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_DefaultBool(self, p):
        """ DefaultBool         : empty
                                | EQUAL Boolean
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """
        if p[1] is None:
            p[0] = p[1]
        else:
            p[0] = p[2]

    def p_ImplRefDef(self, p):
        """ ImplRefDef  : ObjectRefType ReferenceName MultipleSpecifier Description SEMI
        """
        p[0] = oil_ast.ImplRefDef(p[1], p[2], p[3], p[4])

    def p_ObjectRefType(self, p):
        """ ObjectRefType   : OS_TYPE
                            | TASK_TYPE
                            | COUNTER_TYPE
                            | ALARM_TYPE
                            | RESOURCE_TYPE
                            | EVENT_TYPE
                            | ISR_TYPE
                            | MESSAGE_TYPE
                            | COM_TYPE
                            | NM_TYPE
                            | APPMODE_TYPE
                            | IPDU_TYPE
        """
        p[0] = p[1]

    def p_ReferenceName(self, p):
        """ ReferenceName   : Name
                            | Object
        """
        p[0] = p[1]

    def p_MultipleSpecifier(self, p):
        """ MultipleSpecifier   : empty
                                | LBRACKET RBRACKET
        """
        if p[1] is None:
            p[0] = p[1]
        else:
            p[0] = '[]'

    def p_ApplicationDefinition(self, p):
        """ ApplicationDefinition   : CPU Name LBRACE ObjectDefinitionList RBRACE Description SEMI
        """
        p[0] = oil_ast.ApplicationDefinition(p[2], p[4], p[6])

    def p_ObjectDefinitionList(self, p):
        """ ObjectDefinitionList    : empty
                                    | ObjectDefinition
                                    | ObjectDefinitionList ObjectDefinition
        """
        if p[1] == None:
            p[0] = []
        else:
            p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

    def p_ObjectDefinition(self, p):
        """ ObjectDefinition        : ObjectName Description SEMI
                                    | ObjectName LBRACE ParameterList RBRACE Description SEMI
        """
        if len(p) == 4:
            p[0] = oil_ast.ObjectDefinition(p[1], None, p[2])
        else:
            p[0] = oil_ast.ObjectDefinition(p[1], p[3], p[5])


    def p_ObjectName(self, p):
        """ ObjectName              : Object Name
        """
        p[0] = oil_ast.ObjectName(p[1], p[2])


    def p_ParameterList(self, p):
        """ ParameterList           : empty
                                    | Parameter
                                    | ParameterList Parameter
        """
        if p[1] == None:
            p[0] = []
        else:
            p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

    def p_Parameter(self, p):
        """ Parameter               : AttributeName EQUAL AttributeValue Description SEMI
        """
        p[0] = oil_ast.Parameter(p[1], p[3], p[4])


    def p_AttributeName(self, p):
        """ AttributeName           : Name
                                    | Object
        """
        p[0] = p[1]


    def p_AttributeValue(self, p):
        """ AttributeValue          : Name
                                    | Name LBRACE ParameterList RBRACE
                                    | Boolean
                                    | Boolean LBRACE ParameterList RBRACE
                                    | Number
                                    | Float
                                    | String
                                    | AUTO
        """
        if len(p) == 2:
            p[0] = oil_ast.AttributeValue(p[1], None)
        else:
            p[0] = oil_ast.AttributeValue(p[1], p[3])

    def p_Name(self, p):
        """ Name                    : IDENT
        """
        p[0] = p[1]

    def p_String(self, p):
        """ String                  : STRING_LITERAL
        """
        p[0] = p[1]

    def p_Boolean(self, p):
        """ Boolean                 : FALSE
                                    | TRUE
        """
        p[0] = p[1]

    def p_Number(self, p):
        """ Number                  : DecNumber
                                    | HexNumber
        """
        p[0] = p[1]

    def p_DecNumber(self, p):
        """ DecNumber               : Sign CONST_DEC
        """
        p[0] = p[1] + p[2]

    def p_Sign(self, p):
        """ Sign                    : empty
                                    | PLUS
                                    | MINUS
        """
        if p[1] is None:
            p[0] = ''
        else:
            p[0] = p[1]

    def p_Float(self, p):
        """ Float       : Sign FLOATING_CONSTANT
        """
        p[0] = p[1] + p[2]

    def p_HexNumber(self, p):
        """ HexNumber    : CONST_HEX
        """
        p[0] = p[1]

    def p_empty(self, p):
        'empty : '
        p[0] = None

    def p_error(self, p):
        raise TypeError("unknown text at %r" % (p.value,))


def parse_file(filename):
    with open(filename) as f:
        text = f.read()
        parser = OILParser()
        return parser.parse(text, filename)

if __name__ == '__main__':
    import sys, json
    result = parse_file(sys.argv[1])
    result.show( nodenames=True)
