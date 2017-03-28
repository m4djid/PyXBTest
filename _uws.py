# ./_uws.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f6614354ce2e10bfcb5388e2172e50c712e28faf
# Generated 2017-02-16 16:44:50.491057 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace http://www.ivoa.net/xml/UWS/v1.0 [xmlns:uws]

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
import _xlink as _ImportedBinding__xlink

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.ivoa.net/xml/UWS/v1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xlink = _ImportedBinding__xlink.Namespace
_Namespace_xlink.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.ivoa.net/xml/UWS/v1.0}ExecutionPhase
class ExecutionPhase (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """ Enumeration of possible phases of job
            execution"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExecutionPhase')
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 48, 3)
    _Documentation = ' Enumeration of possible phases of job\n            execution'
ExecutionPhase._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ExecutionPhase, enum_prefix=None)
ExecutionPhase.PENDING = ExecutionPhase._CF_enumeration.addEnumeration(unicode_value='PENDING', tag='PENDING')
ExecutionPhase.QUEUED = ExecutionPhase._CF_enumeration.addEnumeration(unicode_value='QUEUED', tag='QUEUED')
ExecutionPhase.EXECUTING = ExecutionPhase._CF_enumeration.addEnumeration(unicode_value='EXECUTING', tag='EXECUTING')
ExecutionPhase.COMPLETED = ExecutionPhase._CF_enumeration.addEnumeration(unicode_value='COMPLETED', tag='COMPLETED')
ExecutionPhase.ERROR = ExecutionPhase._CF_enumeration.addEnumeration(unicode_value='ERROR', tag='ERROR')
ExecutionPhase.UNKNOWN = ExecutionPhase._CF_enumeration.addEnumeration(unicode_value='UNKNOWN', tag='UNKNOWN')
ExecutionPhase.HELD = ExecutionPhase._CF_enumeration.addEnumeration(unicode_value='HELD', tag='HELD')
ExecutionPhase.SUSPENDED = ExecutionPhase._CF_enumeration.addEnumeration(unicode_value='SUSPENDED', tag='SUSPENDED')
ExecutionPhase.ABORTED = ExecutionPhase._CF_enumeration.addEnumeration(unicode_value='ABORTED', tag='ABORTED')
ExecutionPhase._InitializeFacetMap(ExecutionPhase._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ExecutionPhase', ExecutionPhase)
_module_typeBindings.ExecutionPhase = ExecutionPhase

# Atomic simple type: {http://www.ivoa.net/xml/UWS/v1.0}JobIdentifier
class JobIdentifier (pyxb.binding.datatypes.string):

    """ The identifier for the job
         """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JobIdentifier')
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 214, 3)
    _Documentation = ' The identifier for the job\n         '
JobIdentifier._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'JobIdentifier', JobIdentifier)
_module_typeBindings.JobIdentifier = JobIdentifier

# Atomic simple type: {http://www.ivoa.net/xml/UWS/v1.0}ErrorType
class ErrorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErrorType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 290, 3)
    _Documentation = None
ErrorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ErrorType, enum_prefix=None)
ErrorType.transient = ErrorType._CF_enumeration.addEnumeration(unicode_value='transient', tag='transient')
ErrorType.fatal = ErrorType._CF_enumeration.addEnumeration(unicode_value='fatal', tag='fatal')
ErrorType._InitializeFacetMap(ErrorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ErrorType', ErrorType)
_module_typeBindings.ErrorType = ErrorType

# Complex type {http://www.ivoa.net/xml/UWS/v1.0}JobSummary with content type ELEMENT_ONLY
class JobSummary (pyxb.binding.basis.complexTypeDefinition):
    """The complete representation of the state
            of a job"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'JobSummary')
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 112, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}jobId uses Python identifier jobId
    __jobId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'jobId'), 'jobId', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0jobId', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 118, 9), )

    
    jobId = property(__jobId.value, __jobId.set, None, None)

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}runId uses Python identifier runId
    __runId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'runId'), 'runId', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0runId', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 119, 9), )

    
    runId = property(__runId.value, __runId.set, None, ' this is a client supplied identifier -\n                  the UWS system does nothing other than to return it as\n                  part of the description of the job')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}ownerId uses Python identifier ownerId
    __ownerId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ownerId'), 'ownerId', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0ownerId', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 128, 9), )

    
    ownerId = property(__ownerId.value, __ownerId.set, None, 'the owner (creator) of the job -\n                  this should be expressed as a string that can be\n                  parsed in accordance with IVOA security standards. If\n                  there was no authenticated job creator then this\n                  should be set to NULL.')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}phase uses Python identifier phase
    __phase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phase'), 'phase', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0phase', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 139, 9), )

    
    phase = property(__phase.value, __phase.set, None, ' the execution phase - returned at\n                  /(jobs)/(jobid)/phase')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}quote uses Python identifier quote
    __quote = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'quote'), 'quote', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0quote', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 145, 9), )

    
    quote = property(__quote.value, __quote.set, None, ' A Quote predicts when the job is likely to complete - returned at /(jobs)/(jobid)/quote\n                  "don\'t know" is encoded by setting to the XML null value xsi:nil="true"')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}startTime uses Python identifier startTime
    __startTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'startTime'), 'startTime', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0startTime', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 153, 9), )

    
    startTime = property(__startTime.value, __startTime.set, None, 'The instant at which the job started execution.')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}endTime uses Python identifier endTime
    __endTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endTime'), 'endTime', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0endTime', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 158, 9), )

    
    endTime = property(__endTime.value, __endTime.set, None, 'The instant at which the job finished execution')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}executionDuration uses Python identifier executionDuration
    __executionDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'executionDuration'), 'executionDuration', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0executionDuration', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 163, 9), )

    
    executionDuration = property(__executionDuration.value, __executionDuration.set, None, ' The duration (in seconds) for which\n                  the job should be allowed to run - a value of 0 is\n                  intended to mean unlimited - returned at\n                  /(jobs)/(jobid)/executionduration')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}destruction uses Python identifier destruction
    __destruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'destruction'), 'destruction', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0destruction', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 174, 9), )

    
    destruction = property(__destruction.value, __destruction.set, None, ' The time at which the whole job +\n                  records + results will be destroyed. returned at\n                  /(jobs)/(jobid)/destruction')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}errorSummary uses Python identifier errorSummary
    __errorSummary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errorSummary'), 'errorSummary', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0errorSummary', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 195, 9), )

    
    errorSummary = property(__errorSummary.value, __errorSummary.set, None, None)

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}jobInfo uses Python identifier jobInfo
    __jobInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'jobInfo'), 'jobInfo', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0jobInfo', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 199, 9), )

    
    jobInfo = property(__jobInfo.value, __jobInfo.set, None, ' This is arbitrary information that can\n                  be added to the job description by the UWS\n                  implementation.')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}results uses Python identifier results
    __results = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'results'), 'results', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0results', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 255, 3), )

    
    results = property(__results.value, __results.set, None, ' The element returned for\n            /(jobs)/(jobid)/results')

    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}parameters uses Python identifier parameters
    __parameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameters'), 'parameters', '__httpwww_ivoa_netxmlUWSv1_0_JobSummary_httpwww_ivoa_netxmlUWSv1_0parameters', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 327, 3), )

    
    parameters = property(__parameters.value, __parameters.set, None, None)

    _ElementMap.update({
        __jobId.name() : __jobId,
        __runId.name() : __runId,
        __ownerId.name() : __ownerId,
        __phase.name() : __phase,
        __quote.name() : __quote,
        __startTime.name() : __startTime,
        __endTime.name() : __endTime,
        __executionDuration.name() : __executionDuration,
        __destruction.name() : __destruction,
        __errorSummary.name() : __errorSummary,
        __jobInfo.name() : __jobInfo,
        __results.name() : __results,
        __parameters.name() : __parameters
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.JobSummary = JobSummary
Namespace.addCategoryObject('typeBinding', 'JobSummary', JobSummary)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """ This is arbitrary information that can
                  be added to the job description by the UWS
                  implementation."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 205, 12)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """ ISSUE - do we want to have any sort of
               paging or selection mechanism in case the job list gets
               very large? Or is that an unnecessary complication...
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 233, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}jobref uses Python identifier jobref
    __jobref = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'jobref'), 'jobref', '__httpwww_ivoa_netxmlUWSv1_0_CTD_ANON__httpwww_ivoa_netxmlUWSv1_0jobref', True, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 241, 12), )

    
    jobref = property(__jobref.value, __jobref.set, None, None)

    _ElementMap.update({
        __jobref.name() : __jobref
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """ The element returned for
            /(jobs)/(jobid)/results"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 260, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__httpwww_ivoa_netxmlUWSv1_0_CTD_ANON_2_httpwww_ivoa_netxmlUWSv1_0result', True, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 262, 12), )

    
    result = property(__result.value, __result.set, None, None)

    _ElementMap.update({
        __result.name() : __result
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type {http://www.ivoa.net/xml/UWS/v1.0}Parameter with content type MIXED
class Parameter (pyxb.binding.basis.complexTypeDefinition):
    """ the list of input parameters to the job - if
            the job description language does not naturally have
            parameters, then this list should contain one element which
            is the content of the original POST that created the job.
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Parameter')
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 296, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute byReference uses Python identifier byReference
    __byReference = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'byReference'), 'byReference', '__httpwww_ivoa_netxmlUWSv1_0_Parameter_byReference', pyxb.binding.datatypes.boolean, unicode_default='false')
    __byReference._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 304, 6)
    __byReference._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 304, 6)
    
    byReference = property(__byReference.value, __byReference.set, None, ' if this attribute is true then the\n               content of the parameter represents a URL to retrieve the\n               actual parameter value. It is up to the implementation to decide\n               if a parameter value cannot be returned directly as the\n               content - the basic rule is that the representation of\n               the parameter must allow the whole job element to be\n               valid XML. If this cannot be achieved then the parameter\n               value must be returned by reference.')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_ivoa_netxmlUWSv1_0_Parameter_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 319, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 319, 6)
    
    id = property(__id.value, __id.set, None, ' the identifier for the parameter\n            ')

    
    # Attribute isPost uses Python identifier isPost
    __isPost = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isPost'), 'isPost', '__httpwww_ivoa_netxmlUWSv1_0_Parameter_isPost', pyxb.binding.datatypes.boolean)
    __isPost._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 325, 6)
    __isPost._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 325, 6)
    
    isPost = property(__isPost.value, __isPost.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __byReference.name() : __byReference,
        __id.name() : __id,
        __isPost.name() : __isPost
    })
