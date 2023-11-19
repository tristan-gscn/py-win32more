from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Composition.Diagnostics
class CompositionDebugHeatMaps(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.CompositionDebugHeatMaps'
    @winrt_mixinmethod
    def Hide(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def ShowRedraw(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def ShowMemoryUsage(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_mixinmethod
    def ShowOverdraw(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps, subtree: win32more.Microsoft.UI.Composition.Visual, contentKinds: win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugOverdrawContentKinds) -> Void: ...
CompositionDebugOverdrawContentKinds = UInt32
CompositionDebugOverdrawContentKinds_None: CompositionDebugOverdrawContentKinds = 0
CompositionDebugOverdrawContentKinds_OffscreenRendered: CompositionDebugOverdrawContentKinds = 1
CompositionDebugOverdrawContentKinds_Colors: CompositionDebugOverdrawContentKinds = 2
CompositionDebugOverdrawContentKinds_Effects: CompositionDebugOverdrawContentKinds = 4
CompositionDebugOverdrawContentKinds_Shadows: CompositionDebugOverdrawContentKinds = 8
CompositionDebugOverdrawContentKinds_Lights: CompositionDebugOverdrawContentKinds = 16
CompositionDebugOverdrawContentKinds_Surfaces: CompositionDebugOverdrawContentKinds = 32
CompositionDebugOverdrawContentKinds_SwapChains: CompositionDebugOverdrawContentKinds = 64
CompositionDebugOverdrawContentKinds_All: CompositionDebugOverdrawContentKinds = 4294967295
class CompositionDebugSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettings
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.CompositionDebugSettings'
    @winrt_mixinmethod
    def get_HeatMaps(self: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettings) -> win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugHeatMaps: ...
    @winrt_classmethod
    def TryGetSettings(cls: win32more.Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettingsStatics, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugSettings: ...
    HeatMaps = property(get_HeatMaps, None)
class ICompositionDebugHeatMaps(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.ICompositionDebugHeatMaps'
    _iid_ = Guid('{815016b8-f645-5c55-87b5-fe2167282b6f}')
    @winrt_commethod(6)
    def Hide(self, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(7)
    def ShowMemoryUsage(self, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(8)
    def ShowOverdraw(self, subtree: win32more.Microsoft.UI.Composition.Visual, contentKinds: win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugOverdrawContentKinds) -> Void: ...
    @winrt_commethod(9)
    def ShowRedraw(self, subtree: win32more.Microsoft.UI.Composition.Visual) -> Void: ...
class ICompositionDebugSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettings'
    _iid_ = Guid('{f4c0c0f6-7f5f-5014-a0d6-c8c7eeecace6}')
    @winrt_commethod(6)
    def get_HeatMaps(self) -> win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugHeatMaps: ...
    HeatMaps = property(get_HeatMaps, None)
class ICompositionDebugSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.Diagnostics.ICompositionDebugSettingsStatics'
    _iid_ = Guid('{b56f8aab-2b8c-51aa-b974-10e5c517f50e}')
    @winrt_commethod(6)
    def TryGetSettings(self, compositor: win32more.Microsoft.UI.Composition.Compositor) -> win32more.Microsoft.UI.Composition.Diagnostics.CompositionDebugSettings: ...
make_ready(__name__)
