from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.Mailslots
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('KERNEL32.dll')
def CreateMailslotA(lpName: Windows.Win32.Foundation.PSTR, nMaxMessageSize: UInt32, lReadTimeout: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateMailslotW(lpName: Windows.Win32.Foundation.PWSTR, nMaxMessageSize: UInt32, lReadTimeout: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetMailslotInfo(hMailslot: Windows.Win32.Foundation.HANDLE, lpMaxMessageSize: POINTER(UInt32), lpNextSize: POINTER(UInt32), lpMessageCount: POINTER(UInt32), lpReadTimeout: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetMailslotInfo(hMailslot: Windows.Win32.Foundation.HANDLE, lReadTimeout: UInt32) -> Windows.Win32.Foundation.BOOL: ...
