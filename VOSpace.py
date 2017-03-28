# ./VOSpace.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4c3801b46e497ed6f2ec64e895b47b5d5a83cd60
# Generated 2017-02-16 16:44:50.490579 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace http://www.ivoa.net/xml/VOSpace/v2.1

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d9b46e22-f45e-11e6-8de3-f8b156cc69f4')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.ivoa.net/xml/VOSpace/v2.1', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.anyURI):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 533, 12)
    _Documentation = None
STD_ANON._InitializeFacetMap()
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 536, 12)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.pushToVoSpace = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='pushToVoSpace', tag='pushToVoSpace')
STD_ANON_.pushFromVoSpace = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='pushFromVoSpace', tag='pushFromVoSpace')
STD_ANON_.pullToVoSpace = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='pullToVoSpace', tag='pullToVoSpace')
STD_ANON_.pullFromVoSpace = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='pullFromVoSpace', tag='pullFromVoSpace')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Union simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_2 (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON, STD_ANON_."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 531, 8)
    _Documentation = None

    _MemberTypes = ( STD_ANON, STD_ANON_, )
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2)
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2.pushToVoSpace = 'pushToVoSpace'        # originally STD_ANON_.pushToVoSpace
STD_ANON_2.pushFromVoSpace = 'pushFromVoSpace'    # originally STD_ANON_.pushFromVoSpace
STD_ANON_2.pullToVoSpace = 'pullToVoSpace'        # originally STD_ANON_.pullToVoSpace
STD_ANON_2.pullFromVoSpace = 'pullFromVoSpace'    # originally STD_ANON_.pullFromVoSpace
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration,
   STD_ANON_2._CF_pattern)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}Node with content type ELEMENT_ONLY
class Node (pyxb.binding.basis.complexTypeDefinition):
    """
        The base class for all nodes.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Node')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 11, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}properties uses Python identifier properties
    __properties = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'properties'), 'properties', '__httpwww_ivoa_netxmlVOSpacev2_1_Node_httpwww_ivoa_netxmlVOSpacev2_1properties', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6), )

    
    properties = property(__properties.value, __properties.set, None, '\n            The list of node properties.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpwww_ivoa_netxmlVOSpacev2_1_Node_uri', pyxb.binding.datatypes.anyURI, required=True)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 26, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 26, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The node identifier URI.\n        ')

    _ElementMap.update({
        __properties.name() : __properties
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
_module_typeBindings.Node = Node
Namespace.addCategoryObject('typeBinding', 'Node', Node)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
                A list of the direct children that the container has.
              """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 124, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}node uses Python identifier node
    __node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'node'), 'node', '__httpwww_ivoa_netxmlVOSpacev2_1_CTD_ANON_httpwww_ivoa_netxmlVOSpacev2_1node', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 126, 16), )

    
    node = property(__node.value, __node.set, None, None)

    _ElementMap.update({
        __node.name() : __node
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}Property with content type SIMPLE
class Property (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}Property with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Property')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 158, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpwww_ivoa_netxmlVOSpacev2_1_Property_uri', pyxb.binding.datatypes.anyURI, required=True)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 198, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 198, 4)
    
    uri = property(__uri.value, __uri.set, None, '                    \n            If the property has been registered, then the URI should point to the registration document. Third party \n            tools may use the urn:xxxx syntax to add unregistered properties.\n        ')

    
    # Attribute readOnly uses Python identifier readOnly
    __readOnly = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'readOnly'), 'readOnly', '__httpwww_ivoa_netxmlVOSpacev2_1_Property_readOnly', pyxb.binding.datatypes.boolean, unicode_default='false')
    __readOnly._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 206, 4)
    __readOnly._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 206, 4)
    
    readOnly = property(__readOnly.value, __readOnly.set, None, '\n          A flag to indicate if the property is considered read-only. Attempting to modify a read-only property\n          should generate a PermissionDenied fault.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __readOnly.name() : __readOnly
    })
_module_typeBindings.Property = Property
Namespace.addCategoryObject('typeBinding', 'Property', Property)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}PropertyList with content type ELEMENT_ONLY
class PropertyList (pyxb.binding.basis.complexTypeDefinition):
    """
        A container element for a list of properties.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyList')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 166, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'property'), 'property_', '__httpwww_ivoa_netxmlVOSpacev2_1_PropertyList_httpwww_ivoa_netxmlVOSpacev2_1property', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 173, 6), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PropertyList = PropertyList
Namespace.addCategoryObject('typeBinding', 'PropertyList', PropertyList)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}PropertyReference with content type EMPTY
class PropertyReference (pyxb.binding.basis.complexTypeDefinition):
    """
        A reference to a property description.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyReference')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 177, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpwww_ivoa_netxmlVOSpacev2_1_PropertyReference_uri', pyxb.binding.datatypes.anyURI, required=True)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 198, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 198, 4)
    
    uri = property(__uri.value, __uri.set, None, '                    \n            If the property has been registered, then the URI should point to the registration document. Third party \n            tools may use the urn:xxxx syntax to add unregistered properties.\n        ')

    
    # Attribute readOnly uses Python identifier readOnly
    __readOnly = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'readOnly'), 'readOnly', '__httpwww_ivoa_netxmlVOSpacev2_1_PropertyReference_readOnly', pyxb.binding.datatypes.boolean, unicode_default='false')
    __readOnly._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 206, 4)
    __readOnly._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 206, 4)
    
    readOnly = property(__readOnly.value, __readOnly.set, None, '\n          A flag to indicate if the property is considered read-only. Attempting to modify a read-only property\n          should generate a PermissionDenied fault.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __readOnly.name() : __readOnly
    })
