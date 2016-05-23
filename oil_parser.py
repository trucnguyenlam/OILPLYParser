

from ply import lex, yacc
from lex import TOKEN


######     #    ######   #####  ####### ######
#     #   # #   #     # #     # #       #     #
#     #  #   #  #     # #       #       #     #
######  #     # ######   #####  #####   ######
#       ####### #   #         # #       #   #
#       #     # #    #  #     # #       #    #
#       #     # #     #  #####  ####### #     #


class OILParser():
    def __init__(self):
        pass

    def p_File(self, p):
        """ File : OilVersion ImplementationDefinition ApplicationDefinition
        """

    def p_OilVersion(self, p):
        """ OilVersion : OIL_VERSION EQUAL Version Description SEMI
        """

    def p_Version(self, p):
        """ Version : STRING """

    def p_ImplementationDefinition(self, p):
        """ ImplementationDefinition :  IMPLEMENTATION Name LBRACE ImplementationSpecList RBRACE Description SEMI
        """

    def p_ImplementationSpecList(self, p):
        """ ImplementationSpecList : ImplementationSpec
                                   | ImplementationSpecList ImplementationSpec
        """

    def p_ImplementationSpec(self, p):
        """ ImplementationSpec : Object LBRACE ImplementationList RBRACE Description SEMI
        """

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

    def p_ImplementationList(self, p):
        """ ImplementationList : empty
                               | ImplementationDef
                               | ImplementationList ImplementationDef
        """

    def p_ImplementationDef(self, p):
        """ ImplementationDef : ImplAttrDef
                              | ImplRefDef
        """


    def p_ImplAttrDef(self, p):
        """ ImplAttrDef : UINT32 AutoSpecifier NumberRange AttributeName MultipleSpecifier DefaultNumber Description SEMI
                        | INT32 AutoSpecifier NumberRange AttributeName MultipleSpecifier DefaultNumber Description SEMI
                        | UINT64 AutoSpecifier NumberRange AttributeName MultipleSpecifier DefaultNumber Description SEMI
                        | INT64 AutoSpecifier NumberRange AttributeName MultipleSpecifier DefaultNumber Description SEMI
                        | FLOAT AutoSpecifier FloatRange AttributeName MultipleSpecifier DefaultFloat Description SEMI
                        | ENUM AutoSpecifier Enumeration AttributeName MultipleSpecifier DefaultName Description SEMI
                        | STRING AutoSpecifier AttributeName MultipleSpecifier DefaultString Description SEMI
                        | BOOLEAN AutoSpecifier BoolValues AttributeName MultipleSpecifier DefaultBool Description SEMI
        """

    def p_ImplParameterList(self, p):
        """ ImplParameterList   : empty
                                | LBRACE ImplDefList RBRACE
        """

    def p_ImplDefList(self, p):
        """ ImplDefList         : empty
                                | ImplementationDef ImplDefList
        """

    def p_AutoSpecifier(self, p):
        """ AutoSpecifier       : empty
                                | WITH_AUTO
        """

    def p_NumberRange(self, p):
        """ NumberRange         : empty
                                | LBRACKET Number TO Number RBRACKET
                                | LBRACKET NumberList RBRACKET
        """

    def p_NumberList(self, p):
        """ NumberList          : Number
                                | NumberList COMMA Number
        """

    def p_DefaultNumber(self, p):
        """ DefaultNumber       : empty
                                | EQUAL Number
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """

    def p_Description(self, p):
        """ Description         : empty
                                | COLON STRING
        """

    def p_FloatRange(self, p):
        """ FloatRange          : empty
                                | LBRACKET Float TO Float RBRACKET
        """

    def p_DefaultFloat(self, p):
        """ DefaultFloat        : empty
                                | EQUAL Float
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """

    def p_Enumeration(self, p):
        """ Enumeration         : LBRACKET EnumerationList RBRACKET
        """

    def p_EnumerationList(self, p):
        """ EnumerationList     : Enumerator
                                | EnumerationList COMMA Enumerator
        """

    def p_Enumerator(self, p):
        """ Enumerator          : Name Description
                                | Name ImplParameterList Description
        """

    def p_BoolValues(self, p):
        """ BoolValues          : empty
                                | LBRACKET TRUE ImplParameterList Description COMMA FALSE ImplParameterList Description RBRACKET
        """

    def p_DefaultName(self, p):
        """ DefaultName         : empty
                                | EQUAL STRING
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """

    def p_DefaultString(self, p):
        """ DefaultString       : empty
                                | EQUAL STRING
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """

    def p_DefaultBool(self, p):
        """ DefaultBool         : empty
                                | EQUAL Boolean
                                | EQUAL NO_DEFAULT
                                | EQUAL AUTO
        """

    def p_ImplRefDef(self, p):
        """ ImplRefDef  : ObjectRefType ReferenceName MultipleSpecifier Description SEMI
        """

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

    def p_ReferenceName(self, p):
        """ ReferenceName   : Name
                            | Object
        """

    def p_MultipleSpecifier(self, p):
        """ MultipleSpecifier   : empty
                                | LBRACKET RBRACKET
        """

    def p_ApplicationDefinition(self, p):
        """ ApplicationDefinition   : CPU Name LBRACE ObjectDefinitionList RBRACE Description SEMI
        """

    def p_ObjectDefinitionList(self, p):
        """ ObjectDefinitionList    : empty
                                    | ObjectDefinition
                                    | ObjectDefinitionList ObjectDefinition
        """

    def p_ObjectDefinition(self, p):
        """ ObjectDefinition        : ObjectName Description SEMI
                                    | ObjectName LBRACE ParameterList RBRACE Description SEMI
        """

    def p_ObjectName(self, p):
        """ ObjectName              : Object Name
        """

    def p_ParameterList(self, p):
        """ ParameterList           : empty
                                    | Parameter
                                    | ParameterList Parameter
        """

    def p_Parameter(self, p):
        """ Parameter               : AttributeName EQUAL AttributeValue Description SEMI
        """

    def p_AttributeName(self, p):
        """ AttributeName           : Name
                                    | Object
        """

    def p_AttributeValue(self, p):
        """ AttributeValue          : Name
                                    | Name LBRACE ParameterList RBRACE
                                    | Boolean
                                    | Boolean LBRACE ParameterList RBRACE
                                    | Number
                                    | Float
                                    | STRING
                                    | AUTO
        """

    def p_Name(self, p):
        """ Name                    : NAME
        """

    def p_String(self, p):
        """ String                  : STRING
        """

    def p_Boolean(self, p):
        """ Boolean                 : FALSE | TRUE
        """

    def p_Number(self, p):
        """ Number                  : DecNumber | HexNumber
        """

    def p_DecNumber(self, p):
        """ DecNumber               : Sign IntDigits
        """

    def p_Sign(self, p):
        """ Sign                    : empty
                                    | PLUS
                                    | MINUS
        """

    def p_IntDigits(self, p):
        """ IntDigits               : ZeroDigit
                                    | PosDigit
                                    | PosDigit DecDigits
        """

    def p_DecDigits(self, p):
        """ DecDigits               : DecDigit
                                    | DecDigit DecDigits
        """

    def p_Float(self, p):
        """ Float       : Sign DecDigits DOT DecDigits Exponent
        """

    def p_Exponent(self, p):
        """ Exponent    : empty
                        | 'e' Sign DecDigits
                        | 'E' Sign DecDigits
        """

    def p_ZeroDigit(self, p):
        """ ZeroDigit   : '0'
        """

    def p_PosDigit(self, p):
        """ PosDigit    : '1'
                        | '2'
                        | '3'
                        | '4'
                        | '5'
                        | '6'
                        | '7'
                        | '8'
                        | '9'
        """

    def p_DecDigit(self, p):
        """ DecDigit    : ZeroDigit
                        | PosDigit
        """

    def p_HexNumber(self, p):
        """ HexNumer    : PREFIX HexDigits
        """

    def p_HexDigits(self, p):
        """ HexDigits   : HexDigit
                        | HexDigit HexDigits
        """

    def p_HexDigit(self, p):
        """ HexDigit    : 'A' | 'a'
                        | 'B' | 'b'
                        | 'C' | 'c'
                        | 'D' | 'd'
                        | 'E' | 'e'
                        | 'F' | 'f'
                        | '0'
                        | '1'
                        | '2'
                        | '3'
                        | '4'
                        | '5'
                        | '6'
                        | '7'
                        | '8'
                        | '9'
        """

    def p_empty(self, p):
        'empty : '
        p[0] = None

    def p_error(p):
        raise TypeError("unknown text at %r" % (p.value,))

