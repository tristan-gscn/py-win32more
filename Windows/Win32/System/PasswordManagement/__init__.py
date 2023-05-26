from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.PasswordManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('ADVAPI32.dll')
def MSChapSrvChangePassword(ServerName: Windows.Win32.Foundation.PWSTR, UserName: Windows.Win32.Foundation.PWSTR, LmOldPresent: Windows.Win32.Foundation.BOOLEAN, LmOldOwfPassword: POINTER(Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD_head), LmNewOwfPassword: POINTER(Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD_head), NtOldOwfPassword: POINTER(Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD_head), NtNewOwfPassword: POINTER(Windows.Win32.System.PasswordManagement.LM_OWF_PASSWORD_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def MSChapSrvChangePassword2(ServerName: Windows.Win32.Foundation.PWSTR, UserName: Windows.Win32.Foundation.PWSTR, NewPasswordEncryptedWithOldNt: POINTER(Windows.Win32.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head), OldNtOwfPasswordEncryptedWithNewNt: POINTER(Windows.Win32.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head), LmPresent: Windows.Win32.Foundation.BOOLEAN, NewPasswordEncryptedWithOldLm: POINTER(Windows.Win32.System.PasswordManagement.SAMPR_ENCRYPTED_USER_PASSWORD_head), OldLmOwfPasswordEncryptedWithNewLmOrNt: POINTER(Windows.Win32.System.PasswordManagement.ENCRYPTED_LM_OWF_PASSWORD_head)) -> UInt32: ...
class CYPHER_BLOCK(EasyCastStructure):
    data: Windows.Win32.Foundation.CHAR * 8
class ENCRYPTED_LM_OWF_PASSWORD(EasyCastStructure):
    data: Windows.Win32.System.PasswordManagement.CYPHER_BLOCK * 2
class LM_OWF_PASSWORD(EasyCastStructure):
    data: Windows.Win32.System.PasswordManagement.CYPHER_BLOCK * 2
class SAMPR_ENCRYPTED_USER_PASSWORD(EasyCastStructure):
    Buffer: Byte * 516
make_head(_module, 'CYPHER_BLOCK')
make_head(_module, 'ENCRYPTED_LM_OWF_PASSWORD')
make_head(_module, 'LM_OWF_PASSWORD')
make_head(_module, 'SAMPR_ENCRYPTED_USER_PASSWORD')
