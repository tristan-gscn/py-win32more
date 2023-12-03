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
import win32more.Windows.Devices.SmartCards
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Cryptography.Core
import win32more.Windows.Storage.Streams
class CardAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ICardAddedEventArgs
    _classid_ = 'Windows.Devices.SmartCards.CardAddedEventArgs'
    @winrt_mixinmethod
    def get_SmartCard(self: win32more.Windows.Devices.SmartCards.ICardAddedEventArgs) -> win32more.Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class CardRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ICardRemovedEventArgs
    _classid_ = 'Windows.Devices.SmartCards.CardRemovedEventArgs'
    @winrt_mixinmethod
    def get_SmartCard(self: win32more.Windows.Devices.SmartCards.ICardRemovedEventArgs) -> win32more.Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class ICardAddedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ICardAddedEventArgs'
    _iid_ = Guid('{18bbef98-f18b-4dd3-b118-dfb2c8e23cc6}')
    @winrt_commethod(6)
    def get_SmartCard(self) -> win32more.Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class ICardRemovedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ICardRemovedEventArgs'
    _iid_ = Guid('{15331aaf-22d7-4945-afc9-03b46f42a6cd}')
    @winrt_commethod(6)
    def get_SmartCard(self) -> win32more.Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class IKnownSmartCardAppletIds(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.IKnownSmartCardAppletIds'
    _iid_ = Guid('{7b04d8d8-95b4-4c88-8cea-411e55511efc}')
    @winrt_commethod(6)
    def get_PaymentSystemEnvironment(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_ProximityPaymentSystemEnvironment(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    PaymentSystemEnvironment = property(get_PaymentSystemEnvironment, None)
    ProximityPaymentSystemEnvironment = property(get_ProximityPaymentSystemEnvironment, None)
class ISmartCard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCard'
    _iid_ = Guid('{1b718871-6434-43f4-b55a-6a29623870aa}')
    @winrt_commethod(6)
    def get_Reader(self) -> win32more.Windows.Devices.SmartCards.SmartCardReader: ...
    @winrt_commethod(7)
    def GetStatusAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardStatus]: ...
    @winrt_commethod(8)
    def GetAnswerToResetAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    Reader = property(get_Reader, None)
class ISmartCardAppletIdGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAppletIdGroup'
    _iid_ = Guid('{7db165e6-6264-56f4-5e03-c86385395eb1}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AppletIds(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(9)
    def get_SmartCardEmulationCategory(self) -> win32more.Windows.Devices.SmartCards.SmartCardEmulationCategory: ...
    @winrt_commethod(10)
    def put_SmartCardEmulationCategory(self, value: win32more.Windows.Devices.SmartCards.SmartCardEmulationCategory) -> Void: ...
    @winrt_commethod(11)
    def get_SmartCardEmulationType(self) -> win32more.Windows.Devices.SmartCards.SmartCardEmulationType: ...
    @winrt_commethod(12)
    def put_SmartCardEmulationType(self, value: win32more.Windows.Devices.SmartCards.SmartCardEmulationType) -> Void: ...
    @winrt_commethod(13)
    def get_AutomaticEnablement(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_AutomaticEnablement(self, value: Boolean) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    AppletIds = property(get_AppletIds, None)
    SmartCardEmulationCategory = property(get_SmartCardEmulationCategory, put_SmartCardEmulationCategory)
    SmartCardEmulationType = property(get_SmartCardEmulationType, put_SmartCardEmulationType)
    AutomaticEnablement = property(get_AutomaticEnablement, put_AutomaticEnablement)
class ISmartCardAppletIdGroup2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAppletIdGroup2'
    _iid_ = Guid('{6b0ef9dc-9956-4a62-8d4e-d37a68ebc3a6}')
    @winrt_commethod(6)
    def get_Logo(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def put_Logo(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_commethod(11)
    def get_SecureUserAuthenticationRequired(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_SecureUserAuthenticationRequired(self, value: Boolean) -> Void: ...
    Logo = property(get_Logo, put_Logo)
    Description = property(get_Description, put_Description)
    Properties = property(get_Properties, None)
    SecureUserAuthenticationRequired = property(get_SecureUserAuthenticationRequired, put_SecureUserAuthenticationRequired)
class ISmartCardAppletIdGroupFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAppletIdGroupFactory'
    _iid_ = Guid('{9105eb4d-4a65-4e41-8061-cbe83f3695e5}')
    @winrt_commethod(6)
    def Create(self, displayName: WinRT_String, appletIds: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IBuffer], emulationCategory: win32more.Windows.Devices.SmartCards.SmartCardEmulationCategory, emulationType: win32more.Windows.Devices.SmartCards.SmartCardEmulationType) -> win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
class ISmartCardAppletIdGroupRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration'
    _iid_ = Guid('{df1208d1-31bb-5596-43b1-6d69a0257b3a}')
    @winrt_commethod(6)
    def get_ActivationPolicy(self) -> win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy: ...
    @winrt_commethod(7)
    def get_AppletIdGroup(self) -> win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
    @winrt_commethod(8)
    def RequestActivationPolicyChangeAsync(self, policy: win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardActivationPolicyChangeResult]: ...
    @winrt_commethod(9)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(10)
    def SetAutomaticResponseApdusAsync(self, apdus: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu]) -> win32more.Windows.Foundation.IAsyncAction: ...
    ActivationPolicy = property(get_ActivationPolicy, None)
    AppletIdGroup = property(get_AppletIdGroup, None)
    Id = property(get_Id, None)
class ISmartCardAppletIdGroupRegistration2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration2'
    _iid_ = Guid('{5f5508d8-98a7-4f2e-91d9-6cfcceda407f}')
    @winrt_commethod(6)
    def get_SmartCardReaderId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def SetPropertiesAsync(self, props: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncAction: ...
    SmartCardReaderId = property(get_SmartCardReaderId, None)
class ISmartCardAppletIdGroupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAppletIdGroupStatics'
    _iid_ = Guid('{ab2899a9-e76c-45cf-bf1d-90eaa6205927}')
    @winrt_commethod(6)
    def get_MaxAppletIds(self) -> UInt16: ...
    MaxAppletIds = property(get_MaxAppletIds, None)
class ISmartCardAutomaticResponseApdu(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu'
    _iid_ = Guid('{52152bab-c63e-4531-a857-d756d99b986a}')
    @winrt_commethod(6)
    def get_CommandApdu(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def put_CommandApdu(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(8)
    def get_CommandApduBitMask(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_CommandApduBitMask(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def get_ShouldMatchLength(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_ShouldMatchLength(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_AppletId(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(13)
    def put_AppletId(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(14)
    def get_ResponseApdu(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(15)
    def put_ResponseApdu(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    CommandApdu = property(get_CommandApdu, put_CommandApdu)
    CommandApduBitMask = property(get_CommandApduBitMask, put_CommandApduBitMask)
    ShouldMatchLength = property(get_ShouldMatchLength, put_ShouldMatchLength)
    AppletId = property(get_AppletId, put_AppletId)
    ResponseApdu = property(get_ResponseApdu, put_ResponseApdu)
class ISmartCardAutomaticResponseApdu2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu2'
    _iid_ = Guid('{44aebb14-559d-4531-4e51-89db6fa8a57a}')
    @winrt_commethod(6)
    def get_InputState(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def put_InputState(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(8)
    def get_OutputState(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def put_OutputState(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    InputState = property(get_InputState, put_InputState)
    OutputState = property(get_OutputState, put_OutputState)
class ISmartCardAutomaticResponseApdu3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu3'
    _iid_ = Guid('{bf43da74-6576-4392-9367-fe3bc9e2d496}')
    @winrt_commethod(6)
    def get_AllowWhenCryptogramGeneratorNotPrepared(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowWhenCryptogramGeneratorNotPrepared(self, value: Boolean) -> Void: ...
    AllowWhenCryptogramGeneratorNotPrepared = property(get_AllowWhenCryptogramGeneratorNotPrepared, put_AllowWhenCryptogramGeneratorNotPrepared)
class ISmartCardAutomaticResponseApduFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardAutomaticResponseApduFactory'
    _iid_ = Guid('{e97ea2fa-d02c-4c55-b02a-8cff7fa9f05b}')
    @winrt_commethod(6)
    def Create(self, commandApdu: win32more.Windows.Storage.Streams.IBuffer, responseApdu: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu: ...
class ISmartCardChallengeContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardChallengeContext'
    _iid_ = Guid('{192a5319-c9c4-4947-81cc-44794a61ef91}')
    @winrt_commethod(6)
    def get_Challenge(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def VerifyResponseAsync(self, response: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def ProvisionAsync(self, response: win32more.Windows.Storage.Streams.IBuffer, formatCard: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ProvisionAsyncWithNewCardId(self, response: win32more.Windows.Storage.Streams.IBuffer, formatCard: Boolean, newCardId: Guid) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ChangeAdministrativeKeyAsync(self, response: win32more.Windows.Storage.Streams.IBuffer, newAdministrativeKey: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    Challenge = property(get_Challenge, None)
class ISmartCardConnect(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardConnect'
    _iid_ = Guid('{2fdf87e5-028d-491e-a058-3382c3986f40}')
    @winrt_commethod(6)
    def ConnectAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardConnection]: ...
class ISmartCardConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardConnection'
    _iid_ = Guid('{7edb991a-a81a-47bc-a649-156be6b7f231}')
    @winrt_commethod(6)
    def TransmitAsync(self, command: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
class ISmartCardCryptogramGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramGenerator'
    _iid_ = Guid('{e39f587b-edd3-4e49-b594-0ff5e4d0c76f}')
    @winrt_commethod(6)
    def get_SupportedCryptogramMaterialTypes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialType]: ...
    @winrt_commethod(7)
    def get_SupportedCryptogramAlgorithms(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_commethod(8)
    def get_SupportedCryptogramMaterialPackageFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat]: ...
    @winrt_commethod(9)
    def get_SupportedCryptogramMaterialPackageConfirmationResponseFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]: ...
    @winrt_commethod(10)
    def get_SupportedSmartCardCryptogramStorageKeyCapabilities(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities]: ...
    @winrt_commethod(11)
    def DeleteCryptogramMaterialStorageKeyAsync(self, storageKeyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(12)
    def CreateCryptogramMaterialStorageKeyAsync(self, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, storageKeyName: WinRT_String, algorithm: win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm, capabilities: win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(13)
    def RequestCryptogramMaterialStorageKeyInfoAsync(self, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, storageKeyName: WinRT_String, format: win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyInfo]: ...
    @winrt_commethod(14)
    def ImportCryptogramMaterialPackageAsync(self, format: win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat, storageKeyName: WinRT_String, materialPackageName: WinRT_String, cryptogramMaterialPackage: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(15)
    def TryProvePossessionOfCryptogramMaterialPackageAsync(self, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, responseFormat: win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat, materialPackageName: WinRT_String, materialName: WinRT_String, challenge: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPossessionProof]: ...
    @winrt_commethod(16)
    def RequestUnlockCryptogramMaterialForUseAsync(self, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(17)
    def DeleteCryptogramMaterialPackageAsync(self, materialPackageName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    SupportedCryptogramMaterialTypes = property(get_SupportedCryptogramMaterialTypes, None)
    SupportedCryptogramAlgorithms = property(get_SupportedCryptogramAlgorithms, None)
    SupportedCryptogramMaterialPackageFormats = property(get_SupportedCryptogramMaterialPackageFormats, None)
    SupportedCryptogramMaterialPackageConfirmationResponseFormats = property(get_SupportedCryptogramMaterialPackageConfirmationResponseFormats, None)
    SupportedSmartCardCryptogramStorageKeyCapabilities = property(get_SupportedSmartCardCryptogramStorageKeyCapabilities, None)
class ISmartCardCryptogramGenerator2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2'
    _iid_ = Guid('{7116aa34-5d6d-4b4a-96a3-efa47d2a7e25}')
    @winrt_commethod(6)
    def ValidateRequestApduAsync(self, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, apduToValidate: win32more.Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(7)
    def GetAllCryptogramStorageKeyCharacteristicsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult]: ...
    @winrt_commethod(8)
    def GetAllCryptogramMaterialPackageCharacteristicsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]: ...
    @winrt_commethod(9)
    def GetAllCryptogramMaterialPackageCharacteristicsWithStorageKeyAsync(self, storageKeyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]: ...
    @winrt_commethod(10)
    def GetAllCryptogramMaterialCharacteristicsAsync(self, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, materialPackageName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult]: ...
class ISmartCardCryptogramGeneratorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramGeneratorStatics'
    _iid_ = Guid('{09933910-cb9c-4015-967d-5234f3b02900}')
    @winrt_commethod(6)
    def GetSmartCardCryptogramGeneratorAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGenerator]: ...
class ISmartCardCryptogramGeneratorStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramGeneratorStatics2'
    _iid_ = Guid('{09bdf5e5-b4bd-4e23-a588-74469204c128}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult'
    _iid_ = Guid('{2798e029-d687-4c92-86c6-399e9a0ecb09}')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_Characteristics(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult'
    _iid_ = Guid('{4e6a8a5c-9773-46c4-a32f-b1e543159e04}')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_Characteristics(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult'
    _iid_ = Guid('{8c7ce857-a7e7-489d-b9d6-368061515012}')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_Characteristics(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class ISmartCardCryptogramMaterialCharacteristics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics'
    _iid_ = Guid('{fc9ac5cc-c1d7-4153-923b-a2d43c6c8d49}')
    @winrt_commethod(6)
    def get_MaterialName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AllowedAlgorithms(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_commethod(8)
    def get_AllowedProofOfPossessionAlgorithms(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]: ...
    @winrt_commethod(9)
    def get_AllowedValidations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_commethod(10)
    def get_MaterialType(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialType: ...
    @winrt_commethod(11)
    def get_ProtectionMethod(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialProtectionMethod: ...
    @winrt_commethod(12)
    def get_ProtectionVersion(self) -> Int32: ...
    @winrt_commethod(13)
    def get_MaterialLength(self) -> Int32: ...
    MaterialName = property(get_MaterialName, None)
    AllowedAlgorithms = property(get_AllowedAlgorithms, None)
    AllowedProofOfPossessionAlgorithms = property(get_AllowedProofOfPossessionAlgorithms, None)
    AllowedValidations = property(get_AllowedValidations, None)
    MaterialType = property(get_MaterialType, None)
    ProtectionMethod = property(get_ProtectionMethod, None)
    ProtectionVersion = property(get_ProtectionVersion, None)
    MaterialLength = property(get_MaterialLength, None)
class ISmartCardCryptogramMaterialPackageCharacteristics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics'
    _iid_ = Guid('{ffb58e1f-0692-4c47-93cf-34d91f9dcd00}')
    @winrt_commethod(6)
    def get_PackageName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_StorageKeyName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DateImported(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_PackageFormat(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat: ...
    PackageName = property(get_PackageName, None)
    StorageKeyName = property(get_StorageKeyName, None)
    DateImported = property(get_DateImported, None)
    PackageFormat = property(get_PackageFormat, None)
class ISmartCardCryptogramMaterialPossessionProof(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPossessionProof'
    _iid_ = Guid('{e5b9ab8c-a141-4135-9add-b0d2e3aa1fc9}')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_Proof(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    OperationStatus = property(get_OperationStatus, None)
    Proof = property(get_Proof, None)
class ISmartCardCryptogramPlacementStep(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep'
    _iid_ = Guid('{947b03eb-8342-4792-a2e5-925636378a53}')
    @winrt_commethod(6)
    def get_Algorithm(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm: ...
    @winrt_commethod(7)
    def put_Algorithm(self, value: win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm) -> Void: ...
    @winrt_commethod(8)
    def get_SourceData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_SourceData(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(10)
    def get_CryptogramMaterialPackageName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_CryptogramMaterialPackageName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_CryptogramMaterialName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_CryptogramMaterialName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_TemplateOffset(self) -> Int32: ...
    @winrt_commethod(15)
    def put_TemplateOffset(self, value: Int32) -> Void: ...
    @winrt_commethod(16)
    def get_CryptogramOffset(self) -> Int32: ...
    @winrt_commethod(17)
    def put_CryptogramOffset(self, value: Int32) -> Void: ...
    @winrt_commethod(18)
    def get_CryptogramLength(self) -> Int32: ...
    @winrt_commethod(19)
    def put_CryptogramLength(self, value: Int32) -> Void: ...
    @winrt_commethod(20)
    def get_CryptogramPlacementOptions(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions: ...
    @winrt_commethod(21)
    def put_CryptogramPlacementOptions(self, value: win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions) -> Void: ...
    @winrt_commethod(22)
    def get_ChainedOutputStep(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep: ...
    @winrt_commethod(23)
    def put_ChainedOutputStep(self, value: win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep) -> Void: ...
    Algorithm = property(get_Algorithm, put_Algorithm)
    SourceData = property(get_SourceData, put_SourceData)
    CryptogramMaterialPackageName = property(get_CryptogramMaterialPackageName, put_CryptogramMaterialPackageName)
    CryptogramMaterialName = property(get_CryptogramMaterialName, put_CryptogramMaterialName)
    TemplateOffset = property(get_TemplateOffset, put_TemplateOffset)
    CryptogramOffset = property(get_CryptogramOffset, put_CryptogramOffset)
    CryptogramLength = property(get_CryptogramLength, put_CryptogramLength)
    CryptogramPlacementOptions = property(get_CryptogramPlacementOptions, put_CryptogramPlacementOptions)
    ChainedOutputStep = property(get_ChainedOutputStep, put_ChainedOutputStep)
class ISmartCardCryptogramStorageKeyCharacteristics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics'
    _iid_ = Guid('{8552546e-4457-4825-b464-635471a39f5c}')
    @winrt_commethod(6)
    def get_StorageKeyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DateCreated(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_Algorithm(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm: ...
    @winrt_commethod(9)
    def get_Capabilities(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities: ...
    StorageKeyName = property(get_StorageKeyName, None)
    DateCreated = property(get_DateCreated, None)
    Algorithm = property(get_Algorithm, None)
    Capabilities = property(get_Capabilities, None)
class ISmartCardCryptogramStorageKeyInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo'
    _iid_ = Guid('{77b0f00d-b097-4f61-a26a-9561639c9c3a}')
    @winrt_commethod(6)
    def get_OperationStatus(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_commethod(7)
    def get_PublicKeyBlobType(self) -> win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType: ...
    @winrt_commethod(8)
    def get_PublicKey(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def get_AttestationStatus(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptographicKeyAttestationStatus: ...
    @winrt_commethod(10)
    def get_Attestation(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def get_AttestationCertificateChain(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def get_Capabilities(self) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities: ...
    OperationStatus = property(get_OperationStatus, None)
    PublicKeyBlobType = property(get_PublicKeyBlobType, None)
    PublicKey = property(get_PublicKey, None)
    AttestationStatus = property(get_AttestationStatus, None)
    Attestation = property(get_Attestation, None)
    AttestationCertificateChain = property(get_AttestationCertificateChain, None)
    Capabilities = property(get_Capabilities, None)
class ISmartCardCryptogramStorageKeyInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo2'
    _iid_ = Guid('{000440f9-f7fd-417d-89e1-fbb0382adc4d}')
    @winrt_commethod(6)
    def get_OperationalRequirements(self) -> WinRT_String: ...
    OperationalRequirements = property(get_OperationalRequirements, None)
class ISmartCardEmulator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulator'
    _iid_ = Guid('{dfb906b2-875e-47e5-8077-e8bff1b1c6fb}')
    @winrt_commethod(6)
    def get_EnablementPolicy(self) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorEnablementPolicy: ...
    EnablementPolicy = property(get_EnablementPolicy, None)
class ISmartCardEmulator2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulator2'
    _iid_ = Guid('{fe3fc0b8-8529-411a-807b-48edc2a0ab44}')
    @winrt_commethod(6)
    def add_ApduReceived(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SmartCards.SmartCardEmulator, win32more.Windows.Devices.SmartCards.SmartCardEmulatorApduReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ApduReceived(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ConnectionDeactivated(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SmartCards.SmartCardEmulator, win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ConnectionDeactivated(self, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def Start(self) -> Void: ...
    @winrt_commethod(11)
    def IsHostCardEmulationSupported(self) -> Boolean: ...
class ISmartCardEmulatorApduReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs'
    _iid_ = Guid('{d55d1576-69d2-5333-5b5f-f8c0d6e9f09f}')
    @winrt_commethod(6)
    def get_CommandApdu(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_ConnectionProperties(self) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties: ...
    @winrt_commethod(8)
    def TryRespondAsync(self, responseApdu: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def get_AutomaticResponseStatus(self) -> win32more.Windows.Devices.SmartCards.SmartCardAutomaticResponseStatus: ...
    CommandApdu = property(get_CommandApdu, None)
    ConnectionProperties = property(get_ConnectionProperties, None)
    AutomaticResponseStatus = property(get_AutomaticResponseStatus, None)
class ISmartCardEmulatorApduReceivedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs2'
    _iid_ = Guid('{8bf93df0-22e1-4238-8610-94ce4a965425}')
    @winrt_commethod(6)
    def get_State(self) -> UInt32: ...
    @winrt_commethod(7)
    def TryRespondWithStateAsync(self, responseApdu: win32more.Windows.Storage.Streams.IBuffer, nextState: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    State = property(get_State, None)
class ISmartCardEmulatorApduReceivedEventArgsWithCryptograms(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgsWithCryptograms'
    _iid_ = Guid('{d550bac7-b7bf-4e29-9294-0c4ac3c941bd}')
    @winrt_commethod(6)
    def TryRespondWithCryptogramsAsync(self, responseTemplate: win32more.Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_commethod(7)
    def TryRespondWithCryptogramsAndStateAsync(self, responseTemplate: win32more.Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep], nextState: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
class ISmartCardEmulatorConnectionDeactivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulatorConnectionDeactivatedEventArgs'
    _iid_ = Guid('{2186d8d3-c5eb-5262-43df-62a0a1b55557}')
    @winrt_commethod(6)
    def get_ConnectionProperties(self) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties: ...
    @winrt_commethod(7)
    def get_Reason(self) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedReason: ...
    ConnectionProperties = property(get_ConnectionProperties, None)
    Reason = property(get_Reason, None)
class ISmartCardEmulatorConnectionProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulatorConnectionProperties'
    _iid_ = Guid('{4e2ca5ee-f969-507d-6cf9-34e2d18df311}')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_Source(self) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionSource: ...
    Id = property(get_Id, None)
    Source = property(get_Source, None)
class ISmartCardEmulatorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulatorStatics'
    _iid_ = Guid('{7a9bfc4b-c4d3-494f-b8a2-6215d81e85b2}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardEmulator]: ...
class ISmartCardEmulatorStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulatorStatics2'
    _iid_ = Guid('{69ae9f8a-b775-488b-8436-6c1e28ed731f}')
    @winrt_commethod(6)
    def GetAppletIdGroupRegistrationsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration]]: ...
    @winrt_commethod(7)
    def RegisterAppletIdGroupAsync(self, appletIdGroup: win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroup) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration]: ...
    @winrt_commethod(8)
    def UnregisterAppletIdGroupAsync(self, registration: win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def get_MaxAppletIdGroupRegistrations(self) -> UInt16: ...
    MaxAppletIdGroupRegistrations = property(get_MaxAppletIdGroupRegistrations, None)
class ISmartCardEmulatorStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardEmulatorStatics3'
    _iid_ = Guid('{59ea142a-9f09-43f5-8565-cfa8148e4cb2}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class ISmartCardPinPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardPinPolicy'
    _iid_ = Guid('{183ce184-4db6-4841-ac9e-2ac1f39b7304}')
    @winrt_commethod(6)
    def get_MinLength(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_MinLength(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_MaxLength(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_MaxLength(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_UppercaseLetters(self) -> win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_commethod(11)
    def put_UppercaseLetters(self, value: win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_commethod(12)
    def get_LowercaseLetters(self) -> win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_commethod(13)
    def put_LowercaseLetters(self, value: win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_commethod(14)
    def get_Digits(self) -> win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_commethod(15)
    def put_Digits(self, value: win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_commethod(16)
    def get_SpecialCharacters(self) -> win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_commethod(17)
    def put_SpecialCharacters(self, value: win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    MinLength = property(get_MinLength, put_MinLength)
    MaxLength = property(get_MaxLength, put_MaxLength)
    UppercaseLetters = property(get_UppercaseLetters, put_UppercaseLetters)
    LowercaseLetters = property(get_LowercaseLetters, put_LowercaseLetters)
    Digits = property(get_Digits, put_Digits)
    SpecialCharacters = property(get_SpecialCharacters, put_SpecialCharacters)
class ISmartCardPinResetDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardPinResetDeferral'
    _iid_ = Guid('{18c94aac-7805-4004-85e4-bbefac8f6884}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class ISmartCardPinResetRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardPinResetRequest'
    _iid_ = Guid('{12fe3c4d-5fb9-4e8e-9ff6-61f475124fef}')
    @winrt_commethod(6)
    def get_Challenge(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Deadline(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Devices.SmartCards.SmartCardPinResetDeferral: ...
    @winrt_commethod(9)
    def SetResponse(self, response: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    Challenge = property(get_Challenge, None)
    Deadline = property(get_Deadline, None)
class ISmartCardProvisioning(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardProvisioning'
    _iid_ = Guid('{19eeedbd-1fab-477c-b712-1a2c5af1fd6e}')
    @winrt_commethod(6)
    def get_SmartCard(self) -> win32more.Windows.Devices.SmartCards.SmartCard: ...
    @winrt_commethod(7)
    def GetIdAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Guid]: ...
    @winrt_commethod(8)
    def GetNameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(9)
    def GetChallengeContextAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardChallengeContext]: ...
    @winrt_commethod(10)
    def RequestPinChangeAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def RequestPinResetAsync(self, handler: win32more.Windows.Devices.SmartCards.SmartCardPinResetHandler) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    SmartCard = property(get_SmartCard, None)
class ISmartCardProvisioning2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardProvisioning2'
    _iid_ = Guid('{10fd28eb-3f79-4b66-9b7c-11c149b7d0bc}')
    @winrt_commethod(6)
    def GetAuthorityKeyContainerNameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
class ISmartCardProvisioningStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardProvisioningStatics'
    _iid_ = Guid('{13882848-0d13-4e70-9735-51daeca5254f}')
    @winrt_commethod(6)
    def FromSmartCardAsync(self, card: win32more.Windows.Devices.SmartCards.SmartCard) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_commethod(7)
    def RequestVirtualSmartCardCreationAsync(self, friendlyName: WinRT_String, administrativeKey: win32more.Windows.Storage.Streams.IBuffer, pinPolicy: win32more.Windows.Devices.SmartCards.SmartCardPinPolicy) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_commethod(8)
    def RequestVirtualSmartCardCreationAsyncWithCardId(self, friendlyName: WinRT_String, administrativeKey: win32more.Windows.Storage.Streams.IBuffer, pinPolicy: win32more.Windows.Devices.SmartCards.SmartCardPinPolicy, cardId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_commethod(9)
    def RequestVirtualSmartCardDeletionAsync(self, card: win32more.Windows.Devices.SmartCards.SmartCard) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ISmartCardProvisioningStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardProvisioningStatics2'
    _iid_ = Guid('{3447c6a8-c9a0-4bd6-b50d-251f4e8d3a62}')
    @winrt_commethod(6)
    def RequestAttestedVirtualSmartCardCreationAsync(self, friendlyName: WinRT_String, administrativeKey: win32more.Windows.Storage.Streams.IBuffer, pinPolicy: win32more.Windows.Devices.SmartCards.SmartCardPinPolicy) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_commethod(7)
    def RequestAttestedVirtualSmartCardCreationAsyncWithCardId(self, friendlyName: WinRT_String, administrativeKey: win32more.Windows.Storage.Streams.IBuffer, pinPolicy: win32more.Windows.Devices.SmartCards.SmartCardPinPolicy, cardId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
class ISmartCardReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardReader'
    _iid_ = Guid('{1074b4e0-54c2-4df0-817a-14c14378f06c}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Kind(self) -> win32more.Windows.Devices.SmartCards.SmartCardReaderKind: ...
    @winrt_commethod(9)
    def GetStatusAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardReaderStatus]: ...
    @winrt_commethod(10)
    def FindAllCardsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCard]]: ...
    @winrt_commethod(11)
    def add_CardAdded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SmartCards.SmartCardReader, win32more.Windows.Devices.SmartCards.CardAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_CardAdded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_CardRemoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SmartCards.SmartCardReader, win32more.Windows.Devices.SmartCards.CardRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_CardRemoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    Name = property(get_Name, None)
    Kind = property(get_Kind, None)
class ISmartCardReaderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardReaderStatics'
    _iid_ = Guid('{103c04e1-a1ca-48f2-a281-5b6f669af107}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorWithKind(self, kind: win32more.Windows.Devices.SmartCards.SmartCardReaderKind) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardReader]: ...
class ISmartCardTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardTriggerDetails'
    _iid_ = Guid('{5f9bf11e-39ef-4f2b-b44f-0a9155b177bc}')
    @winrt_commethod(6)
    def get_TriggerType(self) -> win32more.Windows.Devices.SmartCards.SmartCardTriggerType: ...
    @winrt_commethod(7)
    def get_SourceAppletId(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_TriggerData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    TriggerType = property(get_TriggerType, None)
    SourceAppletId = property(get_SourceAppletId, None)
    TriggerData = property(get_TriggerData, None)
class ISmartCardTriggerDetails2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardTriggerDetails2'
    _iid_ = Guid('{2945c569-8975-4a51-9e1a-5f8a76ee51af}')
    @winrt_commethod(6)
    def get_Emulator(self) -> win32more.Windows.Devices.SmartCards.SmartCardEmulator: ...
    @winrt_commethod(7)
    def TryLaunchCurrentAppAsync(self, arguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryLaunchCurrentAppWithBehaviorAsync(self, arguments: WinRT_String, behavior: win32more.Windows.Devices.SmartCards.SmartCardLaunchBehavior) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    Emulator = property(get_Emulator, None)
class ISmartCardTriggerDetails3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.ISmartCardTriggerDetails3'
    _iid_ = Guid('{b3e2c27d-18c6-4ba8-8376-ef03d4912666}')
    @winrt_commethod(6)
    def get_SmartCard(self) -> win32more.Windows.Devices.SmartCards.SmartCard: ...
    SmartCard = property(get_SmartCard, None)
class _KnownSmartCardAppletIds_Meta_(ComPtr.__class__):
    pass
class KnownSmartCardAppletIds(ComPtr, metaclass=_KnownSmartCardAppletIds_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SmartCards.KnownSmartCardAppletIds'
    @winrt_classmethod
    def get_PaymentSystemEnvironment(cls: win32more.Windows.Devices.SmartCards.IKnownSmartCardAppletIds) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def get_ProximityPaymentSystemEnvironment(cls: win32more.Windows.Devices.SmartCards.IKnownSmartCardAppletIds) -> win32more.Windows.Storage.Streams.IBuffer: ...
    _KnownSmartCardAppletIds_Meta_.PaymentSystemEnvironment = property(get_PaymentSystemEnvironment.__wrapped__, None)
    _KnownSmartCardAppletIds_Meta_.ProximityPaymentSystemEnvironment = property(get_ProximityPaymentSystemEnvironment.__wrapped__, None)
class SmartCard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCard
    _classid_ = 'Windows.Devices.SmartCards.SmartCard'
    @winrt_mixinmethod
    def get_Reader(self: win32more.Windows.Devices.SmartCards.ISmartCard) -> win32more.Windows.Devices.SmartCards.SmartCardReader: ...
    @winrt_mixinmethod
    def GetStatusAsync(self: win32more.Windows.Devices.SmartCards.ISmartCard) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardStatus]: ...
    @winrt_mixinmethod
    def GetAnswerToResetAsync(self: win32more.Windows.Devices.SmartCards.ISmartCard) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def ConnectAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardConnect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardConnection]: ...
    Reader = property(get_Reader, None)
SmartCardActivationPolicyChangeResult = Int32
SmartCardActivationPolicyChangeResult_Denied: SmartCardActivationPolicyChangeResult = 0
SmartCardActivationPolicyChangeResult_Allowed: SmartCardActivationPolicyChangeResult = 1
class _SmartCardAppletIdGroup_Meta_(ComPtr.__class__):
    pass
class SmartCardAppletIdGroup(ComPtr, metaclass=_SmartCardAppletIdGroup_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup
    _classid_ = 'Windows.Devices.SmartCards.SmartCardAppletIdGroup'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupFactory, displayName: WinRT_String, appletIds: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IBuffer], emulationCategory: win32more.Windows.Devices.SmartCards.SmartCardEmulationCategory, emulationType: win32more.Windows.Devices.SmartCards.SmartCardEmulationType) -> win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AppletIds(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def get_SmartCardEmulationCategory(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> win32more.Windows.Devices.SmartCards.SmartCardEmulationCategory: ...
    @winrt_mixinmethod
    def put_SmartCardEmulationCategory(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup, value: win32more.Windows.Devices.SmartCards.SmartCardEmulationCategory) -> Void: ...
    @winrt_mixinmethod
    def get_SmartCardEmulationType(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> win32more.Windows.Devices.SmartCards.SmartCardEmulationType: ...
    @winrt_mixinmethod
    def put_SmartCardEmulationType(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup, value: win32more.Windows.Devices.SmartCards.SmartCardEmulationType) -> Void: ...
    @winrt_mixinmethod
    def get_AutomaticEnablement(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutomaticEnablement(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Logo(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup2) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Logo(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup2, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup2) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_SecureUserAuthenticationRequired(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup2) -> Boolean: ...
    @winrt_mixinmethod
    def put_SecureUserAuthenticationRequired(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroup2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_MaxAppletIds(cls: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupStatics) -> UInt16: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    AppletIds = property(get_AppletIds, None)
    SmartCardEmulationCategory = property(get_SmartCardEmulationCategory, put_SmartCardEmulationCategory)
    SmartCardEmulationType = property(get_SmartCardEmulationType, put_SmartCardEmulationType)
    AutomaticEnablement = property(get_AutomaticEnablement, put_AutomaticEnablement)
    Logo = property(get_Logo, put_Logo)
    Description = property(get_Description, put_Description)
    Properties = property(get_Properties, None)
    SecureUserAuthenticationRequired = property(get_SecureUserAuthenticationRequired, put_SecureUserAuthenticationRequired)
    _SmartCardAppletIdGroup_Meta_.MaxAppletIds = property(get_MaxAppletIds.__wrapped__, None)
SmartCardAppletIdGroupActivationPolicy = Int32
SmartCardAppletIdGroupActivationPolicy_Disabled: SmartCardAppletIdGroupActivationPolicy = 0
SmartCardAppletIdGroupActivationPolicy_ForegroundOverride: SmartCardAppletIdGroupActivationPolicy = 1
SmartCardAppletIdGroupActivationPolicy_Enabled: SmartCardAppletIdGroupActivationPolicy = 2
class SmartCardAppletIdGroupRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration
    _classid_ = 'Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration'
    @winrt_mixinmethod
    def get_ActivationPolicy(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration) -> win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy: ...
    @winrt_mixinmethod
    def get_AppletIdGroup(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration) -> win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroup: ...
    @winrt_mixinmethod
    def RequestActivationPolicyChangeAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration, policy: win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupActivationPolicy) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardActivationPolicyChangeResult]: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration) -> Guid: ...
    @winrt_mixinmethod
    def SetAutomaticResponseApdusAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration, apdus: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_SmartCardReaderId(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration2) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetPropertiesAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardAppletIdGroupRegistration2, props: win32more.Windows.Foundation.Collections.ValueSet) -> win32more.Windows.Foundation.IAsyncAction: ...
    ActivationPolicy = property(get_ActivationPolicy, None)
    AppletIdGroup = property(get_AppletIdGroup, None)
    Id = property(get_Id, None)
    SmartCardReaderId = property(get_SmartCardReaderId, None)
class SmartCardAutomaticResponseApdu(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu
    _classid_ = 'Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu'
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApduFactory, commandApdu: win32more.Windows.Storage.Streams.IBuffer, responseApdu: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.SmartCards.SmartCardAutomaticResponseApdu: ...
    @winrt_mixinmethod
    def get_CommandApdu(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_CommandApdu(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_CommandApduBitMask(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_CommandApduBitMask(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldMatchLength(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldMatchLength(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AppletId(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_AppletId(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_ResponseApdu(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_ResponseApdu(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_InputState(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu2) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_InputState(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu2, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_OutputState(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu2) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_OutputState(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu2, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_AllowWhenCryptogramGeneratorNotPrepared(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu3) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowWhenCryptogramGeneratorNotPrepared(self: win32more.Windows.Devices.SmartCards.ISmartCardAutomaticResponseApdu3, value: Boolean) -> Void: ...
    CommandApdu = property(get_CommandApdu, put_CommandApdu)
    CommandApduBitMask = property(get_CommandApduBitMask, put_CommandApduBitMask)
    ShouldMatchLength = property(get_ShouldMatchLength, put_ShouldMatchLength)
    AppletId = property(get_AppletId, put_AppletId)
    ResponseApdu = property(get_ResponseApdu, put_ResponseApdu)
    InputState = property(get_InputState, put_InputState)
    OutputState = property(get_OutputState, put_OutputState)
    AllowWhenCryptogramGeneratorNotPrepared = property(get_AllowWhenCryptogramGeneratorNotPrepared, put_AllowWhenCryptogramGeneratorNotPrepared)
SmartCardAutomaticResponseStatus = Int32
SmartCardAutomaticResponseStatus_None: SmartCardAutomaticResponseStatus = 0
SmartCardAutomaticResponseStatus_Success: SmartCardAutomaticResponseStatus = 1
SmartCardAutomaticResponseStatus_UnknownError: SmartCardAutomaticResponseStatus = 2
SmartCardBackgroundTriggerContract: UInt32 = 196608
class SmartCardChallengeContext(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardChallengeContext
    _classid_ = 'Windows.Devices.SmartCards.SmartCardChallengeContext'
    @winrt_mixinmethod
    def get_Challenge(self: win32more.Windows.Devices.SmartCards.ISmartCardChallengeContext) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def VerifyResponseAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardChallengeContext, response: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def ProvisionAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardChallengeContext, response: win32more.Windows.Storage.Streams.IBuffer, formatCard: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ProvisionAsyncWithNewCardId(self: win32more.Windows.Devices.SmartCards.ISmartCardChallengeContext, response: win32more.Windows.Storage.Streams.IBuffer, formatCard: Boolean, newCardId: Guid) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ChangeAdministrativeKeyAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardChallengeContext, response: win32more.Windows.Storage.Streams.IBuffer, newAdministrativeKey: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Challenge = property(get_Challenge, None)
class SmartCardConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardConnection
    _classid_ = 'Windows.Devices.SmartCards.SmartCardConnection'
    @winrt_mixinmethod
    def TransmitAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardConnection, command: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
SmartCardCryptogramAlgorithm = Int32
SmartCardCryptogramAlgorithm_None: SmartCardCryptogramAlgorithm = 0
SmartCardCryptogramAlgorithm_CbcMac: SmartCardCryptogramAlgorithm = 1
SmartCardCryptogramAlgorithm_Cvc3Umd: SmartCardCryptogramAlgorithm = 2
SmartCardCryptogramAlgorithm_DecimalizedMsd: SmartCardCryptogramAlgorithm = 3
SmartCardCryptogramAlgorithm_Cvc3MD: SmartCardCryptogramAlgorithm = 4
SmartCardCryptogramAlgorithm_Sha1: SmartCardCryptogramAlgorithm = 5
SmartCardCryptogramAlgorithm_SignedDynamicApplicationData: SmartCardCryptogramAlgorithm = 6
SmartCardCryptogramAlgorithm_RsaPkcs1: SmartCardCryptogramAlgorithm = 7
SmartCardCryptogramAlgorithm_Sha256Hmac: SmartCardCryptogramAlgorithm = 8
class SmartCardCryptogramGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramGenerator'
    @winrt_mixinmethod
    def get_SupportedCryptogramMaterialTypes(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialType]: ...
    @winrt_mixinmethod
    def get_SupportedCryptogramAlgorithms(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_mixinmethod
    def get_SupportedCryptogramMaterialPackageFormats(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat]: ...
    @winrt_mixinmethod
    def get_SupportedCryptogramMaterialPackageConfirmationResponseFormats(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]: ...
    @winrt_mixinmethod
    def get_SupportedSmartCardCryptogramStorageKeyCapabilities(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities]: ...
    @winrt_mixinmethod
    def DeleteCryptogramMaterialStorageKeyAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, storageKeyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def CreateCryptogramMaterialStorageKeyAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, storageKeyName: WinRT_String, algorithm: win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm, capabilities: win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def RequestCryptogramMaterialStorageKeyInfoAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, storageKeyName: WinRT_String, format: win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyInfo]: ...
    @winrt_mixinmethod
    def ImportCryptogramMaterialPackageAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, format: win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat, storageKeyName: WinRT_String, materialPackageName: WinRT_String, cryptogramMaterialPackage: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def TryProvePossessionOfCryptogramMaterialPackageAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, responseFormat: win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat, materialPackageName: WinRT_String, materialName: WinRT_String, challenge: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPossessionProof]: ...
    @winrt_mixinmethod
    def RequestUnlockCryptogramMaterialForUseAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def DeleteCryptogramMaterialPackageAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator, materialPackageName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def ValidateRequestApduAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, apduToValidate: win32more.Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def GetAllCryptogramStorageKeyCharacteristicsAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetAllCryptogramMaterialPackageCharacteristicsAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetAllCryptogramMaterialPackageCharacteristicsWithStorageKeyAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2, storageKeyName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetAllCryptogramMaterialCharacteristicsAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGenerator2, promptingBehavior: win32more.Windows.Devices.SmartCards.SmartCardUnlockPromptingBehavior, materialPackageName: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult]: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGeneratorStatics2) -> Boolean: ...
    @winrt_classmethod
    def GetSmartCardCryptogramGeneratorAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGeneratorStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGenerator]: ...
    SupportedCryptogramMaterialTypes = property(get_SupportedCryptogramMaterialTypes, None)
    SupportedCryptogramAlgorithms = property(get_SupportedCryptogramAlgorithms, None)
    SupportedCryptogramMaterialPackageFormats = property(get_SupportedCryptogramMaterialPackageFormats, None)
    SupportedCryptogramMaterialPackageConfirmationResponseFormats = property(get_SupportedCryptogramMaterialPackageConfirmationResponseFormats, None)
    SupportedSmartCardCryptogramStorageKeyCapabilities = property(get_SupportedSmartCardCryptogramStorageKeyCapabilities, None)
SmartCardCryptogramGeneratorOperationStatus = Int32
SmartCardCryptogramGeneratorOperationStatus_Success: SmartCardCryptogramGeneratorOperationStatus = 0
SmartCardCryptogramGeneratorOperationStatus_AuthorizationFailed: SmartCardCryptogramGeneratorOperationStatus = 1
SmartCardCryptogramGeneratorOperationStatus_AuthorizationCanceled: SmartCardCryptogramGeneratorOperationStatus = 2
SmartCardCryptogramGeneratorOperationStatus_AuthorizationRequired: SmartCardCryptogramGeneratorOperationStatus = 3
SmartCardCryptogramGeneratorOperationStatus_CryptogramMaterialPackageStorageKeyExists: SmartCardCryptogramGeneratorOperationStatus = 4
SmartCardCryptogramGeneratorOperationStatus_NoCryptogramMaterialPackageStorageKey: SmartCardCryptogramGeneratorOperationStatus = 5
SmartCardCryptogramGeneratorOperationStatus_NoCryptogramMaterialPackage: SmartCardCryptogramGeneratorOperationStatus = 6
SmartCardCryptogramGeneratorOperationStatus_UnsupportedCryptogramMaterialPackage: SmartCardCryptogramGeneratorOperationStatus = 7
SmartCardCryptogramGeneratorOperationStatus_UnknownCryptogramMaterialName: SmartCardCryptogramGeneratorOperationStatus = 8
SmartCardCryptogramGeneratorOperationStatus_InvalidCryptogramMaterialUsage: SmartCardCryptogramGeneratorOperationStatus = 9
SmartCardCryptogramGeneratorOperationStatus_ApduResponseNotSent: SmartCardCryptogramGeneratorOperationStatus = 10
SmartCardCryptogramGeneratorOperationStatus_OtherError: SmartCardCryptogramGeneratorOperationStatus = 11
SmartCardCryptogramGeneratorOperationStatus_ValidationFailed: SmartCardCryptogramGeneratorOperationStatus = 12
SmartCardCryptogramGeneratorOperationStatus_NotSupported: SmartCardCryptogramGeneratorOperationStatus = 13
class SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult: ...
    @winrt_mixinmethod
    def get_OperationStatus(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_Characteristics(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialCharacteristicsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult: ...
    @winrt_mixinmethod
    def get_OperationStatus(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_Characteristics(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramMaterialPackageCharacteristicsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult: ...
    @winrt_mixinmethod
    def get_OperationStatus(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_Characteristics(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramGetAllCryptogramStorageKeyCharacteristicsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCharacteristics]: ...
    OperationStatus = property(get_OperationStatus, None)
    Characteristics = property(get_Characteristics, None)
class SmartCardCryptogramMaterialCharacteristics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramMaterialCharacteristics'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialCharacteristics: ...
    @winrt_mixinmethod
    def get_MaterialName(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AllowedAlgorithms(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_mixinmethod
    def get_AllowedProofOfPossessionAlgorithms(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageConfirmationResponseFormat]: ...
    @winrt_mixinmethod
    def get_AllowedValidations(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm]: ...
    @winrt_mixinmethod
    def get_MaterialType(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialType: ...
    @winrt_mixinmethod
    def get_ProtectionMethod(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialProtectionMethod: ...
    @winrt_mixinmethod
    def get_ProtectionVersion(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> Int32: ...
    @winrt_mixinmethod
    def get_MaterialLength(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialCharacteristics) -> Int32: ...
    MaterialName = property(get_MaterialName, None)
    AllowedAlgorithms = property(get_AllowedAlgorithms, None)
    AllowedProofOfPossessionAlgorithms = property(get_AllowedProofOfPossessionAlgorithms, None)
    AllowedValidations = property(get_AllowedValidations, None)
    MaterialType = property(get_MaterialType, None)
    ProtectionMethod = property(get_ProtectionMethod, None)
    ProtectionVersion = property(get_ProtectionVersion, None)
    MaterialLength = property(get_MaterialLength, None)
class SmartCardCryptogramMaterialPackageCharacteristics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageCharacteristics'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageCharacteristics: ...
    @winrt_mixinmethod
    def get_PackageName(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StorageKeyName(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DateImported(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PackageFormat(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPackageCharacteristics) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramMaterialPackageFormat: ...
    PackageName = property(get_PackageName, None)
    StorageKeyName = property(get_StorageKeyName, None)
    DateImported = property(get_DateImported, None)
    PackageFormat = property(get_PackageFormat, None)
SmartCardCryptogramMaterialPackageConfirmationResponseFormat = Int32
SmartCardCryptogramMaterialPackageConfirmationResponseFormat_None: SmartCardCryptogramMaterialPackageConfirmationResponseFormat = 0
SmartCardCryptogramMaterialPackageConfirmationResponseFormat_VisaHmac: SmartCardCryptogramMaterialPackageConfirmationResponseFormat = 1
SmartCardCryptogramMaterialPackageFormat = Int32
SmartCardCryptogramMaterialPackageFormat_None: SmartCardCryptogramMaterialPackageFormat = 0
SmartCardCryptogramMaterialPackageFormat_JweRsaPki: SmartCardCryptogramMaterialPackageFormat = 1
class SmartCardCryptogramMaterialPossessionProof(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPossessionProof
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramMaterialPossessionProof'
    @winrt_mixinmethod
    def get_OperationStatus(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPossessionProof) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_Proof(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramMaterialPossessionProof) -> win32more.Windows.Storage.Streams.IBuffer: ...
    OperationStatus = property(get_OperationStatus, None)
    Proof = property(get_Proof, None)
SmartCardCryptogramMaterialProtectionMethod = Int32
SmartCardCryptogramMaterialProtectionMethod_None: SmartCardCryptogramMaterialProtectionMethod = 0
SmartCardCryptogramMaterialProtectionMethod_WhiteBoxing: SmartCardCryptogramMaterialProtectionMethod = 1
SmartCardCryptogramMaterialType = Int32
SmartCardCryptogramMaterialType_None: SmartCardCryptogramMaterialType = 0
SmartCardCryptogramMaterialType_StaticDataAuthentication: SmartCardCryptogramMaterialType = 1
SmartCardCryptogramMaterialType_TripleDes112: SmartCardCryptogramMaterialType = 2
SmartCardCryptogramMaterialType_Aes: SmartCardCryptogramMaterialType = 3
SmartCardCryptogramMaterialType_RsaPkcs1: SmartCardCryptogramMaterialType = 4
SmartCardCryptogramPlacementOptions = UInt32
SmartCardCryptogramPlacementOptions_None: SmartCardCryptogramPlacementOptions = 0
SmartCardCryptogramPlacementOptions_UnitsAreInNibbles: SmartCardCryptogramPlacementOptions = 1
SmartCardCryptogramPlacementOptions_ChainOutput: SmartCardCryptogramPlacementOptions = 2
class SmartCardCryptogramPlacementStep(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep: ...
    @winrt_mixinmethod
    def get_Algorithm(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm: ...
    @winrt_mixinmethod
    def put_Algorithm(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: win32more.Windows.Devices.SmartCards.SmartCardCryptogramAlgorithm) -> Void: ...
    @winrt_mixinmethod
    def get_SourceData(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_SourceData(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramMaterialPackageName(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CryptogramMaterialPackageName(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramMaterialName(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CryptogramMaterialName(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TemplateOffset(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Int32: ...
    @winrt_mixinmethod
    def put_TemplateOffset(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramOffset(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Int32: ...
    @winrt_mixinmethod
    def put_CryptogramOffset(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramLength(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> Int32: ...
    @winrt_mixinmethod
    def put_CryptogramLength(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_CryptogramPlacementOptions(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions: ...
    @winrt_mixinmethod
    def put_CryptogramPlacementOptions(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementOptions) -> Void: ...
    @winrt_mixinmethod
    def get_ChainedOutputStep(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep: ...
    @winrt_mixinmethod
    def put_ChainedOutputStep(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramPlacementStep, value: win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep) -> Void: ...
    Algorithm = property(get_Algorithm, put_Algorithm)
    SourceData = property(get_SourceData, put_SourceData)
    CryptogramMaterialPackageName = property(get_CryptogramMaterialPackageName, put_CryptogramMaterialPackageName)
    CryptogramMaterialName = property(get_CryptogramMaterialName, put_CryptogramMaterialName)
    TemplateOffset = property(get_TemplateOffset, put_TemplateOffset)
    CryptogramOffset = property(get_CryptogramOffset, put_CryptogramOffset)
    CryptogramLength = property(get_CryptogramLength, put_CryptogramLength)
    CryptogramPlacementOptions = property(get_CryptogramPlacementOptions, put_CryptogramPlacementOptions)
    ChainedOutputStep = property(get_ChainedOutputStep, put_ChainedOutputStep)
SmartCardCryptogramStorageKeyAlgorithm = Int32
SmartCardCryptogramStorageKeyAlgorithm_None: SmartCardCryptogramStorageKeyAlgorithm = 0
SmartCardCryptogramStorageKeyAlgorithm_Rsa2048: SmartCardCryptogramStorageKeyAlgorithm = 1
SmartCardCryptogramStorageKeyCapabilities = UInt32
SmartCardCryptogramStorageKeyCapabilities_None: SmartCardCryptogramStorageKeyCapabilities = 0
SmartCardCryptogramStorageKeyCapabilities_HardwareProtection: SmartCardCryptogramStorageKeyCapabilities = 1
SmartCardCryptogramStorageKeyCapabilities_UnlockPrompt: SmartCardCryptogramStorageKeyCapabilities = 2
class SmartCardCryptogramStorageKeyCharacteristics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCharacteristics'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCharacteristics: ...
    @winrt_mixinmethod
    def get_StorageKeyName(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DateCreated(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Algorithm(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyAlgorithm: ...
    @winrt_mixinmethod
    def get_Capabilities(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyCharacteristics) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities: ...
    StorageKeyName = property(get_StorageKeyName, None)
    DateCreated = property(get_DateCreated, None)
    Algorithm = property(get_Algorithm, None)
    Capabilities = property(get_Capabilities, None)
class SmartCardCryptogramStorageKeyInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo
    _classid_ = 'Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyInfo'
    @winrt_mixinmethod
    def get_OperationStatus(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus: ...
    @winrt_mixinmethod
    def get_PublicKeyBlobType(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> win32more.Windows.Security.Cryptography.Core.CryptographicPublicKeyBlobType: ...
    @winrt_mixinmethod
    def get_PublicKey(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_AttestationStatus(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> win32more.Windows.Devices.SmartCards.SmartCardCryptographicKeyAttestationStatus: ...
    @winrt_mixinmethod
    def get_Attestation(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_AttestationCertificateChain(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Capabilities(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo) -> win32more.Windows.Devices.SmartCards.SmartCardCryptogramStorageKeyCapabilities: ...
    @winrt_mixinmethod
    def get_OperationalRequirements(self: win32more.Windows.Devices.SmartCards.ISmartCardCryptogramStorageKeyInfo2) -> WinRT_String: ...
    OperationStatus = property(get_OperationStatus, None)
    PublicKeyBlobType = property(get_PublicKeyBlobType, None)
    PublicKey = property(get_PublicKey, None)
    AttestationStatus = property(get_AttestationStatus, None)
    Attestation = property(get_Attestation, None)
    AttestationCertificateChain = property(get_AttestationCertificateChain, None)
    Capabilities = property(get_Capabilities, None)
    OperationalRequirements = property(get_OperationalRequirements, None)
SmartCardCryptographicKeyAttestationStatus = Int32
SmartCardCryptographicKeyAttestationStatus_NoAttestation: SmartCardCryptographicKeyAttestationStatus = 0
SmartCardCryptographicKeyAttestationStatus_SoftwareKeyWithoutTpm: SmartCardCryptographicKeyAttestationStatus = 1
SmartCardCryptographicKeyAttestationStatus_SoftwareKeyWithTpm: SmartCardCryptographicKeyAttestationStatus = 2
SmartCardCryptographicKeyAttestationStatus_TpmKeyUnknownAttestationStatus: SmartCardCryptographicKeyAttestationStatus = 3
SmartCardCryptographicKeyAttestationStatus_TpmKeyWithoutAttestationCapability: SmartCardCryptographicKeyAttestationStatus = 4
SmartCardCryptographicKeyAttestationStatus_TpmKeyWithTemporaryAttestationFailure: SmartCardCryptographicKeyAttestationStatus = 5
SmartCardCryptographicKeyAttestationStatus_TpmKeyWithLongTermAttestationFailure: SmartCardCryptographicKeyAttestationStatus = 6
SmartCardCryptographicKeyAttestationStatus_TpmKeyWithAttestation: SmartCardCryptographicKeyAttestationStatus = 7
SmartCardEmulationCategory = Int32
SmartCardEmulationCategory_Other: SmartCardEmulationCategory = 0
SmartCardEmulationCategory_Payment: SmartCardEmulationCategory = 1
SmartCardEmulationType = Int32
SmartCardEmulationType_Host: SmartCardEmulationType = 0
SmartCardEmulationType_Uicc: SmartCardEmulationType = 1
SmartCardEmulationType_EmbeddedSE: SmartCardEmulationType = 2
class _SmartCardEmulator_Meta_(ComPtr.__class__):
    pass
class SmartCardEmulator(ComPtr, metaclass=_SmartCardEmulator_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardEmulator
    _classid_ = 'Windows.Devices.SmartCards.SmartCardEmulator'
    @winrt_mixinmethod
    def get_EnablementPolicy(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulator) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorEnablementPolicy: ...
    @winrt_mixinmethod
    def add_ApduReceived(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulator2, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SmartCards.SmartCardEmulator, win32more.Windows.Devices.SmartCards.SmartCardEmulatorApduReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ApduReceived(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulator2, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ConnectionDeactivated(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulator2, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SmartCards.SmartCardEmulator, win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionDeactivated(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulator2, value: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulator2) -> Void: ...
    @winrt_mixinmethod
    def IsHostCardEmulationSupported(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulator2) -> Boolean: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorStatics3) -> Boolean: ...
    @winrt_classmethod
    def GetAppletIdGroupRegistrationsAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration]]: ...
    @winrt_classmethod
    def RegisterAppletIdGroupAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorStatics2, appletIdGroup: win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroup) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration]: ...
    @winrt_classmethod
    def UnregisterAppletIdGroupAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorStatics2, registration: win32more.Windows.Devices.SmartCards.SmartCardAppletIdGroupRegistration) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def get_MaxAppletIdGroupRegistrations(cls: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorStatics2) -> UInt16: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardEmulator]: ...
    EnablementPolicy = property(get_EnablementPolicy, None)
    _SmartCardEmulator_Meta_.MaxAppletIdGroupRegistrations = property(get_MaxAppletIdGroupRegistrations.__wrapped__, None)
class SmartCardEmulatorApduReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs
    _classid_ = 'Windows.Devices.SmartCards.SmartCardEmulatorApduReceivedEventArgs'
    @winrt_mixinmethod
    def get_CommandApdu(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ConnectionProperties(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties: ...
    @winrt_mixinmethod
    def TryRespondAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs, responseApdu: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_AutomaticResponseStatus(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs) -> win32more.Windows.Devices.SmartCards.SmartCardAutomaticResponseStatus: ...
    @winrt_mixinmethod
    def TryRespondWithCryptogramsAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgsWithCryptograms, responseTemplate: win32more.Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def TryRespondWithCryptogramsAndStateAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgsWithCryptograms, responseTemplate: win32more.Windows.Storage.Streams.IBuffer, cryptogramPlacementSteps: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.SmartCards.SmartCardCryptogramPlacementStep], nextState: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardCryptogramGeneratorOperationStatus]: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs2) -> UInt32: ...
    @winrt_mixinmethod
    def TryRespondWithStateAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorApduReceivedEventArgs2, responseApdu: win32more.Windows.Storage.Streams.IBuffer, nextState: win32more.Windows.Foundation.IReference[UInt32]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    CommandApdu = property(get_CommandApdu, None)
    ConnectionProperties = property(get_ConnectionProperties, None)
    AutomaticResponseStatus = property(get_AutomaticResponseStatus, None)
    State = property(get_State, None)
class SmartCardEmulatorConnectionDeactivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorConnectionDeactivatedEventArgs
    _classid_ = 'Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedEventArgs'
    @winrt_mixinmethod
    def get_ConnectionProperties(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorConnectionDeactivatedEventArgs) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties: ...
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorConnectionDeactivatedEventArgs) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionDeactivatedReason: ...
    ConnectionProperties = property(get_ConnectionProperties, None)
    Reason = property(get_Reason, None)
SmartCardEmulatorConnectionDeactivatedReason = Int32
SmartCardEmulatorConnectionDeactivatedReason_ConnectionLost: SmartCardEmulatorConnectionDeactivatedReason = 0
SmartCardEmulatorConnectionDeactivatedReason_ConnectionRedirected: SmartCardEmulatorConnectionDeactivatedReason = 1
class SmartCardEmulatorConnectionProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorConnectionProperties
    _classid_ = 'Windows.Devices.SmartCards.SmartCardEmulatorConnectionProperties'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorConnectionProperties) -> Guid: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Devices.SmartCards.ISmartCardEmulatorConnectionProperties) -> win32more.Windows.Devices.SmartCards.SmartCardEmulatorConnectionSource: ...
    Id = property(get_Id, None)
    Source = property(get_Source, None)
SmartCardEmulatorConnectionSource = Int32
SmartCardEmulatorConnectionSource_Unknown: SmartCardEmulatorConnectionSource = 0
SmartCardEmulatorConnectionSource_NfcReader: SmartCardEmulatorConnectionSource = 1
SmartCardEmulatorContract: UInt32 = 393216
SmartCardEmulatorEnablementPolicy = Int32
SmartCardEmulatorEnablementPolicy_Never: SmartCardEmulatorEnablementPolicy = 0
SmartCardEmulatorEnablementPolicy_Always: SmartCardEmulatorEnablementPolicy = 1
SmartCardEmulatorEnablementPolicy_ScreenOn: SmartCardEmulatorEnablementPolicy = 2
SmartCardEmulatorEnablementPolicy_ScreenUnlocked: SmartCardEmulatorEnablementPolicy = 3
SmartCardLaunchBehavior = Int32
SmartCardLaunchBehavior_Default: SmartCardLaunchBehavior = 0
SmartCardLaunchBehavior_AboveLock: SmartCardLaunchBehavior = 1
SmartCardPinCharacterPolicyOption = Int32
SmartCardPinCharacterPolicyOption_Allow: SmartCardPinCharacterPolicyOption = 0
SmartCardPinCharacterPolicyOption_RequireAtLeastOne: SmartCardPinCharacterPolicyOption = 1
SmartCardPinCharacterPolicyOption_Disallow: SmartCardPinCharacterPolicyOption = 2
class SmartCardPinPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy
    _classid_ = 'Windows.Devices.SmartCards.SmartCardPinPolicy'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.SmartCards.SmartCardPinPolicy: ...
    @winrt_mixinmethod
    def get_MinLength(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy) -> UInt32: ...
    @winrt_mixinmethod
    def put_MinLength(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_MaxLength(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxLength(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_UppercaseLetters(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy) -> win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_mixinmethod
    def put_UppercaseLetters(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy, value: win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_mixinmethod
    def get_LowercaseLetters(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy) -> win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_mixinmethod
    def put_LowercaseLetters(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy, value: win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_mixinmethod
    def get_Digits(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy) -> win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_mixinmethod
    def put_Digits(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy, value: win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    @winrt_mixinmethod
    def get_SpecialCharacters(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy) -> win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption: ...
    @winrt_mixinmethod
    def put_SpecialCharacters(self: win32more.Windows.Devices.SmartCards.ISmartCardPinPolicy, value: win32more.Windows.Devices.SmartCards.SmartCardPinCharacterPolicyOption) -> Void: ...
    MinLength = property(get_MinLength, put_MinLength)
    MaxLength = property(get_MaxLength, put_MaxLength)
    UppercaseLetters = property(get_UppercaseLetters, put_UppercaseLetters)
    LowercaseLetters = property(get_LowercaseLetters, put_LowercaseLetters)
    Digits = property(get_Digits, put_Digits)
    SpecialCharacters = property(get_SpecialCharacters, put_SpecialCharacters)
class SmartCardPinResetDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardPinResetDeferral
    _classid_ = 'Windows.Devices.SmartCards.SmartCardPinResetDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.Devices.SmartCards.ISmartCardPinResetDeferral) -> Void: ...
class SmartCardPinResetHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{138d5e40-f3bc-4a5c-b41d-4b4ef684e237}')
    def Invoke(self, sender: win32more.Windows.Devices.SmartCards.SmartCardProvisioning, request: win32more.Windows.Devices.SmartCards.SmartCardPinResetRequest) -> Void: ...
class SmartCardPinResetRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardPinResetRequest
    _classid_ = 'Windows.Devices.SmartCards.SmartCardPinResetRequest'
    @winrt_mixinmethod
    def get_Challenge(self: win32more.Windows.Devices.SmartCards.ISmartCardPinResetRequest) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.Devices.SmartCards.ISmartCardPinResetRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.SmartCards.ISmartCardPinResetRequest) -> win32more.Windows.Devices.SmartCards.SmartCardPinResetDeferral: ...
    @winrt_mixinmethod
    def SetResponse(self: win32more.Windows.Devices.SmartCards.ISmartCardPinResetRequest, response: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    Challenge = property(get_Challenge, None)
    Deadline = property(get_Deadline, None)
class SmartCardProvisioning(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardProvisioning
    _classid_ = 'Windows.Devices.SmartCards.SmartCardProvisioning'
    @winrt_mixinmethod
    def get_SmartCard(self: win32more.Windows.Devices.SmartCards.ISmartCardProvisioning) -> win32more.Windows.Devices.SmartCards.SmartCard: ...
    @winrt_mixinmethod
    def GetIdAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardProvisioning) -> win32more.Windows.Foundation.IAsyncOperation[Guid]: ...
    @winrt_mixinmethod
    def GetNameAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardProvisioning) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetChallengeContextAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardProvisioning) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardChallengeContext]: ...
    @winrt_mixinmethod
    def RequestPinChangeAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardProvisioning) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPinResetAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardProvisioning, handler: win32more.Windows.Devices.SmartCards.SmartCardPinResetHandler) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GetAuthorityKeyContainerNameAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardProvisioning2) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def RequestAttestedVirtualSmartCardCreationAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardProvisioningStatics2, friendlyName: WinRT_String, administrativeKey: win32more.Windows.Storage.Streams.IBuffer, pinPolicy: win32more.Windows.Devices.SmartCards.SmartCardPinPolicy) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def RequestAttestedVirtualSmartCardCreationAsyncWithCardId(cls: win32more.Windows.Devices.SmartCards.ISmartCardProvisioningStatics2, friendlyName: WinRT_String, administrativeKey: win32more.Windows.Storage.Streams.IBuffer, pinPolicy: win32more.Windows.Devices.SmartCards.SmartCardPinPolicy, cardId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def FromSmartCardAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardProvisioningStatics, card: win32more.Windows.Devices.SmartCards.SmartCard) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def RequestVirtualSmartCardCreationAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardProvisioningStatics, friendlyName: WinRT_String, administrativeKey: win32more.Windows.Storage.Streams.IBuffer, pinPolicy: win32more.Windows.Devices.SmartCards.SmartCardPinPolicy) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def RequestVirtualSmartCardCreationAsyncWithCardId(cls: win32more.Windows.Devices.SmartCards.ISmartCardProvisioningStatics, friendlyName: WinRT_String, administrativeKey: win32more.Windows.Storage.Streams.IBuffer, pinPolicy: win32more.Windows.Devices.SmartCards.SmartCardPinPolicy, cardId: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardProvisioning]: ...
    @winrt_classmethod
    def RequestVirtualSmartCardDeletionAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardProvisioningStatics, card: win32more.Windows.Devices.SmartCards.SmartCard) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    SmartCard = property(get_SmartCard, None)
class SmartCardReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardReader
    _classid_ = 'Windows.Devices.SmartCards.SmartCardReader'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.SmartCards.ISmartCardReader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Devices.SmartCards.ISmartCardReader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Devices.SmartCards.ISmartCardReader) -> win32more.Windows.Devices.SmartCards.SmartCardReaderKind: ...
    @winrt_mixinmethod
    def GetStatusAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardReaderStatus]: ...
    @winrt_mixinmethod
    def FindAllCardsAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.SmartCards.SmartCard]]: ...
    @winrt_mixinmethod
    def add_CardAdded(self: win32more.Windows.Devices.SmartCards.ISmartCardReader, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SmartCards.SmartCardReader, win32more.Windows.Devices.SmartCards.CardAddedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CardAdded(self: win32more.Windows.Devices.SmartCards.ISmartCardReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CardRemoved(self: win32more.Windows.Devices.SmartCards.ISmartCardReader, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SmartCards.SmartCardReader, win32more.Windows.Devices.SmartCards.CardRemovedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CardRemoved(self: win32more.Windows.Devices.SmartCards.ISmartCardReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.SmartCards.ISmartCardReaderStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorWithKind(cls: win32more.Windows.Devices.SmartCards.ISmartCardReaderStatics, kind: win32more.Windows.Devices.SmartCards.SmartCardReaderKind) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.SmartCards.ISmartCardReaderStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SmartCards.SmartCardReader]: ...
    DeviceId = property(get_DeviceId, None)
    Name = property(get_Name, None)
    Kind = property(get_Kind, None)
SmartCardReaderKind = Int32
SmartCardReaderKind_Any: SmartCardReaderKind = 0
SmartCardReaderKind_Generic: SmartCardReaderKind = 1
SmartCardReaderKind_Tpm: SmartCardReaderKind = 2
SmartCardReaderKind_Nfc: SmartCardReaderKind = 3
SmartCardReaderKind_Uicc: SmartCardReaderKind = 4
SmartCardReaderKind_EmbeddedSE: SmartCardReaderKind = 5
SmartCardReaderStatus = Int32
SmartCardReaderStatus_Disconnected: SmartCardReaderStatus = 0
SmartCardReaderStatus_Ready: SmartCardReaderStatus = 1
SmartCardReaderStatus_Exclusive: SmartCardReaderStatus = 2
SmartCardStatus = Int32
SmartCardStatus_Disconnected: SmartCardStatus = 0
SmartCardStatus_Ready: SmartCardStatus = 1
SmartCardStatus_Shared: SmartCardStatus = 2
SmartCardStatus_Exclusive: SmartCardStatus = 3
SmartCardStatus_Unresponsive: SmartCardStatus = 4
class SmartCardTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SmartCards.ISmartCardTriggerDetails
    _classid_ = 'Windows.Devices.SmartCards.SmartCardTriggerDetails'
    @winrt_mixinmethod
    def get_TriggerType(self: win32more.Windows.Devices.SmartCards.ISmartCardTriggerDetails) -> win32more.Windows.Devices.SmartCards.SmartCardTriggerType: ...
    @winrt_mixinmethod
    def get_SourceAppletId(self: win32more.Windows.Devices.SmartCards.ISmartCardTriggerDetails) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_TriggerData(self: win32more.Windows.Devices.SmartCards.ISmartCardTriggerDetails) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Emulator(self: win32more.Windows.Devices.SmartCards.ISmartCardTriggerDetails2) -> win32more.Windows.Devices.SmartCards.SmartCardEmulator: ...
    @winrt_mixinmethod
    def TryLaunchCurrentAppAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardTriggerDetails2, arguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryLaunchCurrentAppWithBehaviorAsync(self: win32more.Windows.Devices.SmartCards.ISmartCardTriggerDetails2, arguments: WinRT_String, behavior: win32more.Windows.Devices.SmartCards.SmartCardLaunchBehavior) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_SmartCard(self: win32more.Windows.Devices.SmartCards.ISmartCardTriggerDetails3) -> win32more.Windows.Devices.SmartCards.SmartCard: ...
    TriggerType = property(get_TriggerType, None)
    SourceAppletId = property(get_SourceAppletId, None)
    TriggerData = property(get_TriggerData, None)
    Emulator = property(get_Emulator, None)
    SmartCard = property(get_SmartCard, None)
SmartCardTriggerType = Int32
SmartCardTriggerType_EmulatorTransaction: SmartCardTriggerType = 0
SmartCardTriggerType_EmulatorNearFieldEntry: SmartCardTriggerType = 1
SmartCardTriggerType_EmulatorNearFieldExit: SmartCardTriggerType = 2
SmartCardTriggerType_EmulatorHostApplicationActivated: SmartCardTriggerType = 3
SmartCardTriggerType_EmulatorAppletIdGroupRegistrationChanged: SmartCardTriggerType = 4
SmartCardTriggerType_ReaderCardAdded: SmartCardTriggerType = 5
SmartCardUnlockPromptingBehavior = Int32
SmartCardUnlockPromptingBehavior_AllowUnlockPrompt: SmartCardUnlockPromptingBehavior = 0
SmartCardUnlockPromptingBehavior_RequireUnlockPrompt: SmartCardUnlockPromptingBehavior = 1
SmartCardUnlockPromptingBehavior_PreventUnlockPrompt: SmartCardUnlockPromptingBehavior = 2
make_ready(__name__)
