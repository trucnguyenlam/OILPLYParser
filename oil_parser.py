

from ply import lex, yacc
from lex import TOKEN


######     #    #######    #
#     #   # #      #      # #
#     #  #   #     #     #   #
#     # #     #    #    #     #
#     # #######    #    #######
#     # #     #    #    #     #
######  #     #    #    #     #


class OIL:
    ''' Definition of OIL file
    '''

    def __init__(self):
        self.version = ""
        self.implementationDef = {}
        self.applicationDef = {}


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
        'LCBRACKET',
        'LBRACKET',
        'RCBRACKET'
        'RBRACKET'
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
        'TO',                      # ..
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
        'MINUS'
    )


    t_FALSE = r'FALSE'



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
        """ ImplementationDefinition :  IMPLEMENTATION Name LCBRACKET ImplementationSpecList RCBRACKET Description SEMI
        """

    def p_ImplementationSpecList(self, p):
        """ ImplementationSpecList : ImplementationSpec
                                   | ImplementationSpecList ImplementationSpec
        """

    def p_ImplementationSpec(self, p):
        """ ImplementationSpec : Object LCBRACKET ImplementationList RCBRACKET Description SEMI
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
                                | LCBRACKET ImplDefList RCBRACKET
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
        """ ApplicationDefinition   : CPU Name LCBRACKET ObjectDefinitionList RCBRACKET Description SEMI
        """

    def p_ObjectDefinitionList(self, p):
        """ ObjectDefinitionList    : empty
                                    | ObjectDefinition
                                    | ObjectDefinitionList ObjectDefinition
        """

    def p_ObjectDefinition(self, p):
        """ ObjectDefinition        : ObjectName Description SEMI
                                    | ObjectName LCBRACKET ParameterList RCBRACKET Description SEMI
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
                                    | Name LCBRACKET ParameterList RCBRACKET
                                    | Boolean
                                    | Boolean LCBRACKET ParameterList RCBRACKET
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
        """ IntDigits               :
        """


    def p_empty(self, p):
        'empty : '
        p[0] = None

    def p_error(p):
        raise TypeError("unknown text at %r" % (p.value,))

# yacc.yacc()

# ######

# import collections


# def atom_count(s):
#     """calculates the total number of atoms in the chemical equation
#     >>> atom_count("H2SO4")
#     7
#     >>>
#     """
#     count = 0
#     for atom in yacc.parse(s):
#         count += atom.count
#     return count


# def element_counts(s):
#     """calculates counts for each element in the chemical equation
#     >>> element_counts("CH3COOH")["C"]
#     2
#     >>> element_counts("CH3COOH")["H"]
#     4
#     >>>
#     """

#     counts = collections.defaultdict(int)
#     for atom in yacc.parse(s):
#         counts[atom.symbol] += atom.count
#     return counts

# ######


# def assert_raises(exc, f, *args):
#     try:
#         f(*args)
#     except exc:
#         pass
#     else:
#         raise AssertionError("Expected %r" % (exc,))


# def test_element_counts():
#     assert element_counts("CH3COOH") == {"C": 2, "H": 4, "O": 2}
#     assert element_counts("Ne") == {"Ne": 1}
#     assert element_counts("") == {}
#     assert element_counts("NaCl") == {"Na": 1, "Cl": 1}
#     assert_raises(TypeError, element_counts, "Blah")
#     assert_raises(TypeError, element_counts, "10")
#     assert_raises(TypeError, element_counts, "1C")


# def test_atom_count():
#     assert atom_count("He") == 1
#     assert atom_count("H2") == 2
#     assert atom_count("H2SO4") == 7
#     assert atom_count("CH3COOH") == 8
#     assert atom_count("NaCl") == 2
#     assert atom_count("C60H60") == 120
#     assert_raises(TypeError, atom_count, "SeZYou")
#     assert_raises(TypeError, element_counts, "10")
#     assert_raises(TypeError, element_counts, "1C")


# def test():
#     test_atom_count()
#     test_element_counts()

# if __name__ == "__main__":
#     test()
#     print "All tests passed."
