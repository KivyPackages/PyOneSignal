from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class GooglePlayServicesUpgradePrompt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/registration/impl/GooglePlayServicesUpgradePrompt"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/device/IDeviceService;Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/registration/impl/GooglePlayServicesUpgradePrompt$Companion;")
    access$get_configModelStore$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/registration/impl/GooglePlayServicesUpgradePrompt;)Lcom/onesignal/core/internal/config/ConfigModelStore;")
    showUpdateGPSDialog = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$openPlayStoreToApp = JavaStaticMethod("(Lcom/onesignal/notifications/internal/registration/impl/GooglePlayServicesUpgradePrompt;Landroid/app/Activity;)V")
    access$get_applicationService$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/registration/impl/GooglePlayServicesUpgradePrompt;)Lcom/onesignal/core/internal/application/IApplicationService;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/registration/impl/GooglePlayServicesUpgradePrompt$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class IPushRegistratorCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/registration/impl/IPushRegistratorCallback"
    fireCallback = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class PushRegistratorADM(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/registration/impl/PushRegistratorADM"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;)V", False)]
    registerForPush = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    fireCallback = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$getWaiter$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/registration/impl/PushRegistratorADM;)Lcom/onesignal/common/threading/WaiterWithValue;")

class PushRegistratorAbstractGoogle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/registration/impl/PushRegistratorAbstractGoogle"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/device/IDeviceService;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/notifications/internal/registration/impl/GooglePlayServicesUpgradePrompt;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/registration/impl/PushRegistratorAbstractGoogle$Companion;")
    registerForPush = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getToken = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    fireCallback = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getProviderName = JavaMethod("()Ljava/lang/String;")
    access$internalRegisterForPush = JavaStaticMethod("(Lcom/onesignal/notifications/internal/registration/impl/PushRegistratorAbstractGoogle;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$registerInBackground = JavaStaticMethod("(Lcom/onesignal/notifications/internal/registration/impl/PushRegistratorAbstractGoogle;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$attemptRegistration = JavaStaticMethod("(Lcom/onesignal/notifications/internal/registration/impl/PushRegistratorAbstractGoogle;Ljava/lang/String;ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/registration/impl/PushRegistratorAbstractGoogle$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class PushRegistratorFCM(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/registration/impl/PushRegistratorFCM"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/notifications/internal/registration/impl/GooglePlayServicesUpgradePrompt;Lcom/onesignal/core/internal/device/IDeviceService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/registration/impl/PushRegistratorFCM$Companion;")
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/registration/impl/PushRegistratorAbstractGoogle$Companion;")
    getToken = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getProviderName = JavaMethod("()Ljava/lang/String;")
    get_configModelStore = JavaMethod("()Lcom/onesignal/core/internal/config/ConfigModelStore;")
    set_configModelStore = JavaMethod("(Lcom/onesignal/core/internal/config/ConfigModelStore;)V")
    get_applicationService = JavaMethod("()Lcom/onesignal/core/internal/application/IApplicationService;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/registration/impl/PushRegistratorFCM$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class PushRegistratorNone(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/registration/impl/PushRegistratorNone"
    __javaconstructor__ = [("()V", False)]
    registerForPush = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    fireCallback = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")