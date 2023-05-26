from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.SubsystemForLinux
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslIsDistributionRegistered(distributionName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslRegisterDistribution(distributionName: Windows.Win32.Foundation.PWSTR, tarGzFilename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslUnregisterDistribution(distributionName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslConfigureDistribution(distributionName: Windows.Win32.Foundation.PWSTR, defaultUID: UInt32, wslDistributionFlags: Windows.Win32.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslGetDistributionConfiguration(distributionName: Windows.Win32.Foundation.PWSTR, distributionVersion: POINTER(UInt32), defaultUID: POINTER(UInt32), wslDistributionFlags: POINTER(Windows.Win32.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS), defaultEnvironmentVariables: POINTER(POINTER(Windows.Win32.Foundation.PSTR)), defaultEnvironmentVariableCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslLaunchInteractive(distributionName: Windows.Win32.Foundation.PWSTR, command: Windows.Win32.Foundation.PWSTR, useCurrentWorkingDirectory: Windows.Win32.Foundation.BOOL, exitCode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslLaunch(distributionName: Windows.Win32.Foundation.PWSTR, command: Windows.Win32.Foundation.PWSTR, useCurrentWorkingDirectory: Windows.Win32.Foundation.BOOL, stdIn: Windows.Win32.Foundation.HANDLE, stdOut: Windows.Win32.Foundation.HANDLE, stdErr: Windows.Win32.Foundation.HANDLE, process: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
WSL_DISTRIBUTION_FLAGS = Int32
WSL_DISTRIBUTION_FLAGS_NONE: WSL_DISTRIBUTION_FLAGS = 0
WSL_DISTRIBUTION_FLAGS_ENABLE_INTEROP: WSL_DISTRIBUTION_FLAGS = 1
WSL_DISTRIBUTION_FLAGS_APPEND_NT_PATH: WSL_DISTRIBUTION_FLAGS = 2
WSL_DISTRIBUTION_FLAGS_ENABLE_DRIVE_MOUNTING: WSL_DISTRIBUTION_FLAGS = 4
