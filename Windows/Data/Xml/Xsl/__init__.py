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
import Windows.Data.Xml.Dom
import Windows.Data.Xml.Xsl
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IXsltProcessor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7b64703f-550c-48c6-a9-0f-93-a5-b9-64-51-8f')
    @winrt_commethod(6)
    def TransformToString(self, inputNode: Windows.Data.Xml.Dom.IXmlNode) -> WinRT_String: ...
class IXsltProcessor2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8da45c56-97a5-44cb-a8-be-27-d8-62-80-c7-0a')
    @winrt_commethod(6)
    def TransformToDocument(self, inputNode: Windows.Data.Xml.Dom.IXmlNode) -> Windows.Data.Xml.Dom.XmlDocument: ...
class IXsltProcessorFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('274146c0-9a51-4663-bf-30-0e-f7-42-14-6f-20')
    @winrt_commethod(6)
    def CreateInstance(self, document: Windows.Data.Xml.Dom.XmlDocument) -> Windows.Data.Xml.Xsl.XsltProcessor: ...
class XsltProcessor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Data.Xml.Xsl.XsltProcessor'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Data.Xml.Xsl.IXsltProcessorFactory, document: Windows.Data.Xml.Dom.XmlDocument) -> Windows.Data.Xml.Xsl.XsltProcessor: ...
    @winrt_mixinmethod
    def TransformToString(self: Windows.Data.Xml.Xsl.IXsltProcessor, inputNode: Windows.Data.Xml.Dom.IXmlNode) -> WinRT_String: ...
    @winrt_mixinmethod
    def TransformToDocument(self: Windows.Data.Xml.Xsl.IXsltProcessor2, inputNode: Windows.Data.Xml.Dom.IXmlNode) -> Windows.Data.Xml.Dom.XmlDocument: ...
make_head(_module, 'IXsltProcessor')
make_head(_module, 'IXsltProcessor2')
make_head(_module, 'IXsltProcessorFactory')
make_head(_module, 'XsltProcessor')
