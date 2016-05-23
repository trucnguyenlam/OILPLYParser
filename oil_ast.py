

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
