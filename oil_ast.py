import sys


class Node():
    def children(self):
        pass

    def show(self, buf=sys.stdout, offset=0, nodenames=False, _my_node_name=None):
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


        for (child_name, child) in self.children():
            if child is not None:
                if hasattr(child, 'show'):
                    child.show(
                        buf,
                        offset=offset + 2,
                        nodenames=nodenames,
                        _my_node_name=child_name)
                else:
                    buf.write(str(child) + '\n')

class File(Node):
    def __init__(self, version, implementationDefinition, applicationDefinition):
        self.version = version
        self.implementationDefinition = implementationDefinition
        self.applicationDefinition = applicationDefinition

    def children(self):
        nodelist = []
        nodelist.append(("version", self.version))
        nodelist.append(("implementationDefinition", self.implementationDefinition))
        nodelist.append(("applicationDefinition", self.applicationDefinition))
        return tuple(nodelist)


class OilVersion(Node):
    def __init__(self, version, description):
        self.version = version
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append(("version", self.version))
        nodelist.append(("description", self.description))
        return tuple(nodelist)


class ImplementationDefinition(Node):
    def __init__(self, name, implementationSpecList, description):
        self.name = name
        self.implementationSpecList = implementationSpecList
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append(("name", self.name))
        for i, child in enumerate(self.implementationSpecList or []):
            nodelist.append(("implementationSpecList[%s]" % i, child))
        nodelist.append(("description", self.description))
        return tuple(nodelist)


class ImplementationSpec(Node):
    def __init__(self, object, implementationList, description):
        self.object = object
        self.implementationList = implementationList
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append(("object", self.object))
        if self.implementationList is None:
            nodelist.append(("implementationList", None))
        else:
            for i, child in enumerate(self.implementationList or []):
                nodelist.append(("implementationList[%s]" % i, child))
        nodelist.append(("description", self.description))
        return tuple(nodelist)

class ImplAttrDef(Node):
    def __init__(self, type, autoSpecifier, range, attributeName, multipleSpecifier, default, description):
        self.type = type
        self.autoSpecifier = autoSpecifier
        self.range = range
        self.attributeName = attributeName
        self.multipleSpecifier = multipleSpecifier
        self.default = default
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append(("type", self.type))
        nodelist.append(("autoSpecifier", self.autoSpecifier))
        nodelist.append(("range", self.range))
        nodelist.append(("attributeName", self.attributeName))
        nodelist.append(("multipleSpecifier", self.multipleSpecifier))
        nodelist.append(("default", self.default))
        nodelist.append(("description", self.description))
        return tuple(nodelist)

class NumberRange(Node):
    def __init__(self, type, left=None, right=None, numberList=[]):
        self.type = type
        self.left = left
        self.right = right
        self.numberList = numberList

    def children(self):
        nodelist = []
        if self.type == 0:
            nodelist.append(("type", "range"))
            nodelist.append(("left", self.left))
            nodelist.append(("right", self.right))
        else:
            nodelist.append(("type", "list"))
            for i, child in enumerate(self.numberList or []):
                nodelist.append(("numberList[%s]" % i, child))
        return tuple(nodelist)


class FloatRange(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def children(self):
        nodelist = []
        nodelist.append(("type", "range"))
        nodelist.append(("left", self.left))
        nodelist.append(("right", self.right))
        return tuple(nodelist)


class Enumeration(Node):
    def __init__(self, enumerationList):
        self.enumerationList = enumerationList

    def children(self):
        nodelist = []
        for i, child in enumerate(self.enumerationList or []):
            nodelist.append(("enumerationList[%s]" % i, child))
        return tuple(nodelist)


class Enumerator(Node):
    def __init__(self, name, implParameterList, description):
        self.name = name
        self.implParameterList = implParameterList
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append(("name", self.name))
        for i, child in enumerate(self.implParameterList or []):
            nodelist.append(("implParameterList[%s]" % i, child))
        nodelist.append(("description", self.description))
        return tuple(nodelist)

class BoolValues(Node):
    def __init__(self, tImplParameterList, tDescription, fImplParameterList, fDescription):
        self.tImplParameterList = tImplParameterList
        self.tDescription = tDescription
        self.fImplParameterList = fImplParameterList
        self.fDescription = fDescription

    def children(self):
        nodelist = []
        for i, child in enumerate(self.tImplParameterList or []):
            nodelist.append(("tImplParameterList[%s]" % i, child))
        nodelist.append(("tDescription", self.tDescription))
        for i, child in enumerate(self.fImplParameterList or []):
            nodelist.append(("fImplParameterList[%s]" % i, child))
        nodelist.append(("fDescription", self.fDescription))
        return tuple(nodelist)


class ImplRefDef(Node):
    def __init__(self, objectRefType, referenceName, multipleSpecifier, description):
        self.objectRefType    = objectRefType
        self.referenceName    = referenceName
        self.multipleSpecifier    = multipleSpecifier
        self.description    = description

    def children(self):
        nodelist = []
        nodelist.append(("objectRefType", self.objectRefType))
        nodelist.append(("referenceName", self.referenceName))
        nodelist.append(("multipleSpecifier", self.multipleSpecifier))
        nodelist.append(("description", self.description))
        return tuple(nodelist)


class ApplicationDefinition(Node):
    def __init__(self, name, objectDefinitionList, description):
        self.name = name
        self.objectDefinitionList = objectDefinitionList
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append(("name", self.name))
        for i, child in enumerate(self.objectDefinitionList or []):
            nodelist.append(("objectDefinitionList[%s]" % i, child))
        nodelist.append(("description", self.description))
        return tuple(nodelist)


class ObjectDefinition(Node):
    def __init__(self, objectName, parameterList, description):
        self.objectName = objectName
        self.parameterList = parameterList
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append(("objectName", self.objectName))
        for i, child in enumerate(self.parameterList or []):
            nodelist.append(("parameterList[%s]" % i, child))
        nodelist.append(("description", self.description))
        return tuple(nodelist)


class ObjectName(Node):
    def __init__(self, object, name):
        self.object = object
        self.name = name

    def children(self):
        nodelist = []
        nodelist.append(("object", self.object))
        nodelist.append(("name", self.name))
        return tuple(nodelist)


class Parameter(Node):
    def __init__(self, attributeName, attributeValue, description):
        self.attributeName = attributeName
        self.attributeValue = attributeValue
        self.description = description

    def children(self):
        nodelist = []
        nodelist.append(("attributeName", self.attributeName))
        nodelist.append(("attributeValue", self.attributeValue))
        nodelist.append(("description", self.description))
        return tuple(nodelist)


class AttributeValue(Node):
    def __init__(self, value, parameterList):
        self.value = value
        self.parameterList = parameterList

    def children(self):
        nodelist = []
        nodelist.append(("value", self.value))
        for i, child in enumerate(self.parameterList or []):
            nodelist.append(("parameterList[%s]" % i, child))
        return tuple(nodelist)

