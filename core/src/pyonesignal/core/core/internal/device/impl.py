from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DeviceService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/device/impl/DeviceService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/device/impl/DeviceService$Companion;")
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

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/device/impl/DeviceService$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class InstallIdService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/device/impl/InstallIdService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)V", False)]
    getId = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$get_prefs$p = JavaStaticMethod("(Lcom/onesignal/core/internal/device/impl/InstallIdService;)Lcom/onesignal/core/internal/preferences/IPreferencesService;")