_module_typeBindings.Parameter = Parameter
Namespace.addCategoryObject('typeBinding', 'Parameter', Parameter)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 328, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}parameter uses Python identifier parameter
    __parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'parameter'), 'parameter', '__httpwww_ivoa_netxmlUWSv1_0_CTD_ANON_3_httpwww_ivoa_netxmlUWSv1_0parameter', True, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 330, 12), )

    
    parameter = property(__parameter.value, __parameter.set, None, None)

    _ElementMap.update({
        __parameter.name() : __parameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type {http://www.ivoa.net/xml/UWS/v1.0}ShortJobDescription with content type ELEMENT_ONLY
class ShortJobDescription (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ivoa.net/xml/UWS/v1.0}ShortJobDescription with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ShortJobDescription')
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 27, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}phase uses Python identifier phase
    __phase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phase'), 'phase', '__httpwww_ivoa_netxmlUWSv1_0_ShortJobDescription_httpwww_ivoa_netxmlUWSv1_0phase', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 29, 9), )

    
    phase = property(__phase.value, __phase.set, None, ' the execution phase - returned at\n                  /(jobs)/(jobid)/phase')

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_ivoa_netxmlUWSv1_0_ShortJobDescription_id', _module_typeBindings.JobIdentifier, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 36, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 36, 6)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_ivoa_netxmlUWSv1_0_ShortJobDescription_httpwww_w3_org1999xlinktype', _ImportedBinding__xlink.STD_ANON, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/Xlink/xlink.xsd', 16, 2)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 44, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_ivoa_netxmlUWSv1_0_ShortJobDescription_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/Xlink/xlink.xsd', 28, 2)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 46, 6)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        __phase.name() : __phase
    })
    _AttributeMap.update({
        __id.name() : __id,
        __type.name() : __type,
        __href.name() : __href
    })