_module_typeBindings.PropertyReference = PropertyReference
Namespace.addCategoryObject('typeBinding', 'PropertyReference', PropertyReference)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}PropertyReferenceList with content type ELEMENT_ONLY
class PropertyReferenceList (pyxb.binding.basis.complexTypeDefinition):
    """
        A container element for a list of property references.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PropertyReferenceList')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 186, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'property'), 'property_', '__httpwww_ivoa_netxmlVOSpacev2_1_PropertyReferenceList_httpwww_ivoa_netxmlVOSpacev2_1property', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 193, 6), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.PropertyReferenceList = PropertyReferenceList
Namespace.addCategoryObject('typeBinding', 'PropertyReferenceList', PropertyReferenceList)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}GetPropertiesResponse with content type ELEMENT_ONLY
class GetPropertiesResponse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}GetPropertiesResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetPropertiesResponse')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 225, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}accepts uses Python identifier accepts
    __accepts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accepts'), 'accepts', '__httpwww_ivoa_netxmlVOSpacev2_1_GetPropertiesResponse_httpwww_ivoa_netxmlVOSpacev2_1accepts', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 227, 6), )

    
    accepts = property(__accepts.value, __accepts.set, None, '\n            A list of identifiers for the properties that the service accepts and understands.\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}provides uses Python identifier provides
    __provides = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'provides'), 'provides', '__httpwww_ivoa_netxmlVOSpacev2_1_GetPropertiesResponse_httpwww_ivoa_netxmlVOSpacev2_1provides', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 234, 6), )

    
    provides = property(__provides.value, __provides.set, None, '\n            A list of identifiers for the properties that the service provides.\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}contains uses Python identifier contains
    __contains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'contains'), 'contains', '__httpwww_ivoa_netxmlVOSpacev2_1_GetPropertiesResponse_httpwww_ivoa_netxmlVOSpacev2_1contains', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 241, 6), )

    
    contains = property(__contains.value, __contains.set, None, '\n            A list of identifiers for all the properties currently used by nodes within the service.\n          ')

    _ElementMap.update({
        __accepts.name() : __accepts,
        __provides.name() : __provides,
        __contains.name() : __contains
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetPropertiesResponse = GetPropertiesResponse
Namespace.addCategoryObject('typeBinding', 'GetPropertiesResponse', GetPropertiesResponse)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}Param with content type SIMPLE
class Param (pyxb.binding.basis.complexTypeDefinition):
    """
        A view or protocol parameter.
      """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Param')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 253, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpwww_ivoa_netxmlVOSpacev2_1_Param_uri', pyxb.binding.datatypes.anyURI, required=True)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 261, 8)
    __uri._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 261, 8)
    
    uri = property(__uri.value, __uri.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
_module_typeBindings.Param = Param
Namespace.addCategoryObject('typeBinding', 'Param', Param)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}View with content type ELEMENT_ONLY
class View (pyxb.binding.basis.complexTypeDefinition):
    """
        An element describing a view of a data-set.
        A view may just provide the original data, or it could be server generated.
        Examples of server generated views could include a votable view of data in a database table,
        or a conversion from one image format to another.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'View')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 266, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'param'), 'param', '__httpwww_ivoa_netxmlVOSpacev2_1_View_httpwww_ivoa_netxmlVOSpacev2_1param', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 276, 6), )

    
    param = property(__param.value, __param.set, None, '\n            A list of parameters for the view.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpwww_ivoa_netxmlVOSpacev2_1_View_uri', pyxb.binding.datatypes.anyURI, required=True)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 284, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 284, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The view URI.\n          This should point to a resource describing the view format and what parameters it requires.\n        ')

    
    # Attribute original uses Python identifier original
    __original = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'original'), 'original', '__httpwww_ivoa_netxmlVOSpacev2_1_View_original', pyxb.binding.datatypes.boolean, unicode_default='true')
    __original._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 292, 4)
    __original._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 292, 4)
    
    original = property(__original.value, __original.set, None, '\n          A flag to indicate if the view provides access to the original data content or a derived form.\n        ')

    _ElementMap.update({
        __param.name() : __param
    })
    _AttributeMap.update({
        __uri.name() : __uri,
        __original.name() : __original
    })
