from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IDeviceService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/device/IDeviceService"
    isGMSInstalledAndEnabled = JavaMethod("()Z")
    isAndroidDeviceType = JavaMethod("()Z")
    isFireOSDeviceType = JavaMethod("()Z")
    isHuaweiDeviceType = JavaMethod("()Z")
    getDeviceType = JavaMethod("()Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
    getHasAllHMSLibrariesForPushKit = JavaMethod("()Z")
    getHasFCMLibrary = JavaMethod("()Z")
    getJetpackLibraryStatus = JavaMethod("()Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
    getSupportsHMS = JavaMethod("()Z")
    supportsGooglePush = JavaMethod("()Z")

    class DeviceType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/device/IDeviceService$DeviceType"
        Fire = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        Android = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        Huawei = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        values = JavaStaticMethod("()[Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        getValue = JavaMethod("()I")
        getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
        Fire = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        Android = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        Huawei = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")

    class JetpackLibraryStatus(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus"
        MISSING = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        OUTDATED = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        OK = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        values = JavaStaticMethod("()[Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
        MISSING = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        OUTDATED = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        OK = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")

class IInstallIdService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/device/IInstallIdService"
    getId = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")