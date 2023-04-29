from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.System.Power
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class BackgroundEnergyManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Power.BackgroundEnergyManager'
    @winrt_classmethod
    def get_LowUsageLevel(cls: Windows.System.Power.IBackgroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_NearMaxAcceptableUsageLevel(cls: Windows.System.Power.IBackgroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_MaxAcceptableUsageLevel(cls: Windows.System.Power.IBackgroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_ExcessiveUsageLevel(cls: Windows.System.Power.IBackgroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_NearTerminationUsageLevel(cls: Windows.System.Power.IBackgroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_TerminationUsageLevel(cls: Windows.System.Power.IBackgroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_RecentEnergyUsage(cls: Windows.System.Power.IBackgroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_RecentEnergyUsageLevel(cls: Windows.System.Power.IBackgroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def add_RecentEnergyUsageIncreased(cls: Windows.System.Power.IBackgroundEnergyManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RecentEnergyUsageIncreased(cls: Windows.System.Power.IBackgroundEnergyManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_RecentEnergyUsageReturnedToLow(cls: Windows.System.Power.IBackgroundEnergyManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RecentEnergyUsageReturnedToLow(cls: Windows.System.Power.IBackgroundEnergyManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    LowUsageLevel = property(get_LowUsageLevel, None)
    NearMaxAcceptableUsageLevel = property(get_NearMaxAcceptableUsageLevel, None)
    MaxAcceptableUsageLevel = property(get_MaxAcceptableUsageLevel, None)
    ExcessiveUsageLevel = property(get_ExcessiveUsageLevel, None)
    NearTerminationUsageLevel = property(get_NearTerminationUsageLevel, None)
    TerminationUsageLevel = property(get_TerminationUsageLevel, None)
    RecentEnergyUsage = property(get_RecentEnergyUsage, None)
    RecentEnergyUsageLevel = property(get_RecentEnergyUsageLevel, None)
BatteryStatus = Int32
BatteryStatus_NotPresent: BatteryStatus = 0
BatteryStatus_Discharging: BatteryStatus = 1
BatteryStatus_Idle: BatteryStatus = 2
BatteryStatus_Charging: BatteryStatus = 3
EnergySaverStatus = Int32
EnergySaverStatus_Disabled: EnergySaverStatus = 0
EnergySaverStatus_Off: EnergySaverStatus = 1
EnergySaverStatus_On: EnergySaverStatus = 2
class ForegroundEnergyManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Power.ForegroundEnergyManager'
    @winrt_classmethod
    def get_LowUsageLevel(cls: Windows.System.Power.IForegroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_NearMaxAcceptableUsageLevel(cls: Windows.System.Power.IForegroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_MaxAcceptableUsageLevel(cls: Windows.System.Power.IForegroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_ExcessiveUsageLevel(cls: Windows.System.Power.IForegroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_RecentEnergyUsage(cls: Windows.System.Power.IForegroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def get_RecentEnergyUsageLevel(cls: Windows.System.Power.IForegroundEnergyManagerStatics) -> UInt32: ...
    @winrt_classmethod
    def add_RecentEnergyUsageIncreased(cls: Windows.System.Power.IForegroundEnergyManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RecentEnergyUsageIncreased(cls: Windows.System.Power.IForegroundEnergyManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_RecentEnergyUsageReturnedToLow(cls: Windows.System.Power.IForegroundEnergyManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RecentEnergyUsageReturnedToLow(cls: Windows.System.Power.IForegroundEnergyManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    LowUsageLevel = property(get_LowUsageLevel, None)
    NearMaxAcceptableUsageLevel = property(get_NearMaxAcceptableUsageLevel, None)
    MaxAcceptableUsageLevel = property(get_MaxAcceptableUsageLevel, None)
    ExcessiveUsageLevel = property(get_ExcessiveUsageLevel, None)
    RecentEnergyUsage = property(get_RecentEnergyUsage, None)
    RecentEnergyUsageLevel = property(get_RecentEnergyUsageLevel, None)
class IBackgroundEnergyManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b3161d95-1180-4376-96-e1-40-95-56-81-47-ce')
    @winrt_commethod(6)
    def get_LowUsageLevel(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_NearMaxAcceptableUsageLevel(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxAcceptableUsageLevel(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ExcessiveUsageLevel(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_NearTerminationUsageLevel(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_TerminationUsageLevel(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_RecentEnergyUsage(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_RecentEnergyUsageLevel(self) -> UInt32: ...
    @winrt_commethod(14)
    def add_RecentEnergyUsageIncreased(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_RecentEnergyUsageIncreased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_RecentEnergyUsageReturnedToLow(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_RecentEnergyUsageReturnedToLow(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    LowUsageLevel = property(get_LowUsageLevel, None)
    NearMaxAcceptableUsageLevel = property(get_NearMaxAcceptableUsageLevel, None)
    MaxAcceptableUsageLevel = property(get_MaxAcceptableUsageLevel, None)
    ExcessiveUsageLevel = property(get_ExcessiveUsageLevel, None)
    NearTerminationUsageLevel = property(get_NearTerminationUsageLevel, None)
    TerminationUsageLevel = property(get_TerminationUsageLevel, None)
    RecentEnergyUsage = property(get_RecentEnergyUsage, None)
    RecentEnergyUsageLevel = property(get_RecentEnergyUsageLevel, None)
class IForegroundEnergyManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9ff86872-e677-4814-9a-20-53-37-ca-73-2b-98')
    @winrt_commethod(6)
    def get_LowUsageLevel(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_NearMaxAcceptableUsageLevel(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxAcceptableUsageLevel(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ExcessiveUsageLevel(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_RecentEnergyUsage(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_RecentEnergyUsageLevel(self) -> UInt32: ...
    @winrt_commethod(12)
    def add_RecentEnergyUsageIncreased(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_RecentEnergyUsageIncreased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_RecentEnergyUsageReturnedToLow(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_RecentEnergyUsageReturnedToLow(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    LowUsageLevel = property(get_LowUsageLevel, None)
    NearMaxAcceptableUsageLevel = property(get_NearMaxAcceptableUsageLevel, None)
    MaxAcceptableUsageLevel = property(get_MaxAcceptableUsageLevel, None)
    ExcessiveUsageLevel = property(get_ExcessiveUsageLevel, None)
    RecentEnergyUsage = property(get_RecentEnergyUsage, None)
    RecentEnergyUsageLevel = property(get_RecentEnergyUsageLevel, None)
class IPowerManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1394825d-62ce-4364-98-d5-aa-28-c7-fb-d1-5b')
    @winrt_commethod(6)
    def get_EnergySaverStatus(self) -> Windows.System.Power.EnergySaverStatus: ...
    @winrt_commethod(7)
    def add_EnergySaverStatusChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_EnergySaverStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def get_BatteryStatus(self) -> Windows.System.Power.BatteryStatus: ...
    @winrt_commethod(10)
    def add_BatteryStatusChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_BatteryStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_PowerSupplyStatus(self) -> Windows.System.Power.PowerSupplyStatus: ...
    @winrt_commethod(13)
    def add_PowerSupplyStatusChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_PowerSupplyStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def get_RemainingChargePercent(self) -> Int32: ...
    @winrt_commethod(16)
    def add_RemainingChargePercentChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_RemainingChargePercentChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def get_RemainingDischargeTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(19)
    def add_RemainingDischargeTimeChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_RemainingDischargeTimeChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    EnergySaverStatus = property(get_EnergySaverStatus, None)
    BatteryStatus = property(get_BatteryStatus, None)
    PowerSupplyStatus = property(get_PowerSupplyStatus, None)
    RemainingChargePercent = property(get_RemainingChargePercent, None)
    RemainingDischargeTime = property(get_RemainingDischargeTime, None)
class PowerManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Power.PowerManager'
    @winrt_classmethod
    def get_EnergySaverStatus(cls: Windows.System.Power.IPowerManagerStatics) -> Windows.System.Power.EnergySaverStatus: ...
    @winrt_classmethod
    def add_EnergySaverStatusChanged(cls: Windows.System.Power.IPowerManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_EnergySaverStatusChanged(cls: Windows.System.Power.IPowerManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_BatteryStatus(cls: Windows.System.Power.IPowerManagerStatics) -> Windows.System.Power.BatteryStatus: ...
    @winrt_classmethod
    def add_BatteryStatusChanged(cls: Windows.System.Power.IPowerManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_BatteryStatusChanged(cls: Windows.System.Power.IPowerManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_PowerSupplyStatus(cls: Windows.System.Power.IPowerManagerStatics) -> Windows.System.Power.PowerSupplyStatus: ...
    @winrt_classmethod
    def add_PowerSupplyStatusChanged(cls: Windows.System.Power.IPowerManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PowerSupplyStatusChanged(cls: Windows.System.Power.IPowerManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_RemainingChargePercent(cls: Windows.System.Power.IPowerManagerStatics) -> Int32: ...
    @winrt_classmethod
    def add_RemainingChargePercentChanged(cls: Windows.System.Power.IPowerManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RemainingChargePercentChanged(cls: Windows.System.Power.IPowerManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_RemainingDischargeTime(cls: Windows.System.Power.IPowerManagerStatics) -> Windows.Foundation.TimeSpan: ...
    @winrt_classmethod
    def add_RemainingDischargeTimeChanged(cls: Windows.System.Power.IPowerManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_RemainingDischargeTimeChanged(cls: Windows.System.Power.IPowerManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    EnergySaverStatus = property(get_EnergySaverStatus, None)
    BatteryStatus = property(get_BatteryStatus, None)
    PowerSupplyStatus = property(get_PowerSupplyStatus, None)
    RemainingChargePercent = property(get_RemainingChargePercent, None)
    RemainingDischargeTime = property(get_RemainingDischargeTime, None)
PowerSupplyStatus = Int32
PowerSupplyStatus_NotPresent: PowerSupplyStatus = 0
PowerSupplyStatus_Inadequate: PowerSupplyStatus = 1
PowerSupplyStatus_Adequate: PowerSupplyStatus = 2
make_head(_module, 'BackgroundEnergyManager')
make_head(_module, 'ForegroundEnergyManager')
make_head(_module, 'IBackgroundEnergyManagerStatics')
make_head(_module, 'IForegroundEnergyManagerStatics')
make_head(_module, 'IPowerManagerStatics')
make_head(_module, 'PowerManager')