_module_typeBindings.View = View
Namespace.addCategoryObject('typeBinding', 'View', View)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}ViewList with content type ELEMENT_ONLY
class ViewList (pyxb.binding.basis.complexTypeDefinition):
    """
        A container element for a list of views.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ViewList')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 301, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}view uses Python identifier view
    __view = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'view'), 'view', '__httpwww_ivoa_netxmlVOSpacev2_1_ViewList_httpwww_ivoa_netxmlVOSpacev2_1view', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 308, 6), )

    
    view = property(__view.value, __view.set, None, None)

    _ElementMap.update({
        __view.name() : __view
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ViewList = ViewList
Namespace.addCategoryObject('typeBinding', 'ViewList', ViewList)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}GetViewsResponse with content type ELEMENT_ONLY
class GetViewsResponse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}GetViewsResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetViewsResponse')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 312, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}accepts uses Python identifier accepts
    __accepts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accepts'), 'accepts', '__httpwww_ivoa_netxmlVOSpacev2_1_GetViewsResponse_httpwww_ivoa_netxmlVOSpacev2_1accepts', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 314, 6), )

    
    accepts = property(__accepts.value, __accepts.set, None, "\n            A list of identifiers for the views that the service can accept.\n            A simple file based system may accept data in 'any' format. \n          ")

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}provides uses Python identifier provides
    __provides = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'provides'), 'provides', '__httpwww_ivoa_netxmlVOSpacev2_1_GetViewsResponse_httpwww_ivoa_netxmlVOSpacev2_1provides', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 322, 6), )

    
    provides = property(__provides.value, __provides.set, None, '\n            A list of identifiers for the views that the service can provide.\n            A simple file based system may only provide data in the original format.\n          ')

    _ElementMap.update({
        __accepts.name() : __accepts,
        __provides.name() : __provides
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetViewsResponse = GetViewsResponse
Namespace.addCategoryObject('typeBinding', 'GetViewsResponse', GetViewsResponse)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}Protocol with content type ELEMENT_ONLY
class Protocol (pyxb.binding.basis.complexTypeDefinition):
    """
        A protocol element, containing the protocol URI, the endpoint and any protocol specific parameters.  
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Protocol')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 335, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}endpoint uses Python identifier endpoint
    __endpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endpoint'), 'endpoint', '__httpwww_ivoa_netxmlVOSpacev2_1_Protocol_httpwww_ivoa_netxmlVOSpacev2_1endpoint', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 342, 6), )

    
    endpoint = property(__endpoint.value, __endpoint.set, None, '\n            The target endpoint to use for a data transfer.\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'param'), 'param', '__httpwww_ivoa_netxmlVOSpacev2_1_Protocol_httpwww_ivoa_netxmlVOSpacev2_1param', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 349, 6), )

    
    param = property(__param.value, __param.set, None, '\n            Any additional protocol specific parameters required to use the endpoint.\n            For example, the user name or password to use for ftp access.\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}securityMethod uses Python identifier securityMethod
    __securityMethod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'securityMethod'), 'securityMethod', '__httpwww_ivoa_netxmlVOSpacev2_1_Protocol_httpwww_ivoa_netxmlVOSpacev2_1securityMethod', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 357, 6), )

    
    securityMethod = property(__securityMethod.value, __securityMethod.set, None, '\n            the mechanism the client must employ to gain secure access to the service.  \n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpwww_ivoa_netxmlVOSpacev2_1_Protocol_uri', pyxb.binding.datatypes.anyURI, required=True)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 365, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 365, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The protocol identifier.\n        ')

    _ElementMap.update({
        __endpoint.name() : __endpoint,
        __param.name() : __param,
        __securityMethod.name() : __securityMethod
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
_module_typeBindings.Protocol = Protocol
Namespace.addCategoryObject('typeBinding', 'Protocol', Protocol)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}SecurityMethod with content type EMPTY
class SecurityMethod (pyxb.binding.basis.complexTypeDefinition):
    """
        a description of a security mechanism.
      
        this type only allows one to refer to the mechanism via a
        URI.  Derived types would allow for more metadata.  
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SecurityMethod')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 374, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpwww_ivoa_netxmlVOSpacev2_1_SecurityMethod_uri', pyxb.binding.datatypes.anyURI)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 384, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 384, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          A URI identifier for a standard security mechanism. \n        \n          This provides a unique way to refer to a security\n          specification standard.\n        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
_module_typeBindings.SecurityMethod = SecurityMethod
Namespace.addCategoryObject('typeBinding', 'SecurityMethod', SecurityMethod)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}ProtocolList with content type ELEMENT_ONLY
class ProtocolList (pyxb.binding.basis.complexTypeDefinition):
    """
        A container element for a list of protocols.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProtocolList')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 397, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'protocol'), 'protocol', '__httpwww_ivoa_netxmlVOSpacev2_1_ProtocolList_httpwww_ivoa_netxmlVOSpacev2_1protocol', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 404, 6), )

    
    protocol = property(__protocol.value, __protocol.set, None, None)

    _ElementMap.update({
        __protocol.name() : __protocol
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ProtocolList = ProtocolList
Namespace.addCategoryObject('typeBinding', 'ProtocolList', ProtocolList)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}GetProtocolsResponse with content type ELEMENT_ONLY
class GetProtocolsResponse (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}GetProtocolsResponse with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GetProtocolsResponse')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 408, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}accepts uses Python identifier accepts
    __accepts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accepts'), 'accepts', '__httpwww_ivoa_netxmlVOSpacev2_1_GetProtocolsResponse_httpwww_ivoa_netxmlVOSpacev2_1accepts', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 410, 6), )

    
    accepts = property(__accepts.value, __accepts.set, None, '\n            A list of identifiers for the protocols that the service can accept.\n            This means that the service can act as a client for the protocol. \n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}provides uses Python identifier provides
    __provides = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'provides'), 'provides', '__httpwww_ivoa_netxmlVOSpacev2_1_GetProtocolsResponse_httpwww_ivoa_netxmlVOSpacev2_1provides', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 418, 6), )

    
    provides = property(__provides.value, __provides.set, None, '\n            A list of identifiers for the protocols that the service can provide.\n            This means that the service can act as a server for the protocol. \n          ')

    _ElementMap.update({
        __accepts.name() : __accepts,
        __provides.name() : __provides
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GetProtocolsResponse = GetProtocolsResponse
Namespace.addCategoryObject('typeBinding', 'GetProtocolsResponse', GetProtocolsResponse)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}Capability with content type ELEMENT_ONLY
class Capability (pyxb.binding.basis.complexTypeDefinition):
    """
        A capability element, containing the capability URI, the
    endpoint and any capability specific parameters(?).
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Capability')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 431, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}endpoint uses Python identifier endpoint
    __endpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endpoint'), 'endpoint', '__httpwww_ivoa_netxmlVOSpacev2_1_Capability_httpwww_ivoa_netxmlVOSpacev2_1endpoint', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 439, 6), )

    
    endpoint = property(__endpoint.value, __endpoint.set, None, '\n            The target endpoint to use for the third-part interface.\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'param'), 'param', '__httpwww_ivoa_netxmlVOSpacev2_1_Capability_httpwww_ivoa_netxmlVOSpacev2_1param', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 449, 6), )

    
    param = property(__param.value, __param.set, None, '\n            Any additional capability specific parameters required to use the endpoint.\n            For example, the user name or password to use for access.\n          ')

    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uri'), 'uri', '__httpwww_ivoa_netxmlVOSpacev2_1_Capability_uri', pyxb.binding.datatypes.anyURI, required=True)
    __uri._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 458, 4)
    __uri._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 458, 4)
    
    uri = property(__uri.value, __uri.set, None, '\n          The capability identifier.\n        ')

    _ElementMap.update({
        __endpoint.name() : __endpoint,
        __param.name() : __param
    })
    _AttributeMap.update({
        __uri.name() : __uri
    })
_module_typeBindings.Capability = Capability
Namespace.addCategoryObject('typeBinding', 'Capability', Capability)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}CapabilityList with content type ELEMENT_ONLY
class CapabilityList (pyxb.binding.basis.complexTypeDefinition):
    """
        A container element for a list of capabilities.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CapabilityList')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 467, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}capability uses Python identifier capability
    __capability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'capability'), 'capability', '__httpwww_ivoa_netxmlVOSpacev2_1_CapabilityList_httpwww_ivoa_netxmlVOSpacev2_1capability', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 474, 6), )

    
    capability = property(__capability.value, __capability.set, None, None)

    _ElementMap.update({
        __capability.name() : __capability
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CapabilityList = CapabilityList
Namespace.addCategoryObject('typeBinding', 'CapabilityList', CapabilityList)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}NodeList with content type ELEMENT_ONLY
class NodeList (pyxb.binding.basis.complexTypeDefinition):
    """
        A container element for search responses.
    """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'NodeList')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 480, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}nodes uses Python identifier nodes
    __nodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nodes'), 'nodes', '__httpwww_ivoa_netxmlVOSpacev2_1_NodeList_httpwww_ivoa_netxmlVOSpacev2_1nodes', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 487, 6), )

    
    nodes = property(__nodes.value, __nodes.set, None, '\n            The list of nodes.\n          ')

    _ElementMap.update({
        __nodes.name() : __nodes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.NodeList = NodeList
Namespace.addCategoryObject('typeBinding', 'NodeList', NodeList)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """
            The list of nodes.
          """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 493, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}node uses Python identifier node
    __node = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'node'), 'node', '__httpwww_ivoa_netxmlVOSpacev2_1_CTD_ANON__httpwww_ivoa_netxmlVOSpacev2_1node', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 495, 12), )

    
    node = property(__node.value, __node.set, None, '\n                  At the maximum level of detail this will be replaced by the full element for the extended type,\n                 using xsi:type to indicate the node type/\n                ')

    _ElementMap.update({
        __node.name() : __node
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}Transfer with content type ELEMENT_ONLY
class Transfer (pyxb.binding.basis.complexTypeDefinition):
    """
        A container element for transfer operations.
    """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Transfer')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 511, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}target uses Python identifier target
    __target = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'target'), 'target', '__httpwww_ivoa_netxmlVOSpacev2_1_Transfer_httpwww_ivoa_netxmlVOSpacev2_1target', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 518, 6), )

    
    target = property(__target.value, __target.set, None, '\n            The target of a transfer operation - the node to/from which data is to be transferred.\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}direction uses Python identifier direction
    __direction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'direction'), 'direction', '__httpwww_ivoa_netxmlVOSpacev2_1_Transfer_httpwww_ivoa_netxmlVOSpacev2_1direction', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 525, 6), )

    
    direction = property(__direction.value, __direction.set, None, '\n            The direction of a data transfer - either a URI or one of the specified directions\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}view uses Python identifier view
    __view = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'view'), 'view', '__httpwww_ivoa_netxmlVOSpacev2_1_Transfer_httpwww_ivoa_netxmlVOSpacev2_1view', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 547, 6), )

    
    view = property(__view.value, __view.set, None, '\n            The requested view for the transfer.\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}protocol uses Python identifier protocol
    __protocol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'protocol'), 'protocol', '__httpwww_ivoa_netxmlVOSpacev2_1_Transfer_httpwww_ivoa_netxmlVOSpacev2_1protocol', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 554, 6), )

    
    protocol = property(__protocol.value, __protocol.set, None, '\n            The transfer protocol(s) to use.\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}keepBytes uses Python identifier keepBytes
    __keepBytes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'keepBytes'), 'keepBytes', '__httpwww_ivoa_netxmlVOSpacev2_1_Transfer_httpwww_ivoa_netxmlVOSpacev2_1keepBytes', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 561, 6), )

    
    keepBytes = property(__keepBytes.value, __keepBytes.set, None, '\n            Indicates whether the source object is to be kept in an internal transfer, i.e., distinguishes between a move and a copy.\n          ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'param'), 'param', '__httpwww_ivoa_netxmlVOSpacev2_1_Transfer_httpwww_ivoa_netxmlVOSpacev2_1param', True, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 568, 6), )

    
    param = property(__param.value, __param.set, None, '\n              Any additional transfer specific parameters required to use the endpoint.\n              For example, the size of the file on a pushToVoSpace transfer.\n            ')

    _ElementMap.update({
        __target.name() : __target,
        __direction.name() : __direction,
        __view.name() : __view,
        __protocol.name() : __protocol,
        __keepBytes.name() : __keepBytes,
        __param.name() : __param
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Transfer = Transfer
Namespace.addCategoryObject('typeBinding', 'Transfer', Transfer)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode with content type ELEMENT_ONLY
class DataNode (Node):
    """
        The base class for data nodes.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DataNode')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 35, 2)
    _ElementMap = Node._ElementMap.copy()
    _AttributeMap = Node._AttributeMap.copy()
    # Base type is Node
    
    # Element properties ({http://www.ivoa.net/xml/VOSpace/v2.1}properties) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}accepts uses Python identifier accepts
    __accepts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'accepts'), 'accepts', '__httpwww_ivoa_netxmlVOSpacev2_1_DataNode_httpwww_ivoa_netxmlVOSpacev2_1accepts', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10), )

    
    accepts = property(__accepts.value, __accepts.set, None, '\n                The list of views or data formats that this node can accept.\n                A simple unstructured node may accept data in any format.\n                A structured node may only accept data in specific formats. \n              ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}provides uses Python identifier provides
    __provides = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'provides'), 'provides', '__httpwww_ivoa_netxmlVOSpacev2_1_DataNode_httpwww_ivoa_netxmlVOSpacev2_1provides', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10), )

    
    provides = property(__provides.value, __provides.set, None, '\n                The list of views or data formats that this node can provide.\n                A simple unstructured node may only provide access to the data in the original format.\n                A structured node may provide different views of the data generated by the service.\n              ')

    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}capabilities uses Python identifier capabilities
    __capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'capabilities'), 'capabilities', '__httpwww_ivoa_netxmlVOSpacev2_1_DataNode_httpwww_ivoa_netxmlVOSpacev2_1capabilities', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10), )

    
    capabilities = property(__capabilities.value, __capabilities.set, None, '\n                The list of capabilities that this node can support. \n              ')

    
    # Attribute uri inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    
    # Attribute busy uses Python identifier busy
    __busy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'busy'), 'busy', '__httpwww_ivoa_netxmlVOSpacev2_1_DataNode_busy', pyxb.binding.datatypes.boolean, unicode_default='false')
    __busy._DeclarationLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 70, 8)
    __busy._UseLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 70, 8)
    
    busy = property(__busy.value, __busy.set, None, '\n              A flag to indicate if the node content is available.\n              This will be set to false while the data is being imported,\n              or if the underlying service is busy.\n            ')

    _ElementMap.update({
        __accepts.name() : __accepts,
        __provides.name() : __provides,
        __capabilities.name() : __capabilities
    })
    _AttributeMap.update({
        __busy.name() : __busy
    })
_module_typeBindings.DataNode = DataNode
Namespace.addCategoryObject('typeBinding', 'DataNode', DataNode)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}LinkNode with content type ELEMENT_ONLY
class LinkNode (Node):
    """
        A node that points to another resource.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LinkNode')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 135, 2)
    _ElementMap = Node._ElementMap.copy()
    _AttributeMap = Node._AttributeMap.copy()
    # Base type is Node
    
    # Element properties ({http://www.ivoa.net/xml/VOSpace/v2.1}properties) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}target uses Python identifier target
    __target = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'target'), 'target', '__httpwww_ivoa_netxmlVOSpacev2_1_LinkNode_httpwww_ivoa_netxmlVOSpacev2_1target', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 144, 10), )

    
    target = property(__target.value, __target.set, None, '\n                The identifier for the object that the LinkNode points to.\n              ')

    
    # Attribute uri inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    _ElementMap.update({
        __target.name() : __target
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LinkNode = LinkNode
Namespace.addCategoryObject('typeBinding', 'LinkNode', LinkNode)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}UnstructuredDataNode with content type ELEMENT_ONLY
class UnstructuredDataNode (DataNode):
    """
        An unstructured data node, containing unspecified content.
        The service does not need to understand or interpret the content.
        This type of node can accept any format, and only provides one view returning the original data.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UnstructuredDataNode')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 83, 2)
    _ElementMap = DataNode._ElementMap.copy()
    _AttributeMap = DataNode._AttributeMap.copy()
    # Base type is DataNode
    
    # Element properties ({http://www.ivoa.net/xml/VOSpace/v2.1}properties) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    
    # Element accepts ({http://www.ivoa.net/xml/VOSpace/v2.1}accepts) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    
    # Element provides ({http://www.ivoa.net/xml/VOSpace/v2.1}provides) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    
    # Element capabilities ({http://www.ivoa.net/xml/VOSpace/v2.1}capabilities) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    
    # Attribute uri inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    
    # Attribute busy inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UnstructuredDataNode = UnstructuredDataNode
Namespace.addCategoryObject('typeBinding', 'UnstructuredDataNode', UnstructuredDataNode)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}StructuredDataNode with content type ELEMENT_ONLY
class StructuredDataNode (DataNode):
    """
        A structured data node, containing a specific data format that the service has understands.
        This type of node may only accept specific data formats, and provide different views of the
        data generated by the service. 
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StructuredDataNode')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 96, 2)
    _ElementMap = DataNode._ElementMap.copy()
    _AttributeMap = DataNode._AttributeMap.copy()
    # Base type is DataNode
    
    # Element properties ({http://www.ivoa.net/xml/VOSpace/v2.1}properties) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    
    # Element accepts ({http://www.ivoa.net/xml/VOSpace/v2.1}accepts) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    
    # Element provides ({http://www.ivoa.net/xml/VOSpace/v2.1}provides) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    
    # Element capabilities ({http://www.ivoa.net/xml/VOSpace/v2.1}capabilities) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    
    # Attribute uri inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    
    # Attribute busy inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.StructuredDataNode = StructuredDataNode
