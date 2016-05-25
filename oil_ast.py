

class Node():
    def children(self):
        pass

    def show(self, buf=sys.stdout, offset=0, attrnames=False, nodenames=False, _my_node_name=None):
        """ Pretty print the Node and all its attributes and
            children (recursively) to a buffer.

            buf:
                Open IO buffer into which the Node is printed.

            offset:
                Initial offset (amount of leading spaces)

            attrnames:
                True if you want to see the attribute names in
                name=value pairs. False to only see the values.

            nodenames:
                True if you want to see the actual node names
                within their parents.

        """
        lead = ' ' * offset
        if nodenames and _my_node_name is not None:
            buf.write(lead + self.__class__.__name__+ ' <' + _my_node_name + '>: ')
        else:
            buf.write(lead + self.__class__.__name__+ ': ')

        if self.attr_names:
            if attrnames:
                nvlist = [(n, getattr(self,n)) for n in self.attr_names]
                attrstr = ', '.join('%s=%s' % nv for nv in nvlist)
            else:
                vlist = [getattr(self, n) for n in self.attr_names]
                attrstr = ', '.join('%s' % v for v in vlist)
            buf.write(attrstr)

        for (child_name, child) in self.children():
            child.show(
                buf,
                offset=offset + 2,
                attrnames=attrnames,
                nodenames=nodenames,
                _my_node_name=child_name)

class File(Node):
    def __init__(self, version, implementationDefinition, applicationDefinition):
        self.version = version
        self.implementationDefinition = implementationDefinition
        self.applicationDefinition = applicationDefinition

    def children(self):
        nodelist = []
        nodelist.append("version", self.version)
        nodelist.append("implementationDefinition", self.implementationDefinition)
        nodelist.append("applicationDefinition", self.applicationDefinition)
        return tuple(nodelist)

    attr_names = ()


class OilVersion(Node):
    def __init__(self, version, description):
        self.version = version
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append("version", self.version)
        nodelist.append("description", self.description)
        return tuple(nodelist)

    attr_names = ()

class ImplementationDefinition(Node):
    def __init__(self, name, implementationSpecList, description):
        self.name = name
        self.implementationSpecList = implementationSpecList
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append("version", self.version)
        nodelist.append("description", self.description)
        return tuple(nodelist)

    attr_names = ()

class ImplementationSpec(Node):
    def __init__(self, object, implementationList, description):
        self.object = object
        self.implementationList = implementationList
        self.description = description


class ImplAttrDef(Node):
    def __init__(self, type, autoSpecifier, range, attributeName, multipleSpecifier, default, description):
        self.type = type
        self.autoSpecifier = autoSpecifier
        self.range = range
        self.attributeName = attributeName
        self.multipleSpecifier = multipleSpecifier
        self.default = default
        self.description = description


class NumberRange(Node):
    def __init__(self, type, left=None, right=None, numberList=[]):
        self.type = type
        self.left = left
        self.right = right
        self.numberList = numberList

class FloatRange(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Enumeration(Node):
    def __init__(self, enumerationList):
        self.enumerationList = enumerationList


class Enumerator(Node):
    def __init__(self, name, implParameterList, description):
        self.name = name
        self.implParameterList = implParameterList
        self.description = description

class BoolValues(Node):
    def __init__(self, tImplParameterList, tDescription, fImplParameterList, fDescription):
        self.tImplParameterList = tImplParameterList
        self.fImplParameterList = fImplParameterList
        self.tDescription = tDescription
        self.fDescription = fDescription


class ImplRefDef(Node):
    def __init__(self, objectRefType, referenceName, multipleSpecifier, description):
        self.objectRefType    = objectRefType
        self.referenceName    = referenceName
        self.multipleSpecifier    = multipleSpecifier
        self.description    = description


class ApplicationDefinition(Node):
    def __init__(self, name, objectDefinitionList, description):
        self.name = name
        self.objectDefinitionList = objectDefinitionList
        self.description = description


class ObjectDefinition(Node):
    def __init__(self, objectName, parameterList, description):
        self.objectName = objectName
        self.parameterList = parameterList
        self.description = description


class ObjectName(Node):
    def __init__(self, object, name):
        self.object = object
        self.name = name


class Parameter(Node):
    def __init__(self, attributeName, attributeValue, description):
        self.attributeName = attributeName
        self.attributeValue = attributeValue
        self.description = description


class AttributeValue(Node):
    def __init__(self, value, parameterList):
        self.value = value
        self.parameterList = parameterList
