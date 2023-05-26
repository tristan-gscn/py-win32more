from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.WindowsSync
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
SYNC_VERSION_FLAG_FROM_FEED: UInt32 = 1
SYNC_VERSION_FLAG_HAS_BY: UInt32 = 2
SYNC_SERIALIZE_REPLICA_KEY_MAP: UInt32 = 1
SYNC_FILTER_INFO_FLAG_ITEM_LIST: UInt32 = 1
SYNC_FILTER_INFO_FLAG_CHANGE_UNIT_LIST: UInt32 = 2
SYNC_FILTER_INFO_FLAG_CUSTOM: UInt32 = 4
SYNC_FILTER_INFO_COMBINED: UInt32 = 8
SYNC_CHANGE_FLAG_DELETED: UInt32 = 1
SYNC_CHANGE_FLAG_DOES_NOT_EXIST: UInt32 = 2
SYNC_CHANGE_FLAG_GHOST: UInt32 = 4
SCC_DEFAULT: UInt32 = 0
SCC_CAN_CREATE_WITHOUT_UI: UInt32 = 1
SCC_CAN_MODIFY_WITHOUT_UI: UInt32 = 2
SCC_CREATE_NOT_SUPPORTED: UInt32 = 4
SCC_MODIFY_NOT_SUPPORTED: UInt32 = 8
SPC_DEFAULT: UInt32 = 0
SYNC_PROVIDER_STATE_ENABLED: UInt32 = 1
SYNC_PROVIDER_STATE_DIRTY: UInt32 = 2
SYNC_PROVIDER_CONFIGURATION_VERSION: UInt32 = 1
SYNC_PROVIDER_CONFIGUI_CONFIGURATION_VERSION: UInt32 = 1
SYNC_32_BIT_SUPPORTED: UInt32 = 1
SYNC_64_BIT_SUPPORTED: UInt32 = 2
def PKEY_PROVIDER_INSTANCEID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=2)
def PKEY_PROVIDER_CLSID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=3)
def PKEY_PROVIDER_CONFIGUI():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=4)
def PKEY_PROVIDER_CONTENTTYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=5)
def PKEY_PROVIDER_CAPABILITIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=6)
def PKEY_PROVIDER_SUPPORTED_ARCHITECTURE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=7)
def PKEY_PROVIDER_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=8)
def PKEY_PROVIDER_DESCRIPTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=9)
def PKEY_PROVIDER_TOOLTIPS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=10)
def PKEY_PROVIDER_ICON():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{84179e61-60f6-4c1c-88ed-f1c531b32bda}'), pid=11)
def PKEY_CONFIGUI_INSTANCEID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=2)
def PKEY_CONFIGUI_CLSID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=3)
def PKEY_CONFIGUI_CONTENTTYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=4)
def PKEY_CONFIGUI_CAPABILITIES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=5)
def PKEY_CONFIGUI_SUPPORTED_ARCHITECTURE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=6)
def PKEY_CONFIGUI_IS_GLOBAL():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=7)
def PKEY_CONFIGUI_NAME():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=8)
def PKEY_CONFIGUI_DESCRIPTION():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=9)
def PKEY_CONFIGUI_TOOLTIPS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=10)
def PKEY_CONFIGUI_ICON():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=11)
def PKEY_CONFIGUI_MENUITEM_NOUI():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=12)
def PKEY_CONFIGUI_MENUITEM():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{554b24ea-e8e3-45ba-9352-dfb561e171e4}'), pid=13)
CONFLICT_RESOLUTION_POLICY = Int32
CRP_NONE: CONFLICT_RESOLUTION_POLICY = 0
CRP_DESTINATION_PROVIDER_WINS: CONFLICT_RESOLUTION_POLICY = 1
CRP_SOURCE_PROVIDER_WINS: CONFLICT_RESOLUTION_POLICY = 2
CRP_LAST: CONFLICT_RESOLUTION_POLICY = 3
CONSTRAINT_CONFLICT_REASON = Int32
CCR_OTHER: CONSTRAINT_CONFLICT_REASON = 0
CCR_COLLISION: CONSTRAINT_CONFLICT_REASON = 1
CCR_NOPARENT: CONSTRAINT_CONFLICT_REASON = 2
CCR_IDENTITY: CONSTRAINT_CONFLICT_REASON = 3
FILTERING_TYPE = Int32
FT_CURRENT_ITEMS_ONLY: FILTERING_TYPE = 0
FT_CURRENT_ITEMS_AND_VERSIONS_FOR_MOVED_OUT_ITEMS: FILTERING_TYPE = 1
FILTER_COMBINATION_TYPE = Int32
FCT_INTERSECTION: FILTER_COMBINATION_TYPE = 0
class IAsynchronousDataRetriever(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9fc7e470-61ea-4a88-9be4-df56a27cfef2}')
    @commethod(3)
    def GetIdParameters(self, pIdParameters: POINTER(Windows.Win32.System.WindowsSync.ID_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterCallback(self, pDataRetrieverCallback: Windows.Win32.System.WindowsSync.IDataRetrieverCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RevokeCallback(self, pDataRetrieverCallback: Windows.Win32.System.WindowsSync.IDataRetrieverCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def LoadChangeData(self, pLoadChangeContext: Windows.Win32.System.WindowsSync.ILoadChangeContext_head) -> Windows.Win32.Foundation.HRESULT: ...
class IChangeConflict(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{014ebf97-9f20-4f7a-bdd4-25979c77c002}')
    @commethod(3)
    def GetDestinationProviderConflictingChange(self, ppConflictingChange: POINTER(Windows.Win32.System.WindowsSync.ISyncChange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceProviderConflictingChange(self, ppConflictingChange: POINTER(Windows.Win32.System.WindowsSync.ISyncChange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDestinationProviderConflictingData(self, ppConflictingData: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceProviderConflictingData(self, ppConflictingData: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResolveActionForChange(self, pResolveAction: POINTER(Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetResolveActionForChange(self, resolveAction: Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetResolveActionForChangeUnit(self, pChangeUnit: Windows.Win32.System.WindowsSync.ISyncChangeUnit_head, pResolveAction: POINTER(Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetResolveActionForChangeUnit(self, pChangeUnit: Windows.Win32.System.WindowsSync.ISyncChangeUnit_head, resolveAction: Windows.Win32.System.WindowsSync.SYNC_RESOLVE_ACTION) -> Windows.Win32.Foundation.HRESULT: ...
class IChangeUnitException(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0cd7ee7c-fec0-4021-99ee-f0e5348f2a5f}')
    @commethod(3)
    def GetItemId(self, pbItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChangeUnitId(self, pbChangeUnitId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetClockVector(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IChangeUnitListFilterInfo(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncFilterInfo
    _iid_ = Guid('{f2837671-0bdf-43fa-b502-232375fb50c2}')
    @commethod(4)
    def Initialize(self, ppbChangeUnitIds: POINTER(POINTER(Byte)), dwChangeUnitCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeUnitIdCount(self, pdwChangeUnitIdCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetChangeUnitId(self, dwChangeUnitIdIndex: UInt32, pbChangeUnitId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IClockVector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{14b2274a-8698-4cc6-9333-f89bd1d47bc4}')
    @commethod(3)
    def GetClockVectorElements(self, riid: POINTER(Guid), ppiEnumClockVector: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClockVectorElementCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IClockVectorElement(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e71c4250-adf8-4a07-8fae-5669596909c1}')
    @commethod(3)
    def GetReplicaKey(self, pdwReplicaKey: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTickCount(self, pullTickCount: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class ICombinedFilterInfo(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncFilterInfo
    _iid_ = Guid('{11f9de71-2818-4779-b2ac-42d450565f45}')
    @commethod(4)
    def GetFilterCount(self, pdwFilterCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFilterInfo(self, dwFilterIndex: UInt32, ppIFilterInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncFilterInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFilterCombinationType(self, pFilterCombinationType: POINTER(Windows.Win32.System.WindowsSync.FILTER_COMBINATION_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
class IConstraintConflict(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00d2302e-1cf8-4835-b85f-b7ca4f799e0a}')
    @commethod(3)
    def GetDestinationProviderConflictingChange(self, ppConflictingChange: POINTER(Windows.Win32.System.WindowsSync.ISyncChange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceProviderConflictingChange(self, ppConflictingChange: POINTER(Windows.Win32.System.WindowsSync.ISyncChange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDestinationProviderOriginalChange(self, ppOriginalChange: POINTER(Windows.Win32.System.WindowsSync.ISyncChange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDestinationProviderConflictingData(self, ppConflictingData: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSourceProviderConflictingData(self, ppConflictingData: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDestinationProviderOriginalData(self, ppOriginalData: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetConstraintResolveActionForChange(self, pConstraintResolveAction: POINTER(Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetConstraintResolveActionForChange(self, constraintResolveAction: Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetConstraintResolveActionForChangeUnit(self, pChangeUnit: Windows.Win32.System.WindowsSync.ISyncChangeUnit_head, pConstraintResolveAction: POINTER(Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetConstraintResolveActionForChangeUnit(self, pChangeUnit: Windows.Win32.System.WindowsSync.ISyncChangeUnit_head, constraintResolveAction: Windows.Win32.System.WindowsSync.SYNC_CONSTRAINT_RESOLVE_ACTION) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetConstraintConflictReason(self, pConstraintConflictReason: POINTER(Windows.Win32.System.WindowsSync.CONSTRAINT_CONFLICT_REASON)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsTemporary(self) -> Windows.Win32.Foundation.HRESULT: ...
class IConstructReplicaKeyMap(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ded10970-ec85-4115-b52c-4405845642a5}')
    @commethod(3)
    def FindOrAddReplica(self, pbReplicaId: POINTER(Byte), pdwReplicaKey: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ICoreFragment(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{613b2ab5-b304-47d9-9c31-ce6c54401a15}')
    @commethod(3)
    def NextColumn(self, pChangeUnitId: POINTER(Byte), pChangeUnitIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NextRange(self, pItemId: POINTER(Byte), pItemIdSize: POINTER(UInt32), piClockVector: POINTER(Windows.Win32.System.WindowsSync.IClockVector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnCount(self, pColumnCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRangeCount(self, pRangeCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ICoreFragmentInspector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f7fcc5fd-ae26-4679-ba16-96aac583c134}')
    @commethod(3)
    def NextCoreFragments(self, requestedCount: UInt32, ppiCoreFragments: POINTER(Windows.Win32.System.WindowsSync.ICoreFragment_head), pFetchedCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class ICustomFilterInfo(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncFilterInfo
    _iid_ = Guid('{1d335dff-6f88-4e4d-91a8-a3f351cfd473}')
    @commethod(4)
    def GetSyncFilter(self, pISyncFilter: POINTER(Windows.Win32.System.WindowsSync.ISyncFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ID_PARAMETERS(EasyCastStructure):
    dwSize: UInt32
    replicaId: Windows.Win32.System.WindowsSync.ID_PARAMETER_PAIR
    itemId: Windows.Win32.System.WindowsSync.ID_PARAMETER_PAIR
    changeUnitId: Windows.Win32.System.WindowsSync.ID_PARAMETER_PAIR
class ID_PARAMETER_PAIR(EasyCastStructure):
    fIsVariable: Windows.Win32.Foundation.BOOL
    cbIdSize: UInt16
class IDataRetrieverCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71b4863b-f969-4676-bbc3-3d9fdc3fb2c7}')
    @commethod(3)
    def LoadChangeDataComplete(self, pUnkData: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadChangeDataError(self, hrError: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumChangeUnitExceptions(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3074e802-9319-4420-be21-1022e2e21da8}')
    @commethod(3)
    def Next(self, cExceptions: UInt32, ppChangeUnitException: POINTER(Windows.Win32.System.WindowsSync.IChangeUnitException_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cExceptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumChangeUnitExceptions_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumClockVector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{525844db-2837-4799-9e80-81a66e02220c}')
    @commethod(3)
    def Next(self, cClockVectorElements: UInt32, ppiClockVectorElements: POINTER(Windows.Win32.System.WindowsSync.IClockVectorElement_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cSyncVersions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppiEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumClockVector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumFeedClockVector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{550f763d-146a-48f6-abeb-6c88c7f70514}')
    @commethod(3)
    def Next(self, cClockVectorElements: UInt32, ppiClockVectorElements: POINTER(Windows.Win32.System.WindowsSync.IFeedClockVectorElement_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cSyncVersions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppiEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumFeedClockVector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumItemIds(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{43aa3f61-4b2e-4b60-83df-b110d3e148f1}')
    @commethod(3)
    def Next(self, pbItemId: POINTER(Byte), pcbItemIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumRangeExceptions(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0944439f-ddb1-4176-b703-046ff22a2386}')
    @commethod(3)
    def Next(self, cExceptions: UInt32, ppRangeException: POINTER(Windows.Win32.System.WindowsSync.IRangeException_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cExceptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumRangeExceptions_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSingleItemExceptions(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e563381c-1b4d-4c66-9796-c86faccdcd40}')
    @commethod(3)
    def Next(self, cExceptions: UInt32, ppSingleItemException: POINTER(Windows.Win32.System.WindowsSync.ISingleItemException_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cExceptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumSingleItemExceptions_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncChangeUnits(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{346b35f1-8703-4c6d-ab1a-4dbca2cff97f}')
    @commethod(3)
    def Next(self, cChanges: UInt32, ppChangeUnit: POINTER(Windows.Win32.System.WindowsSync.ISyncChangeUnit_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cChanges: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumSyncChangeUnits_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncChanges(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5f86be4a-5e78-4e32-ac1c-c24fd223ef85}')
    @commethod(3)
    def Next(self, cChanges: UInt32, ppChange: POINTER(Windows.Win32.System.WindowsSync.ISyncChange_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cChanges: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumSyncChanges_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncProviderConfigUIInfos(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f6be2602-17c6-4658-a2d7-68ed3330f641}')
    @commethod(3)
    def Next(self, cFactories: UInt32, ppSyncProviderConfigUIInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderConfigUIInfo_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cFactories: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumSyncProviderConfigUIInfos_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncProviderInfos(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a04ba850-5eb1-460d-a973-393fcb608a11}')
    @commethod(3)
    def Next(self, cInstances: UInt32, ppSyncProviderInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderInfo_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cInstances: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumSyncProviderInfos_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFeedClockVector(ComPtr):
    extends: Windows.Win32.System.WindowsSync.IClockVector
    _iid_ = Guid('{8d1d98d1-9fb8-4ec9-a553-54dd924e0f67}')
    @commethod(5)
    def GetUpdateCount(self, pdwUpdateCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsNoConflictsSpecified(self, pfIsNoConflictsSpecified: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IFeedClockVectorElement(ComPtr):
    extends: Windows.Win32.System.WindowsSync.IClockVectorElement
    _iid_ = Guid('{a40b46d2-e97b-4156-b6da-991f501b0f05}')
    @commethod(5)
    def GetSyncTime(self, pSyncTime: POINTER(Windows.Win32.System.WindowsSync.SYNC_TIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFlags(self, pbFlags: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IFilterKeyMap(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ca169652-07c6-4708-a3da-6e4eba8d2297}')
    @commethod(3)
    def GetCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddFilter(self, pISyncFilter: Windows.Win32.System.WindowsSync.ISyncFilter_head, pdwFilterKey: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFilter(self, dwFilterKey: UInt32, ppISyncFilter: POINTER(Windows.Win32.System.WindowsSync.ISyncFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Serialize(self, pbFilterKeyMap: POINTER(Byte), pcbFilterKeyMap: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IFilterRequestCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82df8873-6360-463a-a8a1-ede5e1a1594d}')
    @commethod(3)
    def RequestFilter(self, pFilter: Windows.Win32.System.Com.IUnknown_head, filteringType: Windows.Win32.System.WindowsSync.FILTERING_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class IFilterTrackingProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{743383c0-fc4e-45ba-ad81-d9d84c7a24f8}')
    @commethod(3)
    def SpecifyTrackedFilters(self, pCallback: Windows.Win32.System.WindowsSync.IFilterTrackingRequestCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddTrackedFilter(self, pFilter: Windows.Win32.System.WindowsSync.ISyncFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFilterTrackingRequestCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{713ca7bb-c858-4674-b4b6-1122436587a9}')
    @commethod(3)
    def RequestTrackedFilter(self, pFilter: Windows.Win32.System.WindowsSync.ISyncFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
class IFilterTrackingSyncChangeBuilder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{295024a0-70da-4c58-883c-ce2afb308d0b}')
    @commethod(3)
    def AddFilterChange(self, dwFilterKey: UInt32, pFilterChange: POINTER(Windows.Win32.System.WindowsSync.SYNC_FILTER_CHANGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAllChangeUnitsPresentFlag(self) -> Windows.Win32.Foundation.HRESULT: ...
class IForgottenKnowledge(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncKnowledge
    _iid_ = Guid('{456e0f96-6036-452b-9f9d-bcc4b4a85db2}')
    @commethod(27)
    def ForgetToVersion(self, pKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IKnowledgeSyncProvider(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncProvider
    _iid_ = Guid('{43434a49-8da4-47f2-8172-ad7b8b024978}')
    @commethod(4)
    def BeginSession(self, role: Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE, pSessionState: Windows.Win32.System.WindowsSync.ISyncSessionState_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSyncBatchParameters(self, ppSyncKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head), pdwRequestedBatchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetChangeBatch(self, dwBatchSize: UInt32, pSyncKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, ppSyncChangeBatch: POINTER(Windows.Win32.System.WindowsSync.ISyncChangeBatch_head), ppUnkDataRetriever: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFullEnumerationChangeBatch(self, dwBatchSize: UInt32, pbLowerEnumerationBound: POINTER(Byte), pSyncKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, ppSyncChangeBatch: POINTER(Windows.Win32.System.WindowsSync.ISyncFullEnumerationChangeBatch_head), ppUnkDataRetriever: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ProcessChangeBatch(self, resolutionPolicy: Windows.Win32.System.WindowsSync.CONFLICT_RESOLUTION_POLICY, pSourceChangeBatch: Windows.Win32.System.WindowsSync.ISyncChangeBatch_head, pUnkDataRetriever: Windows.Win32.System.Com.IUnknown_head, pCallback: Windows.Win32.System.WindowsSync.ISyncCallback_head, pSyncSessionStatistics: POINTER(Windows.Win32.System.WindowsSync.SYNC_SESSION_STATISTICS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ProcessFullEnumerationChangeBatch(self, resolutionPolicy: Windows.Win32.System.WindowsSync.CONFLICT_RESOLUTION_POLICY, pSourceChangeBatch: Windows.Win32.System.WindowsSync.ISyncFullEnumerationChangeBatch_head, pUnkDataRetriever: Windows.Win32.System.Com.IUnknown_head, pCallback: Windows.Win32.System.WindowsSync.ISyncCallback_head, pSyncSessionStatistics: POINTER(Windows.Win32.System.WindowsSync.SYNC_SESSION_STATISTICS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndSession(self, pSessionState: Windows.Win32.System.WindowsSync.ISyncSessionState_head) -> Windows.Win32.Foundation.HRESULT: ...
class ILoadChangeContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{44a4aaca-ec39-46d5-b5c9-d633c0ee67e2}')
    @commethod(3)
    def GetSyncChange(self, ppSyncChange: POINTER(Windows.Win32.System.WindowsSync.ISyncChange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetRecoverableErrorOnChange(self, hrError: Windows.Win32.Foundation.HRESULT, pErrorData: Windows.Win32.System.WindowsSync.IRecoverableErrorData_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetRecoverableErrorOnChangeUnit(self, hrError: Windows.Win32.Foundation.HRESULT, pChangeUnit: Windows.Win32.System.WindowsSync.ISyncChangeUnit_head, pErrorData: Windows.Win32.System.WindowsSync.IRecoverableErrorData_head) -> Windows.Win32.Foundation.HRESULT: ...
class IProviderConverter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{809b7276-98cf-4957-93a5-0ebdd3dddffd}')
    @commethod(3)
    def Initialize(self, pISyncProvider: Windows.Win32.System.WindowsSync.ISyncProvider_head) -> Windows.Win32.Foundation.HRESULT: ...
class IRangeException(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75ae8777-6848-49f7-956c-a3a92f5096e8}')
    @commethod(3)
    def GetClosedRangeStart(self, pbClosedRangeStart: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClosedRangeEnd(self, pbClosedRangeEnd: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetClockVector(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IRecoverableError(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0f5625e8-0a7b-45ee-9637-1ce13645909e}')
    @commethod(3)
    def GetStage(self, pStage: POINTER(Windows.Win32.System.WindowsSync.SYNC_PROGRESS_STAGE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProvider(self, pProviderRole: POINTER(Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeWithRecoverableError(self, ppChangeWithRecoverableError: POINTER(Windows.Win32.System.WindowsSync.ISyncChange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRecoverableErrorDataForChange(self, phrError: POINTER(Windows.Win32.Foundation.HRESULT), ppErrorData: POINTER(Windows.Win32.System.WindowsSync.IRecoverableErrorData_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRecoverableErrorDataForChangeUnit(self, pChangeUnit: Windows.Win32.System.WindowsSync.ISyncChangeUnit_head, phrError: POINTER(Windows.Win32.Foundation.HRESULT), ppErrorData: POINTER(Windows.Win32.System.WindowsSync.IRecoverableErrorData_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRecoverableErrorData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b37c4a0a-4b7d-4c2d-9711-3b00d119b1c8}')
    @commethod(3)
    def Initialize(self, pcszItemDisplayName: Windows.Win32.Foundation.PWSTR, pcszErrorDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemDisplayName(self, pszItemDisplayName: Windows.Win32.Foundation.PWSTR, pcchItemDisplayName: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorDescription(self, pszErrorDescription: Windows.Win32.Foundation.PWSTR, pcchErrorDescription: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRegisteredSyncProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{913bcf76-47c1-40b5-a896-5e8a9c414c14}')
    @commethod(3)
    def Init(self, pguidInstanceId: POINTER(Guid), pguidContentType: POINTER(Guid), pContextPropertyStore: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstanceId(self, pguidInstanceId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
class IReplicaKeyMap(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2209f4fc-fd10-4ff0-84a8-f0a1982e440e}')
    @commethod(3)
    def LookupReplicaKey(self, pbReplicaId: POINTER(Byte), pdwReplicaKey: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LookupReplicaId(self, dwReplicaKey: UInt32, pbReplicaId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Serialize(self, pbReplicaKeyMap: POINTER(Byte), pcbReplicaKeyMap: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRequestFilteredSync(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2e020184-6d18-46a7-a32a-da4aeb06696c}')
    @commethod(3)
    def SpecifyFilter(self, pCallback: Windows.Win32.System.WindowsSync.IFilterRequestCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISingleItemException(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{892fb9b0-7c55-4a18-9316-fdf449569b64}')
    @commethod(3)
    def GetItemId(self, pbItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClockVector(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class ISupportFilteredSync(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d128ded-d555-4e0d-bf4b-fb213a8a9302}')
    @commethod(3)
    def AddFilter(self, pFilter: Windows.Win32.System.Com.IUnknown_head, filteringType: Windows.Win32.System.WindowsSync.FILTERING_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class ISupportLastWriteTime(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eadf816f-d0bd-43ca-8f40-5acdc6c06f7a}')
    @commethod(3)
    def GetItemChangeTime(self, pbItemId: POINTER(Byte), pullTimestamp: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChangeUnitChangeTime(self, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte), pullTimestamp: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0599797f-5ed9-485c-ae36-0c5d1bf2e7a5}')
    @commethod(3)
    def OnProgress(self, provider: Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE, syncStage: Windows.Win32.System.WindowsSync.SYNC_PROGRESS_STAGE, dwCompletedWork: UInt32, dwTotalWork: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnChange(self, pSyncChange: Windows.Win32.System.WindowsSync.ISyncChange_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnConflict(self, pConflict: Windows.Win32.System.WindowsSync.IChangeConflict_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnFullEnumerationNeeded(self, pFullEnumerationAction: POINTER(Windows.Win32.System.WindowsSync.SYNC_FULL_ENUMERATION_ACTION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnRecoverableError(self, pRecoverableError: Windows.Win32.System.WindowsSync.IRecoverableError_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncCallback2(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncCallback
    _iid_ = Guid('{47ce84af-7442-4ead-8630-12015e030ad7}')
    @commethod(8)
    def OnChangeApplied(self, dwChangesApplied: UInt32, dwChangesFailed: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnChangeFailed(self, dwChangesApplied: UInt32, dwChangesFailed: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChange(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1952beb-0f6b-4711-b136-01da85b968a6}')
    @commethod(3)
    def GetOwnerReplicaId(self, pbReplicaId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRootItemId(self, pbRootItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeVersion(self, pbCurrentReplicaId: POINTER(Byte), pVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCreationVersion(self, pbCurrentReplicaId: POINTER(Byte), pVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWorkEstimate(self, pdwWork: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetChangeUnits(self, ppEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumSyncChangeUnits_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMadeWithKnowledge(self, ppMadeWithKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLearnedKnowledge(self, ppLearnedKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetWorkEstimate(self, dwWork: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatch(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncChangeBatchBase
    _iid_ = Guid('{70c64dee-380f-4c2e-8f70-31c55bd5f9b3}')
    @commethod(17)
    def BeginUnorderedGroup(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def EndUnorderedGroup(self, pMadeWithKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, fAllChangesForKnowledge: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddLoggedConflict(self, pbOwnerReplicaId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), dwFlags: UInt32, dwWorkForChange: UInt32, pConflictKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, ppChangeBuilder: POINTER(Windows.Win32.System.WindowsSync.ISyncChangeBuilder_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatch2(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncChangeBatch
    _iid_ = Guid('{225f4a33-f5ee-4cc7-b039-67a262b4b2ac}')
    @commethod(20)
    def AddMergeTombstoneMetadataToGroup(self, pbOwnerReplicaId: POINTER(Byte), pbWinnerItemId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), dwWorkForChange: UInt32, ppChangeBuilder: POINTER(Windows.Win32.System.WindowsSync.ISyncChangeBuilder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddMergeTombstoneLoggedConflict(self, pbOwnerReplicaId: POINTER(Byte), pbWinnerItemId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), dwWorkForChange: UInt32, pConflictKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, ppChangeBuilder: POINTER(Windows.Win32.System.WindowsSync.ISyncChangeBuilder_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchAdvanced(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0f1a4995-cbc8-421d-b550-5d0bebf3e9a5}')
    @commethod(3)
    def GetFilterInfo(self, ppFilterInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncFilterInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConvertFullEnumerationChangeBatchToRegularChangeBatch(self, ppChangeBatch: POINTER(Windows.Win32.System.WindowsSync.ISyncChangeBatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUpperBoundItemId(self, pbItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBatchLevelKnowledgeShouldBeApplied(self, pfBatchKnowledgeShouldBeApplied: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchBase(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52f6e694-6a71-4494-a184-a8311bf5d227}')
    @commethod(3)
    def GetChangeEnumerator(self, ppEnum: POINTER(Windows.Win32.System.WindowsSync.IEnumSyncChanges_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIsLastBatch(self, pfLastBatch: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetWorkEstimateForBatch(self, pdwWorkForBatch: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetRemainingWorkEstimateForSession(self, pdwRemainingWorkForSession: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginOrderedGroup(self, pbLowerBound: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EndOrderedGroup(self, pbUpperBound: POINTER(Byte), pMadeWithKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddItemMetadataToGroup(self, pbOwnerReplicaId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), dwFlags: UInt32, dwWorkForChange: UInt32, ppChangeBuilder: POINTER(Windows.Win32.System.WindowsSync.ISyncChangeBuilder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetLearnedKnowledge(self, ppLearnedKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPrerequisiteKnowledge(self, ppPrerequisteKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSourceForgottenKnowledge(self, ppSourceForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.IForgottenKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetLastBatch(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetWorkEstimateForBatch(self, dwWorkForBatch: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetRemainingWorkEstimateForSession(self, dwRemainingWorkForSession: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Serialize(self, pbChangeBatch: POINTER(Byte), pcbChangeBatch: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchBase2(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncChangeBatchBase
    _iid_ = Guid('{6fdb596a-d755-4584-bd0c-c0c23a548fbf}')
    @commethod(17)
    def SerializeWithOptions(self, targetFormatVersion: Windows.Win32.System.WindowsSync.SYNC_SERIALIZATION_VERSION, dwFlags: UInt32, pbBuffer: POINTER(Byte), pdwSerializedSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchWithFilterKeyMap(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de247002-566d-459a-a6ed-a5aab3459fb7}')
    @commethod(3)
    def GetFilterKeyMap(self, ppIFilterKeyMap: POINTER(Windows.Win32.System.WindowsSync.IFilterKeyMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFilterKeyMap(self, pIFilterKeyMap: Windows.Win32.System.WindowsSync.IFilterKeyMap_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFilterForgottenKnowledge(self, dwFilterKey: UInt32, pFilterForgottenKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFilteredReplicaLearnedKnowledge(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLearnedFilterForgottenKnowledge(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFilteredReplicaLearnedForgottenKnowledge(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBatchWithPrerequisite(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncChangeBatchBase
    _iid_ = Guid('{097f13be-5b92-4048-b3f2-7b42a2515e07}')
    @commethod(17)
    def SetPrerequisiteKnowledge(self, pPrerequisiteKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetLearnedKnowledgeWithPrerequisite(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, ppLearnedWithPrerequisiteKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetLearnedForgottenKnowledge(self, ppLearnedForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.IForgottenKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeBuilder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56f14771-8677-484f-a170-e386e418a676}')
    @commethod(3)
    def AddChangeUnitMetadata(self, pbChangeUnitId: POINTER(Byte), pChangeUnitVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeUnit(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{60edd8ca-7341-4bb7-95ce-fab6394b51cb}')
    @commethod(3)
    def GetItemChange(self, ppSyncChange: POINTER(Windows.Win32.System.WindowsSync.ISyncChange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChangeUnitId(self, pbChangeUnitId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChangeUnitVersion(self, pbCurrentReplicaId: POINTER(Byte), pVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeWithFilterKeyMap(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bfe1ef00-e87d-42fd-a4e9-242d70414aef}')
    @commethod(3)
    def GetFilterCount(self, pdwFilterCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFilterChange(self, dwFilterKey: UInt32, pFilterChange: POINTER(Windows.Win32.System.WindowsSync.SYNC_FILTER_CHANGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAllChangeUnitsPresentFlag(self, pfAllChangeUnitsPresent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFilterForgottenKnowledge(self, dwFilterKey: UInt32, ppIFilterForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFilteredReplicaLearnedKnowledge(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, ppLearnedKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetLearnedFilterForgottenKnowledge(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFilteredReplicaLearnedForgottenKnowledge(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFilteredReplicaLearnedForgottenKnowledgeAfterRecoveryComplete(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, ppLearnedForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLearnedFilterForgottenKnowledgeAfterRecoveryComplete(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pNewMoveins: Windows.Win32.System.WindowsSync.IEnumItemIds_head, dwFilterKey: UInt32, ppLearnedFilterForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncChangeWithPrerequisite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9e38382f-1589-48c3-92e4-05ecdcb4f3f7}')
    @commethod(3)
    def GetPrerequisiteKnowledge(self, ppPrerequisiteKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLearnedKnowledgeWithPrerequisite(self, pDestinationKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, ppLearnedKnowledgeWithPrerequisite: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncConstraintCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8af3843e-75b3-438c-bb51-6f020d70d3cb}')
    @commethod(3)
    def OnConstraintConflict(self, pConflict: Windows.Win32.System.WindowsSync.IConstraintConflict_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncDataConverter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{435d4861-68d5-44aa-a0f9-72a0b00ef9cf}')
    @commethod(3)
    def ConvertDataRetrieverFromProviderFormat(self, pUnkDataRetrieverIn: Windows.Win32.System.Com.IUnknown_head, pEnumSyncChanges: Windows.Win32.System.WindowsSync.IEnumSyncChanges_head, ppUnkDataOut: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConvertDataRetrieverToProviderFormat(self, pUnkDataRetrieverIn: Windows.Win32.System.Com.IUnknown_head, pEnumSyncChanges: Windows.Win32.System.WindowsSync.IEnumSyncChanges_head, ppUnkDataOut: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertDataFromProviderFormat(self, pDataContext: Windows.Win32.System.WindowsSync.ILoadChangeContext_head, pUnkDataIn: Windows.Win32.System.Com.IUnknown_head, ppUnkDataOut: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ConvertDataToProviderFormat(self, pDataContext: Windows.Win32.System.WindowsSync.ILoadChangeContext_head, pUnkDataOut: Windows.Win32.System.Com.IUnknown_head, ppUnkDataout: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncFilter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{087a3f15-0fcb-44c1-9639-53c14e2b5506}')
    @commethod(3)
    def IsIdentical(self, pSyncFilter: Windows.Win32.System.WindowsSync.ISyncFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Serialize(self, pbSyncFilter: POINTER(Byte), pcbSyncFilter: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncFilterDeserializer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b45b7a72-e5c7-46be-9c82-77b8b15dab8a}')
    @commethod(3)
    def DeserializeSyncFilter(self, pbSyncFilter: POINTER(Byte), dwCbSyncFilter: UInt32, ppISyncFilter: POINTER(Windows.Win32.System.WindowsSync.ISyncFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncFilterInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{794eaaf8-3f2e-47e6-9728-17e6fcf94cb7}')
    @commethod(3)
    def Serialize(self, pbBuffer: POINTER(Byte), pcbBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncFilterInfo2(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncFilterInfo
    _iid_ = Guid('{19b394ba-e3d0-468c-934d-321968b2ab34}')
    @commethod(4)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncFullEnumerationChange(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9785e0bd-bdff-40c4-98c5-b34b2f1991b3}')
    @commethod(3)
    def GetLearnedKnowledgeAfterRecoveryComplete(self, ppLearnedKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLearnedForgottenKnowledge(self, ppLearnedForgottenKnowledge: POINTER(Windows.Win32.System.WindowsSync.IForgottenKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncFullEnumerationChangeBatch(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncChangeBatchBase
    _iid_ = Guid('{ef64197d-4f44-4ea2-b355-4524713e3bed}')
    @commethod(17)
    def GetLearnedKnowledgeAfterRecoveryComplete(self, ppLearnedKnowledgeAfterRecoveryComplete: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetClosedLowerBoundItemId(self, pbClosedLowerBoundItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetClosedUpperBoundItemId(self, pbClosedUpperBoundItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncFullEnumerationChangeBatch2(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncFullEnumerationChangeBatch
    _iid_ = Guid('{e06449f4-a205-4b65-9724-01b22101eec1}')
    @commethod(20)
    def AddMergeTombstoneMetadataToGroup(self, pbOwnerReplicaId: POINTER(Byte), pbWinnerItemId: POINTER(Byte), pbItemId: POINTER(Byte), pChangeVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), pCreationVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), dwWorkForChange: UInt32, ppChangeBuilder: POINTER(Windows.Win32.System.WindowsSync.ISyncChangeBuilder_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncKnowledge(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{615bbb53-c945-4203-bf4b-2cb65919a0aa}')
    @commethod(3)
    def GetOwnerReplicaId(self, pbReplicaId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Serialize(self, fSerializeReplicaKeyMap: Windows.Win32.Foundation.BOOL, pbKnowledge: POINTER(Byte), pcbKnowledge: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetLocalTickCount(self, ullTickCount: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ContainsChange(self, pbVersionOwnerReplicaId: POINTER(Byte), pgidItemId: POINTER(Byte), pSyncVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ContainsChangeUnit(self, pbVersionOwnerReplicaId: POINTER(Byte), pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte), pSyncVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetScopeVector(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetReplicaKeyMap(self, ppReplicaKeyMap: POINTER(Windows.Win32.System.WindowsSync.IReplicaKeyMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Clone(self, ppClonedKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ConvertVersion(self, pKnowledgeIn: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pbCurrentOwnerId: POINTER(Byte), pVersionIn: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head), pbNewOwnerId: POINTER(Byte), pcbIdSize: POINTER(UInt32), pVersionOut: POINTER(Windows.Win32.System.WindowsSync.SYNC_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MapRemoteToLocal(self, pRemoteKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, ppMappedKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Union(self, pKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ProjectOntoItem(self, pbItemId: POINTER(Byte), ppKnowledgeOut: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ProjectOntoChangeUnit(self, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte), ppKnowledgeOut: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ProjectOntoRange(self, psrngSyncRange: POINTER(Windows.Win32.System.WindowsSync.SYNC_RANGE_head), ppKnowledgeOut: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ExcludeItem(self, pbItemId: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ExcludeChangeUnit(self, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ContainsKnowledge(self, pKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def FindMinTickCountForReplica(self, pbReplicaId: POINTER(Byte), pullReplicaTickCount: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetRangeExceptions(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetSingleItemExceptions(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetChangeUnitExceptions(self, riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def FindClockVectorForItem(self, pbItemId: POINTER(Byte), riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def FindClockVectorForChangeUnit(self, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte), riid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetVersion(self, pdwVersion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncKnowledge2(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncKnowledge
    _iid_ = Guid('{ed0addc0-3b4b-46a1-9a45-45661d2114c8}')
    @commethod(27)
    def GetIdParameters(self, pIdParameters: POINTER(Windows.Win32.System.WindowsSync.ID_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def ProjectOntoColumnSet(self, ppColumns: POINTER(POINTER(Byte)), count: UInt32, ppiKnowledgeOut: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SerializeWithOptions(self, targetFormatVersion: Windows.Win32.System.WindowsSync.SYNC_SERIALIZATION_VERSION, dwFlags: UInt32, pbBuffer: POINTER(Byte), pdwSerializedSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetLowestUncontainedId(self, piSyncKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge2_head, pbItemId: POINTER(Byte), pcbItemIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetInspector(self, riid: POINTER(Guid), ppiInspector: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetMinimumSupportedVersion(self, pVersion: POINTER(Windows.Win32.System.WindowsSync.SYNC_SERIALIZATION_VERSION)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetStatistics(self, which: Windows.Win32.System.WindowsSync.SYNC_STATISTICS, pValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def ContainsKnowledgeForItem(self, pKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pbItemId: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ContainsKnowledgeForChangeUnit(self, pKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pbItemId: POINTER(Byte), pbChangeUnitId: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def ProjectOntoKnowledgeWithPrerequisite(self, pPrerequisiteKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, pTemplateKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, ppProjectedKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Complement(self, pSyncKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head, ppComplementedKnowledge: POINTER(Windows.Win32.System.WindowsSync.ISyncKnowledge_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def IntersectsWithKnowledge(self, pSyncKnowledge: Windows.Win32.System.WindowsSync.ISyncKnowledge_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetKnowledgeCookie(self, ppKnowledgeCookie: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def CompareToKnowledgeCookie(self, pKnowledgeCookie: Windows.Win32.System.Com.IUnknown_head, pResult: POINTER(Windows.Win32.System.WindowsSync.KNOWLEDGE_COOKIE_COMPARISON_RESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncMergeTombstoneChange(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6ec62597-0903-484c-ad61-36d6e938f47b}')
    @commethod(3)
    def GetWinnerItemId(self, pbWinnerItemId: POINTER(Byte), pcbIdSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8f657056-2bce-4a17-8c68-c7bb7898b56f}')
    @commethod(3)
    def GetIdParameters(self, pIdParameters: POINTER(Windows.Win32.System.WindowsSync.ID_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncProviderConfigUI(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7b0705f6-cbcd-4071-ab05-3bdc364d4a0c}')
    @commethod(3)
    def Init(self, pguidInstanceId: POINTER(Guid), pguidContentType: POINTER(Guid), pConfigurationProperties: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRegisteredProperties(self, ppConfigUIProperties: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateAndRegisterNewSyncProvider(self, hwndParent: Windows.Win32.Foundation.HWND, pUnkContext: Windows.Win32.System.Com.IUnknown_head, ppProviderInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ModifySyncProvider(self, hwndParent: Windows.Win32.Foundation.HWND, pUnkContext: Windows.Win32.System.Com.IUnknown_head, pProviderInfo: Windows.Win32.System.WindowsSync.ISyncProviderInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncProviderConfigUIInfo(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    _iid_ = Guid('{214141ae-33d7-4d8d-8e37-f227e880ce50}')
    @commethod(8)
    def GetSyncProviderConfigUI(self, dwClsContext: UInt32, ppSyncProviderConfigUI: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderConfigUI_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncProviderInfo(ComPtr):
    extends: Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore
    _iid_ = Guid('{1ee135de-88a4-4504-b0d0-f7920d7e5ba6}')
    @commethod(8)
    def GetSyncProvider(self, dwClsContext: UInt32, ppSyncProvider: POINTER(Windows.Win32.System.WindowsSync.IRegisteredSyncProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncProviderRegistration(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cb45953b-7624-47bc-a472-eb8cac6b222e}')
    @commethod(3)
    def CreateSyncProviderConfigUIRegistrationInstance(self, pConfigUIConfig: POINTER(Windows.Win32.System.WindowsSync.SyncProviderConfigUIConfiguration_head), ppConfigUIInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderConfigUIInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterSyncProviderConfigUI(self, pguidInstanceId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumerateSyncProviderConfigUIs(self, pguidContentType: POINTER(Guid), dwSupportedArchitecture: UInt32, ppEnumSyncProviderConfigUIInfos: POINTER(Windows.Win32.System.WindowsSync.IEnumSyncProviderConfigUIInfos_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateSyncProviderRegistrationInstance(self, pProviderConfiguration: POINTER(Windows.Win32.System.WindowsSync.SyncProviderConfiguration_head), ppProviderInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterSyncProvider(self, pguidInstanceId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSyncProviderConfigUIInfoforProvider(self, pguidProviderInstanceId: POINTER(Guid), ppProviderConfigUIInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderConfigUIInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumerateSyncProviders(self, pguidContentType: POINTER(Guid), dwStateFlagsToFilterMask: UInt32, dwStateFlagsToFilter: UInt32, refProviderClsId: POINTER(Guid), dwSupportedArchitecture: UInt32, ppEnumSyncProviderInfos: POINTER(Windows.Win32.System.WindowsSync.IEnumSyncProviderInfos_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSyncProviderInfo(self, pguidInstanceId: POINTER(Guid), ppProviderInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSyncProviderFromInstanceId(self, pguidInstanceId: POINTER(Guid), dwClsContext: UInt32, ppSyncProvider: POINTER(Windows.Win32.System.WindowsSync.IRegisteredSyncProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSyncProviderConfigUIInfo(self, pguidInstanceId: POINTER(Guid), ppConfigUIInfo: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderConfigUIInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSyncProviderConfigUIFromInstanceId(self, pguidInstanceId: POINTER(Guid), dwClsContext: UInt32, ppConfigUI: POINTER(Windows.Win32.System.WindowsSync.ISyncProviderConfigUI_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSyncProviderState(self, pguidInstanceId: POINTER(Guid), pdwStateFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetSyncProviderState(self, pguidInstanceId: POINTER(Guid), dwStateFlagsMask: UInt32, dwStateFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterForEvent(self, phEvent: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RevokeEvent(self, hEvent: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetChange(self, hEvent: Windows.Win32.Foundation.HANDLE, ppChange: POINTER(Windows.Win32.System.WindowsSync.ISyncRegistrationChange_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncRegistrationChange(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eea0d9ae-6b29-43b4-9e70-e3ae33bb2c3b}')
    @commethod(3)
    def GetEvent(self, psreEvent: POINTER(Windows.Win32.System.WindowsSync.SYNC_REGISTRATION_EVENT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInstanceId(self, pguidInstanceId: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncSessionExtendedErrorInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{326c6810-790a-409b-b741-6999388761eb}')
    @commethod(3)
    def GetSyncProviderWithError(self, ppProviderWithError: POINTER(Windows.Win32.System.WindowsSync.ISyncProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncSessionState(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b8a940fe-9f01-483b-9434-c37d361225d9}')
    @commethod(3)
    def IsCanceled(self, pfIsCanceled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInfoForChangeApplication(self, pbChangeApplierInfo: POINTER(Byte), pcbChangeApplierInfo: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadInfoFromChangeApplication(self, pbChangeApplierInfo: POINTER(Byte), cbChangeApplierInfo: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetForgottenKnowledgeRecoveryRangeStart(self, pbRangeStart: POINTER(Byte), pcbRangeStart: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetForgottenKnowledgeRecoveryRangeEnd(self, pbRangeEnd: POINTER(Byte), pcbRangeEnd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetForgottenKnowledgeRecoveryRange(self, pRange: POINTER(Windows.Win32.System.WindowsSync.SYNC_RANGE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnProgress(self, provider: Windows.Win32.System.WindowsSync.SYNC_PROVIDER_ROLE, syncStage: Windows.Win32.System.WindowsSync.SYNC_PROGRESS_STAGE, dwCompletedWork: UInt32, dwTotalWork: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISyncSessionState2(ComPtr):
    extends: Windows.Win32.System.WindowsSync.ISyncSessionState
    _iid_ = Guid('{9e37cfa3-9e38-4c61-9ca3-ffe810b45ca2}')
    @commethod(10)
    def SetProviderWithError(self, fSelf: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSessionErrorStatus(self, phrSessionError: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class ISynchronousDataRetriever(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b22f2a9-a4cd-4648-9d8e-3a510d4da04b}')
    @commethod(3)
    def GetIdParameters(self, pIdParameters: POINTER(Windows.Win32.System.WindowsSync.ID_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadChangeData(self, pLoadChangeContext: Windows.Win32.System.WindowsSync.ILoadChangeContext_head, ppUnkData: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
KNOWLEDGE_COOKIE_COMPARISON_RESULT = Int32
KCCR_COOKIE_KNOWLEDGE_EQUAL: KNOWLEDGE_COOKIE_COMPARISON_RESULT = 0
KCCR_COOKIE_KNOWLEDGE_CONTAINED: KNOWLEDGE_COOKIE_COMPARISON_RESULT = 1
KCCR_COOKIE_KNOWLEDGE_CONTAINS: KNOWLEDGE_COOKIE_COMPARISON_RESULT = 2
KCCR_COOKIE_KNOWLEDGE_NOT_COMPARABLE: KNOWLEDGE_COOKIE_COMPARISON_RESULT = 3
SYNC_CONSTRAINT_RESOLVE_ACTION = Int32
SCRA_DEFER: SYNC_CONSTRAINT_RESOLVE_ACTION = 0
SCRA_ACCEPT_DESTINATION_PROVIDER: SYNC_CONSTRAINT_RESOLVE_ACTION = 1
SCRA_ACCEPT_SOURCE_PROVIDER: SYNC_CONSTRAINT_RESOLVE_ACTION = 2
SCRA_TRANSFER_AND_DEFER: SYNC_CONSTRAINT_RESOLVE_ACTION = 3
SCRA_MERGE: SYNC_CONSTRAINT_RESOLVE_ACTION = 4
SCRA_RENAME_SOURCE: SYNC_CONSTRAINT_RESOLVE_ACTION = 5
SCRA_RENAME_DESTINATION: SYNC_CONSTRAINT_RESOLVE_ACTION = 6
class SYNC_FILTER_CHANGE(EasyCastStructure):
    fMoveIn: Windows.Win32.Foundation.BOOL
    moveVersion: Windows.Win32.System.WindowsSync.SYNC_VERSION
SYNC_FULL_ENUMERATION_ACTION = Int32
SFEA_FULL_ENUMERATION: SYNC_FULL_ENUMERATION_ACTION = 0
SFEA_PARTIAL_SYNC: SYNC_FULL_ENUMERATION_ACTION = 1
SFEA_ABORT: SYNC_FULL_ENUMERATION_ACTION = 2
SYNC_PROGRESS_STAGE = Int32
SPS_CHANGE_DETECTION: SYNC_PROGRESS_STAGE = 0
SPS_CHANGE_ENUMERATION: SYNC_PROGRESS_STAGE = 1
SPS_CHANGE_APPLICATION: SYNC_PROGRESS_STAGE = 2
SYNC_PROVIDER_ROLE = Int32
SPR_SOURCE: SYNC_PROVIDER_ROLE = 0
SPR_DESTINATION: SYNC_PROVIDER_ROLE = 1
class SYNC_RANGE(EasyCastStructure):
    pbClosedLowerBound: POINTER(Byte)
    pbClosedUpperBound: POINTER(Byte)
SYNC_REGISTRATION_EVENT = Int32
SRE_PROVIDER_ADDED: SYNC_REGISTRATION_EVENT = 0
SRE_PROVIDER_REMOVED: SYNC_REGISTRATION_EVENT = 1
SRE_PROVIDER_UPDATED: SYNC_REGISTRATION_EVENT = 2
SRE_PROVIDER_STATE_CHANGED: SYNC_REGISTRATION_EVENT = 3
SRE_CONFIGUI_ADDED: SYNC_REGISTRATION_EVENT = 4
SRE_CONFIGUI_REMOVED: SYNC_REGISTRATION_EVENT = 5
SRE_CONFIGUI_UPDATED: SYNC_REGISTRATION_EVENT = 6
SYNC_RESOLVE_ACTION = Int32
SRA_DEFER: SYNC_RESOLVE_ACTION = 0
SRA_ACCEPT_DESTINATION_PROVIDER: SYNC_RESOLVE_ACTION = 1
SRA_ACCEPT_SOURCE_PROVIDER: SYNC_RESOLVE_ACTION = 2
SRA_MERGE: SYNC_RESOLVE_ACTION = 3
SRA_TRANSFER_AND_DEFER: SYNC_RESOLVE_ACTION = 4
SRA_LAST: SYNC_RESOLVE_ACTION = 5
SYNC_SERIALIZATION_VERSION = Int32
SYNC_SERIALIZATION_VERSION_V1: SYNC_SERIALIZATION_VERSION = 1
SYNC_SERIALIZATION_VERSION_V2: SYNC_SERIALIZATION_VERSION = 4
SYNC_SERIALIZATION_VERSION_V3: SYNC_SERIALIZATION_VERSION = 5
class SYNC_SESSION_STATISTICS(EasyCastStructure):
    dwChangesApplied: UInt32
    dwChangesFailed: UInt32
SYNC_STATISTICS = Int32
SYNC_STATISTICS_RANGE_COUNT: SYNC_STATISTICS = 0
class SYNC_TIME(EasyCastStructure):
    dwDate: UInt32
    dwTime: UInt32
class SYNC_VERSION(EasyCastStructure):
    dwLastUpdatingReplicaKey: UInt32
    ullTickCount: UInt64
class SyncProviderConfigUIConfiguration(EasyCastStructure):
    dwVersion: UInt32
    guidInstanceId: Guid
    clsidConfigUI: Guid
    guidContentType: Guid
    dwCapabilities: UInt32
    dwSupportedArchitecture: UInt32
    fIsGlobal: Windows.Win32.Foundation.BOOL
class SyncProviderConfiguration(EasyCastStructure):
    dwVersion: UInt32
    guidInstanceId: Guid
    clsidProvider: Guid
    guidConfigUIInstanceId: Guid
    guidContentType: Guid
    dwCapabilities: UInt32
    dwSupportedArchitecture: UInt32
SyncProviderRegistration = Guid('{f82b4ef1-93a9-4dde-8015-f7950a1a6e31}')
make_head(_module, 'PKEY_PROVIDER_INSTANCEID')
make_head(_module, 'PKEY_PROVIDER_CLSID')
make_head(_module, 'PKEY_PROVIDER_CONFIGUI')
make_head(_module, 'PKEY_PROVIDER_CONTENTTYPE')
make_head(_module, 'PKEY_PROVIDER_CAPABILITIES')
make_head(_module, 'PKEY_PROVIDER_SUPPORTED_ARCHITECTURE')
make_head(_module, 'PKEY_PROVIDER_NAME')
make_head(_module, 'PKEY_PROVIDER_DESCRIPTION')
make_head(_module, 'PKEY_PROVIDER_TOOLTIPS')
make_head(_module, 'PKEY_PROVIDER_ICON')
make_head(_module, 'PKEY_CONFIGUI_INSTANCEID')
make_head(_module, 'PKEY_CONFIGUI_CLSID')
make_head(_module, 'PKEY_CONFIGUI_CONTENTTYPE')
make_head(_module, 'PKEY_CONFIGUI_CAPABILITIES')
make_head(_module, 'PKEY_CONFIGUI_SUPPORTED_ARCHITECTURE')
make_head(_module, 'PKEY_CONFIGUI_IS_GLOBAL')
make_head(_module, 'PKEY_CONFIGUI_NAME')
make_head(_module, 'PKEY_CONFIGUI_DESCRIPTION')
make_head(_module, 'PKEY_CONFIGUI_TOOLTIPS')
make_head(_module, 'PKEY_CONFIGUI_ICON')
make_head(_module, 'PKEY_CONFIGUI_MENUITEM_NOUI')
make_head(_module, 'PKEY_CONFIGUI_MENUITEM')
make_head(_module, 'IAsynchronousDataRetriever')
make_head(_module, 'IChangeConflict')
make_head(_module, 'IChangeUnitException')
make_head(_module, 'IChangeUnitListFilterInfo')
make_head(_module, 'IClockVector')
make_head(_module, 'IClockVectorElement')
make_head(_module, 'ICombinedFilterInfo')
make_head(_module, 'IConstraintConflict')
make_head(_module, 'IConstructReplicaKeyMap')
make_head(_module, 'ICoreFragment')
make_head(_module, 'ICoreFragmentInspector')
make_head(_module, 'ICustomFilterInfo')
make_head(_module, 'ID_PARAMETERS')
make_head(_module, 'ID_PARAMETER_PAIR')
make_head(_module, 'IDataRetrieverCallback')
make_head(_module, 'IEnumChangeUnitExceptions')
make_head(_module, 'IEnumClockVector')
make_head(_module, 'IEnumFeedClockVector')
make_head(_module, 'IEnumItemIds')
make_head(_module, 'IEnumRangeExceptions')
make_head(_module, 'IEnumSingleItemExceptions')
make_head(_module, 'IEnumSyncChangeUnits')
make_head(_module, 'IEnumSyncChanges')
make_head(_module, 'IEnumSyncProviderConfigUIInfos')
make_head(_module, 'IEnumSyncProviderInfos')
make_head(_module, 'IFeedClockVector')
make_head(_module, 'IFeedClockVectorElement')
make_head(_module, 'IFilterKeyMap')
make_head(_module, 'IFilterRequestCallback')
make_head(_module, 'IFilterTrackingProvider')
make_head(_module, 'IFilterTrackingRequestCallback')
make_head(_module, 'IFilterTrackingSyncChangeBuilder')
make_head(_module, 'IForgottenKnowledge')
make_head(_module, 'IKnowledgeSyncProvider')
make_head(_module, 'ILoadChangeContext')
make_head(_module, 'IProviderConverter')
make_head(_module, 'IRangeException')
make_head(_module, 'IRecoverableError')
make_head(_module, 'IRecoverableErrorData')
make_head(_module, 'IRegisteredSyncProvider')
make_head(_module, 'IReplicaKeyMap')
make_head(_module, 'IRequestFilteredSync')
make_head(_module, 'ISingleItemException')
make_head(_module, 'ISupportFilteredSync')
make_head(_module, 'ISupportLastWriteTime')
make_head(_module, 'ISyncCallback')
make_head(_module, 'ISyncCallback2')
make_head(_module, 'ISyncChange')
make_head(_module, 'ISyncChangeBatch')
make_head(_module, 'ISyncChangeBatch2')
make_head(_module, 'ISyncChangeBatchAdvanced')
make_head(_module, 'ISyncChangeBatchBase')
make_head(_module, 'ISyncChangeBatchBase2')
make_head(_module, 'ISyncChangeBatchWithFilterKeyMap')
make_head(_module, 'ISyncChangeBatchWithPrerequisite')
make_head(_module, 'ISyncChangeBuilder')
make_head(_module, 'ISyncChangeUnit')
make_head(_module, 'ISyncChangeWithFilterKeyMap')
make_head(_module, 'ISyncChangeWithPrerequisite')
make_head(_module, 'ISyncConstraintCallback')
make_head(_module, 'ISyncDataConverter')
make_head(_module, 'ISyncFilter')
make_head(_module, 'ISyncFilterDeserializer')
make_head(_module, 'ISyncFilterInfo')
make_head(_module, 'ISyncFilterInfo2')
make_head(_module, 'ISyncFullEnumerationChange')
make_head(_module, 'ISyncFullEnumerationChangeBatch')
make_head(_module, 'ISyncFullEnumerationChangeBatch2')
make_head(_module, 'ISyncKnowledge')
make_head(_module, 'ISyncKnowledge2')
make_head(_module, 'ISyncMergeTombstoneChange')
make_head(_module, 'ISyncProvider')
make_head(_module, 'ISyncProviderConfigUI')
make_head(_module, 'ISyncProviderConfigUIInfo')
make_head(_module, 'ISyncProviderInfo')
make_head(_module, 'ISyncProviderRegistration')
make_head(_module, 'ISyncRegistrationChange')
make_head(_module, 'ISyncSessionExtendedErrorInfo')
make_head(_module, 'ISyncSessionState')
make_head(_module, 'ISyncSessionState2')
make_head(_module, 'ISynchronousDataRetriever')
make_head(_module, 'SYNC_FILTER_CHANGE')
make_head(_module, 'SYNC_RANGE')
make_head(_module, 'SYNC_SESSION_STATISTICS')
make_head(_module, 'SYNC_TIME')
make_head(_module, 'SYNC_VERSION')
make_head(_module, 'SyncProviderConfigUIConfiguration')
make_head(_module, 'SyncProviderConfiguration')
