from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct2D
import Windows.Win32.Graphics.Imaging
import Windows.Win32.Graphics.Imaging.D2D
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWICImageEncoder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04c75bf8-3ce1-473b-acc5-3cc4f5e94999}')
    @commethod(3)
    def WriteFrame(self, pImage: Windows.Win32.Graphics.Direct2D.ID2D1Image_head, pFrameEncode: Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode_head, pImageParameters: POINTER(Windows.Win32.Graphics.Imaging.WICImageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteFrameThumbnail(self, pImage: Windows.Win32.Graphics.Direct2D.ID2D1Image_head, pFrameEncode: Windows.Win32.Graphics.Imaging.IWICBitmapFrameEncode_head, pImageParameters: POINTER(Windows.Win32.Graphics.Imaging.WICImageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteThumbnail(self, pImage: Windows.Win32.Graphics.Direct2D.ID2D1Image_head, pEncoder: Windows.Win32.Graphics.Imaging.IWICBitmapEncoder_head, pImageParameters: POINTER(Windows.Win32.Graphics.Imaging.WICImageParameters_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWICImagingFactory2(ComPtr):
    extends: Windows.Win32.Graphics.Imaging.IWICImagingFactory
    _iid_ = Guid('{7b816b45-1996-4476-b132-de9e247c8af0}')
    @commethod(28)
    def CreateImageEncoder(self, pD2DDevice: Windows.Win32.Graphics.Direct2D.ID2D1Device_head, ppWICImageEncoder: POINTER(Windows.Win32.Graphics.Imaging.D2D.IWICImageEncoder_head)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IWICImageEncoder')
make_head(_module, 'IWICImagingFactory2')
