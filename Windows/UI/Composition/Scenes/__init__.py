from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Graphics.DirectX
import Windows.UI.Composition
import Windows.UI.Composition.Scenes
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISceneBoundingBox(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5d8ffc70-c618-4083-82-51-99-62-59-31-14-aa')
    @winrt_commethod(6)
    def get_Center(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_Extents(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(8)
    def get_Max(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(9)
    def get_Min(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(10)
    def get_Size(self) -> Windows.Foundation.Numerics.Vector3: ...
    Center = property(get_Center, None)
    Extents = property(get_Extents, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Size = property(get_Size, None)
class ISceneComponent(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae20fc96-226c-44bd-95-cb-dd-5e-d9-eb-e9-a5')
    @winrt_commethod(6)
    def get_ComponentType(self) -> Windows.UI.Composition.Scenes.SceneComponentType: ...
    ComponentType = property(get_ComponentType, None)
class ISceneComponentCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c483791c-5f46-45e4-b6-66-a3-d2-25-9f-9b-2e')
class ISceneComponentFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5fbc5574-ddd8-5889-ab-5b-d8-fa-71-6e-7c-9e')
class ISceneMaterial(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8ca74b7c-30df-4e07-94-90-37-87-5a-f1-a1-23')
class ISceneMaterialFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('67536c19-a707-5254-a4-95-7f-dc-79-98-93-b9')
class ISceneMaterialInput(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('422a1642-1ef1-485c-97-e9-ae-6f-95-ad-81-2f')
class ISceneMaterialInputFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a88feb74-7d0a-5e4c-a7-48-10-15-af-9c-a7-4f')
class ISceneMesh(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ee9a1530-1155-4c0c-92-bd-40-02-0c-f7-83-47')
    @winrt_commethod(6)
    def get_Bounds(self) -> Windows.UI.Composition.Scenes.SceneBoundingBox: ...
    @winrt_commethod(7)
    def get_PrimitiveTopology(self) -> Windows.Graphics.DirectX.DirectXPrimitiveTopology: ...
    @winrt_commethod(8)
    def put_PrimitiveTopology(self, value: Windows.Graphics.DirectX.DirectXPrimitiveTopology) -> Void: ...
    @winrt_commethod(9)
    def FillMeshAttribute(self, semantic: Windows.UI.Composition.Scenes.SceneAttributeSemantic, format: Windows.Graphics.DirectX.DirectXPixelFormat, memory: Windows.Foundation.MemoryBuffer) -> Void: ...
    Bounds = property(get_Bounds, None)
    PrimitiveTopology = property(get_PrimitiveTopology, put_PrimitiveTopology)
class ISceneMeshMaterialAttributeMap(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ce843171-3d43-4855-aa-69-31-ff-98-8d-04-9d')
class ISceneMeshRendererComponent(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9929f7e3-6364-477e-98-fe-74-ed-9f-d4-c2-de')
    @winrt_commethod(6)
    def get_Material(self) -> Windows.UI.Composition.Scenes.SceneMaterial: ...
    @winrt_commethod(7)
    def put_Material(self, value: Windows.UI.Composition.Scenes.SceneMaterial) -> Void: ...
    @winrt_commethod(8)
    def get_Mesh(self) -> Windows.UI.Composition.Scenes.SceneMesh: ...
    @winrt_commethod(9)
    def put_Mesh(self, value: Windows.UI.Composition.Scenes.SceneMesh) -> Void: ...
    @winrt_commethod(10)
    def get_UVMappings(self) -> Windows.UI.Composition.Scenes.SceneMeshMaterialAttributeMap: ...
    Material = property(get_Material, put_Material)
    Mesh = property(get_Mesh, put_Mesh)
    UVMappings = property(get_UVMappings, None)
class ISceneMeshRendererComponentStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4954f37a-4459-4521-bd-6e-2b-38-b8-d7-11-ea')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneMeshRendererComponent: ...
class ISceneMeshStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8412316c-7b57-473f-96-6b-81-dc-27-7b-17-51')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneMesh: ...
class ISceneMetallicRoughnessMaterial(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c1d91446-799c-429e-a4-e4-5d-a6-45-f1-8e-61')
    @winrt_commethod(6)
    def get_BaseColorInput(self) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(7)
    def put_BaseColorInput(self, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(8)
    def get_BaseColorFactor(self) -> Windows.Foundation.Numerics.Vector4: ...
    @winrt_commethod(9)
    def put_BaseColorFactor(self, value: Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_commethod(10)
    def get_MetallicFactor(self) -> Single: ...
    @winrt_commethod(11)
    def put_MetallicFactor(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_MetallicRoughnessInput(self) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(13)
    def put_MetallicRoughnessInput(self, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(14)
    def get_RoughnessFactor(self) -> Single: ...
    @winrt_commethod(15)
    def put_RoughnessFactor(self, value: Single) -> Void: ...
    BaseColorInput = property(get_BaseColorInput, put_BaseColorInput)
    BaseColorFactor = property(get_BaseColorFactor, put_BaseColorFactor)
    MetallicFactor = property(get_MetallicFactor, put_MetallicFactor)
    MetallicRoughnessInput = property(get_MetallicRoughnessInput, put_MetallicRoughnessInput)
    RoughnessFactor = property(get_RoughnessFactor, put_RoughnessFactor)
class ISceneMetallicRoughnessMaterialStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3bddca50-6d9d-4531-8d-c4-b2-7e-3e-49-b7-ab')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneMetallicRoughnessMaterial: ...
class ISceneModelTransform(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c05576c2-32b1-4269-98-0d-b9-85-37-10-0a-e4')
    @winrt_commethod(6)
    def get_Orientation(self) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(7)
    def put_Orientation(self, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_commethod(8)
    def get_RotationAngle(self) -> Single: ...
    @winrt_commethod(9)
    def put_RotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_RotationAngleInDegrees(self) -> Single: ...
    @winrt_commethod(11)
    def put_RotationAngleInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_RotationAxis(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_RotationAxis(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_Scale(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(15)
    def put_Scale(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(16)
    def get_Translation(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(17)
    def put_Translation(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    Orientation = property(get_Orientation, put_Orientation)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    Scale = property(get_Scale, put_Scale)
    Translation = property(get_Translation, put_Translation)
class ISceneNode(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('acf2c247-f307-4581-9c-41-af-2e-29-c3-b0-16')
    @winrt_commethod(6)
    def get_Children(self) -> Windows.UI.Composition.Scenes.SceneNodeCollection: ...
    @winrt_commethod(7)
    def get_Components(self) -> Windows.UI.Composition.Scenes.SceneComponentCollection: ...
    @winrt_commethod(8)
    def get_Parent(self) -> Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_commethod(9)
    def get_Transform(self) -> Windows.UI.Composition.Scenes.SceneModelTransform: ...
    @winrt_commethod(10)
    def FindFirstComponentOfType(self, value: Windows.UI.Composition.Scenes.SceneComponentType) -> Windows.UI.Composition.Scenes.SceneComponent: ...
    Children = property(get_Children, None)
    Components = property(get_Components, None)
    Parent = property(get_Parent, None)
    Transform = property(get_Transform, None)
class ISceneNodeCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('29ada101-2dd9-4332-be-63-60-d2-cf-42-69-f2')
class ISceneNodeStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('579a0faa-be9d-4210-90-8c-93-d1-5f-ee-d0-b7')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneNode: ...
class ISceneObject(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1e94249b-0f1b-49eb-a8-19-87-7d-84-50-00-5b')
class ISceneObjectFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('14fe799a-33e4-52ef-95-6c-44-22-9d-21-f2-c1')
class IScenePbrMaterial(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aab6ebbe-d680-46df-82-94-b6-80-0a-9f-95-e7')
    @winrt_commethod(6)
    def get_AlphaCutoff(self) -> Single: ...
    @winrt_commethod(7)
    def put_AlphaCutoff(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_AlphaMode(self) -> Windows.UI.Composition.Scenes.SceneAlphaMode: ...
    @winrt_commethod(9)
    def put_AlphaMode(self, value: Windows.UI.Composition.Scenes.SceneAlphaMode) -> Void: ...
    @winrt_commethod(10)
    def get_EmissiveInput(self) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(11)
    def put_EmissiveInput(self, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(12)
    def get_EmissiveFactor(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(13)
    def put_EmissiveFactor(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(14)
    def get_IsDoubleSided(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsDoubleSided(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_NormalInput(self) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(17)
    def put_NormalInput(self, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(18)
    def get_NormalScale(self) -> Single: ...
    @winrt_commethod(19)
    def put_NormalScale(self, value: Single) -> Void: ...
    @winrt_commethod(20)
    def get_OcclusionInput(self) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(21)
    def put_OcclusionInput(self, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(22)
    def get_OcclusionStrength(self) -> Single: ...
    @winrt_commethod(23)
    def put_OcclusionStrength(self, value: Single) -> Void: ...
    AlphaCutoff = property(get_AlphaCutoff, put_AlphaCutoff)
    AlphaMode = property(get_AlphaMode, put_AlphaMode)
    EmissiveInput = property(get_EmissiveInput, put_EmissiveInput)
    EmissiveFactor = property(get_EmissiveFactor, put_EmissiveFactor)
    IsDoubleSided = property(get_IsDoubleSided, put_IsDoubleSided)
    NormalInput = property(get_NormalInput, put_NormalInput)
    NormalScale = property(get_NormalScale, put_NormalScale)
    OcclusionInput = property(get_OcclusionInput, put_OcclusionInput)
    OcclusionStrength = property(get_OcclusionStrength, put_OcclusionStrength)
class IScenePbrMaterialFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2e3f3dfe-0b85-5727-b5-be-b7-d3-cb-ac-37-fa')
class ISceneRendererComponent(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f1acb857-cf4f-4025-9b-25-a2-d1-94-4c-f5-07')
class ISceneRendererComponentFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1db6ed6c-aa2c-5967-90-35-56-35-2d-c6-96-58')
class ISceneSurfaceMaterialInput(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9937da5c-a9ca-4cfc-b3-aa-08-83-56-51-87-42')
    @winrt_commethod(6)
    def get_BitmapInterpolationMode(self) -> Windows.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_commethod(7)
    def put_BitmapInterpolationMode(self, value: Windows.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_commethod(8)
    def get_Surface(self) -> Windows.UI.Composition.ICompositionSurface: ...
    @winrt_commethod(9)
    def put_Surface(self, value: Windows.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_commethod(10)
    def get_WrappingUMode(self) -> Windows.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_commethod(11)
    def put_WrappingUMode(self, value: Windows.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    @winrt_commethod(12)
    def get_WrappingVMode(self) -> Windows.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_commethod(13)
    def put_WrappingVMode(self, value: Windows.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    Surface = property(get_Surface, put_Surface)
    WrappingUMode = property(get_WrappingUMode, put_WrappingUMode)
    WrappingVMode = property(get_WrappingVMode, put_WrappingVMode)
class ISceneSurfaceMaterialInputStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5a2394d3-6429-4589-bb-cf-b8-4f-4f-3c-fb-fe')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneSurfaceMaterialInput: ...
class ISceneVisual(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8e672c1e-d734-47b1-be-14-3d-69-4f-fa-43-01')
    @winrt_commethod(6)
    def get_Root(self) -> Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_commethod(7)
    def put_Root(self, value: Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    Root = property(get_Root, put_Root)
class ISceneVisualStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b8347e9a-50aa-4527-8d-34-de-4c-b8-ea-88-b4')
    @winrt_commethod(6)
    def Create(self, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneVisual: ...
SceneAlphaMode = Int32
SceneAlphaMode_Opaque: SceneAlphaMode = 0
SceneAlphaMode_AlphaTest: SceneAlphaMode = 1
SceneAlphaMode_Blend: SceneAlphaMode = 2
SceneAttributeSemantic = Int32
SceneAttributeSemantic_Index: SceneAttributeSemantic = 0
SceneAttributeSemantic_Vertex: SceneAttributeSemantic = 1
SceneAttributeSemantic_Normal: SceneAttributeSemantic = 2
SceneAttributeSemantic_TexCoord0: SceneAttributeSemantic = 3
SceneAttributeSemantic_TexCoord1: SceneAttributeSemantic = 4
SceneAttributeSemantic_Color: SceneAttributeSemantic = 5
SceneAttributeSemantic_Tangent: SceneAttributeSemantic = 6
class SceneBoundingBox(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneObject
    ClassId = 'Windows.UI.Composition.Scenes.SceneBoundingBox'
    @winrt_mixinmethod
    def get_Center(self: Windows.UI.Composition.Scenes.ISceneBoundingBox) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Extents(self: Windows.UI.Composition.Scenes.ISceneBoundingBox) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Max(self: Windows.UI.Composition.Scenes.ISceneBoundingBox) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Min(self: Windows.UI.Composition.Scenes.ISceneBoundingBox) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Composition.Scenes.ISceneBoundingBox) -> Windows.Foundation.Numerics.Vector3: ...
    Center = property(get_Center, None)
    Extents = property(get_Extents, None)
    Max = property(get_Max, None)
    Min = property(get_Min, None)
    Size = property(get_Size, None)
class SceneComponent(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneObject
    @winrt_commethod(7)
    def get_ComponentType(self) -> Windows.UI.Composition.Scenes.SceneComponentType: ...
    ComponentType = property(get_ComponentType, None)
class SceneComponentCollection(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneObject
    ClassId = 'Windows.UI.Composition.Scenes.SceneComponentCollection'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent], index: UInt32) -> Windows.UI.Composition.Scenes.SceneComponent: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Composition.Scenes.SceneComponent]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent], value: Windows.UI.Composition.Scenes.SceneComponent, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent], index: UInt32, value: Windows.UI.Composition.Scenes.SceneComponent) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent], index: UInt32, value: Windows.UI.Composition.Scenes.SceneComponent) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent], value: Windows.UI.Composition.Scenes.SceneComponent) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent], startIndex: UInt32, items: POINTER(Windows.UI.Composition.Scenes.SceneComponent)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneComponent], items: POINTER(Windows.UI.Composition.Scenes.SceneComponent)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Scenes.SceneComponent]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.Scenes.SceneComponent]: ...
    Size = property(get_Size, None)
SceneComponentType = Int32
SceneComponentType_MeshRendererComponent: SceneComponentType = 0
class SceneMaterial(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneObject
class SceneMaterialInput(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneObject
class SceneMesh(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneObject
    ClassId = 'Windows.UI.Composition.Scenes.SceneMesh'
    @winrt_mixinmethod
    def get_Bounds(self: Windows.UI.Composition.Scenes.ISceneMesh) -> Windows.UI.Composition.Scenes.SceneBoundingBox: ...
    @winrt_mixinmethod
    def get_PrimitiveTopology(self: Windows.UI.Composition.Scenes.ISceneMesh) -> Windows.Graphics.DirectX.DirectXPrimitiveTopology: ...
    @winrt_mixinmethod
    def put_PrimitiveTopology(self: Windows.UI.Composition.Scenes.ISceneMesh, value: Windows.Graphics.DirectX.DirectXPrimitiveTopology) -> Void: ...
    @winrt_mixinmethod
    def FillMeshAttribute(self: Windows.UI.Composition.Scenes.ISceneMesh, semantic: Windows.UI.Composition.Scenes.SceneAttributeSemantic, format: Windows.Graphics.DirectX.DirectXPixelFormat, memory: Windows.Foundation.MemoryBuffer) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Scenes.ISceneMeshStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneMesh: ...
    Bounds = property(get_Bounds, None)
    PrimitiveTopology = property(get_PrimitiveTopology, put_PrimitiveTopology)
class SceneMeshMaterialAttributeMap(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneObject
    ClassId = 'Windows.UI.Composition.Scenes.SceneMeshMaterialAttributeMap'
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String) -> Windows.UI.Composition.Scenes.SceneAttributeSemantic: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic]) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic]: ...
    @winrt_mixinmethod
    def Insert(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String, value: Windows.UI.Composition.Scenes.SceneAttributeSemantic) -> Boolean: ...
    @winrt_mixinmethod
    def Remove(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic], key: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IMap[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic]) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.UI.Composition.Scenes.SceneAttributeSemantic]]: ...
    Size = property(get_Size, None)
class SceneMeshRendererComponent(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneRendererComponent
    ClassId = 'Windows.UI.Composition.Scenes.SceneMeshRendererComponent'
    @winrt_mixinmethod
    def get_Material(self: Windows.UI.Composition.Scenes.ISceneMeshRendererComponent) -> Windows.UI.Composition.Scenes.SceneMaterial: ...
    @winrt_mixinmethod
    def put_Material(self: Windows.UI.Composition.Scenes.ISceneMeshRendererComponent, value: Windows.UI.Composition.Scenes.SceneMaterial) -> Void: ...
    @winrt_mixinmethod
    def get_Mesh(self: Windows.UI.Composition.Scenes.ISceneMeshRendererComponent) -> Windows.UI.Composition.Scenes.SceneMesh: ...
    @winrt_mixinmethod
    def put_Mesh(self: Windows.UI.Composition.Scenes.ISceneMeshRendererComponent, value: Windows.UI.Composition.Scenes.SceneMesh) -> Void: ...
    @winrt_mixinmethod
    def get_UVMappings(self: Windows.UI.Composition.Scenes.ISceneMeshRendererComponent) -> Windows.UI.Composition.Scenes.SceneMeshMaterialAttributeMap: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Scenes.ISceneMeshRendererComponentStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneMeshRendererComponent: ...
    Material = property(get_Material, put_Material)
    Mesh = property(get_Mesh, put_Mesh)
    UVMappings = property(get_UVMappings, None)
class SceneMetallicRoughnessMaterial(c_void_p):
    extends: Windows.UI.Composition.Scenes.ScenePbrMaterial
    ClassId = 'Windows.UI.Composition.Scenes.SceneMetallicRoughnessMaterial'
    @winrt_mixinmethod
    def get_BaseColorInput(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def put_BaseColorInput(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_BaseColorFactor(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> Windows.Foundation.Numerics.Vector4: ...
    @winrt_mixinmethod
    def put_BaseColorFactor(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: Windows.Foundation.Numerics.Vector4) -> Void: ...
    @winrt_mixinmethod
    def get_MetallicFactor(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_MetallicFactor(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_MetallicRoughnessInput(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_mixinmethod
    def put_MetallicRoughnessInput(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_mixinmethod
    def get_RoughnessFactor(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial) -> Single: ...
    @winrt_mixinmethod
    def put_RoughnessFactor(self: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterial, value: Single) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Scenes.ISceneMetallicRoughnessMaterialStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneMetallicRoughnessMaterial: ...
    BaseColorInput = property(get_BaseColorInput, put_BaseColorInput)
    BaseColorFactor = property(get_BaseColorFactor, put_BaseColorFactor)
    MetallicFactor = property(get_MetallicFactor, put_MetallicFactor)
    MetallicRoughnessInput = property(get_MetallicRoughnessInput, put_MetallicRoughnessInput)
    RoughnessFactor = property(get_RoughnessFactor, put_RoughnessFactor)
class SceneModelTransform(c_void_p):
    extends: Windows.UI.Composition.CompositionTransform
    ClassId = 'Windows.UI.Composition.Scenes.SceneModelTransform'
    @winrt_mixinmethod
    def get_Orientation(self: Windows.UI.Composition.Scenes.ISceneModelTransform) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def put_Orientation(self: Windows.UI.Composition.Scenes.ISceneModelTransform, value: Windows.Foundation.Numerics.Quaternion) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: Windows.UI.Composition.Scenes.ISceneModelTransform) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: Windows.UI.Composition.Scenes.ISceneModelTransform, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngleInDegrees(self: Windows.UI.Composition.Scenes.ISceneModelTransform) -> Single: ...
    @winrt_mixinmethod
    def put_RotationAngleInDegrees(self: Windows.UI.Composition.Scenes.ISceneModelTransform, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAxis(self: Windows.UI.Composition.Scenes.ISceneModelTransform) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_RotationAxis(self: Windows.UI.Composition.Scenes.ISceneModelTransform, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: Windows.UI.Composition.Scenes.ISceneModelTransform) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Scale(self: Windows.UI.Composition.Scenes.ISceneModelTransform, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_mixinmethod
    def get_Translation(self: Windows.UI.Composition.Scenes.ISceneModelTransform) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def put_Translation(self: Windows.UI.Composition.Scenes.ISceneModelTransform, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    Orientation = property(get_Orientation, put_Orientation)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    RotationAngleInDegrees = property(get_RotationAngleInDegrees, put_RotationAngleInDegrees)
    RotationAxis = property(get_RotationAxis, put_RotationAxis)
    Scale = property(get_Scale, put_Scale)
    Translation = property(get_Translation, put_Translation)
class SceneNode(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneObject
    ClassId = 'Windows.UI.Composition.Scenes.SceneNode'
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Composition.Scenes.ISceneNode) -> Windows.UI.Composition.Scenes.SceneNodeCollection: ...
    @winrt_mixinmethod
    def get_Components(self: Windows.UI.Composition.Scenes.ISceneNode) -> Windows.UI.Composition.Scenes.SceneComponentCollection: ...
    @winrt_mixinmethod
    def get_Parent(self: Windows.UI.Composition.Scenes.ISceneNode) -> Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_mixinmethod
    def get_Transform(self: Windows.UI.Composition.Scenes.ISceneNode) -> Windows.UI.Composition.Scenes.SceneModelTransform: ...
    @winrt_mixinmethod
    def FindFirstComponentOfType(self: Windows.UI.Composition.Scenes.ISceneNode, value: Windows.UI.Composition.Scenes.SceneComponentType) -> Windows.UI.Composition.Scenes.SceneComponent: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Scenes.ISceneNodeStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneNode: ...
    Children = property(get_Children, None)
    Components = property(get_Components, None)
    Parent = property(get_Parent, None)
    Transform = property(get_Transform, None)
class SceneNodeCollection(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneObject
    ClassId = 'Windows.UI.Composition.Scenes.SceneNodeCollection'
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode], index: UInt32) -> Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Composition.Scenes.SceneNode]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode], value: Windows.UI.Composition.Scenes.SceneNode, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode], index: UInt32, value: Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode], index: UInt32, value: Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode], value: Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode], startIndex: UInt32, items: POINTER(Windows.UI.Composition.Scenes.SceneNode)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Composition.Scenes.SceneNode], items: POINTER(Windows.UI.Composition.Scenes.SceneNode)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Composition.Scenes.SceneNode]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Composition.Scenes.SceneNode]: ...
    Size = property(get_Size, None)
class SceneObject(c_void_p):
    extends: Windows.UI.Composition.CompositionObject
class ScenePbrMaterial(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneMaterial
    @winrt_commethod(24)
    def get_AlphaCutoff(self) -> Single: ...
    @winrt_commethod(25)
    def put_AlphaCutoff(self, value: Single) -> Void: ...
    @winrt_commethod(26)
    def get_AlphaMode(self) -> Windows.UI.Composition.Scenes.SceneAlphaMode: ...
    @winrt_commethod(27)
    def put_AlphaMode(self, value: Windows.UI.Composition.Scenes.SceneAlphaMode) -> Void: ...
    @winrt_commethod(28)
    def get_EmissiveInput(self) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(29)
    def put_EmissiveInput(self, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(30)
    def get_EmissiveFactor(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(31)
    def put_EmissiveFactor(self, value: Windows.Foundation.Numerics.Vector3) -> Void: ...
    @winrt_commethod(32)
    def get_IsDoubleSided(self) -> Boolean: ...
    @winrt_commethod(33)
    def put_IsDoubleSided(self, value: Boolean) -> Void: ...
    @winrt_commethod(34)
    def get_NormalInput(self) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(35)
    def put_NormalInput(self, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(36)
    def get_NormalScale(self) -> Single: ...
    @winrt_commethod(37)
    def put_NormalScale(self, value: Single) -> Void: ...
    @winrt_commethod(38)
    def get_OcclusionInput(self) -> Windows.UI.Composition.Scenes.SceneMaterialInput: ...
    @winrt_commethod(39)
    def put_OcclusionInput(self, value: Windows.UI.Composition.Scenes.SceneMaterialInput) -> Void: ...
    @winrt_commethod(40)
    def get_OcclusionStrength(self) -> Single: ...
    @winrt_commethod(41)
    def put_OcclusionStrength(self, value: Single) -> Void: ...
    AlphaCutoff = property(get_AlphaCutoff, put_AlphaCutoff)
    AlphaMode = property(get_AlphaMode, put_AlphaMode)
    EmissiveInput = property(get_EmissiveInput, put_EmissiveInput)
    EmissiveFactor = property(get_EmissiveFactor, put_EmissiveFactor)
    IsDoubleSided = property(get_IsDoubleSided, put_IsDoubleSided)
    NormalInput = property(get_NormalInput, put_NormalInput)
    NormalScale = property(get_NormalScale, put_NormalScale)
    OcclusionInput = property(get_OcclusionInput, put_OcclusionInput)
    OcclusionStrength = property(get_OcclusionStrength, put_OcclusionStrength)
class SceneRendererComponent(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneComponent
class SceneSurfaceMaterialInput(c_void_p):
    extends: Windows.UI.Composition.Scenes.SceneMaterialInput
    ClassId = 'Windows.UI.Composition.Scenes.SceneSurfaceMaterialInput'
    @winrt_mixinmethod
    def get_BitmapInterpolationMode(self: Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> Windows.UI.Composition.CompositionBitmapInterpolationMode: ...
    @winrt_mixinmethod
    def put_BitmapInterpolationMode(self: Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: Windows.UI.Composition.CompositionBitmapInterpolationMode) -> Void: ...
    @winrt_mixinmethod
    def get_Surface(self: Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> Windows.UI.Composition.ICompositionSurface: ...
    @winrt_mixinmethod
    def put_Surface(self: Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: Windows.UI.Composition.ICompositionSurface) -> Void: ...
    @winrt_mixinmethod
    def get_WrappingUMode(self: Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> Windows.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_mixinmethod
    def put_WrappingUMode(self: Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: Windows.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    @winrt_mixinmethod
    def get_WrappingVMode(self: Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput) -> Windows.UI.Composition.Scenes.SceneWrappingMode: ...
    @winrt_mixinmethod
    def put_WrappingVMode(self: Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInput, value: Windows.UI.Composition.Scenes.SceneWrappingMode) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Scenes.ISceneSurfaceMaterialInputStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneSurfaceMaterialInput: ...
    BitmapInterpolationMode = property(get_BitmapInterpolationMode, put_BitmapInterpolationMode)
    Surface = property(get_Surface, put_Surface)
    WrappingUMode = property(get_WrappingUMode, put_WrappingUMode)
    WrappingVMode = property(get_WrappingVMode, put_WrappingVMode)
class SceneVisual(c_void_p):
    extends: Windows.UI.Composition.ContainerVisual
    ClassId = 'Windows.UI.Composition.Scenes.SceneVisual'
    @winrt_mixinmethod
    def get_Root(self: Windows.UI.Composition.Scenes.ISceneVisual) -> Windows.UI.Composition.Scenes.SceneNode: ...
    @winrt_mixinmethod
    def put_Root(self: Windows.UI.Composition.Scenes.ISceneVisual, value: Windows.UI.Composition.Scenes.SceneNode) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.UI.Composition.Scenes.ISceneVisualStatics, compositor: Windows.UI.Composition.Compositor) -> Windows.UI.Composition.Scenes.SceneVisual: ...
    Root = property(get_Root, put_Root)
SceneWrappingMode = Int32
SceneWrappingMode_ClampToEdge: SceneWrappingMode = 0
SceneWrappingMode_MirroredRepeat: SceneWrappingMode = 1
SceneWrappingMode_Repeat: SceneWrappingMode = 2
make_head(_module, 'ISceneBoundingBox')
make_head(_module, 'ISceneComponent')
make_head(_module, 'ISceneComponentCollection')
make_head(_module, 'ISceneComponentFactory')
make_head(_module, 'ISceneMaterial')
make_head(_module, 'ISceneMaterialFactory')
make_head(_module, 'ISceneMaterialInput')
make_head(_module, 'ISceneMaterialInputFactory')
make_head(_module, 'ISceneMesh')
make_head(_module, 'ISceneMeshMaterialAttributeMap')
make_head(_module, 'ISceneMeshRendererComponent')
make_head(_module, 'ISceneMeshRendererComponentStatics')
make_head(_module, 'ISceneMeshStatics')
make_head(_module, 'ISceneMetallicRoughnessMaterial')
make_head(_module, 'ISceneMetallicRoughnessMaterialStatics')
make_head(_module, 'ISceneModelTransform')
make_head(_module, 'ISceneNode')
make_head(_module, 'ISceneNodeCollection')
make_head(_module, 'ISceneNodeStatics')
make_head(_module, 'ISceneObject')
make_head(_module, 'ISceneObjectFactory')
make_head(_module, 'IScenePbrMaterial')
make_head(_module, 'IScenePbrMaterialFactory')
make_head(_module, 'ISceneRendererComponent')
make_head(_module, 'ISceneRendererComponentFactory')
make_head(_module, 'ISceneSurfaceMaterialInput')
make_head(_module, 'ISceneSurfaceMaterialInputStatics')
make_head(_module, 'ISceneVisual')
make_head(_module, 'ISceneVisualStatics')
make_head(_module, 'SceneBoundingBox')
make_head(_module, 'SceneComponent')
make_head(_module, 'SceneComponentCollection')
make_head(_module, 'SceneMaterial')
make_head(_module, 'SceneMaterialInput')
make_head(_module, 'SceneMesh')
make_head(_module, 'SceneMeshMaterialAttributeMap')
make_head(_module, 'SceneMeshRendererComponent')
make_head(_module, 'SceneMetallicRoughnessMaterial')
make_head(_module, 'SceneModelTransform')
make_head(_module, 'SceneNode')
make_head(_module, 'SceneNodeCollection')
make_head(_module, 'SceneObject')
make_head(_module, 'ScenePbrMaterial')
make_head(_module, 'SceneRendererComponent')
make_head(_module, 'SceneSurfaceMaterialInput')
make_head(_module, 'SceneVisual')
