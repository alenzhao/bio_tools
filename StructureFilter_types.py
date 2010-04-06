##################################################
# file: StructureFilter_types.py
#
# schema types generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#    /usr/bin/wsdl2py http://structurefilter.embl.de/webservice/structureFilter.wsdl
#
##################################################

import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED

##############################
# targetNamespace
# http://structureFilter.embl.de/StructureFilter
##############################

class ns0:
    targetNamespace = "http://structureFilter.embl.de/StructureFilter"

    class SequenceType_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://structureFilter.embl.de/StructureFilter"
        type = (schema, "SequenceType")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.SequenceType_Def.schema
            TClist = [self.__class__.identifier_Dec(minOccurs=1, maxOccurs=1, nillable=False, encoded=kw.get("encoded")), self.__class__.sequence_Dec(minOccurs=1, maxOccurs=1, nillable=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._identifier = None
                    self._sequence = None
                    return
            Holder.__name__ = "SequenceType_Holder"
            self.pyclass = Holder


        class identifier_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "identifier"
            schema = "http://structureFilter.embl.de/StructureFilter"
            def __init__(self, **kw):
                kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","identifier")
                kw["aname"] = "_identifier"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_identifier_immutable_holder"





        class sequence_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "sequence"
            schema = "http://structureFilter.embl.de/StructureFilter"
            def __init__(self, **kw):
                kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","sequence")
                kw["aname"] = "_sequence"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_sequence_immutable_holder"




    class AccessibilityRecordType_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://structureFilter.embl.de/StructureFilter"
        type = (schema, "AccessibilityRecordType")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.AccessibilityRecordType_Def.schema
            TClist = [ZSI.TCnumbers.Iinteger(pname=(ns,"position"), aname="_position", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Decimal(pname=(ns,"accessibility"), aname="_accessibility", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"targetDomainStructure"), aname="_targetDomainStructure", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._position = None
                    self._accessibility = None
                    self._targetDomainStructure = None
                    return
            Holder.__name__ = "AccessibilityRecordType_Holder"
            self.pyclass = Holder

    class SecondaryStructureRecordType_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://structureFilter.embl.de/StructureFilter"
        type = (schema, "SecondaryStructureRecordType")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.SecondaryStructureRecordType_Def.schema
            TClist = [ZSI.TCnumbers.Iinteger(pname=(ns,"start"), aname="_start", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iinteger(pname=(ns,"end"), aname="_end", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"secondaryStructure"), aname="_secondaryStructure", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"targetDomainStructure"), aname="_targetDomainStructure", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._start = None
                    self._end = None
                    self._secondaryStructure = None
                    self._targetDomainStructure = None
                    return
            Holder.__name__ = "SecondaryStructureRecordType_Holder"
            self.pyclass = Holder

    class StructureFilterRecordType_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://structureFilter.embl.de/StructureFilter"
        type = (schema, "StructureFilterRecordType")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.StructureFilterRecordType_Def.schema
            TClist = [ZSI.TC.String(pname=(ns,"ELMIdentifier"), aname="_ELMIdentifier", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"regularExpression"), aname="_regularExpression", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iinteger(pname=(ns,"start"), aname="_start", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iinteger(pname=(ns,"end"), aname="_end", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Decimal(pname=(ns,"accessibilityScore"), aname="_accessibilityScore", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Decimal(pname=(ns,"accessibilityScorePValue"), aname="_accessibilityScorePValue", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Decimal(pname=(ns,"secondaryStructureScore"), aname="_secondaryStructureScore", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Decimal(pname=(ns,"secondaryStructureScorePValue"), aname="_secondaryStructureScorePValue", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Decimal(pname=(ns,"totalScore"), aname="_totalScore", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Decimal(pname=(ns,"totalScorePValue"), aname="_totalScorePValue", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"targetDomainStructure"), aname="_targetDomainStructure", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Decimal(pname=(ns,"percentageIdentity"), aname="_percentageIdentity", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"benchmarkAssignment"), aname="_benchmarkAssignment", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), GTD("http://structureFilter.embl.de/StructureFilter","IndividualResidueValuesType",lazy=False)(pname=(ns,"individualResidueValues"), aname="_individualResidueValues", minOccurs=0, maxOccurs="unbounded", nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._ELMIdentifier = None
                    self._regularExpression = None
                    self._start = None
                    self._end = None
                    self._accessibilityScore = None
                    self._accessibilityScorePValue = None
                    self._secondaryStructureScore = None
                    self._secondaryStructureScorePValue = None
                    self._totalScore = None
                    self._totalScorePValue = None
                    self._targetDomainStructure = None
                    self._percentageIdentity = None
                    self._benchmarkAssignment = None
                    self._individualResidueValues = []
                    return
            Holder.__name__ = "StructureFilterRecordType_Holder"
            self.pyclass = Holder

    class IndividualResidueValuesType_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://structureFilter.embl.de/StructureFilter"
        type = (schema, "IndividualResidueValuesType")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.IndividualResidueValuesType_Def.schema
            TClist = [ZSI.TCnumbers.Iinteger(pname=(ns,"position"), aname="_position", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"targetDomainStructure"), aname="_targetDomainStructure", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.Decimal(pname=(ns,"accessibility"), aname="_accessibility", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"secondaryStructure"), aname="_secondaryStructure", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._position = None
                    self._targetDomainStructure = None
                    self._accessibility = None
                    self._secondaryStructure = None
                    return
            Holder.__name__ = "IndividualResidueValuesType_Holder"
            self.pyclass = Holder

    class RunJob_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "RunJob"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            ns = ns0.RunJob_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"identifier"), aname="_identifier", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), self.__class__.querySequence_Dec(minOccurs=1, maxOccurs=1, nillable=False, encoded=kw.get("encoded")), self.__class__.regularExpression_Dec(minOccurs=0, maxOccurs=5, nillable=False, encoded=kw.get("encoded")), self.__class__.elmIdentifierName_Dec(minOccurs=0, maxOccurs=5, nillable=False, encoded=kw.get("encoded")), self.__class__.includeSecondaryStructureRecords_Dec(minOccurs=0, maxOccurs=1, nillable=False, encoded=kw.get("encoded")), self.__class__.includeAccessibilityRecords_Dec(minOccurs=0, maxOccurs=1, nillable=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","RunJob")
            kw["aname"] = "_RunJob"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._identifier = None
                    self._querySequence = None
                    self._regularExpression = []
                    self._elmIdentifierName = []
                    self._includeSecondaryStructureRecords = None
                    self._includeAccessibilityRecords = None
                    return
            Holder.__name__ = "RunJob_Holder"
            self.pyclass = Holder


        class querySequence_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "querySequence"
            schema = "http://structureFilter.embl.de/StructureFilter"
            def __init__(self, **kw):
                kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","querySequence")
                kw["aname"] = "_querySequence"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_querySequence_immutable_holder"





        class regularExpression_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "regularExpression"
            schema = "http://structureFilter.embl.de/StructureFilter"
            def __init__(self, **kw):
                kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","regularExpression")
                kw["aname"] = "_regularExpression"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_regularExpression_immutable_holder"





        class elmIdentifierName_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "elmIdentifierName"
            schema = "http://structureFilter.embl.de/StructureFilter"
            def __init__(self, **kw):
                kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","elmIdentifierName")
                kw["aname"] = "_elmIdentifierName"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_elmIdentifierName_immutable_holder"





        class includeSecondaryStructureRecords_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "includeSecondaryStructureRecords"
            schema = "http://structureFilter.embl.de/StructureFilter"
            def __init__(self, **kw):
                kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","includeSecondaryStructureRecords")
                kw["aname"] = "_includeSecondaryStructureRecords"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_includeSecondaryStructureRecords_immutable_holder"





        class includeAccessibilityRecords_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "includeAccessibilityRecords"
            schema = "http://structureFilter.embl.de/StructureFilter"
            def __init__(self, **kw):
                kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","includeAccessibilityRecords")
                kw["aname"] = "_includeAccessibilityRecords"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_includeAccessibilityRecords_immutable_holder"




    class RunJobResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "RunJobResponse"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            ns = ns0.RunJobResponse_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"JobIdentifier"), aname="_JobIdentifier", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","RunJobResponse")
            kw["aname"] = "_RunJobResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._JobIdentifier = None
                    return
            Holder.__name__ = "RunJobResponse_Holder"
            self.pyclass = Holder

    class GetStatus_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetStatus"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            ns = ns0.GetStatus_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"JobIdentifier"), aname="_JobIdentifier", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","GetStatus")
            kw["aname"] = "_GetStatus"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._JobIdentifier = None
                    return
            Holder.__name__ = "GetStatus_Holder"
            self.pyclass = Holder

    class Status_Dec(ZSI.TC.String, ElementDeclaration):
        literal = "Status"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","Status")
            kw["aname"] = "_Status"
            class IHolder(str): typecode=self
            kw["pyclass"] = IHolder
            IHolder.__name__ = "_Status_immutable_holder"
            ZSI.TC.String.__init__(self, **kw)

    class StatusDetails_Dec(ZSI.TC.String, ElementDeclaration):
        literal = "StatusDetails"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","StatusDetails")
            kw["aname"] = "_StatusDetails"
            class IHolder(str): typecode=self
            kw["pyclass"] = IHolder
            IHolder.__name__ = "_StatusDetails_immutable_holder"
            ZSI.TC.String.__init__(self, **kw)

    class GetStatusResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetStatusResponse"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            ns = ns0.GetStatusResponse_Dec.schema
            TClist = [GED("http://structureFilter.embl.de/StructureFilter","Status",lazy=False, isref=True)(minOccurs=1, maxOccurs=1, nillable=False, encoded=kw.get("encoded")), GED("http://structureFilter.embl.de/StructureFilter","StatusDetails",lazy=False, isref=True)(minOccurs=0, maxOccurs=1, nillable=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","GetStatusResponse")
            kw["aname"] = "_GetStatusResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._Status = None
                    self._StatusDetails = None
                    return
            Holder.__name__ = "GetStatusResponse_Holder"
            self.pyclass = Holder

    class GetResult_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetResult"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            ns = ns0.GetResult_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"JobIdentifier"), aname="_JobIdentifier", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","GetResult")
            kw["aname"] = "_GetResult"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._JobIdentifier = None
                    return
            Holder.__name__ = "GetResult_Holder"
            self.pyclass = Holder

    class GetResultResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetResultResponse"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            ns = ns0.GetResultResponse_Dec.schema
            TClist = [GTD("http://structureFilter.embl.de/StructureFilter","SequenceType",lazy=False)(pname=(ns,"sequence"), aname="_sequence", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), GTD("http://structureFilter.embl.de/StructureFilter","StructureFilterRecordType",lazy=False)(pname=(ns,"structureFilterRecord"), aname="_structureFilterRecord", minOccurs=0, maxOccurs="unbounded", nillable=False, typed=False, encoded=kw.get("encoded")), GTD("http://structureFilter.embl.de/StructureFilter","SecondaryStructureRecordType",lazy=False)(pname=(ns,"secondaryStructureRecord"), aname="_secondaryStructureRecord", minOccurs=0, maxOccurs="unbounded", nillable=False, typed=False, encoded=kw.get("encoded")), GTD("http://structureFilter.embl.de/StructureFilter","AccessibilityRecordType",lazy=False)(pname=(ns,"accessibilityRecord"), aname="_accessibilityRecord", minOccurs=0, maxOccurs="unbounded", nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","GetResultResponse")
            kw["aname"] = "_GetResultResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._sequence = None
                    self._structureFilterRecord = []
                    self._secondaryStructureRecord = []
                    self._accessibilityRecord = []
                    return
            Holder.__name__ = "GetResultResponse_Holder"
            self.pyclass = Holder

    class FaultDescription_Dec(ZSI.TC.String, ElementDeclaration):
        literal = "FaultDescription"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","FaultDescription")
            kw["aname"] = "_FaultDescription"
            class IHolder(str): typecode=self
            kw["pyclass"] = IHolder
            IHolder.__name__ = "_FaultDescription_immutable_holder"
            ZSI.TC.String.__init__(self, **kw)

    class JobIdentifierFault_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "JobIdentifierFault"
        schema = "http://structureFilter.embl.de/StructureFilter"
        def __init__(self, **kw):
            ns = ns0.JobIdentifierFault_Dec.schema
            TClist = [GED("http://structureFilter.embl.de/StructureFilter","FaultDescription",lazy=False, isref=True)(minOccurs=1, maxOccurs=1, nillable=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("http://structureFilter.embl.de/StructureFilter","JobIdentifierFault")
            kw["aname"] = "_JobIdentifierFault"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._FaultDescription = None
                    return
            Holder.__name__ = "JobIdentifierFault_Holder"
            self.pyclass = Holder

# end class ns0 (tns: http://structureFilter.embl.de/StructureFilter)