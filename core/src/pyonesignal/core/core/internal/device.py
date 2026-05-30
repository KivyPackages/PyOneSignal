from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IDeviceService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/device/IDeviceService"
    isFireOSDeviceType = JavaMethod("()Z")
    isAndroidDeviceType = JavaMethod("()Z")
    isHuaweiDeviceType = JavaMethod("()Z")
    getHasAllHMSLibrariesForPushKit = JavaMethod("()Z")
    getHasFCMLibrary = JavaMethod("()Z")
    getJetpackLibraryStatus = JavaMethod("()Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
    getSupportsHMS = JavaMethod("()Z")
    supportsGooglePush = JavaMethod("()Z")
    getDeviceType = JavaMethod("()Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
    isGMSInstalledAndEnabled = JavaMethod("()Z")

    class DeviceType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/device/IDeviceService$DeviceType"
        Fire = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        Android = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        Huawei = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
        values = JavaStaticMethod("()[Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        getValue = JavaMethod("()I")
        Fire = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        Android = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")
        Huawei = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;")

    class JetpackLibraryStatus(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus"
        MISSING = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        OUTDATED = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        OK = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
        values = JavaStaticMethod("()[Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        MISSING = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        OUTDATED = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")
        OK = JavaStaticField("Lcom/onesignal/core/internal/device/IDeviceService$JetpackLibraryStatus;")

class IInstallIdService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/device/IInstallIdService"
    getId = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")