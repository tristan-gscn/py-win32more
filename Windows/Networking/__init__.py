from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Networking
import Windows.Networking.Connectivity
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DomainNameType = Int32
DomainNameType_Suffix: DomainNameType = 0
DomainNameType_FullyQualified: DomainNameType = 1
class EndpointPair(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.EndpointPair'
    @winrt_factorymethod
    def CreateEndpointPair(cls: Windows.Networking.IEndpointPairFactory, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Networking.EndpointPair: ...
    @winrt_mixinmethod
    def get_LocalHostName(self: Windows.Networking.IEndpointPair) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_LocalHostName(self: Windows.Networking.IEndpointPair, value: Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_LocalServiceName(self: Windows.Networking.IEndpointPair) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LocalServiceName(self: Windows.Networking.IEndpointPair, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteHostName(self: Windows.Networking.IEndpointPair) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def put_RemoteHostName(self: Windows.Networking.IEndpointPair, value: Windows.Networking.HostName) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteServiceName(self: Windows.Networking.IEndpointPair) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteServiceName(self: Windows.Networking.IEndpointPair, value: WinRT_String) -> Void: ...
    LocalHostName = property(get_LocalHostName, put_LocalHostName)
    LocalServiceName = property(get_LocalServiceName, put_LocalServiceName)
    RemoteHostName = property(get_RemoteHostName, put_RemoteHostName)
    RemoteServiceName = property(get_RemoteServiceName, put_RemoteServiceName)
class HostName(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Networking.HostName'
    @winrt_factorymethod
    def CreateHostName(cls: Windows.Networking.IHostNameFactory, hostName: WinRT_String) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_IPInformation(self: Windows.Networking.IHostName) -> Windows.Networking.Connectivity.IPInformation: ...
    @winrt_mixinmethod
    def get_RawName(self: Windows.Networking.IHostName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Networking.IHostName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CanonicalName(self: Windows.Networking.IHostName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Networking.IHostName) -> Windows.Networking.HostNameType: ...
    @winrt_mixinmethod
    def IsEqual(self: Windows.Networking.IHostName, hostName: Windows.Networking.HostName) -> Boolean: ...
    @winrt_mixinmethod
    def ToString(self: Windows.Foundation.IStringable) -> WinRT_String: ...
    @winrt_classmethod
    def Compare(cls: Windows.Networking.IHostNameStatics, value1: WinRT_String, value2: WinRT_String) -> Int32: ...
    IPInformation = property(get_IPInformation, None)
    RawName = property(get_RawName, None)
    DisplayName = property(get_DisplayName, None)
    CanonicalName = property(get_CanonicalName, None)
    Type = property(get_Type, None)
HostNameSortOptions = UInt32
HostNameSortOptions_None: HostNameSortOptions = 0
HostNameSortOptions_OptimizeForLongConnections: HostNameSortOptions = 2
HostNameType = Int32
HostNameType_DomainName: HostNameType = 0
HostNameType_Ipv4: HostNameType = 1
HostNameType_Ipv6: HostNameType = 2
HostNameType_Bluetooth: HostNameType = 3
class IEndpointPair(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('33a0aa36-f8fa-4b30-b8-56-76-51-7c-3b-d0-6d')
    @winrt_commethod(6)
    def get_LocalHostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(7)
    def put_LocalHostName(self, value: Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(8)
    def get_LocalServiceName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_LocalServiceName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_RemoteHostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(11)
    def put_RemoteHostName(self, value: Windows.Networking.HostName) -> Void: ...
    @winrt_commethod(12)
    def get_RemoteServiceName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_RemoteServiceName(self, value: WinRT_String) -> Void: ...
    LocalHostName = property(get_LocalHostName, put_LocalHostName)
    LocalServiceName = property(get_LocalServiceName, put_LocalServiceName)
    RemoteHostName = property(get_RemoteHostName, put_RemoteHostName)
    RemoteServiceName = property(get_RemoteServiceName, put_RemoteServiceName)
class IEndpointPairFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b609d971-64e0-442b-aa-6f-cc-8c-8f-18-1f-78')
    @winrt_commethod(6)
    def CreateEndpointPair(self, localHostName: Windows.Networking.HostName, localServiceName: WinRT_String, remoteHostName: Windows.Networking.HostName, remoteServiceName: WinRT_String) -> Windows.Networking.EndpointPair: ...
class IHostName(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bf8ecaad-ed96-49a7-90-84-d4-16-ca-e8-8d-cb')
    @winrt_commethod(6)
    def get_IPInformation(self) -> Windows.Networking.Connectivity.IPInformation: ...
    @winrt_commethod(7)
    def get_RawName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CanonicalName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Type(self) -> Windows.Networking.HostNameType: ...
    @winrt_commethod(11)
    def IsEqual(self, hostName: Windows.Networking.HostName) -> Boolean: ...
    IPInformation = property(get_IPInformation, None)
    RawName = property(get_RawName, None)
    DisplayName = property(get_DisplayName, None)
    CanonicalName = property(get_CanonicalName, None)
    Type = property(get_Type, None)
class IHostNameFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('458c23ed-712f-4576-ad-f1-c2-0b-2c-64-35-58')
    @winrt_commethod(6)
    def CreateHostName(self, hostName: WinRT_String) -> Windows.Networking.HostName: ...
class IHostNameStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f68cd4bf-a388-4e8b-91-ea-54-dd-6d-d9-01-c0')
    @winrt_commethod(6)
    def Compare(self, value1: WinRT_String, value2: WinRT_String) -> Int32: ...
make_head(_module, 'EndpointPair')
make_head(_module, 'HostName')
make_head(_module, 'IEndpointPair')
make_head(_module, 'IEndpointPairFactory')
make_head(_module, 'IHostName')
make_head(_module, 'IHostNameFactory')
make_head(_module, 'IHostNameStatics')
