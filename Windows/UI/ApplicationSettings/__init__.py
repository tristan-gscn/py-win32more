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
import Windows.Security.Credentials
import Windows.System
import Windows.UI.ApplicationSettings
import Windows.UI.Popups
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AccountsSettingsPane(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ApplicationSettings.AccountsSettingsPane'
    @winrt_mixinmethod
    def add_AccountCommandsRequested(self: Windows.UI.ApplicationSettings.IAccountsSettingsPane, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ApplicationSettings.AccountsSettingsPane, Windows.UI.ApplicationSettings.AccountsSettingsPaneCommandsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AccountCommandsRequested(self: Windows.UI.ApplicationSettings.IAccountsSettingsPane, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def ShowManageAccountsForUserAsync(cls: Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics3, user: Windows.System.User) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowAddAccountForUserAsync(cls: Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics3, user: Windows.System.User) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowManageAccountsAsync(cls: Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def ShowAddAccountAsync(cls: Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics2) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics) -> Windows.UI.ApplicationSettings.AccountsSettingsPane: ...
    @winrt_classmethod
    def Show(cls: Windows.UI.ApplicationSettings.IAccountsSettingsPaneStatics) -> Void: ...
class AccountsSettingsPaneCommandsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ApplicationSettings.AccountsSettingsPaneCommandsRequestedEventArgs'
    @winrt_mixinmethod
    def get_WebAccountProviderCommands(self: Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> Windows.Foundation.Collections.IVector[Windows.UI.ApplicationSettings.WebAccountProviderCommand]: ...
    @winrt_mixinmethod
    def get_WebAccountCommands(self: Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> Windows.Foundation.Collections.IVector[Windows.UI.ApplicationSettings.WebAccountCommand]: ...
    @winrt_mixinmethod
    def get_CredentialCommands(self: Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> Windows.Foundation.Collections.IVector[Windows.UI.ApplicationSettings.CredentialCommand]: ...
    @winrt_mixinmethod
    def get_Commands(self: Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> Windows.Foundation.Collections.IVector[Windows.UI.ApplicationSettings.SettingsCommand]: ...
    @winrt_mixinmethod
    def get_HeaderText(self: Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HeaderText(self: Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs) -> Windows.UI.ApplicationSettings.AccountsSettingsPaneEventDeferral: ...
    @winrt_mixinmethod
    def get_User(self: Windows.UI.ApplicationSettings.IAccountsSettingsPaneCommandsRequestedEventArgs2) -> Windows.System.User: ...
    WebAccountProviderCommands = property(get_WebAccountProviderCommands, None)
    WebAccountCommands = property(get_WebAccountCommands, None)
    CredentialCommands = property(get_CredentialCommands, None)
    Commands = property(get_Commands, None)
    HeaderText = property(get_HeaderText, put_HeaderText)
    User = property(get_User, None)
class AccountsSettingsPaneEventDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ApplicationSettings.AccountsSettingsPaneEventDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.UI.ApplicationSettings.IAccountsSettingsPaneEventDeferral) -> Void: ...
class CredentialCommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ApplicationSettings.CredentialCommand'
    @winrt_factorymethod
    def CreateCredentialCommand(cls: Windows.UI.ApplicationSettings.ICredentialCommandFactory, passwordCredential: Windows.Security.Credentials.PasswordCredential) -> Windows.UI.ApplicationSettings.CredentialCommand: ...
    @winrt_factorymethod
    def CreateCredentialCommandWithHandler(cls: Windows.UI.ApplicationSettings.ICredentialCommandFactory, passwordCredential: Windows.Security.Credentials.PasswordCredential, deleted: Windows.UI.ApplicationSettings.CredentialCommandCredentialDeletedHandler) -> Windows.UI.ApplicationSettings.CredentialCommand: ...
    @winrt_mixinmethod
    def get_PasswordCredential(self: Windows.UI.ApplicationSettings.ICredentialCommand) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_mixinmethod
    def get_CredentialDeleted(self: Windows.UI.ApplicationSettings.ICredentialCommand) -> Windows.UI.ApplicationSettings.CredentialCommandCredentialDeletedHandler: ...
    PasswordCredential = property(get_PasswordCredential, None)
    CredentialDeleted = property(get_CredentialDeleted, None)
class CredentialCommandCredentialDeletedHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('61c0e185-0977-4678-b4-e2-98-72-7a-fb-ee-d9')
    ClassId = 'Windows.UI.ApplicationSettings.CredentialCommandCredentialDeletedHandler'
    @winrt_commethod(3)
    def Invoke(self, command: Windows.UI.ApplicationSettings.CredentialCommand) -> Void: ...
class IAccountsSettingsPane(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('81ea942c-4f09-4406-a5-38-83-8d-9b-14-b7-e6')
    @winrt_commethod(6)
    def add_AccountCommandsRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ApplicationSettings.AccountsSettingsPane, Windows.UI.ApplicationSettings.AccountsSettingsPaneCommandsRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AccountCommandsRequested(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IAccountsSettingsPaneCommandsRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3b68c099-db19-45d0-9a-bf-95-d3-77-3c-93-30')
    @winrt_commethod(6)
    def get_WebAccountProviderCommands(self) -> Windows.Foundation.Collections.IVector[Windows.UI.ApplicationSettings.WebAccountProviderCommand]: ...
    @winrt_commethod(7)
    def get_WebAccountCommands(self) -> Windows.Foundation.Collections.IVector[Windows.UI.ApplicationSettings.WebAccountCommand]: ...
    @winrt_commethod(8)
    def get_CredentialCommands(self) -> Windows.Foundation.Collections.IVector[Windows.UI.ApplicationSettings.CredentialCommand]: ...
    @winrt_commethod(9)
    def get_Commands(self) -> Windows.Foundation.Collections.IVector[Windows.UI.ApplicationSettings.SettingsCommand]: ...
    @winrt_commethod(10)
    def get_HeaderText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_HeaderText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def GetDeferral(self) -> Windows.UI.ApplicationSettings.AccountsSettingsPaneEventDeferral: ...
    WebAccountProviderCommands = property(get_WebAccountProviderCommands, None)
    WebAccountCommands = property(get_WebAccountCommands, None)
    CredentialCommands = property(get_CredentialCommands, None)
    Commands = property(get_Commands, None)
    HeaderText = property(get_HeaderText, put_HeaderText)
class IAccountsSettingsPaneCommandsRequestedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('362f7bad-4e37-4967-8c-40-e7-8e-e7-a1-e5-bb')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IAccountsSettingsPaneEventDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cbf25d3f-e5ba-40ef-93-da-65-e0-96-e5-fb-04')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IAccountsSettingsPaneStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('561f8b60-b0ec-4150-a8-dc-20-8e-e4-4b-06-8a')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.ApplicationSettings.AccountsSettingsPane: ...
    @winrt_commethod(7)
    def Show(self) -> Void: ...
class IAccountsSettingsPaneStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d21df7c2-ce0d-484f-b8-e8-e8-23-c2-15-76-5e')
    @winrt_commethod(6)
    def ShowManageAccountsAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ShowAddAccountAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IAccountsSettingsPaneStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('08410458-a2ba-4c6f-b4-ac-48-f5-14-33-12-16')
    @winrt_commethod(6)
    def ShowManageAccountsForUserAsync(self, user: Windows.System.User) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ShowAddAccountForUserAsync(self, user: Windows.System.User) -> Windows.Foundation.IAsyncAction: ...
class ICredentialCommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a5f665e6-6143-4a7a-a9-71-b0-17-ba-97-8c-e2')
    @winrt_commethod(6)
    def get_PasswordCredential(self) -> Windows.Security.Credentials.PasswordCredential: ...
    @winrt_commethod(7)
    def get_CredentialDeleted(self) -> Windows.UI.ApplicationSettings.CredentialCommandCredentialDeletedHandler: ...
    PasswordCredential = property(get_PasswordCredential, None)
    CredentialDeleted = property(get_CredentialDeleted, None)
class ICredentialCommandFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('27e88c17-bc3e-4b80-94-95-4e-d7-20-e4-8a-91')
    @winrt_commethod(6)
    def CreateCredentialCommand(self, passwordCredential: Windows.Security.Credentials.PasswordCredential) -> Windows.UI.ApplicationSettings.CredentialCommand: ...
    @winrt_commethod(7)
    def CreateCredentialCommandWithHandler(self, passwordCredential: Windows.Security.Credentials.PasswordCredential, deleted: Windows.UI.ApplicationSettings.CredentialCommandCredentialDeletedHandler) -> Windows.UI.ApplicationSettings.CredentialCommand: ...
class ISettingsCommandFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('68e15b33-1c83-433a-aa-5a-ce-ee-a5-bd-47-64')
    @winrt_commethod(6)
    def CreateSettingsCommand(self, settingsCommandId: Windows.Win32.System.WinRT.IInspectable_head, label: WinRT_String, handler: Windows.UI.Popups.UICommandInvokedHandler) -> Windows.UI.ApplicationSettings.SettingsCommand: ...
class ISettingsCommandStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('749ae954-2f69-4b17-8a-ba-d0-5c-e5-77-8e-46')
    @winrt_commethod(6)
    def get_AccountsCommand(self) -> Windows.UI.ApplicationSettings.SettingsCommand: ...
    AccountsCommand = property(get_AccountsCommand, None)
class IWebAccountCommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('caa39398-9cfa-4246-b0-c4-a9-13-a3-89-65-41')
    @winrt_commethod(6)
    def get_WebAccount(self) -> Windows.Security.Credentials.WebAccount: ...
    @winrt_commethod(7)
    def get_Invoked(self) -> Windows.UI.ApplicationSettings.WebAccountCommandInvokedHandler: ...
    @winrt_commethod(8)
    def get_Actions(self) -> Windows.UI.ApplicationSettings.SupportedWebAccountActions: ...
    WebAccount = property(get_WebAccount, None)
    Invoked = property(get_Invoked, None)
    Actions = property(get_Actions, None)
class IWebAccountCommandFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bfa6cdff-2f2d-42f5-81-de-1d-56-ba-fc-49-6d')
    @winrt_commethod(6)
    def CreateWebAccountCommand(self, webAccount: Windows.Security.Credentials.WebAccount, invoked: Windows.UI.ApplicationSettings.WebAccountCommandInvokedHandler, actions: Windows.UI.ApplicationSettings.SupportedWebAccountActions) -> Windows.UI.ApplicationSettings.WebAccountCommand: ...
class IWebAccountInvokedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e7abcc40-a1d8-4c5d-9a-7f-1d-34-b2-f9-0a-d2')
    @winrt_commethod(6)
    def get_Action(self) -> Windows.UI.ApplicationSettings.WebAccountAction: ...
    Action = property(get_Action, None)
class IWebAccountProviderCommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d69bdd9a-a0a6-4e9b-88-dc-c7-1e-75-7a-35-01')
    @winrt_commethod(6)
    def get_WebAccountProvider(self) -> Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_commethod(7)
    def get_Invoked(self) -> Windows.UI.ApplicationSettings.WebAccountProviderCommandInvokedHandler: ...
    WebAccountProvider = property(get_WebAccountProvider, None)
    Invoked = property(get_Invoked, None)
class IWebAccountProviderCommandFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d5658a1b-b176-4776-84-69-a9-d3-ff-0b-3f-59')
    @winrt_commethod(6)
    def CreateWebAccountProviderCommand(self, webAccountProvider: Windows.Security.Credentials.WebAccountProvider, invoked: Windows.UI.ApplicationSettings.WebAccountProviderCommandInvokedHandler) -> Windows.UI.ApplicationSettings.WebAccountProviderCommand: ...
class SettingsCommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ApplicationSettings.SettingsCommand'
    @winrt_factorymethod
    def CreateSettingsCommand(cls: Windows.UI.ApplicationSettings.ISettingsCommandFactory, settingsCommandId: Windows.Win32.System.WinRT.IInspectable_head, label: WinRT_String, handler: Windows.UI.Popups.UICommandInvokedHandler) -> Windows.UI.ApplicationSettings.SettingsCommand: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.UI.Popups.IUICommand) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Label(self: Windows.UI.Popups.IUICommand, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Invoked(self: Windows.UI.Popups.IUICommand) -> Windows.UI.Popups.UICommandInvokedHandler: ...
    @winrt_mixinmethod
    def put_Invoked(self: Windows.UI.Popups.IUICommand, value: Windows.UI.Popups.UICommandInvokedHandler) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Popups.IUICommand) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.UI.Popups.IUICommand, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_classmethod
    def get_AccountsCommand(cls: Windows.UI.ApplicationSettings.ISettingsCommandStatics) -> Windows.UI.ApplicationSettings.SettingsCommand: ...
    Label = property(get_Label, put_Label)
    Invoked = property(get_Invoked, put_Invoked)
    Id = property(get_Id, put_Id)
    AccountsCommand = property(get_AccountsCommand, None)
SupportedWebAccountActions = UInt32
SupportedWebAccountActions_None: SupportedWebAccountActions = 0
SupportedWebAccountActions_Reconnect: SupportedWebAccountActions = 1
SupportedWebAccountActions_Remove: SupportedWebAccountActions = 2
SupportedWebAccountActions_ViewDetails: SupportedWebAccountActions = 4
SupportedWebAccountActions_Manage: SupportedWebAccountActions = 8
SupportedWebAccountActions_More: SupportedWebAccountActions = 16
WebAccountAction = Int32
WebAccountAction_Reconnect: WebAccountAction = 0
WebAccountAction_Remove: WebAccountAction = 1
WebAccountAction_ViewDetails: WebAccountAction = 2
WebAccountAction_Manage: WebAccountAction = 3
WebAccountAction_More: WebAccountAction = 4
class WebAccountCommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ApplicationSettings.WebAccountCommand'
    @winrt_factorymethod
    def CreateWebAccountCommand(cls: Windows.UI.ApplicationSettings.IWebAccountCommandFactory, webAccount: Windows.Security.Credentials.WebAccount, invoked: Windows.UI.ApplicationSettings.WebAccountCommandInvokedHandler, actions: Windows.UI.ApplicationSettings.SupportedWebAccountActions) -> Windows.UI.ApplicationSettings.WebAccountCommand: ...
    @winrt_mixinmethod
    def get_WebAccount(self: Windows.UI.ApplicationSettings.IWebAccountCommand) -> Windows.Security.Credentials.WebAccount: ...
    @winrt_mixinmethod
    def get_Invoked(self: Windows.UI.ApplicationSettings.IWebAccountCommand) -> Windows.UI.ApplicationSettings.WebAccountCommandInvokedHandler: ...
    @winrt_mixinmethod
    def get_Actions(self: Windows.UI.ApplicationSettings.IWebAccountCommand) -> Windows.UI.ApplicationSettings.SupportedWebAccountActions: ...
    WebAccount = property(get_WebAccount, None)
    Invoked = property(get_Invoked, None)
    Actions = property(get_Actions, None)
class WebAccountCommandInvokedHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('1ee6e459-1705-4a9a-b5-99-a0-c3-d6-92-19-73')
    ClassId = 'Windows.UI.ApplicationSettings.WebAccountCommandInvokedHandler'
    @winrt_commethod(3)
    def Invoke(self, command: Windows.UI.ApplicationSettings.WebAccountCommand, args: Windows.UI.ApplicationSettings.WebAccountInvokedArgs) -> Void: ...
class WebAccountInvokedArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ApplicationSettings.WebAccountInvokedArgs'
    @winrt_mixinmethod
    def get_Action(self: Windows.UI.ApplicationSettings.IWebAccountInvokedArgs) -> Windows.UI.ApplicationSettings.WebAccountAction: ...
    Action = property(get_Action, None)
class WebAccountProviderCommand(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ApplicationSettings.WebAccountProviderCommand'
    @winrt_factorymethod
    def CreateWebAccountProviderCommand(cls: Windows.UI.ApplicationSettings.IWebAccountProviderCommandFactory, webAccountProvider: Windows.Security.Credentials.WebAccountProvider, invoked: Windows.UI.ApplicationSettings.WebAccountProviderCommandInvokedHandler) -> Windows.UI.ApplicationSettings.WebAccountProviderCommand: ...
    @winrt_mixinmethod
    def get_WebAccountProvider(self: Windows.UI.ApplicationSettings.IWebAccountProviderCommand) -> Windows.Security.Credentials.WebAccountProvider: ...
    @winrt_mixinmethod
    def get_Invoked(self: Windows.UI.ApplicationSettings.IWebAccountProviderCommand) -> Windows.UI.ApplicationSettings.WebAccountProviderCommandInvokedHandler: ...
    WebAccountProvider = property(get_WebAccountProvider, None)
    Invoked = property(get_Invoked, None)
class WebAccountProviderCommandInvokedHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('b7de5527-4c8f-42dd-84-da-5e-c4-93-ab-db-9a')
    ClassId = 'Windows.UI.ApplicationSettings.WebAccountProviderCommandInvokedHandler'
    @winrt_commethod(3)
    def Invoke(self, command: Windows.UI.ApplicationSettings.WebAccountProviderCommand) -> Void: ...
make_head(_module, 'AccountsSettingsPane')
make_head(_module, 'AccountsSettingsPaneCommandsRequestedEventArgs')
make_head(_module, 'AccountsSettingsPaneEventDeferral')
make_head(_module, 'CredentialCommand')
make_head(_module, 'CredentialCommandCredentialDeletedHandler')
make_head(_module, 'IAccountsSettingsPane')
make_head(_module, 'IAccountsSettingsPaneCommandsRequestedEventArgs')
make_head(_module, 'IAccountsSettingsPaneCommandsRequestedEventArgs2')
make_head(_module, 'IAccountsSettingsPaneEventDeferral')
make_head(_module, 'IAccountsSettingsPaneStatics')
make_head(_module, 'IAccountsSettingsPaneStatics2')
make_head(_module, 'IAccountsSettingsPaneStatics3')
make_head(_module, 'ICredentialCommand')
make_head(_module, 'ICredentialCommandFactory')
make_head(_module, 'ISettingsCommandFactory')
make_head(_module, 'ISettingsCommandStatics')
make_head(_module, 'IWebAccountCommand')
make_head(_module, 'IWebAccountCommandFactory')
make_head(_module, 'IWebAccountInvokedArgs')
make_head(_module, 'IWebAccountProviderCommand')
make_head(_module, 'IWebAccountProviderCommandFactory')
make_head(_module, 'SettingsCommand')
make_head(_module, 'WebAccountCommand')
make_head(_module, 'WebAccountCommandInvokedHandler')
make_head(_module, 'WebAccountInvokedArgs')
make_head(_module, 'WebAccountProviderCommand')
make_head(_module, 'WebAccountProviderCommandInvokedHandler')