Namespace.addCategoryObject('typeBinding', 'StructuredDataNode', StructuredDataNode)


# Complex type {http://www.ivoa.net/xml/VOSpace/v2.1}ContainerNode with content type ELEMENT_ONLY
class ContainerNode (DataNode):
    """
        A container node containing any type of node.
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContainerNode')
    _XSDLocation = pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 109, 2)
    _ElementMap = DataNode._ElementMap.copy()
    _AttributeMap = DataNode._AttributeMap.copy()
    # Base type is DataNode
    
    # Element properties ({http://www.ivoa.net/xml/VOSpace/v2.1}properties) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    
    # Element accepts ({http://www.ivoa.net/xml/VOSpace/v2.1}accepts) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    
    # Element provides ({http://www.ivoa.net/xml/VOSpace/v2.1}provides) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    
    # Element capabilities ({http://www.ivoa.net/xml/VOSpace/v2.1}capabilities) inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    
    # Element {http://www.ivoa.net/xml/VOSpace/v2.1}nodes uses Python identifier nodes
    __nodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nodes'), 'nodes', '__httpwww_ivoa_netxmlVOSpacev2_1_ContainerNode_httpwww_ivoa_netxmlVOSpacev2_1nodes', False, pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 118, 10), )

    
    nodes = property(__nodes.value, __nodes.set, None, '\n                A list of the direct children that the container has.\n              ')

    
    # Attribute uri inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}Node
    
    # Attribute busy inherited from {http://www.ivoa.net/xml/VOSpace/v2.1}DataNode
    _ElementMap.update({
        __nodes.name() : __nodes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ContainerNode = ContainerNode
Namespace.addCategoryObject('typeBinding', 'ContainerNode', ContainerNode)


protocols = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'protocols'), ProtocolList, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 581, 2))
Namespace.addCategoryObject('elementBinding', protocols.name().localName(), protocols)

views = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'views'), ViewList, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 583, 2))
Namespace.addCategoryObject('elementBinding', views.name().localName(), views)

properties = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'properties'), PropertyList, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 585, 2))
Namespace.addCategoryObject('elementBinding', properties.name().localName(), properties)

transfer = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transfer'), Transfer, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 587, 2))
Namespace.addCategoryObject('elementBinding', transfer.name().localName(), transfer)

searchDetails = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searchDetails'), NodeList, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 589, 2))
Namespace.addCategoryObject('elementBinding', searchDetails.name().localName(), searchDetails)



Node._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'properties'), PropertyList, scope=Node, documentation='\n            The list of node properties.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Node._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'properties')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Node._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'node'), Node, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 126, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 126, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'node')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 126, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




PropertyList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'property'), Property, nillable=pyxb.binding.datatypes.boolean(1), scope=PropertyList, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 173, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 173, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PropertyList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'property')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 173, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PropertyList._Automaton = _BuildAutomaton_2()




PropertyReferenceList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'property'), PropertyReference, nillable=pyxb.binding.datatypes.boolean(1), scope=PropertyReferenceList, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 193, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 193, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PropertyReferenceList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'property')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 193, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PropertyReferenceList._Automaton = _BuildAutomaton_3()




GetPropertiesResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accepts'), PropertyReferenceList, scope=GetPropertiesResponse, documentation='\n            A list of identifiers for the properties that the service accepts and understands.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 227, 6)))

GetPropertiesResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'provides'), PropertyReferenceList, scope=GetPropertiesResponse, documentation='\n            A list of identifiers for the properties that the service provides.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 234, 6)))

GetPropertiesResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'contains'), PropertyReferenceList, scope=GetPropertiesResponse, documentation='\n            A list of identifiers for all the properties currently used by nodes within the service.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 241, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetPropertiesResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accepts')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 227, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetPropertiesResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'provides')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 234, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetPropertiesResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'contains')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 241, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetPropertiesResponse._Automaton = _BuildAutomaton_4()




View._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'param'), Param, nillable=pyxb.binding.datatypes.boolean(1), scope=View, documentation='\n            A list of parameters for the view.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 276, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 276, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(View._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'param')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 276, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
View._Automaton = _BuildAutomaton_5()




ViewList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'view'), View, nillable=pyxb.binding.datatypes.boolean(1), scope=ViewList, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 308, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 308, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ViewList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'view')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 308, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ViewList._Automaton = _BuildAutomaton_6()




GetViewsResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accepts'), ViewList, scope=GetViewsResponse, documentation="\n            A list of identifiers for the views that the service can accept.\n            A simple file based system may accept data in 'any' format. \n          ", location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 314, 6)))

GetViewsResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'provides'), ViewList, scope=GetViewsResponse, documentation='\n            A list of identifiers for the views that the service can provide.\n            A simple file based system may only provide data in the original format.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 322, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetViewsResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accepts')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 314, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetViewsResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'provides')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 322, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetViewsResponse._Automaton = _BuildAutomaton_7()




Protocol._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endpoint'), pyxb.binding.datatypes.anyURI, scope=Protocol, documentation='\n            The target endpoint to use for a data transfer.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 342, 6)))

Protocol._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'param'), Param, nillable=pyxb.binding.datatypes.boolean(1), scope=Protocol, documentation='\n            Any additional protocol specific parameters required to use the endpoint.\n            For example, the user name or password to use for ftp access.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 349, 6)))

Protocol._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityMethod'), SecurityMethod, nillable=pyxb.binding.datatypes.boolean(1), scope=Protocol, documentation='\n            the mechanism the client must employ to gain secure access to the service.  \n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 357, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 342, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 349, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 357, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Protocol._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endpoint')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 342, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Protocol._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'param')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 349, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Protocol._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'securityMethod')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 357, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Protocol._Automaton = _BuildAutomaton_8()




ProtocolList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'protocol'), Protocol, nillable=pyxb.binding.datatypes.boolean(1), scope=ProtocolList, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 404, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 404, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProtocolList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'protocol')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 404, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProtocolList._Automaton = _BuildAutomaton_9()




GetProtocolsResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accepts'), ProtocolList, scope=GetProtocolsResponse, documentation='\n            A list of identifiers for the protocols that the service can accept.\n            This means that the service can act as a client for the protocol. \n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 410, 6)))

GetProtocolsResponse._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'provides'), ProtocolList, scope=GetProtocolsResponse, documentation='\n            A list of identifiers for the protocols that the service can provide.\n            This means that the service can act as a server for the protocol. \n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 418, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GetProtocolsResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accepts')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 410, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GetProtocolsResponse._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'provides')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 418, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GetProtocolsResponse._Automaton = _BuildAutomaton_10()




Capability._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endpoint'), pyxb.binding.datatypes.anyURI, scope=Capability, documentation='\n            The target endpoint to use for the third-part interface.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 439, 6)))

Capability._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'param'), Param, nillable=pyxb.binding.datatypes.boolean(1), scope=Capability, documentation='\n            Any additional capability specific parameters required to use the endpoint.\n            For example, the user name or password to use for access.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 449, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 439, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 449, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Capability._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endpoint')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 439, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Capability._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'param')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 449, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Capability._Automaton = _BuildAutomaton_11()




CapabilityList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'capability'), Capability, nillable=pyxb.binding.datatypes.boolean(1), scope=CapabilityList, location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 474, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 474, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CapabilityList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'capability')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 474, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CapabilityList._Automaton = _BuildAutomaton_12()




NodeList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nodes'), CTD_ANON_, scope=NodeList, documentation='\n            The list of nodes.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 487, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 487, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NodeList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nodes')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 487, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NodeList._Automaton = _BuildAutomaton_13()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'node'), Node, scope=CTD_ANON_, documentation='\n                  At the maximum level of detail this will be replaced by the full element for the extended type,\n                 using xsi:type to indicate the node type/\n                ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 495, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 495, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'node')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 495, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_14()




Transfer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'target'), pyxb.binding.datatypes.anyURI, scope=Transfer, documentation='\n            The target of a transfer operation - the node to/from which data is to be transferred.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 518, 6)))

Transfer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'direction'), STD_ANON_2, scope=Transfer, documentation='\n            The direction of a data transfer - either a URI or one of the specified directions\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 525, 6)))

Transfer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'view'), View, scope=Transfer, documentation='\n            The requested view for the transfer.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 547, 6)))

Transfer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'protocol'), Protocol, scope=Transfer, documentation='\n            The transfer protocol(s) to use.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 554, 6)))

Transfer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'keepBytes'), pyxb.binding.datatypes.boolean, scope=Transfer, documentation='\n            Indicates whether the source object is to be kept in an internal transfer, i.e., distinguishes between a move and a copy.\n          ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 561, 6)))

Transfer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'param'), Param, nillable=pyxb.binding.datatypes.boolean(1), scope=Transfer, documentation='\n              Any additional transfer specific parameters required to use the endpoint.\n              For example, the size of the file on a pushToVoSpace transfer.\n            ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 568, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 525, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 547, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 554, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 561, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 568, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Transfer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'target')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 518, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Transfer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'direction')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 525, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Transfer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'view')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 547, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Transfer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'protocol')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 554, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Transfer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'keepBytes')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 561, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Transfer._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'param')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 568, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Transfer._Automaton = _BuildAutomaton_15()




DataNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'accepts'), ViewList, scope=DataNode, documentation='\n                The list of views or data formats that this node can accept.\n                A simple unstructured node may accept data in any format.\n                A structured node may only accept data in specific formats. \n              ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10)))

DataNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'provides'), ViewList, scope=DataNode, documentation='\n                The list of views or data formats that this node can provide.\n                A simple unstructured node may only provide access to the data in the original format.\n                A structured node may provide different views of the data generated by the service.\n              ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10)))

DataNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'capabilities'), CapabilityList, scope=DataNode, documentation='\n                The list of capabilities that this node can support. \n              ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'properties')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accepts')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'provides')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'capabilities')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DataNode._Automaton = _BuildAutomaton_16()




LinkNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'target'), pyxb.binding.datatypes.anyURI, scope=LinkNode, documentation='\n                The identifier for the object that the LinkNode points to.\n              ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 144, 10)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LinkNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'properties')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LinkNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'target')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 144, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LinkNode._Automaton = _BuildAutomaton_17()




def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UnstructuredDataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'properties')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UnstructuredDataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accepts')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UnstructuredDataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'provides')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UnstructuredDataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'capabilities')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UnstructuredDataNode._Automaton = _BuildAutomaton_18()




def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StructuredDataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'properties')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StructuredDataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accepts')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StructuredDataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'provides')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(StructuredDataNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'capabilities')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StructuredDataNode._Automaton = _BuildAutomaton_19()




ContainerNode._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nodes'), CTD_ANON, scope=ContainerNode, documentation='\n                A list of the direct children that the container has.\n              ', location=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 118, 10)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContainerNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'properties')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 18, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContainerNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'accepts')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 44, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContainerNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'provides')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 53, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ContainerNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'capabilities')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 62, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ContainerNode._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nodes')), pyxb.utils.utility.Location('/home/bouchair/Bureau/VOSpace-2.1.xsd', 118, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ContainerNode._Automaton = _BuildAutomaton_20()