_module_typeBindings.ShortJobDescription = ShortJobDescription
Namespace.addCategoryObject('typeBinding', 'ShortJobDescription', ShortJobDescription)


# Complex type {http://www.ivoa.net/xml/UWS/v1.0}ResultReference with content type EMPTY
class ResultReference (pyxb.binding.basis.complexTypeDefinition):
    """ A reference to a UWS result
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResultReference')
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 247, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_ivoa_netxmlUWSv1_0_ResultReference_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 252, 6)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 252, 6)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'type'), 'type', '__httpwww_ivoa_netxmlUWSv1_0_ResultReference_httpwww_w3_org1999xlinktype', _ImportedBinding__xlink.STD_ANON, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/Xlink/xlink.xsd', 16, 2)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 44, 6)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_xlink, 'href'), 'href', '__httpwww_ivoa_netxmlUWSv1_0_ResultReference_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.anyURI)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/Xlink/xlink.xsd', 28, 2)
    __href._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 46, 6)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __type.name() : __type,
        __href.name() : __href
    })
_module_typeBindings.ResultReference = ResultReference
Namespace.addCategoryObject('typeBinding', 'ResultReference', ResultReference)


# Complex type {http://www.ivoa.net/xml/UWS/v1.0}ErrorSummary with content type ELEMENT_ONLY
class ErrorSummary (pyxb.binding.basis.complexTypeDefinition):
    """
            A short summary of an error - a fuller representation of the
            error may be retrieved from /(jobs)/(jobid)/error
         """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ErrorSummary')
    _XSDLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 268, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ivoa.net/xml/UWS/v1.0}message uses Python identifier message
    __message = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'message'), 'message', '__httpwww_ivoa_netxmlUWSv1_0_ErrorSummary_httpwww_ivoa_netxmlUWSv1_0message', False, pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 276, 9), )

    
    message = property(__message.value, __message.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_ivoa_netxmlUWSv1_0_ErrorSummary_type', _module_typeBindings.ErrorType, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 278, 6)
    __type._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 278, 6)
    
    type = property(__type.value, __type.set, None, '\n               characterization of the type of the error\n            ')

    
    # Attribute hasDetail uses Python identifier hasDetail
    __hasDetail = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hasDetail'), 'hasDetail', '__httpwww_ivoa_netxmlUWSv1_0_ErrorSummary_hasDetail', pyxb.binding.datatypes.boolean, required=True)
    __hasDetail._DeclarationLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 285, 6)
    __hasDetail._UseLocation = pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 285, 6)
    
    hasDetail = property(__hasDetail.value, __hasDetail.set, None, 'if true then there is a more detailed error message available at /(jobs)/(jobid)/error')

    _ElementMap.update({
        __message.name() : __message
    })
    _AttributeMap.update({
        __type.name() : __type,
        __hasDetail.name() : __hasDetail
    })
_module_typeBindings.ErrorSummary = ErrorSummary
Namespace.addCategoryObject('typeBinding', 'ErrorSummary', ErrorSummary)


job = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'job'), JobSummary, documentation=' This is the information that is returned\n            when a GET is made for a single job resource - i.e.\n            /(jobs)/(jobid)', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 221, 3))
Namespace.addCategoryObject('elementBinding', job.name().localName(), job)

jobs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'jobs'), CTD_ANON_, documentation=' The list of job references returned at\n            /(jobs)', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 228, 3))
Namespace.addCategoryObject('elementBinding', jobs.name().localName(), jobs)

results = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'results'), CTD_ANON_2, documentation=' The element returned for\n            /(jobs)/(jobid)/results', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 255, 3))
Namespace.addCategoryObject('elementBinding', results.name().localName(), results)

parameters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameters'), CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 327, 3))
Namespace.addCategoryObject('elementBinding', parameters.name().localName(), parameters)



JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'jobId'), JobIdentifier, scope=JobSummary, location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 118, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'runId'), pyxb.binding.datatypes.string, scope=JobSummary, documentation=' this is a client supplied identifier -\n                  the UWS system does nothing other than to return it as\n                  part of the description of the job', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 119, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ownerId'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=JobSummary, documentation='the owner (creator) of the job -\n                  this should be expressed as a string that can be\n                  parsed in accordance with IVOA security standards. If\n                  there was no authenticated job creator then this\n                  should be set to NULL.', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 128, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phase'), ExecutionPhase, scope=JobSummary, documentation=' the execution phase - returned at\n                  /(jobs)/(jobid)/phase', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 139, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'quote'), pyxb.binding.datatypes.dateTime, nillable=pyxb.binding.datatypes.boolean(1), scope=JobSummary, documentation=' A Quote predicts when the job is likely to complete - returned at /(jobs)/(jobid)/quote\n                  "don\'t know" is encoded by setting to the XML null value xsi:nil="true"', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 145, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'startTime'), pyxb.binding.datatypes.dateTime, nillable=pyxb.binding.datatypes.boolean(1), scope=JobSummary, documentation='The instant at which the job started execution.', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 153, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endTime'), pyxb.binding.datatypes.dateTime, nillable=pyxb.binding.datatypes.boolean(1), scope=JobSummary, documentation='The instant at which the job finished execution', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 158, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'executionDuration'), pyxb.binding.datatypes.int, scope=JobSummary, documentation=' The duration (in seconds) for which\n                  the job should be allowed to run - a value of 0 is\n                  intended to mean unlimited - returned at\n                  /(jobs)/(jobid)/executionduration', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 163, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'destruction'), pyxb.binding.datatypes.dateTime, nillable=pyxb.binding.datatypes.boolean(1), scope=JobSummary, documentation=' The time at which the whole job +\n                  records + results will be destroyed. returned at\n                  /(jobs)/(jobid)/destruction', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 174, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errorSummary'), ErrorSummary, scope=JobSummary, location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 195, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'jobInfo'), CTD_ANON, scope=JobSummary, documentation=' This is arbitrary information that can\n                  be added to the job description by the UWS\n                  implementation.', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 199, 9)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'results'), CTD_ANON_2, scope=JobSummary, documentation=' The element returned for\n            /(jobs)/(jobid)/results', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 255, 3)))

JobSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameters'), CTD_ANON_3, scope=JobSummary, location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 327, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 119, 9))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 145, 9))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 183, 9))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 195, 9))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 199, 9))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'jobId')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 118, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'runId')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 119, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ownerId')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 128, 9))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phase')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 139, 9))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'quote')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 145, 9))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'startTime')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 153, 9))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endTime')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 158, 9))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'executionDuration')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 163, 9))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'destruction')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 174, 9))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameters')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 183, 9))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'results')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 191, 9))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errorSummary')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 195, 9))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(JobSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'jobInfo')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 199, 9))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
JobSummary._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 207, 18))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 207, 18))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'jobref'), ShortJobDescription, scope=CTD_ANON_, location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 241, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 241, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'jobref')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 241, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), ResultReference, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 262, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 262, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 262, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
Parameter._Automaton = _BuildAutomaton_4()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parameter'), Parameter, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 330, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 330, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'parameter')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 330, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_5()




ShortJobDescription._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phase'), ExecutionPhase, scope=ShortJobDescription, documentation=' the execution phase - returned at\n                  /(jobs)/(jobid)/phase', location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 29, 9)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ShortJobDescription._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phase')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 29, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ShortJobDescription._Automaton = _BuildAutomaton_6()




ErrorSummary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'message'), pyxb.binding.datatypes.string, scope=ErrorSummary, location=pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 276, 9)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ErrorSummary._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'message')), pyxb.utils.utility.Location('http://www.ivoa.net/xml/UWS/v1.0', 276, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ErrorSummary._Automaton = _BuildAutomaton_7()

