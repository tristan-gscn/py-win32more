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
import Windows.Foundation.Collections
import Windows.Media.PlayTo
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CurrentTimeChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.ICurrentTimeChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.CurrentTimeChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Time(self: Windows.Media.PlayTo.ICurrentTimeChangeRequestedEventArgs) -> Windows.Foundation.TimeSpan: ...
    Time = property(get_Time, None)
class ICurrentTimeChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.ICurrentTimeChangeRequestedEventArgs'
    _iid_ = Guid('{99711324-edc7-4bf5-91f6-3c8627db59e5}')
    @winrt_commethod(6)
    def get_Time(self) -> Windows.Foundation.TimeSpan: ...
    Time = property(get_Time, None)
class IMuteChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IMuteChangeRequestedEventArgs'
    _iid_ = Guid('{e4b4f5f6-af1f-4f1e-b437-7da32400e1d4}')
    @winrt_commethod(6)
    def get_Mute(self) -> Boolean: ...
    Mute = property(get_Mute, None)
class IPlayToConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToConnection'
    _iid_ = Guid('{112fbfc8-f235-4fde-8d41-9bf27c9e9a40}')
    @winrt_commethod(6)
    def get_State(self) -> Windows.Media.PlayTo.PlayToConnectionState: ...
    @winrt_commethod(7)
    def add_StateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToConnection, Windows.Media.PlayTo.PlayToConnectionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Transferred(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToConnection, Windows.Media.PlayTo.PlayToConnectionTransferredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Transferred(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Error(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToConnection, Windows.Media.PlayTo.PlayToConnectionErrorEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Error(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
class IPlayToConnectionErrorEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToConnectionErrorEventArgs'
    _iid_ = Guid('{bf5eada6-88e6-445f-9d40-d9b9f8939896}')
    @winrt_commethod(6)
    def get_Code(self) -> Windows.Media.PlayTo.PlayToConnectionError: ...
    @winrt_commethod(7)
    def get_Message(self) -> WinRT_String: ...
    Code = property(get_Code, None)
    Message = property(get_Message, None)
class IPlayToConnectionStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToConnectionStateChangedEventArgs'
    _iid_ = Guid('{68c4b50f-0c20-4980-8602-58c62238d423}')
    @winrt_commethod(6)
    def get_PreviousState(self) -> Windows.Media.PlayTo.PlayToConnectionState: ...
    @winrt_commethod(7)
    def get_CurrentState(self) -> Windows.Media.PlayTo.PlayToConnectionState: ...
    PreviousState = property(get_PreviousState, None)
    CurrentState = property(get_CurrentState, None)
class IPlayToConnectionTransferredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToConnectionTransferredEventArgs'
    _iid_ = Guid('{fae3193a-0683-47d9-8df0-18cbb48984d8}')
    @winrt_commethod(6)
    def get_PreviousSource(self) -> Windows.Media.PlayTo.PlayToSource: ...
    @winrt_commethod(7)
    def get_CurrentSource(self) -> Windows.Media.PlayTo.PlayToSource: ...
    PreviousSource = property(get_PreviousSource, None)
    CurrentSource = property(get_CurrentSource, None)
class IPlayToManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToManager'
    _iid_ = Guid('{f56a206e-1b77-42ef-8f0d-b949f8d9b260}')
    @winrt_commethod(6)
    def add_SourceRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToManager, Windows.Media.PlayTo.PlayToSourceRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceSelected(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToManager, Windows.Media.PlayTo.PlayToSourceSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceSelected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def put_DefaultSourceSelection(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_DefaultSourceSelection(self) -> Boolean: ...
    DefaultSourceSelection = property(get_DefaultSourceSelection, put_DefaultSourceSelection)
class IPlayToManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToManagerStatics'
    _iid_ = Guid('{64e6a887-3982-4f3b-ba20-6155e435325b}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.Media.PlayTo.PlayToManager: ...
    @winrt_commethod(7)
    def ShowPlayToUI(self) -> Void: ...
class IPlayToReceiver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToReceiver'
    _iid_ = Guid('{ac15cf47-a162-4aa6-af1b-3aa35f3b9069}')
    @winrt_commethod(6)
    def add_PlayRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PlayRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PauseRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PauseRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SourceChangeRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.SourceChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SourceChangeRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PlaybackRateChangeRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.PlaybackRateChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PlaybackRateChangeRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_CurrentTimeChangeRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.CurrentTimeChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_CurrentTimeChangeRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_MuteChangeRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.MuteChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_MuteChangeRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_VolumeChangeRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.VolumeChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_VolumeChangeRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_TimeUpdateRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_TimeUpdateRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_StopRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_StopRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def NotifyVolumeChange(self, volume: Double, mute: Boolean) -> Void: ...
    @winrt_commethod(25)
    def NotifyRateChange(self, rate: Double) -> Void: ...
    @winrt_commethod(26)
    def NotifyLoadedMetadata(self) -> Void: ...
    @winrt_commethod(27)
    def NotifyTimeUpdate(self, currentTime: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(28)
    def NotifyDurationChange(self, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(29)
    def NotifySeeking(self) -> Void: ...
    @winrt_commethod(30)
    def NotifySeeked(self) -> Void: ...
    @winrt_commethod(31)
    def NotifyPaused(self) -> Void: ...
    @winrt_commethod(32)
    def NotifyPlaying(self) -> Void: ...
    @winrt_commethod(33)
    def NotifyEnded(self) -> Void: ...
    @winrt_commethod(34)
    def NotifyError(self) -> Void: ...
    @winrt_commethod(35)
    def NotifyStopped(self) -> Void: ...
    @winrt_commethod(36)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def put_FriendlyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(38)
    def put_SupportsImage(self, value: Boolean) -> Void: ...
    @winrt_commethod(39)
    def get_SupportsImage(self) -> Boolean: ...
    @winrt_commethod(40)
    def put_SupportsAudio(self, value: Boolean) -> Void: ...
    @winrt_commethod(41)
    def get_SupportsAudio(self) -> Boolean: ...
    @winrt_commethod(42)
    def put_SupportsVideo(self, value: Boolean) -> Void: ...
    @winrt_commethod(43)
    def get_SupportsVideo(self) -> Boolean: ...
    @winrt_commethod(44)
    def get_Properties(self) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(45)
    def StartAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(46)
    def StopAsync(self) -> Windows.Foundation.IAsyncAction: ...
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    SupportsImage = property(get_SupportsImage, put_SupportsImage)
    SupportsAudio = property(get_SupportsAudio, put_SupportsAudio)
    SupportsVideo = property(get_SupportsVideo, put_SupportsVideo)
    Properties = property(get_Properties, None)
class IPlayToSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSource'
    _iid_ = Guid('{7f138a08-fbb7-4b09-8356-aa5f4e335c31}')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.Media.PlayTo.PlayToConnection: ...
    @winrt_commethod(7)
    def get_Next(self) -> Windows.Media.PlayTo.PlayToSource: ...
    @winrt_commethod(8)
    def put_Next(self, value: Windows.Media.PlayTo.PlayToSource) -> Void: ...
    @winrt_commethod(9)
    def PlayNext(self) -> Void: ...
    Connection = property(get_Connection, None)
    Next = property(get_Next, put_Next)
class IPlayToSourceDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceDeferral'
    _iid_ = Guid('{4100891d-278e-4f29-859b-a9e501053e7d}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IPlayToSourceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceRequest'
    _iid_ = Guid('{f8584665-64f4-44a0-ac0d-468d2b8fda83}')
    @winrt_commethod(6)
    def get_Deadline(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def DisplayErrorString(self, errorString: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Media.PlayTo.PlayToSourceDeferral: ...
    @winrt_commethod(9)
    def SetSource(self, value: Windows.Media.PlayTo.PlayToSource) -> Void: ...
    Deadline = property(get_Deadline, None)
class IPlayToSourceRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceRequestedEventArgs'
    _iid_ = Guid('{c5cdc330-29df-4ec6-9da9-9fbdfcfc1b3e}')
    @winrt_commethod(6)
    def get_SourceRequest(self) -> Windows.Media.PlayTo.PlayToSourceRequest: ...
    SourceRequest = property(get_SourceRequest, None)
class IPlayToSourceSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs'
    _iid_ = Guid('{0c9d8511-5202-4dcb-8c67-abda12bb3c12}')
    @winrt_commethod(6)
    def get_FriendlyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Icon(self) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(8)
    def get_SupportsImage(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SupportsAudio(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_SupportsVideo(self) -> Boolean: ...
    FriendlyName = property(get_FriendlyName, None)
    Icon = property(get_Icon, None)
    SupportsImage = property(get_SupportsImage, None)
    SupportsAudio = property(get_SupportsAudio, None)
    SupportsVideo = property(get_SupportsVideo, None)
class IPlayToSourceWithPreferredSourceUri(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlayToSourceWithPreferredSourceUri'
    _iid_ = Guid('{aab253eb-3301-4dc4-afba-b2f2ed9635a0}')
    @winrt_commethod(6)
    def get_PreferredSourceUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_PreferredSourceUri(self, value: Windows.Foundation.Uri) -> Void: ...
    PreferredSourceUri = property(get_PreferredSourceUri, put_PreferredSourceUri)
class IPlaybackRateChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IPlaybackRateChangeRequestedEventArgs'
    _iid_ = Guid('{0f5661ae-2c88-4cca-8540-d586095d13a5}')
    @winrt_commethod(6)
    def get_Rate(self) -> Double: ...
    Rate = property(get_Rate, None)
class ISourceChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.ISourceChangeRequestedEventArgs'
    _iid_ = Guid('{fb3f3a96-7aa6-4a8b-86e7-54f6c6d34f64}')
    @winrt_commethod(6)
    def get_Stream(self) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_commethod(7)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Author(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Album(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Genre(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Date(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(13)
    def get_Thumbnail(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(14)
    def get_Rating(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(15)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Stream = property(get_Stream, None)
    Title = property(get_Title, None)
    Author = property(get_Author, None)
    Album = property(get_Album, None)
    Genre = property(get_Genre, None)
    Description = property(get_Description, None)
    Date = property(get_Date, None)
    Thumbnail = property(get_Thumbnail, None)
    Rating = property(get_Rating, None)
    Properties = property(get_Properties, None)
class IVolumeChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.PlayTo.IVolumeChangeRequestedEventArgs'
    _iid_ = Guid('{6f026d5c-cf75-4c2b-913e-6d7c6c329179}')
    @winrt_commethod(6)
    def get_Volume(self) -> Double: ...
    Volume = property(get_Volume, None)
class MuteChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IMuteChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.MuteChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Mute(self: Windows.Media.PlayTo.IMuteChangeRequestedEventArgs) -> Boolean: ...
    Mute = property(get_Mute, None)
class PlayToConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToConnection
    _classid_ = 'Windows.Media.PlayTo.PlayToConnection'
    @winrt_mixinmethod
    def get_State(self: Windows.Media.PlayTo.IPlayToConnection) -> Windows.Media.PlayTo.PlayToConnectionState: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Media.PlayTo.IPlayToConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToConnection, Windows.Media.PlayTo.PlayToConnectionStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Media.PlayTo.IPlayToConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Transferred(self: Windows.Media.PlayTo.IPlayToConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToConnection, Windows.Media.PlayTo.PlayToConnectionTransferredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Transferred(self: Windows.Media.PlayTo.IPlayToConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Error(self: Windows.Media.PlayTo.IPlayToConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToConnection, Windows.Media.PlayTo.PlayToConnectionErrorEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Error(self: Windows.Media.PlayTo.IPlayToConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
PlayToConnectionError = Int32
PlayToConnectionError_None: PlayToConnectionError = 0
PlayToConnectionError_DeviceNotResponding: PlayToConnectionError = 1
PlayToConnectionError_DeviceError: PlayToConnectionError = 2
PlayToConnectionError_DeviceLocked: PlayToConnectionError = 3
PlayToConnectionError_ProtectedPlaybackFailed: PlayToConnectionError = 4
class PlayToConnectionErrorEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToConnectionErrorEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToConnectionErrorEventArgs'
    @winrt_mixinmethod
    def get_Code(self: Windows.Media.PlayTo.IPlayToConnectionErrorEventArgs) -> Windows.Media.PlayTo.PlayToConnectionError: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.Media.PlayTo.IPlayToConnectionErrorEventArgs) -> WinRT_String: ...
    Code = property(get_Code, None)
    Message = property(get_Message, None)
PlayToConnectionState = Int32
PlayToConnectionState_Disconnected: PlayToConnectionState = 0
PlayToConnectionState_Connected: PlayToConnectionState = 1
PlayToConnectionState_Rendering: PlayToConnectionState = 2
class PlayToConnectionStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToConnectionStateChangedEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToConnectionStateChangedEventArgs'
    @winrt_mixinmethod
    def get_PreviousState(self: Windows.Media.PlayTo.IPlayToConnectionStateChangedEventArgs) -> Windows.Media.PlayTo.PlayToConnectionState: ...
    @winrt_mixinmethod
    def get_CurrentState(self: Windows.Media.PlayTo.IPlayToConnectionStateChangedEventArgs) -> Windows.Media.PlayTo.PlayToConnectionState: ...
    PreviousState = property(get_PreviousState, None)
    CurrentState = property(get_CurrentState, None)
class PlayToConnectionTransferredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToConnectionTransferredEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToConnectionTransferredEventArgs'
    @winrt_mixinmethod
    def get_PreviousSource(self: Windows.Media.PlayTo.IPlayToConnectionTransferredEventArgs) -> Windows.Media.PlayTo.PlayToSource: ...
    @winrt_mixinmethod
    def get_CurrentSource(self: Windows.Media.PlayTo.IPlayToConnectionTransferredEventArgs) -> Windows.Media.PlayTo.PlayToSource: ...
    PreviousSource = property(get_PreviousSource, None)
    CurrentSource = property(get_CurrentSource, None)
class PlayToManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToManager
    _classid_ = 'Windows.Media.PlayTo.PlayToManager'
    @winrt_mixinmethod
    def add_SourceRequested(self: Windows.Media.PlayTo.IPlayToManager, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToManager, Windows.Media.PlayTo.PlayToSourceRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceRequested(self: Windows.Media.PlayTo.IPlayToManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceSelected(self: Windows.Media.PlayTo.IPlayToManager, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToManager, Windows.Media.PlayTo.PlayToSourceSelectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceSelected(self: Windows.Media.PlayTo.IPlayToManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_DefaultSourceSelection(self: Windows.Media.PlayTo.IPlayToManager, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultSourceSelection(self: Windows.Media.PlayTo.IPlayToManager) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Media.PlayTo.IPlayToManagerStatics) -> Windows.Media.PlayTo.PlayToManager: ...
    @winrt_classmethod
    def ShowPlayToUI(cls: Windows.Media.PlayTo.IPlayToManagerStatics) -> Void: ...
    DefaultSourceSelection = property(get_DefaultSourceSelection, put_DefaultSourceSelection)
class PlayToReceiver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToReceiver
    _classid_ = 'Windows.Media.PlayTo.PlayToReceiver'
    @winrt_activatemethod
    def New(cls) -> Windows.Media.PlayTo.PlayToReceiver: ...
    @winrt_mixinmethod
    def add_PlayRequested(self: Windows.Media.PlayTo.IPlayToReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PlayRequested(self: Windows.Media.PlayTo.IPlayToReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PauseRequested(self: Windows.Media.PlayTo.IPlayToReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PauseRequested(self: Windows.Media.PlayTo.IPlayToReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.SourceChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PlaybackRateChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.PlaybackRateChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PlaybackRateChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CurrentTimeChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.CurrentTimeChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CurrentTimeChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MuteChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.MuteChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MuteChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VolumeChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Media.PlayTo.VolumeChangeRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VolumeChangeRequested(self: Windows.Media.PlayTo.IPlayToReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TimeUpdateRequested(self: Windows.Media.PlayTo.IPlayToReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TimeUpdateRequested(self: Windows.Media.PlayTo.IPlayToReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StopRequested(self: Windows.Media.PlayTo.IPlayToReceiver, handler: Windows.Foundation.TypedEventHandler[Windows.Media.PlayTo.PlayToReceiver, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StopRequested(self: Windows.Media.PlayTo.IPlayToReceiver, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyVolumeChange(self: Windows.Media.PlayTo.IPlayToReceiver, volume: Double, mute: Boolean) -> Void: ...
    @winrt_mixinmethod
    def NotifyRateChange(self: Windows.Media.PlayTo.IPlayToReceiver, rate: Double) -> Void: ...
    @winrt_mixinmethod
    def NotifyLoadedMetadata(self: Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyTimeUpdate(self: Windows.Media.PlayTo.IPlayToReceiver, currentTime: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def NotifyDurationChange(self: Windows.Media.PlayTo.IPlayToReceiver, duration: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def NotifySeeking(self: Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifySeeked(self: Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyPaused(self: Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyPlaying(self: Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyEnded(self: Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyError(self: Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def NotifyStopped(self: Windows.Media.PlayTo.IPlayToReceiver) -> Void: ...
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Media.PlayTo.IPlayToReceiver) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FriendlyName(self: Windows.Media.PlayTo.IPlayToReceiver, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def put_SupportsImage(self: Windows.Media.PlayTo.IPlayToReceiver, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsImage(self: Windows.Media.PlayTo.IPlayToReceiver) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsAudio(self: Windows.Media.PlayTo.IPlayToReceiver, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsAudio(self: Windows.Media.PlayTo.IPlayToReceiver) -> Boolean: ...
    @winrt_mixinmethod
    def put_SupportsVideo(self: Windows.Media.PlayTo.IPlayToReceiver, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SupportsVideo(self: Windows.Media.PlayTo.IPlayToReceiver) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.PlayTo.IPlayToReceiver) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Media.PlayTo.IPlayToReceiver) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopAsync(self: Windows.Media.PlayTo.IPlayToReceiver) -> Windows.Foundation.IAsyncAction: ...
    FriendlyName = property(get_FriendlyName, put_FriendlyName)
    SupportsImage = property(get_SupportsImage, put_SupportsImage)
    SupportsAudio = property(get_SupportsAudio, put_SupportsAudio)
    SupportsVideo = property(get_SupportsVideo, put_SupportsVideo)
    Properties = property(get_Properties, None)
class PlayToSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToSource
    _classid_ = 'Windows.Media.PlayTo.PlayToSource'
    @winrt_mixinmethod
    def get_Connection(self: Windows.Media.PlayTo.IPlayToSource) -> Windows.Media.PlayTo.PlayToConnection: ...
    @winrt_mixinmethod
    def get_Next(self: Windows.Media.PlayTo.IPlayToSource) -> Windows.Media.PlayTo.PlayToSource: ...
    @winrt_mixinmethod
    def put_Next(self: Windows.Media.PlayTo.IPlayToSource, value: Windows.Media.PlayTo.PlayToSource) -> Void: ...
    @winrt_mixinmethod
    def PlayNext(self: Windows.Media.PlayTo.IPlayToSource) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredSourceUri(self: Windows.Media.PlayTo.IPlayToSourceWithPreferredSourceUri) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_PreferredSourceUri(self: Windows.Media.PlayTo.IPlayToSourceWithPreferredSourceUri, value: Windows.Foundation.Uri) -> Void: ...
    Connection = property(get_Connection, None)
    Next = property(get_Next, put_Next)
    PreferredSourceUri = property(get_PreferredSourceUri, put_PreferredSourceUri)
class PlayToSourceDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToSourceDeferral
    _classid_ = 'Windows.Media.PlayTo.PlayToSourceDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.Media.PlayTo.IPlayToSourceDeferral) -> Void: ...
class PlayToSourceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToSourceRequest
    _classid_ = 'Windows.Media.PlayTo.PlayToSourceRequest'
    @winrt_mixinmethod
    def get_Deadline(self: Windows.Media.PlayTo.IPlayToSourceRequest) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def DisplayErrorString(self: Windows.Media.PlayTo.IPlayToSourceRequest, errorString: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Media.PlayTo.IPlayToSourceRequest) -> Windows.Media.PlayTo.PlayToSourceDeferral: ...
    @winrt_mixinmethod
    def SetSource(self: Windows.Media.PlayTo.IPlayToSourceRequest, value: Windows.Media.PlayTo.PlayToSource) -> Void: ...
    Deadline = property(get_Deadline, None)
class PlayToSourceRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToSourceRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToSourceRequestedEventArgs'
    @winrt_mixinmethod
    def get_SourceRequest(self: Windows.Media.PlayTo.IPlayToSourceRequestedEventArgs) -> Windows.Media.PlayTo.PlayToSourceRequest: ...
    SourceRequest = property(get_SourceRequest, None)
class PlayToSourceSelectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlayToSourceSelectedEventArgs'
    @winrt_mixinmethod
    def get_FriendlyName(self: Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Icon(self: Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def get_SupportsImage(self: Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportsAudio(self: Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportsVideo(self: Windows.Media.PlayTo.IPlayToSourceSelectedEventArgs) -> Boolean: ...
    FriendlyName = property(get_FriendlyName, None)
    Icon = property(get_Icon, None)
    SupportsImage = property(get_SupportsImage, None)
    SupportsAudio = property(get_SupportsAudio, None)
    SupportsVideo = property(get_SupportsVideo, None)
class PlaybackRateChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IPlaybackRateChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.PlaybackRateChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Rate(self: Windows.Media.PlayTo.IPlaybackRateChangeRequestedEventArgs) -> Double: ...
    Rate = property(get_Rate, None)
class SourceChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.SourceChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Stream(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Author(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Album(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Genre(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Date(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_Rating(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Media.PlayTo.ISourceChangeRequestedEventArgs) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Stream = property(get_Stream, None)
    Title = property(get_Title, None)
    Author = property(get_Author, None)
    Album = property(get_Album, None)
    Genre = property(get_Genre, None)
    Description = property(get_Description, None)
    Date = property(get_Date, None)
    Thumbnail = property(get_Thumbnail, None)
    Rating = property(get_Rating, None)
    Properties = property(get_Properties, None)
class VolumeChangeRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.PlayTo.IVolumeChangeRequestedEventArgs
    _classid_ = 'Windows.Media.PlayTo.VolumeChangeRequestedEventArgs'
    @winrt_mixinmethod
    def get_Volume(self: Windows.Media.PlayTo.IVolumeChangeRequestedEventArgs) -> Double: ...
    Volume = property(get_Volume, None)
make_head(_module, 'CurrentTimeChangeRequestedEventArgs')
make_head(_module, 'ICurrentTimeChangeRequestedEventArgs')
make_head(_module, 'IMuteChangeRequestedEventArgs')
make_head(_module, 'IPlayToConnection')
make_head(_module, 'IPlayToConnectionErrorEventArgs')
make_head(_module, 'IPlayToConnectionStateChangedEventArgs')
make_head(_module, 'IPlayToConnectionTransferredEventArgs')
make_head(_module, 'IPlayToManager')
make_head(_module, 'IPlayToManagerStatics')
make_head(_module, 'IPlayToReceiver')
make_head(_module, 'IPlayToSource')
make_head(_module, 'IPlayToSourceDeferral')
make_head(_module, 'IPlayToSourceRequest')
make_head(_module, 'IPlayToSourceRequestedEventArgs')
make_head(_module, 'IPlayToSourceSelectedEventArgs')
make_head(_module, 'IPlayToSourceWithPreferredSourceUri')
make_head(_module, 'IPlaybackRateChangeRequestedEventArgs')
make_head(_module, 'ISourceChangeRequestedEventArgs')
make_head(_module, 'IVolumeChangeRequestedEventArgs')
make_head(_module, 'MuteChangeRequestedEventArgs')
make_head(_module, 'PlayToConnection')
make_head(_module, 'PlayToConnectionErrorEventArgs')
make_head(_module, 'PlayToConnectionStateChangedEventArgs')
make_head(_module, 'PlayToConnectionTransferredEventArgs')
make_head(_module, 'PlayToManager')
make_head(_module, 'PlayToReceiver')
make_head(_module, 'PlayToSource')
make_head(_module, 'PlayToSourceDeferral')
make_head(_module, 'PlayToSourceRequest')
make_head(_module, 'PlayToSourceRequestedEventArgs')
make_head(_module, 'PlayToSourceSelectedEventArgs')
make_head(_module, 'PlaybackRateChangeRequestedEventArgs')
make_head(_module, 'SourceChangeRequestedEventArgs')
make_head(_module, 'VolumeChangeRequestedEventArgs')
