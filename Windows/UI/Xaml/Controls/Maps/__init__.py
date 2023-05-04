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
import Windows.Devices.Geolocation
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Services.Maps
import Windows.Services.Maps.LocalSearch
import Windows.Storage.Streams
import Windows.UI
import Windows.UI.Xaml
import Windows.UI.Xaml.Controls.Maps
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CustomMapTileDataSource(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapTileDataSource
    default_interface: Windows.UI.Xaml.Controls.Maps.ICustomMapTileDataSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource'
    @winrt_commethod(10)
    def add_BitmapRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource, Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_BitmapRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class HttpMapTileDataSource(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapTileDataSource
    default_interface: Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource'
    @winrt_commethod(16)
    def get_UriFormatString(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_UriFormatString(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_AdditionalRequestHeaders(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(19)
    def get_AllowCaching(self) -> Boolean: ...
    @winrt_commethod(20)
    def put_AllowCaching(self, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def add_UriRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource, Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_UriRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    UriFormatString = property(get_UriFormatString, put_UriFormatString)
    AdditionalRequestHeaders = property(get_AdditionalRequestHeaders, None)
    AllowCaching = property(get_AllowCaching, put_AllowCaching)
class ICustomMapTileDataSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.ICustomMapTileDataSource'
    _iid_ = Guid('{65da384a-2db1-4be1-b155-3d0c9ecf4799}')
    @winrt_commethod(6)
    def add_BitmapRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource, Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BitmapRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICustomMapTileDataSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.ICustomMapTileDataSourceFactory'
    _iid_ = Guid('{c8477947-c955-4f22-9444-a1d8d744af11}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.CustomMapTileDataSource: ...
class IHttpMapTileDataSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSource'
    _iid_ = Guid('{9d03cb5c-fd79-4795-87be-7e54ca0b37d0}')
    @winrt_commethod(6)
    def get_UriFormatString(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_UriFormatString(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AdditionalRequestHeaders(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(9)
    def get_AllowCaching(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_AllowCaching(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def add_UriRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource, Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_UriRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    UriFormatString = property(get_UriFormatString, put_UriFormatString)
    AdditionalRequestHeaders = property(get_AdditionalRequestHeaders, None)
    AllowCaching = property(get_AllowCaching, put_AllowCaching)
class IHttpMapTileDataSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IHttpMapTileDataSourceFactory'
    _iid_ = Guid('{53b4b107-84dc-4291-89f8-6d0bb612a055}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithUriFormatString(self, uriFormatString: WinRT_String, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.HttpMapTileDataSource: ...
class ILocalMapTileDataSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSource'
    _iid_ = Guid('{616257b5-9108-4f12-8bf4-bb3c8f6274e5}')
    @winrt_commethod(6)
    def get_UriFormatString(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_UriFormatString(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def add_UriRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource, Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_UriRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    UriFormatString = property(get_UriFormatString, put_UriFormatString)
class ILocalMapTileDataSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSourceFactory'
    _iid_ = Guid('{c5cfe9fc-72ac-4839-8a0d-011f24693c79}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithUriFormatString(self, uriFormatString: WinRT_String, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource: ...
class IMapActualCameraChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs'
    _iid_ = Guid('{daa080da-b7f4-422c-a618-bbaa7c1d814c}')
    @winrt_commethod(6)
    def get_Camera(self) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    Camera = property(get_Camera, None)
class IMapActualCameraChangedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs2'
    _iid_ = Guid('{7ba4c7e5-10dc-455a-9d04-1d72fb6d9b93}')
    @winrt_commethod(6)
    def get_ChangeReason(self) -> Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    ChangeReason = property(get_ChangeReason, None)
class IMapActualCameraChangingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs'
    _iid_ = Guid('{6b0dbed6-93f7-4682-8de5-a47a1cc7a945}')
    @winrt_commethod(6)
    def get_Camera(self) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    Camera = property(get_Camera, None)
class IMapActualCameraChangingEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs2'
    _iid_ = Guid('{f2867897-40ac-4e8a-a927-510f3846a47e}')
    @winrt_commethod(6)
    def get_ChangeReason(self) -> Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    ChangeReason = property(get_ChangeReason, None)
class IMapBillboard(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapBillboard'
    _iid_ = Guid('{1694259d-0ae2-4f42-a02e-292ca835d39d}')
    @winrt_commethod(6)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Location(self, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_NormalizedAnchorPoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_NormalizedAnchorPoint(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(10)
    def get_Image(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(11)
    def put_Image(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(12)
    def get_CollisionBehaviorDesired(self) -> Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior: ...
    @winrt_commethod(13)
    def put_CollisionBehaviorDesired(self, value: Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior) -> Void: ...
    @winrt_commethod(14)
    def get_ReferenceCamera(self) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    Location = property(get_Location, put_Location)
    NormalizedAnchorPoint = property(get_NormalizedAnchorPoint, put_NormalizedAnchorPoint)
    Image = property(get_Image, put_Image)
    CollisionBehaviorDesired = property(get_CollisionBehaviorDesired, put_CollisionBehaviorDesired)
    ReferenceCamera = property(get_ReferenceCamera, None)
class IMapBillboardFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapBillboardFactory'
    _iid_ = Guid('{be45a4c5-8f09-4b86-ae28-783740eb8b31}')
    @winrt_commethod(6)
    def CreateInstanceFromCamera(self, camera: Windows.UI.Xaml.Controls.Maps.MapCamera) -> Windows.UI.Xaml.Controls.Maps.MapBillboard: ...
class IMapBillboardStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapBillboardStatics'
    _iid_ = Guid('{fdf839fe-e1f7-4fb0-8887-7da68c647333}')
    @winrt_commethod(6)
    def get_LocationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_NormalizedAnchorPointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CollisionBehaviorDesiredProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    LocationProperty = property(get_LocationProperty, None)
    NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
    CollisionBehaviorDesiredProperty = property(get_CollisionBehaviorDesiredProperty, None)
class IMapCamera(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCamera'
    _iid_ = Guid('{53a6b623-c0f8-4d8b-ad1e-a59598ea840b}')
    @winrt_commethod(6)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Location(self, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_Heading(self) -> Double: ...
    @winrt_commethod(9)
    def put_Heading(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_Pitch(self) -> Double: ...
    @winrt_commethod(11)
    def put_Pitch(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_Roll(self) -> Double: ...
    @winrt_commethod(13)
    def put_Roll(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_FieldOfView(self) -> Double: ...
    @winrt_commethod(15)
    def put_FieldOfView(self, value: Double) -> Void: ...
    Location = property(get_Location, put_Location)
    Heading = property(get_Heading, put_Heading)
    Pitch = property(get_Pitch, put_Pitch)
    Roll = property(get_Roll, put_Roll)
    FieldOfView = property(get_FieldOfView, put_FieldOfView)
class IMapCameraFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCameraFactory'
    _iid_ = Guid('{ea3b0f16-83af-4ace-8e71-10ad9f1e9e7f}')
    @winrt_commethod(6)
    def CreateInstanceWithLocation(self, location: Windows.Devices.Geolocation.Geopoint) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(7)
    def CreateInstanceWithLocationAndHeading(self, location: Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(8)
    def CreateInstanceWithLocationHeadingAndPitch(self, location: Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(9)
    def CreateInstanceWithLocationHeadingPitchRollAndFieldOfView(self, location: Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double, rollInDegrees: Double, fieldOfViewInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
class IMapContextRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs'
    _iid_ = Guid('{fdd1b423-c961-4df2-bb57-82ee0f0bb591}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElements(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
class IMapControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl'
    _iid_ = Guid('{42d0b851-5256-4747-9e6c-0d11e966141e}')
    @winrt_commethod(6)
    def get_Center(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Center(self, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_Children(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(9)
    def get_ColorScheme(self) -> Windows.UI.Xaml.Controls.Maps.MapColorScheme: ...
    @winrt_commethod(10)
    def put_ColorScheme(self, value: Windows.UI.Xaml.Controls.Maps.MapColorScheme) -> Void: ...
    @winrt_commethod(11)
    def get_DesiredPitch(self) -> Double: ...
    @winrt_commethod(12)
    def put_DesiredPitch(self, value: Double) -> Void: ...
    @winrt_commethod(13)
    def get_Heading(self) -> Double: ...
    @winrt_commethod(14)
    def put_Heading(self, value: Double) -> Void: ...
    @winrt_commethod(15)
    def get_LandmarksVisible(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_LandmarksVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def get_LoadingStatus(self) -> Windows.UI.Xaml.Controls.Maps.MapLoadingStatus: ...
    @winrt_commethod(18)
    def get_MapServiceToken(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def put_MapServiceToken(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(20)
    def get_MaxZoomLevel(self) -> Double: ...
    @winrt_commethod(21)
    def get_MinZoomLevel(self) -> Double: ...
    @winrt_commethod(22)
    def get_PedestrianFeaturesVisible(self) -> Boolean: ...
    @winrt_commethod(23)
    def put_PedestrianFeaturesVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(24)
    def get_Pitch(self) -> Double: ...
    @winrt_commethod(25)
    def get_Style(self) -> Windows.UI.Xaml.Controls.Maps.MapStyle: ...
    @winrt_commethod(26)
    def put_Style(self, value: Windows.UI.Xaml.Controls.Maps.MapStyle) -> Void: ...
    @winrt_commethod(27)
    def get_TrafficFlowVisible(self) -> Boolean: ...
    @winrt_commethod(28)
    def put_TrafficFlowVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(29)
    def get_TransformOrigin(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(30)
    def put_TransformOrigin(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(31)
    def get_WatermarkMode(self) -> Windows.UI.Xaml.Controls.Maps.MapWatermarkMode: ...
    @winrt_commethod(32)
    def put_WatermarkMode(self, value: Windows.UI.Xaml.Controls.Maps.MapWatermarkMode) -> Void: ...
    @winrt_commethod(33)
    def get_ZoomLevel(self) -> Double: ...
    @winrt_commethod(34)
    def put_ZoomLevel(self, value: Double) -> Void: ...
    @winrt_commethod(35)
    def get_MapElements(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_commethod(36)
    def get_Routes(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapRouteView]: ...
    @winrt_commethod(37)
    def get_TileSources(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapTileSource]: ...
    @winrt_commethod(38)
    def add_CenterChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(39)
    def remove_CenterChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(40)
    def add_HeadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(41)
    def remove_HeadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(42)
    def add_LoadingStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(43)
    def remove_LoadingStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(44)
    def add_MapDoubleTapped(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(45)
    def remove_MapDoubleTapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(46)
    def add_MapHolding(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(47)
    def remove_MapHolding(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(48)
    def add_MapTapped(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(49)
    def remove_MapTapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(50)
    def add_PitchChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(51)
    def remove_PitchChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(52)
    def add_TransformOriginChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(53)
    def remove_TransformOriginChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(54)
    def add_ZoomLevelChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(55)
    def remove_ZoomLevelChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(56)
    def FindMapElementsAtOffset(self, offset: Windows.Foundation.Point) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_commethod(57)
    def GetLocationFromOffset(self, offset: Windows.Foundation.Point, location: POINTER(Windows.Devices.Geolocation.Geopoint)) -> Void: ...
    @winrt_commethod(58)
    def GetOffsetFromLocation(self, location: Windows.Devices.Geolocation.Geopoint, offset: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_commethod(59)
    def IsLocationInView(self, location: Windows.Devices.Geolocation.Geopoint, isInView: POINTER(Boolean)) -> Void: ...
    @winrt_commethod(60)
    def TrySetViewBoundsAsync(self, bounds: Windows.Devices.Geolocation.GeoboundingBox, margin: Windows.Foundation.IReference[Windows.UI.Xaml.Thickness], animation: Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(61)
    def TrySetViewWithCenterAsync(self, center: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(62)
    def TrySetViewWithCenterAndZoomAsync(self, center: Windows.Devices.Geolocation.Geopoint, zoomLevel: Windows.Foundation.IReference[Double]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(63)
    def TrySetViewWithCenterZoomHeadingAndPitchAsync(self, center: Windows.Devices.Geolocation.Geopoint, zoomLevel: Windows.Foundation.IReference[Double], heading: Windows.Foundation.IReference[Double], desiredPitch: Windows.Foundation.IReference[Double]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(64)
    def TrySetViewWithCenterZoomHeadingPitchAndAnimationAsync(self, center: Windows.Devices.Geolocation.Geopoint, zoomLevel: Windows.Foundation.IReference[Double], heading: Windows.Foundation.IReference[Double], desiredPitch: Windows.Foundation.IReference[Double], animation: Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    Center = property(get_Center, put_Center)
    Children = property(get_Children, None)
    ColorScheme = property(get_ColorScheme, put_ColorScheme)
    DesiredPitch = property(get_DesiredPitch, put_DesiredPitch)
    Heading = property(get_Heading, put_Heading)
    LandmarksVisible = property(get_LandmarksVisible, put_LandmarksVisible)
    LoadingStatus = property(get_LoadingStatus, None)
    MapServiceToken = property(get_MapServiceToken, put_MapServiceToken)
    MaxZoomLevel = property(get_MaxZoomLevel, None)
    MinZoomLevel = property(get_MinZoomLevel, None)
    PedestrianFeaturesVisible = property(get_PedestrianFeaturesVisible, put_PedestrianFeaturesVisible)
    Pitch = property(get_Pitch, None)
    Style = property(get_Style, put_Style)
    TrafficFlowVisible = property(get_TrafficFlowVisible, put_TrafficFlowVisible)
    TransformOrigin = property(get_TransformOrigin, put_TransformOrigin)
    WatermarkMode = property(get_WatermarkMode, put_WatermarkMode)
    ZoomLevel = property(get_ZoomLevel, put_ZoomLevel)
    MapElements = property(get_MapElements, None)
    Routes = property(get_Routes, None)
    TileSources = property(get_TileSources, None)
class IMapControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl2'
    _iid_ = Guid('{e1fd644d-96ec-4065-b0f0-75281da3654d}')
    @winrt_commethod(6)
    def get_BusinessLandmarksVisible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_BusinessLandmarksVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TransitFeaturesVisible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_TransitFeaturesVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_PanInteractionMode(self) -> Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode: ...
    @winrt_commethod(11)
    def put_PanInteractionMode(self, value: Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode) -> Void: ...
    @winrt_commethod(12)
    def get_RotateInteractionMode(self) -> Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_commethod(13)
    def put_RotateInteractionMode(self, value: Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_commethod(14)
    def get_TiltInteractionMode(self) -> Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_commethod(15)
    def put_TiltInteractionMode(self, value: Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_commethod(16)
    def get_ZoomInteractionMode(self) -> Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_commethod(17)
    def put_ZoomInteractionMode(self, value: Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_commethod(18)
    def get_Is3DSupported(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_IsStreetsideSupported(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_Scene(self) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(21)
    def put_Scene(self, value: Windows.UI.Xaml.Controls.Maps.MapScene) -> Void: ...
    @winrt_commethod(22)
    def get_ActualCamera(self) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(23)
    def get_TargetCamera(self) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(24)
    def get_CustomExperience(self) -> Windows.UI.Xaml.Controls.Maps.MapCustomExperience: ...
    @winrt_commethod(25)
    def put_CustomExperience(self, value: Windows.UI.Xaml.Controls.Maps.MapCustomExperience) -> Void: ...
    @winrt_commethod(26)
    def add_MapElementClick(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapElementClickEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_MapElementClick(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_MapElementPointerEntered(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapElementPointerEnteredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_MapElementPointerEntered(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_MapElementPointerExited(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapElementPointerExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_MapElementPointerExited(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_ActualCameraChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapActualCameraChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_ActualCameraChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_ActualCameraChanging(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapActualCameraChangingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_ActualCameraChanging(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(36)
    def add_TargetCameraChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(37)
    def remove_TargetCameraChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(38)
    def add_CustomExperienceChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapCustomExperienceChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(39)
    def remove_CustomExperienceChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(40)
    def StartContinuousRotate(self, rateInDegreesPerSecond: Double) -> Void: ...
    @winrt_commethod(41)
    def StopContinuousRotate(self) -> Void: ...
    @winrt_commethod(42)
    def StartContinuousTilt(self, rateInDegreesPerSecond: Double) -> Void: ...
    @winrt_commethod(43)
    def StopContinuousTilt(self) -> Void: ...
    @winrt_commethod(44)
    def StartContinuousZoom(self, rateOfChangePerSecond: Double) -> Void: ...
    @winrt_commethod(45)
    def StopContinuousZoom(self) -> Void: ...
    @winrt_commethod(46)
    def TryRotateAsync(self, degrees: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(47)
    def TryRotateToAsync(self, angleInDegrees: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(48)
    def TryTiltAsync(self, degrees: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(49)
    def TryTiltToAsync(self, angleInDegrees: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(50)
    def TryZoomInAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(51)
    def TryZoomOutAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(52)
    def TryZoomToAsync(self, zoomLevel: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(53)
    def TrySetSceneAsync(self, scene: Windows.UI.Xaml.Controls.Maps.MapScene) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(54)
    def TrySetSceneWithAnimationAsync(self, scene: Windows.UI.Xaml.Controls.Maps.MapScene, animationKind: Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    BusinessLandmarksVisible = property(get_BusinessLandmarksVisible, put_BusinessLandmarksVisible)
    TransitFeaturesVisible = property(get_TransitFeaturesVisible, put_TransitFeaturesVisible)
    PanInteractionMode = property(get_PanInteractionMode, put_PanInteractionMode)
    RotateInteractionMode = property(get_RotateInteractionMode, put_RotateInteractionMode)
    TiltInteractionMode = property(get_TiltInteractionMode, put_TiltInteractionMode)
    ZoomInteractionMode = property(get_ZoomInteractionMode, put_ZoomInteractionMode)
    Is3DSupported = property(get_Is3DSupported, None)
    IsStreetsideSupported = property(get_IsStreetsideSupported, None)
    Scene = property(get_Scene, put_Scene)
    ActualCamera = property(get_ActualCamera, None)
    TargetCamera = property(get_TargetCamera, None)
    CustomExperience = property(get_CustomExperience, put_CustomExperience)
class IMapControl3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl3'
    _iid_ = Guid('{586328f8-8cdd-40ae-9338-af2a7be845e5}')
    @winrt_commethod(6)
    def add_MapRightTapped(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapRightTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MapRightTapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMapControl4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl4'
    _iid_ = Guid('{068f132a-1817-466d-b7ce-419b3f8e248b}')
    @winrt_commethod(6)
    def get_BusinessLandmarksEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_BusinessLandmarksEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TransitFeaturesEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_TransitFeaturesEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetVisibleRegion(self, region: Windows.UI.Xaml.Controls.Maps.MapVisibleRegionKind) -> Windows.Devices.Geolocation.Geopath: ...
    BusinessLandmarksEnabled = property(get_BusinessLandmarksEnabled, put_BusinessLandmarksEnabled)
    TransitFeaturesEnabled = property(get_TransitFeaturesEnabled, put_TransitFeaturesEnabled)
class IMapControl5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl5'
    _iid_ = Guid('{dd9b0ffd-7823-46a2-82c9-65ddac4f365f}')
    @winrt_commethod(6)
    def get_MapProjection(self) -> Windows.UI.Xaml.Controls.Maps.MapProjection: ...
    @winrt_commethod(7)
    def put_MapProjection(self, value: Windows.UI.Xaml.Controls.Maps.MapProjection) -> Void: ...
    @winrt_commethod(8)
    def get_StyleSheet(self) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(9)
    def put_StyleSheet(self, value: Windows.UI.Xaml.Controls.Maps.MapStyleSheet) -> Void: ...
    @winrt_commethod(10)
    def get_ViewPadding(self) -> Windows.UI.Xaml.Thickness: ...
    @winrt_commethod(11)
    def put_ViewPadding(self, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_commethod(12)
    def add_MapContextRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapContextRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_MapContextRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def FindMapElementsAtOffsetWithRadius(self, offset: Windows.Foundation.Point, radius: Double) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_commethod(15)
    def GetLocationFromOffsetWithReferenceSystem(self, offset: Windows.Foundation.Point, desiredReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, location: POINTER(Windows.Devices.Geolocation.Geopoint)) -> Void: ...
    @winrt_commethod(16)
    def StartContinuousPan(self, horizontalPixelsPerSecond: Double, verticalPixelsPerSecond: Double) -> Void: ...
    @winrt_commethod(17)
    def StopContinuousPan(self) -> Void: ...
    @winrt_commethod(18)
    def TryPanAsync(self, horizontalPixels: Double, verticalPixels: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(19)
    def TryPanToAsync(self, location: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    MapProjection = property(get_MapProjection, put_MapProjection)
    StyleSheet = property(get_StyleSheet, put_StyleSheet)
    ViewPadding = property(get_ViewPadding, put_ViewPadding)
class IMapControl6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl6'
    _iid_ = Guid('{b0da89a2-1041-4bea-b88a-12ac9a82e0e2}')
    @winrt_commethod(6)
    def get_Layers(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapLayer]: ...
    @winrt_commethod(7)
    def put_Layers(self, value: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapLayer]) -> Void: ...
    @winrt_commethod(8)
    def TryGetLocationFromOffset(self, offset: Windows.Foundation.Point, location: POINTER(Windows.Devices.Geolocation.Geopoint)) -> Boolean: ...
    @winrt_commethod(9)
    def TryGetLocationFromOffsetWithReferenceSystem(self, offset: Windows.Foundation.Point, desiredReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, location: POINTER(Windows.Devices.Geolocation.Geopoint)) -> Boolean: ...
    Layers = property(get_Layers, put_Layers)
class IMapControl7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl7'
    _iid_ = Guid('{0d86e453-0c1f-4f7e-ae66-4ad0b4987857}')
    @winrt_commethod(6)
    def get_Region(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Region(self, value: WinRT_String) -> Void: ...
    Region = property(get_Region, put_Region)
class IMapControl8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControl8'
    _iid_ = Guid('{009e9c46-724d-53ca-9421-7a48fc731523}')
    @winrt_commethod(6)
    def get_CanTiltDown(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanTiltUp(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanZoomIn(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_CanZoomOut(self) -> Boolean: ...
    CanTiltDown = property(get_CanTiltDown, None)
    CanTiltUp = property(get_CanTiltUp, None)
    CanZoomIn = property(get_CanZoomIn, None)
    CanZoomOut = property(get_CanZoomOut, None)
class IMapControlBusinessLandmarkClickEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkClickEventArgs'
    _iid_ = Guid('{5e464922-4a1a-4797-beb7-5cf7754cb867}')
    @winrt_commethod(6)
    def get_LocalLocations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class IMapControlBusinessLandmarkPointerEnteredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerEnteredEventArgs'
    _iid_ = Guid('{5e4081a6-ea98-4f95-8caf-5b42696ff504}')
    @winrt_commethod(6)
    def get_LocalLocations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class IMapControlBusinessLandmarkPointerExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerExitedEventArgs'
    _iid_ = Guid('{2bb52caf-f24a-46d0-b463-65f719731057}')
    @winrt_commethod(6)
    def get_LocalLocations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class IMapControlBusinessLandmarkRightTappedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkRightTappedEventArgs'
    _iid_ = Guid('{59ab8ae7-f184-4ab1-b0b0-35c8bf0654b2}')
    @winrt_commethod(6)
    def get_LocalLocations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class IMapControlDataHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper'
    _iid_ = Guid('{8bb0f09c-14ab-486c-9de5-5a5def0205a2}')
    @winrt_commethod(6)
    def add_BusinessLandmarkClick(self, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkClickEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BusinessLandmarkClick(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_TransitFeatureClick(self, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureClickEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_TransitFeatureClick(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_BusinessLandmarkRightTapped(self, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkRightTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_BusinessLandmarkRightTapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_TransitFeatureRightTapped(self, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureRightTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_TransitFeatureRightTapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMapControlDataHelper2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2'
    _iid_ = Guid('{59ce429e-562f-4c21-a674-0f11decf0fb3}')
    @winrt_commethod(6)
    def add_BusinessLandmarkPointerEntered(self, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerEnteredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BusinessLandmarkPointerEntered(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_TransitFeaturePointerEntered(self, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerEnteredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_TransitFeaturePointerEntered(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_BusinessLandmarkPointerExited(self, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_BusinessLandmarkPointerExited(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_TransitFeaturePointerExited(self, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_TransitFeaturePointerExited(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMapControlDataHelperFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlDataHelperFactory'
    _iid_ = Guid('{3b70aa8e-02ef-469c-bbaf-dc2158d4289b}')
    @winrt_commethod(6)
    def CreateInstance(self, map: Windows.UI.Xaml.Controls.Maps.MapControl) -> Windows.UI.Xaml.Controls.Maps.MapControlDataHelper: ...
class IMapControlDataHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlDataHelperStatics'
    _iid_ = Guid('{7a6632d6-e944-4110-83cf-314d0722e2e5}')
    @winrt_commethod(6)
    def CreateMapControl(self, rasterRenderMode: Boolean) -> Windows.UI.Xaml.Controls.Maps.MapControl: ...
class IMapControlStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics'
    _iid_ = Guid('{c2c61795-2147-4f0a-942a-5493a85de807}')
    @winrt_commethod(6)
    def get_CenterProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ChildrenProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ColorSchemeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_DesiredPitchProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_HeadingProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_LandmarksVisibleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_LoadingStatusProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_MapServiceTokenProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_PedestrianFeaturesVisibleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_PitchProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_StyleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_TrafficFlowVisibleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_TransformOriginProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(19)
    def get_WatermarkModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(20)
    def get_ZoomLevelProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(21)
    def get_MapElementsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(22)
    def get_RoutesProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(23)
    def get_TileSourcesProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(24)
    def get_LocationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(25)
    def GetLocation(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(26)
    def SetLocation(self, element: Windows.UI.Xaml.DependencyObject, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(27)
    def get_NormalizedAnchorPointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(28)
    def GetNormalizedAnchorPoint(self, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Point: ...
    @winrt_commethod(29)
    def SetNormalizedAnchorPoint(self, element: Windows.UI.Xaml.DependencyObject, value: Windows.Foundation.Point) -> Void: ...
    CenterProperty = property(get_CenterProperty, None)
    ChildrenProperty = property(get_ChildrenProperty, None)
    ColorSchemeProperty = property(get_ColorSchemeProperty, None)
    DesiredPitchProperty = property(get_DesiredPitchProperty, None)
    HeadingProperty = property(get_HeadingProperty, None)
    LandmarksVisibleProperty = property(get_LandmarksVisibleProperty, None)
    LoadingStatusProperty = property(get_LoadingStatusProperty, None)
    MapServiceTokenProperty = property(get_MapServiceTokenProperty, None)
    PedestrianFeaturesVisibleProperty = property(get_PedestrianFeaturesVisibleProperty, None)
    PitchProperty = property(get_PitchProperty, None)
    StyleProperty = property(get_StyleProperty, None)
    TrafficFlowVisibleProperty = property(get_TrafficFlowVisibleProperty, None)
    TransformOriginProperty = property(get_TransformOriginProperty, None)
    WatermarkModeProperty = property(get_WatermarkModeProperty, None)
    ZoomLevelProperty = property(get_ZoomLevelProperty, None)
    MapElementsProperty = property(get_MapElementsProperty, None)
    RoutesProperty = property(get_RoutesProperty, None)
    TileSourcesProperty = property(get_TileSourcesProperty, None)
    LocationProperty = property(get_LocationProperty, None)
    NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
class IMapControlStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics2'
    _iid_ = Guid('{04852b93-b446-4d31-9752-1ec69a5996ae}')
    @winrt_commethod(6)
    def get_BusinessLandmarksVisibleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TransitFeaturesVisibleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_PanInteractionModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RotateInteractionModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_TiltInteractionModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_ZoomInteractionModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_Is3DSupportedProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_IsStreetsideSupportedProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_SceneProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    BusinessLandmarksVisibleProperty = property(get_BusinessLandmarksVisibleProperty, None)
    TransitFeaturesVisibleProperty = property(get_TransitFeaturesVisibleProperty, None)
    PanInteractionModeProperty = property(get_PanInteractionModeProperty, None)
    RotateInteractionModeProperty = property(get_RotateInteractionModeProperty, None)
    TiltInteractionModeProperty = property(get_TiltInteractionModeProperty, None)
    ZoomInteractionModeProperty = property(get_ZoomInteractionModeProperty, None)
    Is3DSupportedProperty = property(get_Is3DSupportedProperty, None)
    IsStreetsideSupportedProperty = property(get_IsStreetsideSupportedProperty, None)
    SceneProperty = property(get_SceneProperty, None)
class IMapControlStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics4'
    _iid_ = Guid('{fe785d97-5d13-4fa1-bf1d-84061768c183}')
    @winrt_commethod(6)
    def get_BusinessLandmarksEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TransitFeaturesEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    BusinessLandmarksEnabledProperty = property(get_BusinessLandmarksEnabledProperty, None)
    TransitFeaturesEnabledProperty = property(get_TransitFeaturesEnabledProperty, None)
class IMapControlStatics5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics5'
    _iid_ = Guid('{09626f00-b7dd-4189-a7f7-830c412deea3}')
    @winrt_commethod(6)
    def get_MapProjectionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StyleSheetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ViewPaddingProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    MapProjectionProperty = property(get_MapProjectionProperty, None)
    StyleSheetProperty = property(get_StyleSheetProperty, None)
    ViewPaddingProperty = property(get_ViewPaddingProperty, None)
class IMapControlStatics6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics6'
    _iid_ = Guid('{3ccfdd7f-24d1-40a2-8351-b3063a8c95a4}')
    @winrt_commethod(6)
    def get_LayersProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    LayersProperty = property(get_LayersProperty, None)
class IMapControlStatics7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics7'
    _iid_ = Guid('{55f1ac4d-72c2-46b2-b7ae-790260be641b}')
    @winrt_commethod(6)
    def get_RegionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    RegionProperty = property(get_RegionProperty, None)
class IMapControlStatics8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlStatics8'
    _iid_ = Guid('{adb7a7b0-0605-592c-bf9d-d10bdc2be47b}')
    @winrt_commethod(6)
    def get_CanTiltDownProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CanTiltUpProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_CanZoomInProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_CanZoomOutProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CanTiltDownProperty = property(get_CanTiltDownProperty, None)
    CanTiltUpProperty = property(get_CanTiltUpProperty, None)
    CanZoomInProperty = property(get_CanZoomInProperty, None)
    CanZoomOutProperty = property(get_CanZoomOutProperty, None)
class IMapControlTransitFeatureClickEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs'
    _iid_ = Guid('{76179969-b765-4622-b08a-3072745a4541}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_TransitProperties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class IMapControlTransitFeaturePointerEnteredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs'
    _iid_ = Guid('{73911a4e-ec4f-479e-94a1-36e081d0d897}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_TransitProperties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class IMapControlTransitFeaturePointerExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs'
    _iid_ = Guid('{6a11258d-448d-44e7-bc69-d13d497154e9}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_TransitProperties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class IMapControlTransitFeatureRightTappedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs'
    _iid_ = Guid('{aea1cc49-a729-4eae-a59a-3ec9a125a028}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_TransitProperties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class IMapCustomExperience(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCustomExperience'
    _iid_ = Guid('{64592866-14a3-4e5f-8883-8e9c500eeede}')
class IMapCustomExperienceChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCustomExperienceChangedEventArgs'
    _iid_ = Guid('{b9e6fb9b-8fc1-4042-ac34-a61b38bb7514}')
class IMapCustomExperienceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapCustomExperienceFactory'
    _iid_ = Guid('{7a403fb5-a1b1-4e7f-921e-3e6b8d8ebed6}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapCustomExperience: ...
class IMapElement(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement'
    _iid_ = Guid('{d61fc4df-b245-47f2-9ac2-43c058b1c903}')
    @winrt_commethod(6)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_ZIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Visible(self, value: Boolean) -> Void: ...
    ZIndex = property(get_ZIndex, put_ZIndex)
    Visible = property(get_Visible, put_Visible)
class IMapElement2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement2'
    _iid_ = Guid('{6619f261-fba6-4964-a7ff-f1af63ab9cb0}')
    @winrt_commethod(6)
    def get_MapTabIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_MapTabIndex(self, value: Int32) -> Void: ...
    MapTabIndex = property(get_MapTabIndex, put_MapTabIndex)
class IMapElement3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement3'
    _iid_ = Guid('{13efbc59-45ed-48b4-93ad-e3f78f8cf218}')
    @winrt_commethod(6)
    def get_MapStyleSheetEntry(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_MapStyleSheetEntry(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_MapStyleSheetEntryState(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_MapStyleSheetEntryState(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Tag(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(11)
    def put_Tag(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    MapStyleSheetEntry = property(get_MapStyleSheetEntry, put_MapStyleSheetEntry)
    MapStyleSheetEntryState = property(get_MapStyleSheetEntryState, put_MapStyleSheetEntryState)
    Tag = property(get_Tag, put_Tag)
class IMapElement3D(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement3D'
    _iid_ = Guid('{827af8d5-3843-48e2-bd00-0f0644fbe6a5}')
    @winrt_commethod(6)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Location(self, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_Model(self) -> Windows.UI.Xaml.Controls.Maps.MapModel3D: ...
    @winrt_commethod(9)
    def put_Model(self, value: Windows.UI.Xaml.Controls.Maps.MapModel3D) -> Void: ...
    @winrt_commethod(10)
    def get_Heading(self) -> Double: ...
    @winrt_commethod(11)
    def put_Heading(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_Pitch(self) -> Double: ...
    @winrt_commethod(13)
    def put_Pitch(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_Roll(self) -> Double: ...
    @winrt_commethod(15)
    def put_Roll(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_Scale(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(17)
    def put_Scale(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    Location = property(get_Location, put_Location)
    Model = property(get_Model, put_Model)
    Heading = property(get_Heading, put_Heading)
    Pitch = property(get_Pitch, put_Pitch)
    Roll = property(get_Roll, put_Roll)
    Scale = property(get_Scale, put_Scale)
class IMapElement3DStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics'
    _iid_ = Guid('{6128011a-450f-442a-b9d9-aa815c71907a}')
    @winrt_commethod(6)
    def get_LocationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_HeadingProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_PitchProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RollProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_ScaleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    LocationProperty = property(get_LocationProperty, None)
    HeadingProperty = property(get_HeadingProperty, None)
    PitchProperty = property(get_PitchProperty, None)
    RollProperty = property(get_RollProperty, None)
    ScaleProperty = property(get_ScaleProperty, None)
class IMapElement4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElement4'
    _iid_ = Guid('{645883b6-1fc1-4ceb-93bd-dc2c960072e9}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class IMapElementClickEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs'
    _iid_ = Guid('{40168a11-d080-4519-99a1-3149fb8999d0}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElements(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
class IMapElementFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementFactory'
    _iid_ = Guid('{4a30d007-0bd6-47a5-860b-7e7cf5f0c573}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapElement: ...
class IMapElementPointerEnteredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs'
    _iid_ = Guid('{ab85dd4e-91d7-4b31-8f0a-d390c7d3a2ef}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElement(self) -> Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
class IMapElementPointerExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs'
    _iid_ = Guid('{c1a45af9-60c9-4679-9119-20abc75d931f}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElement(self) -> Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
class IMapElementStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementStatics'
    _iid_ = Guid('{e8c71cf2-bfef-4b49-8e99-41b5e3789fd2}')
    @winrt_commethod(6)
    def get_ZIndexProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_VisibleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ZIndexProperty = property(get_ZIndexProperty, None)
    VisibleProperty = property(get_VisibleProperty, None)
class IMapElementStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementStatics2'
    _iid_ = Guid('{9bf72f30-80fe-4f30-bcc1-fa894050f676}')
    @winrt_commethod(6)
    def get_MapTabIndexProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    MapTabIndexProperty = property(get_MapTabIndexProperty, None)
class IMapElementStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementStatics3'
    _iid_ = Guid('{e11ee92f-9742-49aa-aad8-2e466bff3796}')
    @winrt_commethod(6)
    def get_MapStyleSheetEntryProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MapStyleSheetEntryStateProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_TagProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    MapStyleSheetEntryProperty = property(get_MapStyleSheetEntryProperty, None)
    MapStyleSheetEntryStateProperty = property(get_MapStyleSheetEntryStateProperty, None)
    TagProperty = property(get_TagProperty, None)
class IMapElementStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementStatics4'
    _iid_ = Guid('{a4296f0b-dff8-467c-9315-6f6db93ee2ba}')
    @winrt_commethod(6)
    def get_IsEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    IsEnabledProperty = property(get_IsEnabledProperty, None)
class IMapElementsLayer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayer'
    _iid_ = Guid('{de79689a-01ef-46f4-ac60-7c200b552610}')
    @winrt_commethod(6)
    def get_MapElements(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_commethod(7)
    def put_MapElements(self, value: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]) -> Void: ...
    @winrt_commethod(8)
    def add_MapElementClick(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapElementsLayer, Windows.UI.Xaml.Controls.Maps.MapElementsLayerClickEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MapElementClick(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_MapElementPointerEntered(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapElementsLayer, Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerEnteredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_MapElementPointerEntered(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_MapElementPointerExited(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapElementsLayer, Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_MapElementPointerExited(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_MapContextRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapElementsLayer, Windows.UI.Xaml.Controls.Maps.MapElementsLayerContextRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_MapContextRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MapElements = property(get_MapElements, put_MapElements)
class IMapElementsLayerClickEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs'
    _iid_ = Guid('{2ca7cf66-af1b-4c05-8c85-f74ae3d4677f}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElements(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
class IMapElementsLayerContextRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs'
    _iid_ = Guid('{da45d0b3-7a0e-4758-808b-3a637627eb0d}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElements(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
class IMapElementsLayerPointerEnteredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs'
    _iid_ = Guid('{757fc032-4694-4404-8c89-348b6b76c5e6}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElement(self) -> Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
class IMapElementsLayerPointerExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs'
    _iid_ = Guid('{92f3c6ad-03ed-4c39-af20-2a07ee1ccea6}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def get_MapElement(self) -> Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
class IMapElementsLayerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapElementsLayerStatics'
    _iid_ = Guid('{34005727-f509-4d28-9180-911c03411d74}')
    @winrt_commethod(6)
    def get_MapElementsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    MapElementsProperty = property(get_MapElementsProperty, None)
class IMapIcon(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapIcon'
    _iid_ = Guid('{d2096872-23d9-4a2b-8be0-69f3a85482ab}')
    @winrt_commethod(6)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def put_Location(self, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_NormalizedAnchorPoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(11)
    def put_NormalizedAnchorPoint(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(12)
    def get_Image(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(13)
    def put_Image(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    Location = property(get_Location, put_Location)
    Title = property(get_Title, put_Title)
    NormalizedAnchorPoint = property(get_NormalizedAnchorPoint, put_NormalizedAnchorPoint)
    Image = property(get_Image, put_Image)
class IMapIcon2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapIcon2'
    _iid_ = Guid('{611254b9-d8aa-4bbd-a316-badf06911d63}')
    @winrt_commethod(6)
    def get_CollisionBehaviorDesired(self) -> Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior: ...
    @winrt_commethod(7)
    def put_CollisionBehaviorDesired(self, value: Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior) -> Void: ...
    CollisionBehaviorDesired = property(get_CollisionBehaviorDesired, put_CollisionBehaviorDesired)
class IMapIconStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapIconStatics'
    _iid_ = Guid('{dcbc9e56-1190-4b5d-9e56-e5b6724aa328}')
    @winrt_commethod(6)
    def get_LocationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TitleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_NormalizedAnchorPointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    LocationProperty = property(get_LocationProperty, None)
    TitleProperty = property(get_TitleProperty, None)
    NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
class IMapIconStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapIconStatics2'
    _iid_ = Guid('{ff4c306a-cf76-46ab-a12f-b603b986c696}')
    @winrt_commethod(6)
    def get_CollisionBehaviorDesiredProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CollisionBehaviorDesiredProperty = property(get_CollisionBehaviorDesiredProperty, None)
class IMapInputEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapInputEventArgs'
    _iid_ = Guid('{9fc503a0-a8a2-4394-92e9-2247764f2f49}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
class IMapItemsControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapItemsControl'
    _iid_ = Guid('{94c2c4d3-b335-42c5-b660-e6a07ec3bddc}')
    @winrt_commethod(6)
    def get_ItemsSource(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def put_ItemsSource(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(8)
    def get_Items(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_commethod(9)
    def get_ItemTemplate(self) -> Windows.UI.Xaml.DataTemplate: ...
    @winrt_commethod(10)
    def put_ItemTemplate(self, value: Windows.UI.Xaml.DataTemplate) -> Void: ...
    ItemsSource = property(get_ItemsSource, put_ItemsSource)
    Items = property(get_Items, None)
    ItemTemplate = property(get_ItemTemplate, put_ItemTemplate)
class IMapItemsControlStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapItemsControlStatics'
    _iid_ = Guid('{33a859c7-789b-425c-8a0a-32385896cb4a}')
    @winrt_commethod(6)
    def get_ItemsSourceProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ItemsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ItemTemplateProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ItemsSourceProperty = property(get_ItemsSourceProperty, None)
    ItemsProperty = property(get_ItemsProperty, None)
    ItemTemplateProperty = property(get_ItemTemplateProperty, None)
class IMapLayer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapLayer'
    _iid_ = Guid('{6d0ff9c1-a14d-4f97-8f57-46715b57683a}')
    @winrt_commethod(6)
    def get_MapTabIndex(self) -> Int32: ...
    @winrt_commethod(7)
    def put_MapTabIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Visible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(11)
    def put_ZIndex(self, value: Int32) -> Void: ...
    MapTabIndex = property(get_MapTabIndex, put_MapTabIndex)
    Visible = property(get_Visible, put_Visible)
    ZIndex = property(get_ZIndex, put_ZIndex)
class IMapLayerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapLayerFactory'
    _iid_ = Guid('{e02a2207-dee3-47c8-9825-bd029c5752f7}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapLayer: ...
class IMapLayerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapLayerStatics'
    _iid_ = Guid('{9ca4a26b-5db9-4f0c-bdd5-b1bffdcce946}')
    @winrt_commethod(6)
    def get_MapTabIndexProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_VisibleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ZIndexProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    MapTabIndexProperty = property(get_MapTabIndexProperty, None)
    VisibleProperty = property(get_VisibleProperty, None)
    ZIndexProperty = property(get_ZIndexProperty, None)
class IMapModel3D(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapModel3D'
    _iid_ = Guid('{f8c541a1-ca27-4968-a2bf-9c20f06a0468}')
class IMapModel3DFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapModel3DFactory'
    _iid_ = Guid('{df7f0bcc-580a-498b-939b-0119a9dadb9e}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapModel3D: ...
class IMapModel3DStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapModel3DStatics'
    _iid_ = Guid('{4834a480-8e56-4b0f-872d-7ead103187cd}')
    @winrt_commethod(6)
    def CreateFrom3MFAsync(self, source: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Controls.Maps.MapModel3D]: ...
    @winrt_commethod(7)
    def CreateFrom3MFWithShadingOptionAsync(self, source: Windows.Storage.Streams.IRandomAccessStreamReference, shadingOption: Windows.UI.Xaml.Controls.Maps.MapModel3DShadingOption) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Controls.Maps.MapModel3D]: ...
class IMapPolygon(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolygon'
    _iid_ = Guid('{abda2285-4926-4c3a-a5f9-19df7f69db3d}')
    @winrt_commethod(6)
    def get_Path(self) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(7)
    def put_Path(self, value: Windows.Devices.Geolocation.Geopath) -> Void: ...
    @winrt_commethod(8)
    def get_StrokeColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_StrokeColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_StrokeThickness(self) -> Double: ...
    @winrt_commethod(11)
    def put_StrokeThickness(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_StrokeDashed(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_StrokeDashed(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_FillColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(15)
    def put_FillColor(self, value: Windows.UI.Color) -> Void: ...
    Path = property(get_Path, put_Path)
    StrokeColor = property(get_StrokeColor, put_StrokeColor)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
    StrokeDashed = property(get_StrokeDashed, put_StrokeDashed)
    FillColor = property(get_FillColor, put_FillColor)
class IMapPolygon2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolygon2'
    _iid_ = Guid('{96c8a11e-636b-4018-9c2e-acc9122a01b2}')
    @winrt_commethod(6)
    def get_Paths(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Geolocation.Geopath]: ...
    Paths = property(get_Paths, None)
class IMapPolygonStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolygonStatics'
    _iid_ = Guid('{37f573be-097b-424c-87cc-2ee042fda6d2}')
    @winrt_commethod(6)
    def get_PathProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StrokeThicknessProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_StrokeDashedProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    PathProperty = property(get_PathProperty, None)
    StrokeThicknessProperty = property(get_StrokeThicknessProperty, None)
    StrokeDashedProperty = property(get_StrokeDashedProperty, None)
class IMapPolyline(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolyline'
    _iid_ = Guid('{fbad24a2-24df-4a86-8ffa-0f8f4d9ec17d}')
    @winrt_commethod(6)
    def get_Path(self) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(7)
    def put_Path(self, value: Windows.Devices.Geolocation.Geopath) -> Void: ...
    @winrt_commethod(8)
    def get_StrokeColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_StrokeColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_StrokeThickness(self) -> Double: ...
    @winrt_commethod(11)
    def put_StrokeThickness(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_StrokeDashed(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_StrokeDashed(self, value: Boolean) -> Void: ...
    Path = property(get_Path, put_Path)
    StrokeColor = property(get_StrokeColor, put_StrokeColor)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
    StrokeDashed = property(get_StrokeDashed, put_StrokeDashed)
class IMapPolylineStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapPolylineStatics'
    _iid_ = Guid('{61fde44b-1ddf-4303-b809-ec87f58ad065}')
    @winrt_commethod(6)
    def get_PathProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StrokeDashedProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    PathProperty = property(get_PathProperty, None)
    StrokeDashedProperty = property(get_StrokeDashedProperty, None)
class IMapRightTappedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapRightTappedEventArgs'
    _iid_ = Guid('{20943171-6fe8-40a6-ad0e-297379b575a7}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
class IMapRouteView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapRouteView'
    _iid_ = Guid('{740eaec5-bacc-41e1-a67e-dd6513832049}')
    @winrt_commethod(6)
    def get_RouteColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_RouteColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_OutlineColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_OutlineColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_Route(self) -> Windows.Services.Maps.MapRoute: ...
    RouteColor = property(get_RouteColor, put_RouteColor)
    OutlineColor = property(get_OutlineColor, put_OutlineColor)
    Route = property(get_Route, None)
class IMapRouteViewFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapRouteViewFactory'
    _iid_ = Guid('{f083addf-0066-4628-82fe-ea78c23cec1e}')
    @winrt_commethod(6)
    def CreateInstanceWithMapRoute(self, route: Windows.Services.Maps.MapRoute, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapRouteView: ...
class IMapScene(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapScene'
    _iid_ = Guid('{8bba10a9-50e7-482c-9789-c688b178ac24}')
    @winrt_commethod(6)
    def get_TargetCamera(self) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_commethod(7)
    def add_TargetCameraChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapScene, Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_TargetCameraChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    TargetCamera = property(get_TargetCamera, None)
class IMapSceneStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapSceneStatics'
    _iid_ = Guid('{03e4ad6c-86ec-44d9-9597-fb75b7deba0a}')
    @winrt_commethod(6)
    def CreateFromBoundingBox(self, bounds: Windows.Devices.Geolocation.GeoboundingBox) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(7)
    def CreateFromBoundingBoxWithHeadingAndPitch(self, bounds: Windows.Devices.Geolocation.GeoboundingBox, headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(8)
    def CreateFromCamera(self, camera: Windows.UI.Xaml.Controls.Maps.MapCamera) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(9)
    def CreateFromLocation(self, location: Windows.Devices.Geolocation.Geopoint) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(10)
    def CreateFromLocationWithHeadingAndPitch(self, location: Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(11)
    def CreateFromLocationAndRadius(self, location: Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(12)
    def CreateFromLocationAndRadiusWithHeadingAndPitch(self, location: Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double, headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(13)
    def CreateFromLocations(self, locations: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint]) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_commethod(14)
    def CreateFromLocationsWithHeadingAndPitch(self, locations: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint], headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
class IMapStyleSheet(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapStyleSheet'
    _iid_ = Guid('{ae54b2bf-8991-42ed-8d58-20473deede1d}')
class IMapStyleSheetEntriesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics'
    _iid_ = Guid('{c9636345-ef1a-41a4-a757-bd4f43e1e4d1}')
    @winrt_commethod(6)
    def get_Area(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Airport(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Cemetery(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Continent(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Education(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_IndigenousPeoplesReserve(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Island(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Medical(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Military(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_Nautical(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_Neighborhood(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_Runway(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_Sand(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_ShoppingCenter(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_Stadium(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_Vegetation(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_Forest(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_GolfCourse(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_Park(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def get_PlayingField(self) -> WinRT_String: ...
    @winrt_commethod(26)
    def get_Reserve(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def get_Point(self) -> WinRT_String: ...
    @winrt_commethod(28)
    def get_NaturalPoint(self) -> WinRT_String: ...
    @winrt_commethod(29)
    def get_Peak(self) -> WinRT_String: ...
    @winrt_commethod(30)
    def get_VolcanicPeak(self) -> WinRT_String: ...
    @winrt_commethod(31)
    def get_WaterPoint(self) -> WinRT_String: ...
    @winrt_commethod(32)
    def get_PointOfInterest(self) -> WinRT_String: ...
    @winrt_commethod(33)
    def get_Business(self) -> WinRT_String: ...
    @winrt_commethod(34)
    def get_FoodPoint(self) -> WinRT_String: ...
    @winrt_commethod(35)
    def get_PopulatedPlace(self) -> WinRT_String: ...
    @winrt_commethod(36)
    def get_Capital(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def get_AdminDistrictCapital(self) -> WinRT_String: ...
    @winrt_commethod(38)
    def get_CountryRegionCapital(self) -> WinRT_String: ...
    @winrt_commethod(39)
    def get_RoadShield(self) -> WinRT_String: ...
    @winrt_commethod(40)
    def get_RoadExit(self) -> WinRT_String: ...
    @winrt_commethod(41)
    def get_Transit(self) -> WinRT_String: ...
    @winrt_commethod(42)
    def get_Political(self) -> WinRT_String: ...
    @winrt_commethod(43)
    def get_CountryRegion(self) -> WinRT_String: ...
    @winrt_commethod(44)
    def get_AdminDistrict(self) -> WinRT_String: ...
    @winrt_commethod(45)
    def get_District(self) -> WinRT_String: ...
    @winrt_commethod(46)
    def get_Structure(self) -> WinRT_String: ...
    @winrt_commethod(47)
    def get_Building(self) -> WinRT_String: ...
    @winrt_commethod(48)
    def get_EducationBuilding(self) -> WinRT_String: ...
    @winrt_commethod(49)
    def get_MedicalBuilding(self) -> WinRT_String: ...
    @winrt_commethod(50)
    def get_TransitBuilding(self) -> WinRT_String: ...
    @winrt_commethod(51)
    def get_Transportation(self) -> WinRT_String: ...
    @winrt_commethod(52)
    def get_Road(self) -> WinRT_String: ...
    @winrt_commethod(53)
    def get_ControlledAccessHighway(self) -> WinRT_String: ...
    @winrt_commethod(54)
    def get_HighSpeedRamp(self) -> WinRT_String: ...
    @winrt_commethod(55)
    def get_Highway(self) -> WinRT_String: ...
    @winrt_commethod(56)
    def get_MajorRoad(self) -> WinRT_String: ...
    @winrt_commethod(57)
    def get_ArterialRoad(self) -> WinRT_String: ...
    @winrt_commethod(58)
    def get_Street(self) -> WinRT_String: ...
    @winrt_commethod(59)
    def get_Ramp(self) -> WinRT_String: ...
    @winrt_commethod(60)
    def get_UnpavedStreet(self) -> WinRT_String: ...
    @winrt_commethod(61)
    def get_TollRoad(self) -> WinRT_String: ...
    @winrt_commethod(62)
    def get_Railway(self) -> WinRT_String: ...
    @winrt_commethod(63)
    def get_Trail(self) -> WinRT_String: ...
    @winrt_commethod(64)
    def get_WaterRoute(self) -> WinRT_String: ...
    @winrt_commethod(65)
    def get_Water(self) -> WinRT_String: ...
    @winrt_commethod(66)
    def get_River(self) -> WinRT_String: ...
    @winrt_commethod(67)
    def get_RouteLine(self) -> WinRT_String: ...
    @winrt_commethod(68)
    def get_WalkingRoute(self) -> WinRT_String: ...
    @winrt_commethod(69)
    def get_DrivingRoute(self) -> WinRT_String: ...
    Area = property(get_Area, None)
    Airport = property(get_Airport, None)
    Cemetery = property(get_Cemetery, None)
    Continent = property(get_Continent, None)
    Education = property(get_Education, None)
    IndigenousPeoplesReserve = property(get_IndigenousPeoplesReserve, None)
    Island = property(get_Island, None)
    Medical = property(get_Medical, None)
    Military = property(get_Military, None)
    Nautical = property(get_Nautical, None)
    Neighborhood = property(get_Neighborhood, None)
    Runway = property(get_Runway, None)
    Sand = property(get_Sand, None)
    ShoppingCenter = property(get_ShoppingCenter, None)
    Stadium = property(get_Stadium, None)
    Vegetation = property(get_Vegetation, None)
    Forest = property(get_Forest, None)
    GolfCourse = property(get_GolfCourse, None)
    Park = property(get_Park, None)
    PlayingField = property(get_PlayingField, None)
    Reserve = property(get_Reserve, None)
    Point = property(get_Point, None)
    NaturalPoint = property(get_NaturalPoint, None)
    Peak = property(get_Peak, None)
    VolcanicPeak = property(get_VolcanicPeak, None)
    WaterPoint = property(get_WaterPoint, None)
    PointOfInterest = property(get_PointOfInterest, None)
    Business = property(get_Business, None)
    FoodPoint = property(get_FoodPoint, None)
    PopulatedPlace = property(get_PopulatedPlace, None)
    Capital = property(get_Capital, None)
    AdminDistrictCapital = property(get_AdminDistrictCapital, None)
    CountryRegionCapital = property(get_CountryRegionCapital, None)
    RoadShield = property(get_RoadShield, None)
    RoadExit = property(get_RoadExit, None)
    Transit = property(get_Transit, None)
    Political = property(get_Political, None)
    CountryRegion = property(get_CountryRegion, None)
    AdminDistrict = property(get_AdminDistrict, None)
    District = property(get_District, None)
    Structure = property(get_Structure, None)
    Building = property(get_Building, None)
    EducationBuilding = property(get_EducationBuilding, None)
    MedicalBuilding = property(get_MedicalBuilding, None)
    TransitBuilding = property(get_TransitBuilding, None)
    Transportation = property(get_Transportation, None)
    Road = property(get_Road, None)
    ControlledAccessHighway = property(get_ControlledAccessHighway, None)
    HighSpeedRamp = property(get_HighSpeedRamp, None)
    Highway = property(get_Highway, None)
    MajorRoad = property(get_MajorRoad, None)
    ArterialRoad = property(get_ArterialRoad, None)
    Street = property(get_Street, None)
    Ramp = property(get_Ramp, None)
    UnpavedStreet = property(get_UnpavedStreet, None)
    TollRoad = property(get_TollRoad, None)
    Railway = property(get_Railway, None)
    Trail = property(get_Trail, None)
    WaterRoute = property(get_WaterRoute, None)
    Water = property(get_Water, None)
    River = property(get_River, None)
    RouteLine = property(get_RouteLine, None)
    WalkingRoute = property(get_WalkingRoute, None)
    DrivingRoute = property(get_DrivingRoute, None)
class IMapStyleSheetEntryStatesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntryStatesStatics'
    _iid_ = Guid('{23ac5532-866d-4bfa-b481-39bea1de3506}')
    @winrt_commethod(6)
    def get_Disabled(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Hover(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Selected(self) -> WinRT_String: ...
    Disabled = property(get_Disabled, None)
    Hover = property(get_Hover, None)
    Selected = property(get_Selected, None)
class IMapStyleSheetStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics'
    _iid_ = Guid('{abbd00ad-0a1c-4335-82f4-61d936aa197d}')
    @winrt_commethod(6)
    def Aerial(self) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(7)
    def AerialWithOverlay(self) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(8)
    def RoadLight(self) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(9)
    def RoadDark(self) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(10)
    def RoadHighContrastLight(self) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(11)
    def RoadHighContrastDark(self) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(12)
    def Combine(self, styleSheets: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Controls.Maps.MapStyleSheet]) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(13)
    def ParseFromJson(self, styleAsJson: WinRT_String) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_commethod(14)
    def TryParseFromJson(self, styleAsJson: WinRT_String, styleSheet: POINTER(Windows.UI.Xaml.Controls.Maps.MapStyleSheet)) -> Boolean: ...
class IMapTargetCameraChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs'
    _iid_ = Guid('{dbf00472-e953-4fa8-97d0-ea86359057cf}')
    @winrt_commethod(6)
    def get_Camera(self) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    Camera = property(get_Camera, None)
class IMapTargetCameraChangedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs2'
    _iid_ = Guid('{97c0b332-f2b6-460b-8d91-ac020a2383dd}')
    @winrt_commethod(6)
    def get_ChangeReason(self) -> Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    ChangeReason = property(get_ChangeReason, None)
class IMapTileBitmapRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest'
    _iid_ = Guid('{46733fbc-d89d-472b-b5f6-d7066b0584f4}')
    @winrt_commethod(6)
    def get_PixelData(self) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def put_PixelData(self, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestDeferral: ...
    PixelData = property(get_PixelData, put_PixelData)
class IMapTileBitmapRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestDeferral'
    _iid_ = Guid('{fe370542-a4ac-4efa-9665-0490b0cafdd2}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMapTileBitmapRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs'
    _iid_ = Guid('{337f691d-9b02-4aa2-8b1e-cc4d91719bf3}')
    @winrt_commethod(6)
    def get_X(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Y(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ZoomLevel(self) -> Int32: ...
    @winrt_commethod(9)
    def get_Request(self) -> Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequest: ...
    X = property(get_X, None)
    Y = property(get_Y, None)
    ZoomLevel = property(get_ZoomLevel, None)
    Request = property(get_Request, None)
class IMapTileBitmapRequestedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs2'
    _iid_ = Guid('{0261d114-246a-5296-bc85-590f53aa39c8}')
    @winrt_commethod(6)
    def get_FrameIndex(self) -> Int32: ...
    FrameIndex = property(get_FrameIndex, None)
class IMapTileDataSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileDataSource'
    _iid_ = Guid('{c03d9f5e-be1f-4c69-9969-79467a513c38}')
class IMapTileDataSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileDataSourceFactory'
    _iid_ = Guid('{a3920fbd-e446-4648-a74d-fd2c5d557c06}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapTileDataSource: ...
class IMapTileSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSource'
    _iid_ = Guid('{88a76e4e-2fdf-4567-9255-1100519c8d62}')
    @winrt_commethod(6)
    def get_DataSource(self) -> Windows.UI.Xaml.Controls.Maps.MapTileDataSource: ...
    @winrt_commethod(7)
    def put_DataSource(self, value: Windows.UI.Xaml.Controls.Maps.MapTileDataSource) -> Void: ...
    @winrt_commethod(8)
    def get_Layer(self) -> Windows.UI.Xaml.Controls.Maps.MapTileLayer: ...
    @winrt_commethod(9)
    def put_Layer(self, value: Windows.UI.Xaml.Controls.Maps.MapTileLayer) -> Void: ...
    @winrt_commethod(10)
    def get_ZoomLevelRange(self) -> Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange: ...
    @winrt_commethod(11)
    def put_ZoomLevelRange(self, value: Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange) -> Void: ...
    @winrt_commethod(12)
    def get_Bounds(self) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(13)
    def put_Bounds(self, value: Windows.Devices.Geolocation.GeoboundingBox) -> Void: ...
    @winrt_commethod(14)
    def get_AllowOverstretch(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AllowOverstretch(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_IsFadingEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsFadingEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_IsTransparencyEnabled(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_IsTransparencyEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_IsRetryEnabled(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_IsRetryEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(23)
    def put_ZIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(24)
    def get_TilePixelSize(self) -> Int32: ...
    @winrt_commethod(25)
    def put_TilePixelSize(self, value: Int32) -> Void: ...
    @winrt_commethod(26)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(27)
    def put_Visible(self, value: Boolean) -> Void: ...
    DataSource = property(get_DataSource, put_DataSource)
    Layer = property(get_Layer, put_Layer)
    ZoomLevelRange = property(get_ZoomLevelRange, put_ZoomLevelRange)
    Bounds = property(get_Bounds, put_Bounds)
    AllowOverstretch = property(get_AllowOverstretch, put_AllowOverstretch)
    IsFadingEnabled = property(get_IsFadingEnabled, put_IsFadingEnabled)
    IsTransparencyEnabled = property(get_IsTransparencyEnabled, put_IsTransparencyEnabled)
    IsRetryEnabled = property(get_IsRetryEnabled, put_IsRetryEnabled)
    ZIndex = property(get_ZIndex, put_ZIndex)
    TilePixelSize = property(get_TilePixelSize, put_TilePixelSize)
    Visible = property(get_Visible, put_Visible)
class IMapTileSource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSource2'
    _iid_ = Guid('{8e65ebbd-4095-5c15-99f1-1260b4e8b0a9}')
    @winrt_commethod(6)
    def get_AnimationState(self) -> Windows.UI.Xaml.Controls.Maps.MapTileAnimationState: ...
    @winrt_commethod(7)
    def get_AutoPlay(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AutoPlay(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_FrameCount(self) -> Int32: ...
    @winrt_commethod(10)
    def put_FrameCount(self, value: Int32) -> Void: ...
    @winrt_commethod(11)
    def get_FrameDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def put_FrameDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(13)
    def Pause(self) -> Void: ...
    @winrt_commethod(14)
    def Play(self) -> Void: ...
    @winrt_commethod(15)
    def Stop(self) -> Void: ...
    AnimationState = property(get_AnimationState, None)
    AutoPlay = property(get_AutoPlay, put_AutoPlay)
    FrameCount = property(get_FrameCount, put_FrameCount)
    FrameDuration = property(get_FrameDuration, put_FrameDuration)
class IMapTileSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSourceFactory'
    _iid_ = Guid('{cd7f811f-77fa-482b-9d34-71d31d465c48}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_commethod(7)
    def CreateInstanceWithDataSource(self, dataSource: Windows.UI.Xaml.Controls.Maps.MapTileDataSource, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_commethod(8)
    def CreateInstanceWithDataSourceAndZoomRange(self, dataSource: Windows.UI.Xaml.Controls.Maps.MapTileDataSource, zoomLevelRange: Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_commethod(9)
    def CreateInstanceWithDataSourceZoomRangeAndBounds(self, dataSource: Windows.UI.Xaml.Controls.Maps.MapTileDataSource, zoomLevelRange: Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange, bounds: Windows.Devices.Geolocation.GeoboundingBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
    @winrt_commethod(10)
    def CreateInstanceWithDataSourceZoomRangeBoundsAndTileSize(self, dataSource: Windows.UI.Xaml.Controls.Maps.MapTileDataSource, zoomLevelRange: Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange, bounds: Windows.Devices.Geolocation.GeoboundingBox, tileSizeInPixels: Int32, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Controls.Maps.MapTileSource: ...
class IMapTileSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics'
    _iid_ = Guid('{93fcc93c-7035-4603-99b1-e659921b6093}')
    @winrt_commethod(6)
    def get_DataSourceProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_LayerProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ZoomLevelRangeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_BoundsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_AllowOverstretchProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_IsFadingEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_IsTransparencyEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_IsRetryEnabledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_ZIndexProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_TilePixelSizeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_VisibleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    DataSourceProperty = property(get_DataSourceProperty, None)
    LayerProperty = property(get_LayerProperty, None)
    ZoomLevelRangeProperty = property(get_ZoomLevelRangeProperty, None)
    BoundsProperty = property(get_BoundsProperty, None)
    AllowOverstretchProperty = property(get_AllowOverstretchProperty, None)
    IsFadingEnabledProperty = property(get_IsFadingEnabledProperty, None)
    IsTransparencyEnabledProperty = property(get_IsTransparencyEnabledProperty, None)
    IsRetryEnabledProperty = property(get_IsRetryEnabledProperty, None)
    ZIndexProperty = property(get_ZIndexProperty, None)
    TilePixelSizeProperty = property(get_TilePixelSizeProperty, None)
    VisibleProperty = property(get_VisibleProperty, None)
class IMapTileSourceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2'
    _iid_ = Guid('{75cdd47e-669c-50fd-ad85-5ea5174cf59b}')
    @winrt_commethod(6)
    def get_AnimationStateProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_AutoPlayProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_FrameCountProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_FrameDurationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    AnimationStateProperty = property(get_AnimationStateProperty, None)
    AutoPlayProperty = property(get_AutoPlayProperty, None)
    FrameCountProperty = property(get_FrameCountProperty, None)
    FrameDurationProperty = property(get_FrameDurationProperty, None)
class IMapTileUriRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest'
    _iid_ = Guid('{17402335-3127-45b8-87a7-99f87d4e2745}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Uri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.UI.Xaml.Controls.Maps.MapTileUriRequestDeferral: ...
    Uri = property(get_Uri, put_Uri)
class IMapTileUriRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestDeferral'
    _iid_ = Guid('{c117ade0-bf3e-4c51-8faa-4b593cf68eb2}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IMapTileUriRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs'
    _iid_ = Guid('{d2147b43-1bbf-4b98-8dd3-b7834e407e0d}')
    @winrt_commethod(6)
    def get_X(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Y(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ZoomLevel(self) -> Int32: ...
    @winrt_commethod(9)
    def get_Request(self) -> Windows.UI.Xaml.Controls.Maps.MapTileUriRequest: ...
    X = property(get_X, None)
    Y = property(get_Y, None)
    ZoomLevel = property(get_ZoomLevel, None)
    Request = property(get_Request, None)
class IMapTileUriRequestedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs2'
    _iid_ = Guid('{2302185d-33b5-5a55-92f5-74a86a22efa6}')
    @winrt_commethod(6)
    def get_FrameIndex(self) -> Int32: ...
    FrameIndex = property(get_FrameIndex, None)
class IStreetsideExperience(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IStreetsideExperience'
    _iid_ = Guid('{a558aec9-e30c-46c8-8116-484691675558}')
    @winrt_commethod(6)
    def get_AddressTextVisible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AddressTextVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CursorVisible(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_CursorVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_OverviewMapVisible(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_OverviewMapVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_StreetLabelsVisible(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_StreetLabelsVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_ExitButtonVisible(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_ExitButtonVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_ZoomButtonsVisible(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_ZoomButtonsVisible(self, value: Boolean) -> Void: ...
    AddressTextVisible = property(get_AddressTextVisible, put_AddressTextVisible)
    CursorVisible = property(get_CursorVisible, put_CursorVisible)
    OverviewMapVisible = property(get_OverviewMapVisible, put_OverviewMapVisible)
    StreetLabelsVisible = property(get_StreetLabelsVisible, put_StreetLabelsVisible)
    ExitButtonVisible = property(get_ExitButtonVisible, put_ExitButtonVisible)
    ZoomButtonsVisible = property(get_ZoomButtonsVisible, put_ZoomButtonsVisible)
class IStreetsideExperienceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IStreetsideExperienceFactory'
    _iid_ = Guid('{7a5bcf3c-649e-4342-9995-68a6cf5961a7}')
    @winrt_commethod(6)
    def CreateInstanceWithPanorama(self, panorama: Windows.UI.Xaml.Controls.Maps.StreetsidePanorama) -> Windows.UI.Xaml.Controls.Maps.StreetsideExperience: ...
    @winrt_commethod(7)
    def CreateInstanceWithPanoramaHeadingPitchAndFieldOfView(self, panorama: Windows.UI.Xaml.Controls.Maps.StreetsidePanorama, headingInDegrees: Double, pitchInDegrees: Double, fieldOfViewInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.StreetsideExperience: ...
class IStreetsidePanorama(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IStreetsidePanorama'
    _iid_ = Guid('{6fe00fd8-ad60-4664-b539-b1069f16c5af}')
    @winrt_commethod(6)
    def get_Location(self) -> Windows.Devices.Geolocation.Geopoint: ...
    Location = property(get_Location, None)
class IStreetsidePanoramaStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.IStreetsidePanoramaStatics'
    _iid_ = Guid('{d3b47f69-54b3-4ec5-b2a0-4f8204576507}')
    @winrt_commethod(6)
    def FindNearbyWithLocationAsync(self, location: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Controls.Maps.StreetsidePanorama]: ...
    @winrt_commethod(7)
    def FindNearbyWithLocationAndRadiusAsync(self, location: Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Controls.Maps.StreetsidePanorama]: ...
class LocalMapTileDataSource(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapTileDataSource
    default_interface: Windows.UI.Xaml.Controls.Maps.ILocalMapTileDataSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource'
    @winrt_commethod(13)
    def get_UriFormatString(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_UriFormatString(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def add_UriRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.LocalMapTileDataSource, Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_UriRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    UriFormatString = property(get_UriFormatString, put_UriFormatString)
class MapActualCameraChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapActualCameraChangedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapActualCameraChangedEventArgs: ...
    @winrt_mixinmethod
    def get_Camera(self: Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_ChangeReason(self: Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangedEventArgs2) -> Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    Camera = property(get_Camera, None)
    ChangeReason = property(get_ChangeReason, None)
class MapActualCameraChangingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapActualCameraChangingEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapActualCameraChangingEventArgs: ...
    @winrt_mixinmethod
    def get_Camera(self: Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_ChangeReason(self: Windows.UI.Xaml.Controls.Maps.IMapActualCameraChangingEventArgs2) -> Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    Camera = property(get_Camera, None)
    ChangeReason = property(get_ChangeReason, None)
MapAnimationKind = Int32
MapAnimationKind_Default: MapAnimationKind = 0
MapAnimationKind_None: MapAnimationKind = 1
MapAnimationKind_Linear: MapAnimationKind = 2
MapAnimationKind_Bow: MapAnimationKind = 3
class MapBillboard(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapBillboard
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapBillboard'
    @winrt_factorymethod
    def CreateInstanceFromCamera(cls: Windows.UI.Xaml.Controls.Maps.IMapBillboardFactory, camera: Windows.UI.Xaml.Controls.Maps.MapCamera) -> Windows.UI.Xaml.Controls.Maps.MapBillboard: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Location(self: Windows.UI.Xaml.Controls.Maps.IMapBillboard, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_NormalizedAnchorPoint(self: Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_NormalizedAnchorPoint(self: Windows.UI.Xaml.Controls.Maps.IMapBillboard, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Image(self: Windows.UI.Xaml.Controls.Maps.IMapBillboard, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_CollisionBehaviorDesired(self: Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior: ...
    @winrt_mixinmethod
    def put_CollisionBehaviorDesired(self: Windows.UI.Xaml.Controls.Maps.IMapBillboard, value: Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior) -> Void: ...
    @winrt_mixinmethod
    def get_ReferenceCamera(self: Windows.UI.Xaml.Controls.Maps.IMapBillboard) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_classmethod
    def get_LocationProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapBillboardStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_NormalizedAnchorPointProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapBillboardStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CollisionBehaviorDesiredProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapBillboardStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Location = property(get_Location, put_Location)
    NormalizedAnchorPoint = property(get_NormalizedAnchorPoint, put_NormalizedAnchorPoint)
    Image = property(get_Image, put_Image)
    CollisionBehaviorDesired = property(get_CollisionBehaviorDesired, put_CollisionBehaviorDesired)
    ReferenceCamera = property(get_ReferenceCamera, None)
    LocationProperty = property(get_LocationProperty, None)
    NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
    CollisionBehaviorDesiredProperty = property(get_CollisionBehaviorDesiredProperty, None)
class MapCamera(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapCamera
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapCamera'
    @winrt_factorymethod
    def CreateInstanceWithLocation(cls: Windows.UI.Xaml.Controls.Maps.IMapCameraFactory, location: Windows.Devices.Geolocation.Geopoint) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_factorymethod
    def CreateInstanceWithLocationAndHeading(cls: Windows.UI.Xaml.Controls.Maps.IMapCameraFactory, location: Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_factorymethod
    def CreateInstanceWithLocationHeadingAndPitch(cls: Windows.UI.Xaml.Controls.Maps.IMapCameraFactory, location: Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_factorymethod
    def CreateInstanceWithLocationHeadingPitchRollAndFieldOfView(cls: Windows.UI.Xaml.Controls.Maps.IMapCameraFactory, location: Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double, rollInDegrees: Double, fieldOfViewInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapCamera) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Location(self: Windows.UI.Xaml.Controls.Maps.IMapCamera, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_Heading(self: Windows.UI.Xaml.Controls.Maps.IMapCamera) -> Double: ...
    @winrt_mixinmethod
    def put_Heading(self: Windows.UI.Xaml.Controls.Maps.IMapCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Pitch(self: Windows.UI.Xaml.Controls.Maps.IMapCamera) -> Double: ...
    @winrt_mixinmethod
    def put_Pitch(self: Windows.UI.Xaml.Controls.Maps.IMapCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Roll(self: Windows.UI.Xaml.Controls.Maps.IMapCamera) -> Double: ...
    @winrt_mixinmethod
    def put_Roll(self: Windows.UI.Xaml.Controls.Maps.IMapCamera, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FieldOfView(self: Windows.UI.Xaml.Controls.Maps.IMapCamera) -> Double: ...
    @winrt_mixinmethod
    def put_FieldOfView(self: Windows.UI.Xaml.Controls.Maps.IMapCamera, value: Double) -> Void: ...
    Location = property(get_Location, put_Location)
    Heading = property(get_Heading, put_Heading)
    Pitch = property(get_Pitch, put_Pitch)
    Roll = property(get_Roll, put_Roll)
    FieldOfView = property(get_FieldOfView, put_FieldOfView)
MapCameraChangeReason = Int32
MapCameraChangeReason_System: MapCameraChangeReason = 0
MapCameraChangeReason_UserInteraction: MapCameraChangeReason = 1
MapCameraChangeReason_Programmatic: MapCameraChangeReason = 2
MapColorScheme = Int32
MapColorScheme_Light: MapColorScheme = 0
MapColorScheme_Dark: MapColorScheme = 1
class MapContextRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapContextRequestedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapContextRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElements(self: Windows.UI.Xaml.Controls.Maps.IMapContextRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
class MapControl(ComPtr):
    extends: Windows.UI.Xaml.Controls.Control
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControl
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControl'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapControl: ...
    @winrt_mixinmethod
    def get_Center(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Center(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_mixinmethod
    def get_ColorScheme(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.UI.Xaml.Controls.Maps.MapColorScheme: ...
    @winrt_mixinmethod
    def put_ColorScheme(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Windows.UI.Xaml.Controls.Maps.MapColorScheme) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredPitch(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def put_DesiredPitch(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Heading(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def put_Heading(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LandmarksVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_LandmarksVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LoadingStatus(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.UI.Xaml.Controls.Maps.MapLoadingStatus: ...
    @winrt_mixinmethod
    def get_MapServiceToken(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_MapServiceToken(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_MaxZoomLevel(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def get_MinZoomLevel(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def get_PedestrianFeaturesVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_PedestrianFeaturesVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Pitch(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def get_Style(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.UI.Xaml.Controls.Maps.MapStyle: ...
    @winrt_mixinmethod
    def put_Style(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Windows.UI.Xaml.Controls.Maps.MapStyle) -> Void: ...
    @winrt_mixinmethod
    def get_TrafficFlowVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_TrafficFlowVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransformOrigin(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_TransformOrigin(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_WatermarkMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.UI.Xaml.Controls.Maps.MapWatermarkMode: ...
    @winrt_mixinmethod
    def put_WatermarkMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Windows.UI.Xaml.Controls.Maps.MapWatermarkMode) -> Void: ...
    @winrt_mixinmethod
    def get_ZoomLevel(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Double: ...
    @winrt_mixinmethod
    def put_ZoomLevel(self: Windows.UI.Xaml.Controls.Maps.IMapControl, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MapElements(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_mixinmethod
    def get_Routes(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapRouteView]: ...
    @winrt_mixinmethod
    def get_TileSources(self: Windows.UI.Xaml.Controls.Maps.IMapControl) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapTileSource]: ...
    @winrt_mixinmethod
    def add_CenterChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CenterChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HeadingChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HeadingChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LoadingStatusChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LoadingStatusChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapDoubleTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControl, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapDoubleTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapHolding(self: Windows.UI.Xaml.Controls.Maps.IMapControl, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapHolding(self: Windows.UI.Xaml.Controls.Maps.IMapControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControl, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapInputEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PitchChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PitchChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransformOriginChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransformOriginChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ZoomLevelChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ZoomLevelChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindMapElementsAtOffset(self: Windows.UI.Xaml.Controls.Maps.IMapControl, offset: Windows.Foundation.Point) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_mixinmethod
    def GetLocationFromOffset(self: Windows.UI.Xaml.Controls.Maps.IMapControl, offset: Windows.Foundation.Point, location: POINTER(Windows.Devices.Geolocation.Geopoint)) -> Void: ...
    @winrt_mixinmethod
    def GetOffsetFromLocation(self: Windows.UI.Xaml.Controls.Maps.IMapControl, location: Windows.Devices.Geolocation.Geopoint, offset: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_mixinmethod
    def IsLocationInView(self: Windows.UI.Xaml.Controls.Maps.IMapControl, location: Windows.Devices.Geolocation.Geopoint, isInView: POINTER(Boolean)) -> Void: ...
    @winrt_mixinmethod
    def TrySetViewBoundsAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl, bounds: Windows.Devices.Geolocation.GeoboundingBox, margin: Windows.Foundation.IReference[Windows.UI.Xaml.Thickness], animation: Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetViewWithCenterAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl, center: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetViewWithCenterAndZoomAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl, center: Windows.Devices.Geolocation.Geopoint, zoomLevel: Windows.Foundation.IReference[Double]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetViewWithCenterZoomHeadingAndPitchAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl, center: Windows.Devices.Geolocation.Geopoint, zoomLevel: Windows.Foundation.IReference[Double], heading: Windows.Foundation.IReference[Double], desiredPitch: Windows.Foundation.IReference[Double]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetViewWithCenterZoomHeadingPitchAndAnimationAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl, center: Windows.Devices.Geolocation.Geopoint, zoomLevel: Windows.Foundation.IReference[Double], heading: Windows.Foundation.IReference[Double], desiredPitch: Windows.Foundation.IReference[Double], animation: Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_BusinessLandmarksVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_BusinessLandmarksVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransitFeaturesVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Boolean: ...
    @winrt_mixinmethod
    def put_TransitFeaturesVisible(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PanInteractionMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode: ...
    @winrt_mixinmethod
    def put_PanInteractionMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode) -> Void: ...
    @winrt_mixinmethod
    def get_RotateInteractionMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_mixinmethod
    def put_RotateInteractionMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_mixinmethod
    def get_TiltInteractionMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_mixinmethod
    def put_TiltInteractionMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_mixinmethod
    def get_ZoomInteractionMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.UI.Xaml.Controls.Maps.MapInteractionMode: ...
    @winrt_mixinmethod
    def put_ZoomInteractionMode(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Windows.UI.Xaml.Controls.Maps.MapInteractionMode) -> Void: ...
    @winrt_mixinmethod
    def get_Is3DSupported(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStreetsideSupported(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Scene(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_mixinmethod
    def put_Scene(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Windows.UI.Xaml.Controls.Maps.MapScene) -> Void: ...
    @winrt_mixinmethod
    def get_ActualCamera(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_TargetCamera(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_CustomExperience(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.UI.Xaml.Controls.Maps.MapCustomExperience: ...
    @winrt_mixinmethod
    def put_CustomExperience(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, value: Windows.UI.Xaml.Controls.Maps.MapCustomExperience) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementClick(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapElementClickEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementClick(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementPointerEntered(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapElementPointerEnteredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementPointerEntered(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementPointerExited(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapElementPointerExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementPointerExited(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActualCameraChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapActualCameraChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActualCameraChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ActualCameraChanging(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapActualCameraChangingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ActualCameraChanging(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TargetCameraChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetCameraChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CustomExperienceChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapCustomExperienceChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CustomExperienceChanged(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartContinuousRotate(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, rateInDegreesPerSecond: Double) -> Void: ...
    @winrt_mixinmethod
    def StopContinuousRotate(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Void: ...
    @winrt_mixinmethod
    def StartContinuousTilt(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, rateInDegreesPerSecond: Double) -> Void: ...
    @winrt_mixinmethod
    def StopContinuousTilt(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Void: ...
    @winrt_mixinmethod
    def StartContinuousZoom(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, rateOfChangePerSecond: Double) -> Void: ...
    @winrt_mixinmethod
    def StopContinuousZoom(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Void: ...
    @winrt_mixinmethod
    def TryRotateAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, degrees: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryRotateToAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, angleInDegrees: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryTiltAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, degrees: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryTiltToAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, angleInDegrees: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryZoomInAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryZoomOutAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl2) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryZoomToAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, zoomLevel: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetSceneAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, scene: Windows.UI.Xaml.Controls.Maps.MapScene) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetSceneWithAnimationAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl2, scene: Windows.UI.Xaml.Controls.Maps.MapScene, animationKind: Windows.UI.Xaml.Controls.Maps.MapAnimationKind) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_MapRightTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControl3, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapRightTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapRightTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControl3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_BusinessLandmarksEnabled(self: Windows.UI.Xaml.Controls.Maps.IMapControl4) -> Boolean: ...
    @winrt_mixinmethod
    def put_BusinessLandmarksEnabled(self: Windows.UI.Xaml.Controls.Maps.IMapControl4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransitFeaturesEnabled(self: Windows.UI.Xaml.Controls.Maps.IMapControl4) -> Boolean: ...
    @winrt_mixinmethod
    def put_TransitFeaturesEnabled(self: Windows.UI.Xaml.Controls.Maps.IMapControl4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetVisibleRegion(self: Windows.UI.Xaml.Controls.Maps.IMapControl4, region: Windows.UI.Xaml.Controls.Maps.MapVisibleRegionKind) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_MapProjection(self: Windows.UI.Xaml.Controls.Maps.IMapControl5) -> Windows.UI.Xaml.Controls.Maps.MapProjection: ...
    @winrt_mixinmethod
    def put_MapProjection(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, value: Windows.UI.Xaml.Controls.Maps.MapProjection) -> Void: ...
    @winrt_mixinmethod
    def get_StyleSheet(self: Windows.UI.Xaml.Controls.Maps.IMapControl5) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_mixinmethod
    def put_StyleSheet(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, value: Windows.UI.Xaml.Controls.Maps.MapStyleSheet) -> Void: ...
    @winrt_mixinmethod
    def get_ViewPadding(self: Windows.UI.Xaml.Controls.Maps.IMapControl5) -> Windows.UI.Xaml.Thickness: ...
    @winrt_mixinmethod
    def put_ViewPadding(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, value: Windows.UI.Xaml.Thickness) -> Void: ...
    @winrt_mixinmethod
    def add_MapContextRequested(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapContextRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapContextRequested(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def FindMapElementsAtOffsetWithRadius(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, offset: Windows.Foundation.Point, radius: Double) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_mixinmethod
    def GetLocationFromOffsetWithReferenceSystem(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, offset: Windows.Foundation.Point, desiredReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, location: POINTER(Windows.Devices.Geolocation.Geopoint)) -> Void: ...
    @winrt_mixinmethod
    def StartContinuousPan(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, horizontalPixelsPerSecond: Double, verticalPixelsPerSecond: Double) -> Void: ...
    @winrt_mixinmethod
    def StopContinuousPan(self: Windows.UI.Xaml.Controls.Maps.IMapControl5) -> Void: ...
    @winrt_mixinmethod
    def TryPanAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, horizontalPixels: Double, verticalPixels: Double) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryPanToAsync(self: Windows.UI.Xaml.Controls.Maps.IMapControl5, location: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Layers(self: Windows.UI.Xaml.Controls.Maps.IMapControl6) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapLayer]: ...
    @winrt_mixinmethod
    def put_Layers(self: Windows.UI.Xaml.Controls.Maps.IMapControl6, value: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapLayer]) -> Void: ...
    @winrt_mixinmethod
    def TryGetLocationFromOffset(self: Windows.UI.Xaml.Controls.Maps.IMapControl6, offset: Windows.Foundation.Point, location: POINTER(Windows.Devices.Geolocation.Geopoint)) -> Boolean: ...
    @winrt_mixinmethod
    def TryGetLocationFromOffsetWithReferenceSystem(self: Windows.UI.Xaml.Controls.Maps.IMapControl6, offset: Windows.Foundation.Point, desiredReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, location: POINTER(Windows.Devices.Geolocation.Geopoint)) -> Boolean: ...
    @winrt_mixinmethod
    def get_Region(self: Windows.UI.Xaml.Controls.Maps.IMapControl7) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Region(self: Windows.UI.Xaml.Controls.Maps.IMapControl7, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CanTiltDown(self: Windows.UI.Xaml.Controls.Maps.IMapControl8) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanTiltUp(self: Windows.UI.Xaml.Controls.Maps.IMapControl8) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanZoomIn(self: Windows.UI.Xaml.Controls.Maps.IMapControl8) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanZoomOut(self: Windows.UI.Xaml.Controls.Maps.IMapControl8) -> Boolean: ...
    @winrt_classmethod
    def get_CanTiltDownProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics8) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanTiltUpProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics8) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanZoomInProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics8) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CanZoomOutProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics8) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RegionProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics7) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LayersProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics6) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapProjectionProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StyleSheetProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ViewPaddingProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics5) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BusinessLandmarksEnabledProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransitFeaturesEnabledProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BusinessLandmarksVisibleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransitFeaturesVisibleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PanInteractionModeProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotateInteractionModeProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TiltInteractionModeProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZoomInteractionModeProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Is3DSupportedProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsStreetsideSupportedProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SceneProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ChildrenProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ColorSchemeProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DesiredPitchProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HeadingProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LandmarksVisibleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LoadingStatusProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapServiceTokenProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PedestrianFeaturesVisibleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PitchProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StyleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TrafficFlowVisibleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransformOriginProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_WatermarkModeProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZoomLevelProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapElementsProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RoutesProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TileSourcesProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocationProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetLocation(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics, element: Windows.UI.Xaml.DependencyObject) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_classmethod
    def SetLocation(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics, element: Windows.UI.Xaml.DependencyObject, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_classmethod
    def get_NormalizedAnchorPointProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def GetNormalizedAnchorPoint(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics, element: Windows.UI.Xaml.DependencyObject) -> Windows.Foundation.Point: ...
    @winrt_classmethod
    def SetNormalizedAnchorPoint(cls: Windows.UI.Xaml.Controls.Maps.IMapControlStatics, element: Windows.UI.Xaml.DependencyObject, value: Windows.Foundation.Point) -> Void: ...
    Center = property(get_Center, put_Center)
    Children = property(get_Children, None)
    ColorScheme = property(get_ColorScheme, put_ColorScheme)
    DesiredPitch = property(get_DesiredPitch, put_DesiredPitch)
    Heading = property(get_Heading, put_Heading)
    LandmarksVisible = property(get_LandmarksVisible, put_LandmarksVisible)
    LoadingStatus = property(get_LoadingStatus, None)
    MapServiceToken = property(get_MapServiceToken, put_MapServiceToken)
    MaxZoomLevel = property(get_MaxZoomLevel, None)
    MinZoomLevel = property(get_MinZoomLevel, None)
    PedestrianFeaturesVisible = property(get_PedestrianFeaturesVisible, put_PedestrianFeaturesVisible)
    Pitch = property(get_Pitch, None)
    Style = property(get_Style, put_Style)
    TrafficFlowVisible = property(get_TrafficFlowVisible, put_TrafficFlowVisible)
    TransformOrigin = property(get_TransformOrigin, put_TransformOrigin)
    WatermarkMode = property(get_WatermarkMode, put_WatermarkMode)
    ZoomLevel = property(get_ZoomLevel, put_ZoomLevel)
    MapElements = property(get_MapElements, None)
    Routes = property(get_Routes, None)
    TileSources = property(get_TileSources, None)
    BusinessLandmarksVisible = property(get_BusinessLandmarksVisible, put_BusinessLandmarksVisible)
    TransitFeaturesVisible = property(get_TransitFeaturesVisible, put_TransitFeaturesVisible)
    PanInteractionMode = property(get_PanInteractionMode, put_PanInteractionMode)
    RotateInteractionMode = property(get_RotateInteractionMode, put_RotateInteractionMode)
    TiltInteractionMode = property(get_TiltInteractionMode, put_TiltInteractionMode)
    ZoomInteractionMode = property(get_ZoomInteractionMode, put_ZoomInteractionMode)
    Is3DSupported = property(get_Is3DSupported, None)
    IsStreetsideSupported = property(get_IsStreetsideSupported, None)
    Scene = property(get_Scene, put_Scene)
    ActualCamera = property(get_ActualCamera, None)
    TargetCamera = property(get_TargetCamera, None)
    CustomExperience = property(get_CustomExperience, put_CustomExperience)
    BusinessLandmarksEnabled = property(get_BusinessLandmarksEnabled, put_BusinessLandmarksEnabled)
    TransitFeaturesEnabled = property(get_TransitFeaturesEnabled, put_TransitFeaturesEnabled)
    MapProjection = property(get_MapProjection, put_MapProjection)
    StyleSheet = property(get_StyleSheet, put_StyleSheet)
    ViewPadding = property(get_ViewPadding, put_ViewPadding)
    Layers = property(get_Layers, put_Layers)
    Region = property(get_Region, put_Region)
    CanTiltDown = property(get_CanTiltDown, None)
    CanTiltUp = property(get_CanTiltUp, None)
    CanZoomIn = property(get_CanZoomIn, None)
    CanZoomOut = property(get_CanZoomOut, None)
    CanTiltDownProperty = property(get_CanTiltDownProperty, None)
    CanTiltUpProperty = property(get_CanTiltUpProperty, None)
    CanZoomInProperty = property(get_CanZoomInProperty, None)
    CanZoomOutProperty = property(get_CanZoomOutProperty, None)
    RegionProperty = property(get_RegionProperty, None)
    LayersProperty = property(get_LayersProperty, None)
    MapProjectionProperty = property(get_MapProjectionProperty, None)
    StyleSheetProperty = property(get_StyleSheetProperty, None)
    ViewPaddingProperty = property(get_ViewPaddingProperty, None)
    BusinessLandmarksEnabledProperty = property(get_BusinessLandmarksEnabledProperty, None)
    TransitFeaturesEnabledProperty = property(get_TransitFeaturesEnabledProperty, None)
    BusinessLandmarksVisibleProperty = property(get_BusinessLandmarksVisibleProperty, None)
    TransitFeaturesVisibleProperty = property(get_TransitFeaturesVisibleProperty, None)
    PanInteractionModeProperty = property(get_PanInteractionModeProperty, None)
    RotateInteractionModeProperty = property(get_RotateInteractionModeProperty, None)
    TiltInteractionModeProperty = property(get_TiltInteractionModeProperty, None)
    ZoomInteractionModeProperty = property(get_ZoomInteractionModeProperty, None)
    Is3DSupportedProperty = property(get_Is3DSupportedProperty, None)
    IsStreetsideSupportedProperty = property(get_IsStreetsideSupportedProperty, None)
    SceneProperty = property(get_SceneProperty, None)
    CenterProperty = property(get_CenterProperty, None)
    ChildrenProperty = property(get_ChildrenProperty, None)
    ColorSchemeProperty = property(get_ColorSchemeProperty, None)
    DesiredPitchProperty = property(get_DesiredPitchProperty, None)
    HeadingProperty = property(get_HeadingProperty, None)
    LandmarksVisibleProperty = property(get_LandmarksVisibleProperty, None)
    LoadingStatusProperty = property(get_LoadingStatusProperty, None)
    MapServiceTokenProperty = property(get_MapServiceTokenProperty, None)
    PedestrianFeaturesVisibleProperty = property(get_PedestrianFeaturesVisibleProperty, None)
    PitchProperty = property(get_PitchProperty, None)
    StyleProperty = property(get_StyleProperty, None)
    TrafficFlowVisibleProperty = property(get_TrafficFlowVisibleProperty, None)
    TransformOriginProperty = property(get_TransformOriginProperty, None)
    WatermarkModeProperty = property(get_WatermarkModeProperty, None)
    ZoomLevelProperty = property(get_ZoomLevelProperty, None)
    MapElementsProperty = property(get_MapElementsProperty, None)
    RoutesProperty = property(get_RoutesProperty, None)
    TileSourcesProperty = property(get_TileSourcesProperty, None)
    LocationProperty = property(get_LocationProperty, None)
    NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
class MapControlBusinessLandmarkClickEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkClickEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkClickEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkClickEventArgs: ...
    @winrt_mixinmethod
    def get_LocalLocations(self: Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkClickEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class MapControlBusinessLandmarkPointerEnteredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerEnteredEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerEnteredEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerEnteredEventArgs: ...
    @winrt_mixinmethod
    def get_LocalLocations(self: Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerEnteredEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class MapControlBusinessLandmarkPointerExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerExitedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerExitedEventArgs: ...
    @winrt_mixinmethod
    def get_LocalLocations(self: Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkPointerExitedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class MapControlBusinessLandmarkRightTappedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkRightTappedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkRightTappedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkRightTappedEventArgs: ...
    @winrt_mixinmethod
    def get_LocalLocations(self: Windows.UI.Xaml.Controls.Maps.IMapControlBusinessLandmarkRightTappedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.LocalSearch.LocalLocation]: ...
    LocalLocations = property(get_LocalLocations, None)
class MapControlDataHelper(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlDataHelper'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelperFactory, map: Windows.UI.Xaml.Controls.Maps.MapControl) -> Windows.UI.Xaml.Controls.Maps.MapControlDataHelper: ...
    @winrt_mixinmethod
    def add_BusinessLandmarkClick(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkClickEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BusinessLandmarkClick(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransitFeatureClick(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureClickEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransitFeatureClick(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BusinessLandmarkRightTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkRightTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BusinessLandmarkRightTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransitFeatureRightTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureRightTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransitFeatureRightTapped(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BusinessLandmarkPointerEntered(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerEnteredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BusinessLandmarkPointerEntered(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransitFeaturePointerEntered(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerEnteredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransitFeaturePointerEntered(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BusinessLandmarkPointerExited(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlBusinessLandmarkPointerExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BusinessLandmarkPointerExited(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TransitFeaturePointerExited(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, value: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapControl, Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TransitFeaturePointerExited(self: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelper2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateMapControl(cls: Windows.UI.Xaml.Controls.Maps.IMapControlDataHelperStatics, rasterRenderMode: Boolean) -> Windows.UI.Xaml.Controls.Maps.MapControl: ...
class MapControlTransitFeatureClickEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureClickEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureClickEventArgs: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_TransitProperties(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureClickEventArgs) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class MapControlTransitFeaturePointerEnteredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerEnteredEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerEnteredEventArgs: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_TransitProperties(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerEnteredEventArgs) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class MapControlTransitFeaturePointerExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerExitedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapControlTransitFeaturePointerExitedEventArgs: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_TransitProperties(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeaturePointerExitedEventArgs) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class MapControlTransitFeatureRightTappedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureRightTappedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapControlTransitFeatureRightTappedEventArgs: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_TransitProperties(self: Windows.UI.Xaml.Controls.Maps.IMapControlTransitFeatureRightTappedEventArgs) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    DisplayName = property(get_DisplayName, None)
    Location = property(get_Location, None)
    TransitProperties = property(get_TransitProperties, None)
class MapCustomExperience(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapCustomExperience
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapCustomExperience'
class MapCustomExperienceChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapCustomExperienceChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapCustomExperienceChangedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapCustomExperienceChangedEventArgs: ...
class MapElement(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElement
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElement'
    @winrt_commethod(28)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(29)
    def put_ZIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(30)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(31)
    def put_Visible(self, value: Boolean) -> Void: ...
    @winrt_commethod(32)
    def get_MapTabIndex(self) -> Int32: ...
    @winrt_commethod(33)
    def put_MapTabIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(34)
    def get_MapStyleSheetEntry(self) -> WinRT_String: ...
    @winrt_commethod(35)
    def put_MapStyleSheetEntry(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(36)
    def get_MapStyleSheetEntryState(self) -> WinRT_String: ...
    @winrt_commethod(37)
    def put_MapStyleSheetEntryState(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(38)
    def get_Tag(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(39)
    def put_Tag(self, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(40)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(41)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_IsEnabledProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElementStatics4) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapStyleSheetEntryProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElementStatics3) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapStyleSheetEntryStateProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElementStatics3) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TagProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElementStatics3) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MapTabIndexProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElementStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZIndexProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VisibleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElementStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    ZIndex = property(get_ZIndex, put_ZIndex)
    Visible = property(get_Visible, put_Visible)
    MapTabIndex = property(get_MapTabIndex, put_MapTabIndex)
    MapStyleSheetEntry = property(get_MapStyleSheetEntry, put_MapStyleSheetEntry)
    MapStyleSheetEntryState = property(get_MapStyleSheetEntryState, put_MapStyleSheetEntryState)
    Tag = property(get_Tag, put_Tag)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    IsEnabledProperty = property(get_IsEnabledProperty, None)
    MapStyleSheetEntryProperty = property(get_MapStyleSheetEntryProperty, None)
    MapStyleSheetEntryStateProperty = property(get_MapStyleSheetEntryStateProperty, None)
    TagProperty = property(get_TagProperty, None)
    MapTabIndexProperty = property(get_MapTabIndexProperty, None)
    ZIndexProperty = property(get_ZIndexProperty, None)
    VisibleProperty = property(get_VisibleProperty, None)
class MapElement3D(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElement3D
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElement3D'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapElement3D: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Location(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_Model(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> Windows.UI.Xaml.Controls.Maps.MapModel3D: ...
    @winrt_mixinmethod
    def put_Model(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: Windows.UI.Xaml.Controls.Maps.MapModel3D) -> Void: ...
    @winrt_mixinmethod
    def get_Heading(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> Double: ...
    @winrt_mixinmethod
    def put_Heading(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Pitch(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> Double: ...
    @winrt_mixinmethod
    def put_Pitch(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Roll(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> Double: ...
    @winrt_mixinmethod
    def put_Roll(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.UI.Xaml.Controls.Maps.IMapElement3D, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_classmethod
    def get_LocationProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_HeadingProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PitchProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RollProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElement3DStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Location = property(get_Location, put_Location)
    Model = property(get_Model, put_Model)
    Heading = property(get_Heading, put_Heading)
    Pitch = property(get_Pitch, put_Pitch)
    Roll = property(get_Roll, put_Roll)
    Scale = property(get_Scale, put_Scale)
    LocationProperty = property(get_LocationProperty, None)
    HeadingProperty = property(get_HeadingProperty, None)
    PitchProperty = property(get_PitchProperty, None)
    RollProperty = property(get_RollProperty, None)
    ScaleProperty = property(get_ScaleProperty, None)
class MapElementClickEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementClickEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapElementClickEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElements(self: Windows.UI.Xaml.Controls.Maps.IMapElementClickEventArgs) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
MapElementCollisionBehavior = Int32
MapElementCollisionBehavior_Hide: MapElementCollisionBehavior = 0
MapElementCollisionBehavior_RemainVisible: MapElementCollisionBehavior = 1
class MapElementPointerEnteredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementPointerEnteredEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapElementPointerEnteredEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElement(self: Windows.UI.Xaml.Controls.Maps.IMapElementPointerEnteredEventArgs) -> Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
class MapElementPointerExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementPointerExitedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapElementPointerExitedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElement(self: Windows.UI.Xaml.Controls.Maps.IMapElementPointerExitedEventArgs) -> Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
class MapElementsLayer(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapLayer
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayer'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapElementsLayer: ...
    @winrt_mixinmethod
    def get_MapElements(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    @winrt_mixinmethod
    def put_MapElements(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, value: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementClick(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapElementsLayer, Windows.UI.Xaml.Controls.Maps.MapElementsLayerClickEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementClick(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementPointerEntered(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapElementsLayer, Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerEnteredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementPointerEntered(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapElementPointerExited(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapElementsLayer, Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerExitedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapElementPointerExited(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MapContextRequested(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapElementsLayer, Windows.UI.Xaml.Controls.Maps.MapElementsLayerContextRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MapContextRequested(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_MapElementsProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    MapElements = property(get_MapElements, put_MapElements)
    MapElementsProperty = property(get_MapElementsProperty, None)
class MapElementsLayerClickEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayerClickEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapElementsLayerClickEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElements(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerClickEventArgs) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
class MapElementsLayerContextRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayerContextRequestedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapElementsLayerContextRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElements(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerContextRequestedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Maps.MapElement]: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElements = property(get_MapElements, None)
class MapElementsLayerPointerEnteredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerEnteredEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerEnteredEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElement(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerEnteredEventArgs) -> Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
class MapElementsLayerPointerExitedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerExitedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapElementsLayerPointerExitedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_MapElement(self: Windows.UI.Xaml.Controls.Maps.IMapElementsLayerPointerExitedEventArgs) -> Windows.UI.Xaml.Controls.Maps.MapElement: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
    MapElement = property(get_MapElement, None)
class MapIcon(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapIcon
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapIcon'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapIcon: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapIcon) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def put_Location(self: Windows.UI.Xaml.Controls.Maps.IMapIcon, value: Windows.Devices.Geolocation.Geopoint) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.UI.Xaml.Controls.Maps.IMapIcon) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: Windows.UI.Xaml.Controls.Maps.IMapIcon, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NormalizedAnchorPoint(self: Windows.UI.Xaml.Controls.Maps.IMapIcon) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_NormalizedAnchorPoint(self: Windows.UI.Xaml.Controls.Maps.IMapIcon, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Image(self: Windows.UI.Xaml.Controls.Maps.IMapIcon) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Image(self: Windows.UI.Xaml.Controls.Maps.IMapIcon, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_CollisionBehaviorDesired(self: Windows.UI.Xaml.Controls.Maps.IMapIcon2) -> Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior: ...
    @winrt_mixinmethod
    def put_CollisionBehaviorDesired(self: Windows.UI.Xaml.Controls.Maps.IMapIcon2, value: Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior) -> Void: ...
    @winrt_classmethod
    def get_CollisionBehaviorDesiredProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapIconStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocationProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapIconStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TitleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapIconStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_NormalizedAnchorPointProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapIconStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Location = property(get_Location, put_Location)
    Title = property(get_Title, put_Title)
    NormalizedAnchorPoint = property(get_NormalizedAnchorPoint, put_NormalizedAnchorPoint)
    Image = property(get_Image, put_Image)
    CollisionBehaviorDesired = property(get_CollisionBehaviorDesired, put_CollisionBehaviorDesired)
    CollisionBehaviorDesiredProperty = property(get_CollisionBehaviorDesiredProperty, None)
    LocationProperty = property(get_LocationProperty, None)
    TitleProperty = property(get_TitleProperty, None)
    NormalizedAnchorPointProperty = property(get_NormalizedAnchorPointProperty, None)
class MapInputEventArgs(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapInputEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapInputEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapInputEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapInputEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapInputEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
MapInteractionMode = Int32
MapInteractionMode_Auto: MapInteractionMode = 0
MapInteractionMode_Disabled: MapInteractionMode = 1
MapInteractionMode_GestureOnly: MapInteractionMode = 2
MapInteractionMode_PointerAndKeyboard: MapInteractionMode = 2
MapInteractionMode_ControlOnly: MapInteractionMode = 3
MapInteractionMode_GestureAndControl: MapInteractionMode = 4
MapInteractionMode_PointerKeyboardAndControl: MapInteractionMode = 4
MapInteractionMode_PointerOnly: MapInteractionMode = 5
class MapItemsControl(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapItemsControl
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapItemsControl'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapItemsControl: ...
    @winrt_mixinmethod
    def get_ItemsSource(self: Windows.UI.Xaml.Controls.Maps.IMapItemsControl) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_ItemsSource(self: Windows.UI.Xaml.Controls.Maps.IMapItemsControl, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def get_Items(self: Windows.UI.Xaml.Controls.Maps.IMapItemsControl) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.DependencyObject]: ...
    @winrt_mixinmethod
    def get_ItemTemplate(self: Windows.UI.Xaml.Controls.Maps.IMapItemsControl) -> Windows.UI.Xaml.DataTemplate: ...
    @winrt_mixinmethod
    def put_ItemTemplate(self: Windows.UI.Xaml.Controls.Maps.IMapItemsControl, value: Windows.UI.Xaml.DataTemplate) -> Void: ...
    @winrt_classmethod
    def get_ItemsSourceProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapItemsControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemsProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapItemsControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ItemTemplateProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapItemsControlStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    ItemsSource = property(get_ItemsSource, put_ItemsSource)
    Items = property(get_Items, None)
    ItemTemplate = property(get_ItemTemplate, put_ItemTemplate)
    ItemsSourceProperty = property(get_ItemsSourceProperty, None)
    ItemsProperty = property(get_ItemsProperty, None)
    ItemTemplateProperty = property(get_ItemTemplateProperty, None)
class MapLayer(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapLayer
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapLayer'
    @winrt_commethod(16)
    def get_MapTabIndex(self) -> Int32: ...
    @winrt_commethod(17)
    def put_MapTabIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_Visible(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(21)
    def put_ZIndex(self, value: Int32) -> Void: ...
    @winrt_classmethod
    def get_MapTabIndexProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapLayerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VisibleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapLayerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZIndexProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapLayerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    MapTabIndex = property(get_MapTabIndex, put_MapTabIndex)
    Visible = property(get_Visible, put_Visible)
    ZIndex = property(get_ZIndex, put_ZIndex)
    MapTabIndexProperty = property(get_MapTabIndexProperty, None)
    VisibleProperty = property(get_VisibleProperty, None)
    ZIndexProperty = property(get_ZIndexProperty, None)
MapLoadingStatus = Int32
MapLoadingStatus_Loading: MapLoadingStatus = 0
MapLoadingStatus_Loaded: MapLoadingStatus = 1
MapLoadingStatus_DataUnavailable: MapLoadingStatus = 2
MapLoadingStatus_DownloadedMapsManagerUnavailable: MapLoadingStatus = 3
class MapModel3D(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapModel3D
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapModel3D'
    @winrt_classmethod
    def CreateFrom3MFAsync(cls: Windows.UI.Xaml.Controls.Maps.IMapModel3DStatics, source: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Controls.Maps.MapModel3D]: ...
    @winrt_classmethod
    def CreateFrom3MFWithShadingOptionAsync(cls: Windows.UI.Xaml.Controls.Maps.IMapModel3DStatics, source: Windows.Storage.Streams.IRandomAccessStreamReference, shadingOption: Windows.UI.Xaml.Controls.Maps.MapModel3DShadingOption) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Controls.Maps.MapModel3D]: ...
MapModel3DShadingOption = Int32
MapModel3DShadingOption_Default: MapModel3DShadingOption = 0
MapModel3DShadingOption_Flat: MapModel3DShadingOption = 1
MapModel3DShadingOption_Smooth: MapModel3DShadingOption = 2
MapPanInteractionMode = Int32
MapPanInteractionMode_Auto: MapPanInteractionMode = 0
MapPanInteractionMode_Disabled: MapPanInteractionMode = 1
class MapPolygon(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapPolygon
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapPolygon'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapPolygon: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def put_Path(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: Windows.Devices.Geolocation.Geopath) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeColor(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_StrokeColor(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeThickness(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeThickness(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashed(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> Boolean: ...
    @winrt_mixinmethod
    def put_StrokeDashed(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FillColor(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_FillColor(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Paths(self: Windows.UI.Xaml.Controls.Maps.IMapPolygon2) -> Windows.Foundation.Collections.IVector[Windows.Devices.Geolocation.Geopath]: ...
    @winrt_classmethod
    def get_PathProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapPolygonStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeThicknessProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapPolygonStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashedProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapPolygonStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Path = property(get_Path, put_Path)
    StrokeColor = property(get_StrokeColor, put_StrokeColor)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
    StrokeDashed = property(get_StrokeDashed, put_StrokeDashed)
    FillColor = property(get_FillColor, put_FillColor)
    Paths = property(get_Paths, None)
    PathProperty = property(get_PathProperty, None)
    StrokeThicknessProperty = property(get_StrokeThicknessProperty, None)
    StrokeDashedProperty = property(get_StrokeDashedProperty, None)
class MapPolyline(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapElement
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapPolyline
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapPolyline'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapPolyline: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.UI.Xaml.Controls.Maps.IMapPolyline) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def put_Path(self: Windows.UI.Xaml.Controls.Maps.IMapPolyline, value: Windows.Devices.Geolocation.Geopath) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeColor(self: Windows.UI.Xaml.Controls.Maps.IMapPolyline) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_StrokeColor(self: Windows.UI.Xaml.Controls.Maps.IMapPolyline, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeThickness(self: Windows.UI.Xaml.Controls.Maps.IMapPolyline) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeThickness(self: Windows.UI.Xaml.Controls.Maps.IMapPolyline, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashed(self: Windows.UI.Xaml.Controls.Maps.IMapPolyline) -> Boolean: ...
    @winrt_mixinmethod
    def put_StrokeDashed(self: Windows.UI.Xaml.Controls.Maps.IMapPolyline, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_PathProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapPolylineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashedProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapPolylineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Path = property(get_Path, put_Path)
    StrokeColor = property(get_StrokeColor, put_StrokeColor)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
    StrokeDashed = property(get_StrokeDashed, put_StrokeDashed)
    PathProperty = property(get_PathProperty, None)
    StrokeDashedProperty = property(get_StrokeDashedProperty, None)
MapProjection = Int32
MapProjection_WebMercator: MapProjection = 0
MapProjection_Globe: MapProjection = 1
class MapRightTappedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapRightTappedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapRightTappedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapRightTappedEventArgs: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Xaml.Controls.Maps.IMapRightTappedEventArgs) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IMapRightTappedEventArgs) -> Windows.Devices.Geolocation.Geopoint: ...
    Position = property(get_Position, None)
    Location = property(get_Location, None)
class MapRouteView(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapRouteView
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapRouteView'
    @winrt_commethod(12)
    def get_RouteColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(13)
    def put_RouteColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(14)
    def get_OutlineColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(15)
    def put_OutlineColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(16)
    def get_Route(self) -> Windows.Services.Maps.MapRoute: ...
    RouteColor = property(get_RouteColor, put_RouteColor)
    OutlineColor = property(get_OutlineColor, put_OutlineColor)
    Route = property(get_Route, None)
class MapScene(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapScene
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapScene'
    @winrt_mixinmethod
    def get_TargetCamera(self: Windows.UI.Xaml.Controls.Maps.IMapScene) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def add_TargetCameraChanged(self: Windows.UI.Xaml.Controls.Maps.IMapScene, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Controls.Maps.MapScene, Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TargetCameraChanged(self: Windows.UI.Xaml.Controls.Maps.IMapScene, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def CreateFromBoundingBox(cls: Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, bounds: Windows.Devices.Geolocation.GeoboundingBox) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromBoundingBoxWithHeadingAndPitch(cls: Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, bounds: Windows.Devices.Geolocation.GeoboundingBox, headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromCamera(cls: Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, camera: Windows.UI.Xaml.Controls.Maps.MapCamera) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocation(cls: Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, location: Windows.Devices.Geolocation.Geopoint) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocationWithHeadingAndPitch(cls: Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, location: Windows.Devices.Geolocation.Geopoint, headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocationAndRadius(cls: Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, location: Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocationAndRadiusWithHeadingAndPitch(cls: Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, location: Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double, headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocations(cls: Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, locations: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint]) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    @winrt_classmethod
    def CreateFromLocationsWithHeadingAndPitch(cls: Windows.UI.Xaml.Controls.Maps.IMapSceneStatics, locations: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint], headingInDegrees: Double, pitchInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.MapScene: ...
    TargetCamera = property(get_TargetCamera, None)
MapStyle = Int32
MapStyle_None: MapStyle = 0
MapStyle_Road: MapStyle = 1
MapStyle_Aerial: MapStyle = 2
MapStyle_AerialWithRoads: MapStyle = 3
MapStyle_Terrain: MapStyle = 4
MapStyle_Aerial3D: MapStyle = 5
MapStyle_Aerial3DWithRoads: MapStyle = 6
MapStyle_Custom: MapStyle = 7
class MapStyleSheet(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapStyleSheet
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapStyleSheet'
    @winrt_classmethod
    def Aerial(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def AerialWithOverlay(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def RoadLight(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def RoadDark(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def RoadHighContrastLight(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def RoadHighContrastDark(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def Combine(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics, styleSheets: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Controls.Maps.MapStyleSheet]) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def ParseFromJson(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics, styleAsJson: WinRT_String) -> Windows.UI.Xaml.Controls.Maps.MapStyleSheet: ...
    @winrt_classmethod
    def TryParseFromJson(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetStatics, styleAsJson: WinRT_String, styleSheet: POINTER(Windows.UI.Xaml.Controls.Maps.MapStyleSheet)) -> Boolean: ...
class MapStyleSheetEntries(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapStyleSheetEntries'
    @winrt_classmethod
    def get_Area(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Airport(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Cemetery(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Continent(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Education(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_IndigenousPeoplesReserve(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Island(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Medical(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Military(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Nautical(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Neighborhood(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Runway(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Sand(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ShoppingCenter(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Stadium(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Vegetation(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Forest(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_GolfCourse(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Park(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PlayingField(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Reserve(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Point(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_NaturalPoint(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Peak(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_VolcanicPeak(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WaterPoint(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PointOfInterest(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Business(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_FoodPoint(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_PopulatedPlace(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Capital(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AdminDistrictCapital(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CountryRegionCapital(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RoadShield(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RoadExit(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Transit(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Political(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CountryRegion(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_AdminDistrict(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_District(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Structure(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Building(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_EducationBuilding(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MedicalBuilding(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TransitBuilding(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Transportation(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Road(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ControlledAccessHighway(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HighSpeedRamp(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Highway(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MajorRoad(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_ArterialRoad(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Street(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Ramp(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_UnpavedStreet(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TollRoad(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Railway(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Trail(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WaterRoute(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Water(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_River(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_RouteLine(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WalkingRoute(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_DrivingRoute(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntriesStatics) -> WinRT_String: ...
    Area = property(get_Area, None)
    Airport = property(get_Airport, None)
    Cemetery = property(get_Cemetery, None)
    Continent = property(get_Continent, None)
    Education = property(get_Education, None)
    IndigenousPeoplesReserve = property(get_IndigenousPeoplesReserve, None)
    Island = property(get_Island, None)
    Medical = property(get_Medical, None)
    Military = property(get_Military, None)
    Nautical = property(get_Nautical, None)
    Neighborhood = property(get_Neighborhood, None)
    Runway = property(get_Runway, None)
    Sand = property(get_Sand, None)
    ShoppingCenter = property(get_ShoppingCenter, None)
    Stadium = property(get_Stadium, None)
    Vegetation = property(get_Vegetation, None)
    Forest = property(get_Forest, None)
    GolfCourse = property(get_GolfCourse, None)
    Park = property(get_Park, None)
    PlayingField = property(get_PlayingField, None)
    Reserve = property(get_Reserve, None)
    Point = property(get_Point, None)
    NaturalPoint = property(get_NaturalPoint, None)
    Peak = property(get_Peak, None)
    VolcanicPeak = property(get_VolcanicPeak, None)
    WaterPoint = property(get_WaterPoint, None)
    PointOfInterest = property(get_PointOfInterest, None)
    Business = property(get_Business, None)
    FoodPoint = property(get_FoodPoint, None)
    PopulatedPlace = property(get_PopulatedPlace, None)
    Capital = property(get_Capital, None)
    AdminDistrictCapital = property(get_AdminDistrictCapital, None)
    CountryRegionCapital = property(get_CountryRegionCapital, None)
    RoadShield = property(get_RoadShield, None)
    RoadExit = property(get_RoadExit, None)
    Transit = property(get_Transit, None)
    Political = property(get_Political, None)
    CountryRegion = property(get_CountryRegion, None)
    AdminDistrict = property(get_AdminDistrict, None)
    District = property(get_District, None)
    Structure = property(get_Structure, None)
    Building = property(get_Building, None)
    EducationBuilding = property(get_EducationBuilding, None)
    MedicalBuilding = property(get_MedicalBuilding, None)
    TransitBuilding = property(get_TransitBuilding, None)
    Transportation = property(get_Transportation, None)
    Road = property(get_Road, None)
    ControlledAccessHighway = property(get_ControlledAccessHighway, None)
    HighSpeedRamp = property(get_HighSpeedRamp, None)
    Highway = property(get_Highway, None)
    MajorRoad = property(get_MajorRoad, None)
    ArterialRoad = property(get_ArterialRoad, None)
    Street = property(get_Street, None)
    Ramp = property(get_Ramp, None)
    UnpavedStreet = property(get_UnpavedStreet, None)
    TollRoad = property(get_TollRoad, None)
    Railway = property(get_Railway, None)
    Trail = property(get_Trail, None)
    WaterRoute = property(get_WaterRoute, None)
    Water = property(get_Water, None)
    River = property(get_River, None)
    RouteLine = property(get_RouteLine, None)
    WalkingRoute = property(get_WalkingRoute, None)
    DrivingRoute = property(get_DrivingRoute, None)
class MapStyleSheetEntryStates(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapStyleSheetEntryStates'
    @winrt_classmethod
    def get_Disabled(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntryStatesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Hover(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntryStatesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Selected(cls: Windows.UI.Xaml.Controls.Maps.IMapStyleSheetEntryStatesStatics) -> WinRT_String: ...
    Disabled = property(get_Disabled, None)
    Hover = property(get_Hover, None)
    Selected = property(get_Selected, None)
class MapTargetCameraChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapTargetCameraChangedEventArgs: ...
    @winrt_mixinmethod
    def get_Camera(self: Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs) -> Windows.UI.Xaml.Controls.Maps.MapCamera: ...
    @winrt_mixinmethod
    def get_ChangeReason(self: Windows.UI.Xaml.Controls.Maps.IMapTargetCameraChangedEventArgs2) -> Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason: ...
    Camera = property(get_Camera, None)
    ChangeReason = property(get_ChangeReason, None)
MapTileAnimationState = Int32
MapTileAnimationState_Stopped: MapTileAnimationState = 0
MapTileAnimationState_Paused: MapTileAnimationState = 1
MapTileAnimationState_Playing: MapTileAnimationState = 2
class MapTileBitmapRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequest'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequest: ...
    @winrt_mixinmethod
    def get_PixelData(self: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest) -> Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_PixelData(self: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest, value: Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequest) -> Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestDeferral: ...
    PixelData = property(get_PixelData, put_PixelData)
class MapTileBitmapRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestDeferral
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestDeferral'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestDeferral: ...
    @winrt_mixinmethod
    def Complete(self: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestDeferral) -> Void: ...
class MapTileBitmapRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_X(self: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Y(self: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ZoomLevel(self: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Request(self: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs) -> Windows.UI.Xaml.Controls.Maps.MapTileBitmapRequest: ...
    @winrt_mixinmethod
    def get_FrameIndex(self: Windows.UI.Xaml.Controls.Maps.IMapTileBitmapRequestedEventArgs2) -> Int32: ...
    X = property(get_X, None)
    Y = property(get_Y, None)
    ZoomLevel = property(get_ZoomLevel, None)
    Request = property(get_Request, None)
    FrameIndex = property(get_FrameIndex, None)
class MapTileDataSource(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapTileDataSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileDataSource'
MapTileLayer = Int32
MapTileLayer_LabelOverlay: MapTileLayer = 0
MapTileLayer_RoadOverlay: MapTileLayer = 1
MapTileLayer_AreaOverlay: MapTileLayer = 2
MapTileLayer_BackgroundOverlay: MapTileLayer = 3
MapTileLayer_BackgroundReplacement: MapTileLayer = 4
class MapTileSource(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapTileSource
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileSource'
    @winrt_commethod(58)
    def get_DataSource(self) -> Windows.UI.Xaml.Controls.Maps.MapTileDataSource: ...
    @winrt_commethod(59)
    def put_DataSource(self, value: Windows.UI.Xaml.Controls.Maps.MapTileDataSource) -> Void: ...
    @winrt_commethod(60)
    def get_Layer(self) -> Windows.UI.Xaml.Controls.Maps.MapTileLayer: ...
    @winrt_commethod(61)
    def put_Layer(self, value: Windows.UI.Xaml.Controls.Maps.MapTileLayer) -> Void: ...
    @winrt_commethod(62)
    def get_ZoomLevelRange(self) -> Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange: ...
    @winrt_commethod(63)
    def put_ZoomLevelRange(self, value: Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange) -> Void: ...
    @winrt_commethod(64)
    def get_Bounds(self) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(65)
    def put_Bounds(self, value: Windows.Devices.Geolocation.GeoboundingBox) -> Void: ...
    @winrt_commethod(66)
    def get_AllowOverstretch(self) -> Boolean: ...
    @winrt_commethod(67)
    def put_AllowOverstretch(self, value: Boolean) -> Void: ...
    @winrt_commethod(68)
    def get_IsFadingEnabled(self) -> Boolean: ...
    @winrt_commethod(69)
    def put_IsFadingEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(70)
    def get_IsTransparencyEnabled(self) -> Boolean: ...
    @winrt_commethod(71)
    def put_IsTransparencyEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(72)
    def get_IsRetryEnabled(self) -> Boolean: ...
    @winrt_commethod(73)
    def put_IsRetryEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(74)
    def get_ZIndex(self) -> Int32: ...
    @winrt_commethod(75)
    def put_ZIndex(self, value: Int32) -> Void: ...
    @winrt_commethod(76)
    def get_TilePixelSize(self) -> Int32: ...
    @winrt_commethod(77)
    def put_TilePixelSize(self, value: Int32) -> Void: ...
    @winrt_commethod(78)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(79)
    def put_Visible(self, value: Boolean) -> Void: ...
    @winrt_commethod(80)
    def get_AnimationState(self) -> Windows.UI.Xaml.Controls.Maps.MapTileAnimationState: ...
    @winrt_commethod(81)
    def get_AutoPlay(self) -> Boolean: ...
    @winrt_commethod(82)
    def put_AutoPlay(self, value: Boolean) -> Void: ...
    @winrt_commethod(83)
    def get_FrameCount(self) -> Int32: ...
    @winrt_commethod(84)
    def put_FrameCount(self, value: Int32) -> Void: ...
    @winrt_commethod(85)
    def get_FrameDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(86)
    def put_FrameDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(87)
    def Pause(self) -> Void: ...
    @winrt_commethod(88)
    def Play(self) -> Void: ...
    @winrt_commethod(89)
    def Stop(self) -> Void: ...
    @winrt_classmethod
    def get_AnimationStateProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AutoPlayProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FrameCountProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FrameDurationProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_DataSourceProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LayerProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZoomLevelRangeProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BoundsProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AllowOverstretchProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsFadingEnabledProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsTransparencyEnabledProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsRetryEnabledProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ZIndexProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TilePixelSizeProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_VisibleProperty(cls: Windows.UI.Xaml.Controls.Maps.IMapTileSourceStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    DataSource = property(get_DataSource, put_DataSource)
    Layer = property(get_Layer, put_Layer)
    ZoomLevelRange = property(get_ZoomLevelRange, put_ZoomLevelRange)
    Bounds = property(get_Bounds, put_Bounds)
    AllowOverstretch = property(get_AllowOverstretch, put_AllowOverstretch)
    IsFadingEnabled = property(get_IsFadingEnabled, put_IsFadingEnabled)
    IsTransparencyEnabled = property(get_IsTransparencyEnabled, put_IsTransparencyEnabled)
    IsRetryEnabled = property(get_IsRetryEnabled, put_IsRetryEnabled)
    ZIndex = property(get_ZIndex, put_ZIndex)
    TilePixelSize = property(get_TilePixelSize, put_TilePixelSize)
    Visible = property(get_Visible, put_Visible)
    AnimationState = property(get_AnimationState, None)
    AutoPlay = property(get_AutoPlay, put_AutoPlay)
    FrameCount = property(get_FrameCount, put_FrameCount)
    FrameDuration = property(get_FrameDuration, put_FrameDuration)
    AnimationStateProperty = property(get_AnimationStateProperty, None)
    AutoPlayProperty = property(get_AutoPlayProperty, None)
    FrameCountProperty = property(get_FrameCountProperty, None)
    FrameDurationProperty = property(get_FrameDurationProperty, None)
    DataSourceProperty = property(get_DataSourceProperty, None)
    LayerProperty = property(get_LayerProperty, None)
    ZoomLevelRangeProperty = property(get_ZoomLevelRangeProperty, None)
    BoundsProperty = property(get_BoundsProperty, None)
    AllowOverstretchProperty = property(get_AllowOverstretchProperty, None)
    IsFadingEnabledProperty = property(get_IsFadingEnabledProperty, None)
    IsTransparencyEnabledProperty = property(get_IsTransparencyEnabledProperty, None)
    IsRetryEnabledProperty = property(get_IsRetryEnabledProperty, None)
    ZIndexProperty = property(get_ZIndexProperty, None)
    TilePixelSizeProperty = property(get_TilePixelSizeProperty, None)
    VisibleProperty = property(get_VisibleProperty, None)
class MapTileUriRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileUriRequest'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapTileUriRequest: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequest) -> Windows.UI.Xaml.Controls.Maps.MapTileUriRequestDeferral: ...
    Uri = property(get_Uri, put_Uri)
class MapTileUriRequestDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestDeferral
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileUriRequestDeferral'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapTileUriRequestDeferral: ...
    @winrt_mixinmethod
    def Complete(self: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestDeferral) -> Void: ...
class MapTileUriRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Controls.Maps.MapTileUriRequestedEventArgs: ...
    @winrt_mixinmethod
    def get_X(self: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Y(self: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ZoomLevel(self: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_Request(self: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs) -> Windows.UI.Xaml.Controls.Maps.MapTileUriRequest: ...
    @winrt_mixinmethod
    def get_FrameIndex(self: Windows.UI.Xaml.Controls.Maps.IMapTileUriRequestedEventArgs2) -> Int32: ...
    X = property(get_X, None)
    Y = property(get_Y, None)
    ZoomLevel = property(get_ZoomLevel, None)
    Request = property(get_Request, None)
    FrameIndex = property(get_FrameIndex, None)
MapVisibleRegionKind = Int32
MapVisibleRegionKind_Near: MapVisibleRegionKind = 0
MapVisibleRegionKind_Full: MapVisibleRegionKind = 1
MapWatermarkMode = Int32
MapWatermarkMode_Automatic: MapWatermarkMode = 0
MapWatermarkMode_On: MapWatermarkMode = 1
class MapZoomLevelRange(EasyCastStructure):
    Min: Double
    Max: Double
class StreetsideExperience(ComPtr):
    extends: Windows.UI.Xaml.Controls.Maps.MapCustomExperience
    default_interface: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.StreetsideExperience'
    @winrt_factorymethod
    def CreateInstanceWithPanorama(cls: Windows.UI.Xaml.Controls.Maps.IStreetsideExperienceFactory, panorama: Windows.UI.Xaml.Controls.Maps.StreetsidePanorama) -> Windows.UI.Xaml.Controls.Maps.StreetsideExperience: ...
    @winrt_factorymethod
    def CreateInstanceWithPanoramaHeadingPitchAndFieldOfView(cls: Windows.UI.Xaml.Controls.Maps.IStreetsideExperienceFactory, panorama: Windows.UI.Xaml.Controls.Maps.StreetsidePanorama, headingInDegrees: Double, pitchInDegrees: Double, fieldOfViewInDegrees: Double) -> Windows.UI.Xaml.Controls.Maps.StreetsideExperience: ...
    @winrt_mixinmethod
    def get_AddressTextVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_AddressTextVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CursorVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_CursorVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OverviewMapVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_OverviewMapVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_StreetLabelsVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_StreetLabelsVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExitButtonVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_ExitButtonVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ZoomButtonsVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience) -> Boolean: ...
    @winrt_mixinmethod
    def put_ZoomButtonsVisible(self: Windows.UI.Xaml.Controls.Maps.IStreetsideExperience, value: Boolean) -> Void: ...
    AddressTextVisible = property(get_AddressTextVisible, put_AddressTextVisible)
    CursorVisible = property(get_CursorVisible, put_CursorVisible)
    OverviewMapVisible = property(get_OverviewMapVisible, put_OverviewMapVisible)
    StreetLabelsVisible = property(get_StreetLabelsVisible, put_StreetLabelsVisible)
    ExitButtonVisible = property(get_ExitButtonVisible, put_ExitButtonVisible)
    ZoomButtonsVisible = property(get_ZoomButtonsVisible, put_ZoomButtonsVisible)
class StreetsidePanorama(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Controls.Maps.IStreetsidePanorama
    _classid_ = 'Windows.UI.Xaml.Controls.Maps.StreetsidePanorama'
    @winrt_mixinmethod
    def get_Location(self: Windows.UI.Xaml.Controls.Maps.IStreetsidePanorama) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_classmethod
    def FindNearbyWithLocationAsync(cls: Windows.UI.Xaml.Controls.Maps.IStreetsidePanoramaStatics, location: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Controls.Maps.StreetsidePanorama]: ...
    @winrt_classmethod
    def FindNearbyWithLocationAndRadiusAsync(cls: Windows.UI.Xaml.Controls.Maps.IStreetsidePanoramaStatics, location: Windows.Devices.Geolocation.Geopoint, radiusInMeters: Double) -> Windows.Foundation.IAsyncOperation[Windows.UI.Xaml.Controls.Maps.StreetsidePanorama]: ...
    Location = property(get_Location, None)
make_head(_module, 'CustomMapTileDataSource')
make_head(_module, 'HttpMapTileDataSource')
make_head(_module, 'ICustomMapTileDataSource')
make_head(_module, 'ICustomMapTileDataSourceFactory')
make_head(_module, 'IHttpMapTileDataSource')
make_head(_module, 'IHttpMapTileDataSourceFactory')
make_head(_module, 'ILocalMapTileDataSource')
make_head(_module, 'ILocalMapTileDataSourceFactory')
make_head(_module, 'IMapActualCameraChangedEventArgs')
make_head(_module, 'IMapActualCameraChangedEventArgs2')
make_head(_module, 'IMapActualCameraChangingEventArgs')
make_head(_module, 'IMapActualCameraChangingEventArgs2')
make_head(_module, 'IMapBillboard')
make_head(_module, 'IMapBillboardFactory')
make_head(_module, 'IMapBillboardStatics')
make_head(_module, 'IMapCamera')
make_head(_module, 'IMapCameraFactory')
make_head(_module, 'IMapContextRequestedEventArgs')
make_head(_module, 'IMapControl')
make_head(_module, 'IMapControl2')
make_head(_module, 'IMapControl3')
make_head(_module, 'IMapControl4')
make_head(_module, 'IMapControl5')
make_head(_module, 'IMapControl6')
make_head(_module, 'IMapControl7')
make_head(_module, 'IMapControl8')
make_head(_module, 'IMapControlBusinessLandmarkClickEventArgs')
make_head(_module, 'IMapControlBusinessLandmarkPointerEnteredEventArgs')
make_head(_module, 'IMapControlBusinessLandmarkPointerExitedEventArgs')
make_head(_module, 'IMapControlBusinessLandmarkRightTappedEventArgs')
make_head(_module, 'IMapControlDataHelper')
make_head(_module, 'IMapControlDataHelper2')
make_head(_module, 'IMapControlDataHelperFactory')
make_head(_module, 'IMapControlDataHelperStatics')
make_head(_module, 'IMapControlStatics')
make_head(_module, 'IMapControlStatics2')
make_head(_module, 'IMapControlStatics4')
make_head(_module, 'IMapControlStatics5')
make_head(_module, 'IMapControlStatics6')
make_head(_module, 'IMapControlStatics7')
make_head(_module, 'IMapControlStatics8')
make_head(_module, 'IMapControlTransitFeatureClickEventArgs')
make_head(_module, 'IMapControlTransitFeaturePointerEnteredEventArgs')
make_head(_module, 'IMapControlTransitFeaturePointerExitedEventArgs')
make_head(_module, 'IMapControlTransitFeatureRightTappedEventArgs')
make_head(_module, 'IMapCustomExperience')
make_head(_module, 'IMapCustomExperienceChangedEventArgs')
make_head(_module, 'IMapCustomExperienceFactory')
make_head(_module, 'IMapElement')
make_head(_module, 'IMapElement2')
make_head(_module, 'IMapElement3')
make_head(_module, 'IMapElement3D')
make_head(_module, 'IMapElement3DStatics')
make_head(_module, 'IMapElement4')
make_head(_module, 'IMapElementClickEventArgs')
make_head(_module, 'IMapElementFactory')
make_head(_module, 'IMapElementPointerEnteredEventArgs')
make_head(_module, 'IMapElementPointerExitedEventArgs')
make_head(_module, 'IMapElementStatics')
make_head(_module, 'IMapElementStatics2')
make_head(_module, 'IMapElementStatics3')
make_head(_module, 'IMapElementStatics4')
make_head(_module, 'IMapElementsLayer')
make_head(_module, 'IMapElementsLayerClickEventArgs')
make_head(_module, 'IMapElementsLayerContextRequestedEventArgs')
make_head(_module, 'IMapElementsLayerPointerEnteredEventArgs')
make_head(_module, 'IMapElementsLayerPointerExitedEventArgs')
make_head(_module, 'IMapElementsLayerStatics')
make_head(_module, 'IMapIcon')
make_head(_module, 'IMapIcon2')
make_head(_module, 'IMapIconStatics')
make_head(_module, 'IMapIconStatics2')
make_head(_module, 'IMapInputEventArgs')
make_head(_module, 'IMapItemsControl')
make_head(_module, 'IMapItemsControlStatics')
make_head(_module, 'IMapLayer')
make_head(_module, 'IMapLayerFactory')
make_head(_module, 'IMapLayerStatics')
make_head(_module, 'IMapModel3D')
make_head(_module, 'IMapModel3DFactory')
make_head(_module, 'IMapModel3DStatics')
make_head(_module, 'IMapPolygon')
make_head(_module, 'IMapPolygon2')
make_head(_module, 'IMapPolygonStatics')
make_head(_module, 'IMapPolyline')
make_head(_module, 'IMapPolylineStatics')
make_head(_module, 'IMapRightTappedEventArgs')
make_head(_module, 'IMapRouteView')
make_head(_module, 'IMapRouteViewFactory')
make_head(_module, 'IMapScene')
make_head(_module, 'IMapSceneStatics')
make_head(_module, 'IMapStyleSheet')
make_head(_module, 'IMapStyleSheetEntriesStatics')
make_head(_module, 'IMapStyleSheetEntryStatesStatics')
make_head(_module, 'IMapStyleSheetStatics')
make_head(_module, 'IMapTargetCameraChangedEventArgs')
make_head(_module, 'IMapTargetCameraChangedEventArgs2')
make_head(_module, 'IMapTileBitmapRequest')
make_head(_module, 'IMapTileBitmapRequestDeferral')
make_head(_module, 'IMapTileBitmapRequestedEventArgs')
make_head(_module, 'IMapTileBitmapRequestedEventArgs2')
make_head(_module, 'IMapTileDataSource')
make_head(_module, 'IMapTileDataSourceFactory')
make_head(_module, 'IMapTileSource')
make_head(_module, 'IMapTileSource2')
make_head(_module, 'IMapTileSourceFactory')
make_head(_module, 'IMapTileSourceStatics')
make_head(_module, 'IMapTileSourceStatics2')
make_head(_module, 'IMapTileUriRequest')
make_head(_module, 'IMapTileUriRequestDeferral')
make_head(_module, 'IMapTileUriRequestedEventArgs')
make_head(_module, 'IMapTileUriRequestedEventArgs2')
make_head(_module, 'IStreetsideExperience')
make_head(_module, 'IStreetsideExperienceFactory')
make_head(_module, 'IStreetsidePanorama')
make_head(_module, 'IStreetsidePanoramaStatics')
make_head(_module, 'LocalMapTileDataSource')
make_head(_module, 'MapActualCameraChangedEventArgs')
make_head(_module, 'MapActualCameraChangingEventArgs')
make_head(_module, 'MapBillboard')
make_head(_module, 'MapCamera')
make_head(_module, 'MapContextRequestedEventArgs')
make_head(_module, 'MapControl')
make_head(_module, 'MapControlBusinessLandmarkClickEventArgs')
make_head(_module, 'MapControlBusinessLandmarkPointerEnteredEventArgs')
make_head(_module, 'MapControlBusinessLandmarkPointerExitedEventArgs')
make_head(_module, 'MapControlBusinessLandmarkRightTappedEventArgs')
make_head(_module, 'MapControlDataHelper')
make_head(_module, 'MapControlTransitFeatureClickEventArgs')
make_head(_module, 'MapControlTransitFeaturePointerEnteredEventArgs')
make_head(_module, 'MapControlTransitFeaturePointerExitedEventArgs')
make_head(_module, 'MapControlTransitFeatureRightTappedEventArgs')
make_head(_module, 'MapCustomExperience')
make_head(_module, 'MapCustomExperienceChangedEventArgs')
make_head(_module, 'MapElement')
make_head(_module, 'MapElement3D')
make_head(_module, 'MapElementClickEventArgs')
make_head(_module, 'MapElementPointerEnteredEventArgs')
make_head(_module, 'MapElementPointerExitedEventArgs')
make_head(_module, 'MapElementsLayer')
make_head(_module, 'MapElementsLayerClickEventArgs')
make_head(_module, 'MapElementsLayerContextRequestedEventArgs')
make_head(_module, 'MapElementsLayerPointerEnteredEventArgs')
make_head(_module, 'MapElementsLayerPointerExitedEventArgs')
make_head(_module, 'MapIcon')
make_head(_module, 'MapInputEventArgs')
make_head(_module, 'MapItemsControl')
make_head(_module, 'MapLayer')
make_head(_module, 'MapModel3D')
make_head(_module, 'MapPolygon')
make_head(_module, 'MapPolyline')
make_head(_module, 'MapRightTappedEventArgs')
make_head(_module, 'MapRouteView')
make_head(_module, 'MapScene')
make_head(_module, 'MapStyleSheet')
make_head(_module, 'MapStyleSheetEntries')
make_head(_module, 'MapStyleSheetEntryStates')
make_head(_module, 'MapTargetCameraChangedEventArgs')
make_head(_module, 'MapTileBitmapRequest')
make_head(_module, 'MapTileBitmapRequestDeferral')
make_head(_module, 'MapTileBitmapRequestedEventArgs')
make_head(_module, 'MapTileDataSource')
make_head(_module, 'MapTileSource')
make_head(_module, 'MapTileUriRequest')
make_head(_module, 'MapTileUriRequestDeferral')
make_head(_module, 'MapTileUriRequestedEventArgs')
make_head(_module, 'MapZoomLevelRange')
make_head(_module, 'StreetsideExperience')
make_head(_module, 'StreetsidePanorama')
