from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AlertDialogPrepromptForAndroidSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/permissions/AlertDialogPrepromptForAndroidSettings"
    INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/permissions/AlertDialogPrepromptForAndroidSettings;")
    show = JavaMultipleMethod([("(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/core/internal/permissions/AlertDialogPrepromptForAndroidSettings$Callback;)V", False, False), ("(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/core/internal/permissions/AlertDialogPrepromptForAndroidSettings$Callback;Lkotlin/jvm/functions/Function0;)V", False, False)])
    dismissCurrentDialog = JavaMethod("()V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/permissions/AlertDialogPrepromptForAndroidSettings$Callback"
        onDecline = JavaMethod("()V")
        onAccept = JavaMethod("()V")

class IRequestPermissionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/permissions/IRequestPermissionService"
    startPrompt = JavaMethod("(ZLjava/lang/String;Ljava/lang/String;Ljava/lang/Class;)V")
    registerAsCallback = JavaMethod("(Ljava/lang/String;Lcom/onesignal/core/internal/permissions/IRequestPermissionService$PermissionCallback;)V")

    class PermissionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/permissions/IRequestPermissionService$PermissionCallback"
        onAccept = JavaMethod("()V")
        onReject = JavaMethod("(Z)V")

class PermissionsViewModel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/permissions/PermissionsViewModel"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/permissions/PermissionsViewModel$Companion;")
    DELAY_TIME_CALLBACK_CALL = JavaStaticField("I")
    ONESIGNAL_PERMISSION_REQUEST_CODE = JavaStaticField("I")
    INTENT_EXTRA_PERMISSION_TYPE = JavaStaticField("Ljava/lang/String;")
    INTENT_EXTRA_ANDROID_PERMISSION_STRING = JavaStaticField("Ljava/lang/String;")
    INTENT_EXTRA_CALLBACK_CLASS = JavaStaticField("Ljava/lang/String;")
    initialize = JavaMethod("(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    onRequestPermissionsResult = JavaMethod("([Ljava/lang/String;[IZ)V")
    getShouldFinish = JavaMethod("()Lkotlinx/coroutines/flow/StateFlow;")
    getWaiting = JavaMethod("()Lkotlinx/coroutines/flow/StateFlow;")
    getPermissionRequestType = JavaMethod("()Ljava/lang/String;")
    onRequestPermissionsResult$default = JavaStaticMethod("(Lcom/onesignal/core/internal/permissions/PermissionsViewModel;[Ljava/lang/String;[IZILjava/lang/Object;)V")
    access$getPreferenceService = JavaStaticMethod("(Lcom/onesignal/core/internal/permissions/PermissionsViewModel;)Lcom/onesignal/core/internal/preferences/IPreferencesService;")
    access$shouldShowSettings = JavaStaticMethod("(Lcom/onesignal/core/internal/permissions/PermissionsViewModel;Ljava/lang/String;Z)Z")
    access$executeCallback = JavaStaticMethod("(Lcom/onesignal/core/internal/permissions/PermissionsViewModel;ZZ)V")
    access$get_shouldFinish$p = JavaStaticMethod("(Lcom/onesignal/core/internal/permissions/PermissionsViewModel;)Lkotlinx/coroutines/flow/MutableStateFlow;")
    resetWaitingState = JavaMethod("()V")
    shouldRequestPermission = JavaMethod("()Z")
    recordRationaleState = JavaMethod("(Z)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/permissions/PermissionsViewModel$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]