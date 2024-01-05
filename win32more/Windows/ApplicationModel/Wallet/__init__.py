from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Wallet
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class IWalletBarcode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletBarcode'
    _iid_ = Guid('{4f857b29-de80-4ea4-a1cd-81cd084dac27}')
    @winrt_commethod(6)
    def get_Symbology(self) -> win32more.Windows.ApplicationModel.Wallet.WalletBarcodeSymbology: ...
    @winrt_commethod(7)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetImageAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    Symbology = property(get_Symbology, None)
    Value = property(get_Value, None)
class IWalletBarcodeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletBarcodeFactory'
    _iid_ = Guid('{30117161-ed9c-469e-bbfd-306c95ea7108}')
    @winrt_commethod(6)
    def CreateWalletBarcode(self, symbology: win32more.Windows.ApplicationModel.Wallet.WalletBarcodeSymbology, value: WinRT_String) -> win32more.Windows.ApplicationModel.Wallet.WalletBarcode: ...
    @winrt_commethod(7)
    def CreateCustomWalletBarcode(self, streamToBarcodeImage: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.ApplicationModel.Wallet.WalletBarcode: ...
class IWalletItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletItem'
    _iid_ = Guid('{20b54be8-118d-4ec4-996c-b963e7bd3e74}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_IsAcknowledged(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsAcknowledged(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IssuerDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_IssuerDisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_LastUpdated(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(14)
    def put_LastUpdated(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(15)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Wallet.WalletItemKind: ...
    @winrt_commethod(16)
    def get_Barcode(self) -> win32more.Windows.ApplicationModel.Wallet.WalletBarcode: ...
    @winrt_commethod(17)
    def put_Barcode(self, value: win32more.Windows.ApplicationModel.Wallet.WalletBarcode) -> Void: ...
    @winrt_commethod(18)
    def get_ExpirationDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(19)
    def put_ExpirationDate(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(20)
    def get_Logo159x159(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(21)
    def put_Logo159x159(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(22)
    def get_Logo336x336(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(23)
    def put_Logo336x336(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(24)
    def get_Logo99x99(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(25)
    def put_Logo99x99(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(26)
    def get_DisplayMessage(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def put_DisplayMessage(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(28)
    def get_IsDisplayMessageLaunchable(self) -> Boolean: ...
    @winrt_commethod(29)
    def put_IsDisplayMessageLaunchable(self, value: Boolean) -> Void: ...
    @winrt_commethod(30)
    def get_LogoText(self) -> WinRT_String: ...
    @winrt_commethod(31)
    def put_LogoText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(32)
    def get_HeaderColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(33)
    def put_HeaderColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(34)
    def get_BodyColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(35)
    def put_BodyColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(36)
    def get_HeaderFontColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(37)
    def put_HeaderFontColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(38)
    def get_BodyFontColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(39)
    def put_BodyFontColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(40)
    def get_HeaderBackgroundImage(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(41)
    def put_HeaderBackgroundImage(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(42)
    def get_BodyBackgroundImage(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(43)
    def put_BodyBackgroundImage(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(44)
    def get_LogoImage(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(45)
    def put_LogoImage(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(46)
    def get_PromotionalImage(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(47)
    def put_PromotionalImage(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(48)
    def get_RelevantDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(49)
    def put_RelevantDate(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(50)
    def get_RelevantDateDisplayMessage(self) -> WinRT_String: ...
    @winrt_commethod(51)
    def put_RelevantDateDisplayMessage(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(52)
    def get_TransactionHistory(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.ApplicationModel.Wallet.WalletTransaction]: ...
    @winrt_commethod(53)
    def get_RelevantLocations(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.ApplicationModel.Wallet.WalletRelevantLocation]: ...
    @winrt_commethod(54)
    def get_IsMoreTransactionHistoryLaunchable(self) -> Boolean: ...
    @winrt_commethod(55)
    def put_IsMoreTransactionHistoryLaunchable(self, value: Boolean) -> Void: ...
    @winrt_commethod(56)
    def get_DisplayProperties(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.ApplicationModel.Wallet.WalletItemCustomProperty]: ...
    @winrt_commethod(57)
    def get_Verbs(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.ApplicationModel.Wallet.WalletVerb]: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    Id = property(get_Id, None)
    IsAcknowledged = property(get_IsAcknowledged, put_IsAcknowledged)
    IssuerDisplayName = property(get_IssuerDisplayName, put_IssuerDisplayName)
    LastUpdated = property(get_LastUpdated, put_LastUpdated)
    Kind = property(get_Kind, None)
    Barcode = property(get_Barcode, put_Barcode)
    ExpirationDate = property(get_ExpirationDate, put_ExpirationDate)
    Logo159x159 = property(get_Logo159x159, put_Logo159x159)
    Logo336x336 = property(get_Logo336x336, put_Logo336x336)
    Logo99x99 = property(get_Logo99x99, put_Logo99x99)
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
    IsDisplayMessageLaunchable = property(get_IsDisplayMessageLaunchable, put_IsDisplayMessageLaunchable)
    LogoText = property(get_LogoText, put_LogoText)
    HeaderColor = property(get_HeaderColor, put_HeaderColor)
    BodyColor = property(get_BodyColor, put_BodyColor)
    HeaderFontColor = property(get_HeaderFontColor, put_HeaderFontColor)
    BodyFontColor = property(get_BodyFontColor, put_BodyFontColor)
    HeaderBackgroundImage = property(get_HeaderBackgroundImage, put_HeaderBackgroundImage)
    BodyBackgroundImage = property(get_BodyBackgroundImage, put_BodyBackgroundImage)
    LogoImage = property(get_LogoImage, put_LogoImage)
    PromotionalImage = property(get_PromotionalImage, put_PromotionalImage)
    RelevantDate = property(get_RelevantDate, put_RelevantDate)
    RelevantDateDisplayMessage = property(get_RelevantDateDisplayMessage, put_RelevantDateDisplayMessage)
    TransactionHistory = property(get_TransactionHistory, None)
    RelevantLocations = property(get_RelevantLocations, None)
    IsMoreTransactionHistoryLaunchable = property(get_IsMoreTransactionHistoryLaunchable, put_IsMoreTransactionHistoryLaunchable)
    DisplayProperties = property(get_DisplayProperties, None)
    Verbs = property(get_Verbs, None)
class IWalletItemCustomProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletItemCustomProperty'
    _iid_ = Guid('{b94b40f3-fa00-40fd-98dc-9de46697f1e7}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Value(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_AutoDetectLinks(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AutoDetectLinks(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_DetailViewPosition(self) -> win32more.Windows.ApplicationModel.Wallet.WalletDetailViewPosition: ...
    @winrt_commethod(13)
    def put_DetailViewPosition(self, value: win32more.Windows.ApplicationModel.Wallet.WalletDetailViewPosition) -> Void: ...
    @winrt_commethod(14)
    def get_SummaryViewPosition(self) -> win32more.Windows.ApplicationModel.Wallet.WalletSummaryViewPosition: ...
    @winrt_commethod(15)
    def put_SummaryViewPosition(self, value: win32more.Windows.ApplicationModel.Wallet.WalletSummaryViewPosition) -> Void: ...
    Name = property(get_Name, put_Name)
    Value = property(get_Value, put_Value)
    AutoDetectLinks = property(get_AutoDetectLinks, put_AutoDetectLinks)
    DetailViewPosition = property(get_DetailViewPosition, put_DetailViewPosition)
    SummaryViewPosition = property(get_SummaryViewPosition, put_SummaryViewPosition)
class IWalletItemCustomPropertyFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletItemCustomPropertyFactory'
    _iid_ = Guid('{d0046a44-61a1-41aa-b259-a5610ab5d575}')
    @winrt_commethod(6)
    def CreateWalletItemCustomProperty(self, name: WinRT_String, value: WinRT_String) -> win32more.Windows.ApplicationModel.Wallet.WalletItemCustomProperty: ...
class IWalletItemFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletItemFactory'
    _iid_ = Guid('{53e27470-4f0b-4a3e-99e5-0bbb1eab38d4}')
    @winrt_commethod(6)
    def CreateWalletItem(self, kind: win32more.Windows.ApplicationModel.Wallet.WalletItemKind, displayName: WinRT_String) -> win32more.Windows.ApplicationModel.Wallet.WalletItem: ...
class IWalletItemStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletItemStore'
    _iid_ = Guid('{7160484b-6d49-48f8-91a9-40a1d0f13ef4}')
    @winrt_commethod(6)
    def AddAsync(self, id: WinRT_String, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ClearAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def GetWalletItemAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.WalletItem]: ...
    @winrt_commethod(9)
    def GetItemsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Wallet.WalletItem]]: ...
    @winrt_commethod(10)
    def GetItemsWithKindAsync(self, kind: win32more.Windows.ApplicationModel.Wallet.WalletItemKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Wallet.WalletItem]]: ...
    @winrt_commethod(11)
    def ImportItemAsync(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.WalletItem]: ...
    @winrt_commethod(12)
    def DeleteAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ShowAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def ShowItemAsync(self, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def UpdateAsync(self, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.Foundation.IAsyncAction: ...
class IWalletItemStore2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletItemStore2'
    _iid_ = Guid('{65e682f0-7009-4a15-bd54-4fff379bffe2}')
    @winrt_commethod(6)
    def add_ItemsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Wallet.WalletItemStore, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ItemsChanged(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWalletManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletManagerStatics'
    _iid_ = Guid('{5111d6b8-c9a4-4c64-b4dd-e1e548001c0d}')
    @winrt_commethod(6)
    def RequestStoreAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.WalletItemStore]: ...
class IWalletRelevantLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletRelevantLocation'
    _iid_ = Guid('{9fd8782a-e3f9-4de1-bab3-bb192e46b3f3}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_commethod(7)
    def put_Position(self, value: win32more.Windows.Devices.Geolocation.BasicGeoposition) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayMessage(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayMessage(self, value: WinRT_String) -> Void: ...
    Position = property(get_Position, put_Position)
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
class IWalletTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletTransaction'
    _iid_ = Guid('{40e1e940-2606-4519-81cb-bff1c60d1f79}')
    @winrt_commethod(6)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_DisplayAmount(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayAmount(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_IgnoreTimeOfDay(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IgnoreTimeOfDay(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_DisplayLocation(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_DisplayLocation(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_TransactionDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(15)
    def put_TransactionDate(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(16)
    def get_IsLaunchable(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsLaunchable(self, value: Boolean) -> Void: ...
    Description = property(get_Description, put_Description)
    DisplayAmount = property(get_DisplayAmount, put_DisplayAmount)
    IgnoreTimeOfDay = property(get_IgnoreTimeOfDay, put_IgnoreTimeOfDay)
    DisplayLocation = property(get_DisplayLocation, put_DisplayLocation)
    TransactionDate = property(get_TransactionDate, put_TransactionDate)
    IsLaunchable = property(get_IsLaunchable, put_IsLaunchable)
class IWalletVerb(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletVerb'
    _iid_ = Guid('{17b826d6-e3c1-4c74-8a94-217aadbc4884}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Name(self, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)
class IWalletVerbFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.IWalletVerbFactory'
    _iid_ = Guid('{76012771-be58-4d5e-83ed-58b1669c7ad9}')
    @winrt_commethod(6)
    def CreateWalletVerb(self, name: WinRT_String) -> win32more.Windows.ApplicationModel.Wallet.WalletVerb: ...
WalletActionKind = Int32
WalletActionKind_OpenItem: WalletActionKind = 0
WalletActionKind_Transaction: WalletActionKind = 1
WalletActionKind_MoreTransactions: WalletActionKind = 2
WalletActionKind_Message: WalletActionKind = 3
WalletActionKind_Verb: WalletActionKind = 4
class WalletBarcode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Wallet.IWalletBarcode
    _classid_ = 'Windows.ApplicationModel.Wallet.WalletBarcode'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.ApplicationModel.Wallet.WalletBarcode.CreateCustomWalletBarcode(*args)
        elif len(args) == 2:
            return win32more.Windows.ApplicationModel.Wallet.WalletBarcode.CreateWalletBarcode(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateCustomWalletBarcode(cls: win32more.Windows.ApplicationModel.Wallet.IWalletBarcodeFactory, streamToBarcodeImage: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.ApplicationModel.Wallet.WalletBarcode: ...
    @winrt_factorymethod
    def CreateWalletBarcode(cls: win32more.Windows.ApplicationModel.Wallet.IWalletBarcodeFactory, symbology: win32more.Windows.ApplicationModel.Wallet.WalletBarcodeSymbology, value: WinRT_String) -> win32more.Windows.ApplicationModel.Wallet.WalletBarcode: ...
    @winrt_mixinmethod
    def get_Symbology(self: win32more.Windows.ApplicationModel.Wallet.IWalletBarcode) -> win32more.Windows.ApplicationModel.Wallet.WalletBarcodeSymbology: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.ApplicationModel.Wallet.IWalletBarcode) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetImageAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletBarcode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamReference]: ...
    Symbology = property(get_Symbology, None)
    Value = property(get_Value, None)
WalletBarcodeSymbology = Int32
WalletBarcodeSymbology_Invalid: WalletBarcodeSymbology = 0
WalletBarcodeSymbology_Upca: WalletBarcodeSymbology = 1
WalletBarcodeSymbology_Upce: WalletBarcodeSymbology = 2
WalletBarcodeSymbology_Ean13: WalletBarcodeSymbology = 3
WalletBarcodeSymbology_Ean8: WalletBarcodeSymbology = 4
WalletBarcodeSymbology_Itf: WalletBarcodeSymbology = 5
WalletBarcodeSymbology_Code39: WalletBarcodeSymbology = 6
WalletBarcodeSymbology_Code128: WalletBarcodeSymbology = 7
WalletBarcodeSymbology_Qr: WalletBarcodeSymbology = 8
WalletBarcodeSymbology_Pdf417: WalletBarcodeSymbology = 9
WalletBarcodeSymbology_Aztec: WalletBarcodeSymbology = 10
WalletBarcodeSymbology_Custom: WalletBarcodeSymbology = 100000
WalletContract: UInt32 = 131072
WalletDetailViewPosition = Int32
WalletDetailViewPosition_Hidden: WalletDetailViewPosition = 0
WalletDetailViewPosition_HeaderField1: WalletDetailViewPosition = 1
WalletDetailViewPosition_HeaderField2: WalletDetailViewPosition = 2
WalletDetailViewPosition_PrimaryField1: WalletDetailViewPosition = 3
WalletDetailViewPosition_PrimaryField2: WalletDetailViewPosition = 4
WalletDetailViewPosition_SecondaryField1: WalletDetailViewPosition = 5
WalletDetailViewPosition_SecondaryField2: WalletDetailViewPosition = 6
WalletDetailViewPosition_SecondaryField3: WalletDetailViewPosition = 7
WalletDetailViewPosition_SecondaryField4: WalletDetailViewPosition = 8
WalletDetailViewPosition_SecondaryField5: WalletDetailViewPosition = 9
WalletDetailViewPosition_CenterField1: WalletDetailViewPosition = 10
WalletDetailViewPosition_FooterField1: WalletDetailViewPosition = 11
WalletDetailViewPosition_FooterField2: WalletDetailViewPosition = 12
WalletDetailViewPosition_FooterField3: WalletDetailViewPosition = 13
WalletDetailViewPosition_FooterField4: WalletDetailViewPosition = 14
class WalletItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Wallet.IWalletItem
    _classid_ = 'Windows.ApplicationModel.Wallet.WalletItem'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 2:
            return win32more.Windows.ApplicationModel.Wallet.WalletItem.CreateWalletItem(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWalletItem(cls: win32more.Windows.ApplicationModel.Wallet.IWalletItemFactory, kind: win32more.Windows.ApplicationModel.Wallet.WalletItemKind, displayName: WinRT_String) -> win32more.Windows.ApplicationModel.Wallet.WalletItem: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsAcknowledged(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAcknowledged(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IssuerDisplayName(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_IssuerDisplayName(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LastUpdated(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_LastUpdated(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.ApplicationModel.Wallet.WalletItemKind: ...
    @winrt_mixinmethod
    def get_Barcode(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.ApplicationModel.Wallet.WalletBarcode: ...
    @winrt_mixinmethod
    def put_Barcode(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.ApplicationModel.Wallet.WalletBarcode) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_ExpirationDate(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Logo159x159(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Logo159x159(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Logo336x336(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Logo336x336(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Logo99x99(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Logo99x99(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayMessage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayMessage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsDisplayMessageLaunchable(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDisplayMessageLaunchable(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LogoText(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LogoText(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_HeaderColor(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_HeaderColor(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_BodyColor(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BodyColor(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_HeaderFontColor(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_HeaderFontColor(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_BodyFontColor(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BodyFontColor(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_HeaderBackgroundImage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_HeaderBackgroundImage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_BodyBackgroundImage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_BodyBackgroundImage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_LogoImage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_LogoImage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_PromotionalImage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_PromotionalImage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_RelevantDate(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_RelevantDate(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_RelevantDateDisplayMessage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RelevantDateDisplayMessage(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TransactionHistory(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.ApplicationModel.Wallet.WalletTransaction]: ...
    @winrt_mixinmethod
    def get_RelevantLocations(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.ApplicationModel.Wallet.WalletRelevantLocation]: ...
    @winrt_mixinmethod
    def get_IsMoreTransactionHistoryLaunchable(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsMoreTransactionHistoryLaunchable(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayProperties(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.ApplicationModel.Wallet.WalletItemCustomProperty]: ...
    @winrt_mixinmethod
    def get_Verbs(self: win32more.Windows.ApplicationModel.Wallet.IWalletItem) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.ApplicationModel.Wallet.WalletVerb]: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    Id = property(get_Id, None)
    IsAcknowledged = property(get_IsAcknowledged, put_IsAcknowledged)
    IssuerDisplayName = property(get_IssuerDisplayName, put_IssuerDisplayName)
    LastUpdated = property(get_LastUpdated, put_LastUpdated)
    Kind = property(get_Kind, None)
    Barcode = property(get_Barcode, put_Barcode)
    ExpirationDate = property(get_ExpirationDate, put_ExpirationDate)
    Logo159x159 = property(get_Logo159x159, put_Logo159x159)
    Logo336x336 = property(get_Logo336x336, put_Logo336x336)
    Logo99x99 = property(get_Logo99x99, put_Logo99x99)
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
    IsDisplayMessageLaunchable = property(get_IsDisplayMessageLaunchable, put_IsDisplayMessageLaunchable)
    LogoText = property(get_LogoText, put_LogoText)
    HeaderColor = property(get_HeaderColor, put_HeaderColor)
    BodyColor = property(get_BodyColor, put_BodyColor)
    HeaderFontColor = property(get_HeaderFontColor, put_HeaderFontColor)
    BodyFontColor = property(get_BodyFontColor, put_BodyFontColor)
    HeaderBackgroundImage = property(get_HeaderBackgroundImage, put_HeaderBackgroundImage)
    BodyBackgroundImage = property(get_BodyBackgroundImage, put_BodyBackgroundImage)
    LogoImage = property(get_LogoImage, put_LogoImage)
    PromotionalImage = property(get_PromotionalImage, put_PromotionalImage)
    RelevantDate = property(get_RelevantDate, put_RelevantDate)
    RelevantDateDisplayMessage = property(get_RelevantDateDisplayMessage, put_RelevantDateDisplayMessage)
    TransactionHistory = property(get_TransactionHistory, None)
    RelevantLocations = property(get_RelevantLocations, None)
    IsMoreTransactionHistoryLaunchable = property(get_IsMoreTransactionHistoryLaunchable, put_IsMoreTransactionHistoryLaunchable)
    DisplayProperties = property(get_DisplayProperties, None)
    Verbs = property(get_Verbs, None)
class WalletItemCustomProperty(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty
    _classid_ = 'Windows.ApplicationModel.Wallet.WalletItemCustomProperty'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 2:
            return win32more.Windows.ApplicationModel.Wallet.WalletItemCustomProperty.CreateWalletItemCustomProperty(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWalletItemCustomProperty(cls: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomPropertyFactory, name: WinRT_String, value: WinRT_String) -> win32more.Windows.ApplicationModel.Wallet.WalletItemCustomProperty: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AutoDetectLinks(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoDetectLinks(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DetailViewPosition(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty) -> win32more.Windows.ApplicationModel.Wallet.WalletDetailViewPosition: ...
    @winrt_mixinmethod
    def put_DetailViewPosition(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty, value: win32more.Windows.ApplicationModel.Wallet.WalletDetailViewPosition) -> Void: ...
    @winrt_mixinmethod
    def get_SummaryViewPosition(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty) -> win32more.Windows.ApplicationModel.Wallet.WalletSummaryViewPosition: ...
    @winrt_mixinmethod
    def put_SummaryViewPosition(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemCustomProperty, value: win32more.Windows.ApplicationModel.Wallet.WalletSummaryViewPosition) -> Void: ...
    Name = property(get_Name, put_Name)
    Value = property(get_Value, put_Value)
    AutoDetectLinks = property(get_AutoDetectLinks, put_AutoDetectLinks)
    DetailViewPosition = property(get_DetailViewPosition, put_DetailViewPosition)
    SummaryViewPosition = property(get_SummaryViewPosition, put_SummaryViewPosition)
WalletItemKind = Int32
WalletItemKind_Invalid: WalletItemKind = 0
WalletItemKind_Deal: WalletItemKind = 1
WalletItemKind_General: WalletItemKind = 2
WalletItemKind_PaymentInstrument: WalletItemKind = 3
WalletItemKind_Ticket: WalletItemKind = 4
WalletItemKind_BoardingPass: WalletItemKind = 5
WalletItemKind_MembershipCard: WalletItemKind = 6
class WalletItemStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore
    _classid_ = 'Windows.ApplicationModel.Wallet.WalletItemStore'
    @winrt_mixinmethod
    def AddAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore, id: WinRT_String, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetWalletItemAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.WalletItem]: ...
    @winrt_mixinmethod
    def GetItemsAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Wallet.WalletItem]]: ...
    @winrt_mixinmethod
    def GetItemsWithKindAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore, kind: win32more.Windows.ApplicationModel.Wallet.WalletItemKind) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Wallet.WalletItem]]: ...
    @winrt_mixinmethod
    def ImportItemAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore, stream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.WalletItem]: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShowAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShowItemAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore, id: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UpdateAsync(self: win32more.Windows.ApplicationModel.Wallet.IWalletItemStore, item: win32more.Windows.ApplicationModel.Wallet.WalletItem) -> win32more.Windows.Foundation.IAsyncAction: ...
class WalletManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Wallet.WalletManager'
    @winrt_classmethod
    def RequestStoreAsync(cls: win32more.Windows.ApplicationModel.Wallet.IWalletManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Wallet.WalletItemStore]: ...
class WalletRelevantLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Wallet.IWalletRelevantLocation
    _classid_ = 'Windows.ApplicationModel.Wallet.WalletRelevantLocation'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.ApplicationModel.Wallet.WalletRelevantLocation.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Wallet.WalletRelevantLocation: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.ApplicationModel.Wallet.IWalletRelevantLocation) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def put_Position(self: win32more.Windows.ApplicationModel.Wallet.IWalletRelevantLocation, value: win32more.Windows.Devices.Geolocation.BasicGeoposition) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayMessage(self: win32more.Windows.ApplicationModel.Wallet.IWalletRelevantLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayMessage(self: win32more.Windows.ApplicationModel.Wallet.IWalletRelevantLocation, value: WinRT_String) -> Void: ...
    Position = property(get_Position, put_Position)
    DisplayMessage = property(get_DisplayMessage, put_DisplayMessage)
WalletSummaryViewPosition = Int32
WalletSummaryViewPosition_Hidden: WalletSummaryViewPosition = 0
WalletSummaryViewPosition_Field1: WalletSummaryViewPosition = 1
WalletSummaryViewPosition_Field2: WalletSummaryViewPosition = 2
class WalletTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction
    _classid_ = 'Windows.ApplicationModel.Wallet.WalletTransaction'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.ApplicationModel.Wallet.WalletTransaction.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Wallet.WalletTransaction: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayAmount(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayAmount(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IgnoreTimeOfDay(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnoreTimeOfDay(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayLocation(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayLocation(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TransactionDate(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_TransactionDate(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_IsLaunchable(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsLaunchable(self: win32more.Windows.ApplicationModel.Wallet.IWalletTransaction, value: Boolean) -> Void: ...
    Description = property(get_Description, put_Description)
    DisplayAmount = property(get_DisplayAmount, put_DisplayAmount)
    IgnoreTimeOfDay = property(get_IgnoreTimeOfDay, put_IgnoreTimeOfDay)
    DisplayLocation = property(get_DisplayLocation, put_DisplayLocation)
    TransactionDate = property(get_TransactionDate, put_TransactionDate)
    IsLaunchable = property(get_IsLaunchable, put_IsLaunchable)
class WalletVerb(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Wallet.IWalletVerb
    _classid_ = 'Windows.ApplicationModel.Wallet.WalletVerb'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.ApplicationModel.Wallet.WalletVerb.CreateWalletVerb(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWalletVerb(cls: win32more.Windows.ApplicationModel.Wallet.IWalletVerbFactory, name: WinRT_String) -> win32more.Windows.ApplicationModel.Wallet.WalletVerb: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.ApplicationModel.Wallet.IWalletVerb) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.ApplicationModel.Wallet.IWalletVerb, value: WinRT_String) -> Void: ...
    Name = property(get_Name, put_Name)


make_ready(__name__)
