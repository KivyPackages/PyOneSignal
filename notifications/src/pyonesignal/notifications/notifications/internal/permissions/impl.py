from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NavigateToAndroidSettingsForNotifications(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/permissions/impl/NavigateToAndroidSettingsForNotifications"
    INSTANCE = JavaStaticField("Lcom/onesignal/notifications/internal/permissions/impl/NavigateToAndroidSettingsForNotifications;")
    show = JavaMethod("(Landroid/content/Context;)V")

class NotificationPermissionController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/permissions/impl/NotificationPermissionController"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/permissions/IRequestPermissionService;Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/preferences/IPreferencesService;Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/permissions/impl/NotificationPermissionController$Companion;")
    subscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/notifications/internal/permissions/INotificationPermissionChangedHandler;)V", False, False)])
    getCanRequestPermission = JavaMethod("()Z")
    unsubscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/notifications/internal/permissions/INotificationPermissionChangedHandler;)V", False, False)])
    getSupportsNativePrompt = JavaMethod("()Z")
    onAccept = JavaMethod("()V")
    onReject = JavaMethod("(Z)V")
    access$setPollingWaitInterval$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/permissions/impl/NotificationPermissionController;J)V")
    access$get_configModelStore$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/permissions/impl/NotificationPermissionController;)Lcom/onesignal/core/internal/config/ConfigModelStore;")
    access$getPollingWaiter$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/permissions/impl/NotificationPermissionController;)Lcom/onesignal/common/threading/Waiter;")
    access$pollForPermission = JavaStaticMethod("(Lcom/onesignal/notifications/internal/permissions/impl/NotificationPermissionController;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$permissionPromptCompleted = JavaStaticMethod("(Lcom/onesignal/notifications/internal/permissions/impl/NotificationPermissionController;Z)V")
    prompt = JavaMethod("(ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getHasSubscribers = JavaMethod("()Z")
    access$get_applicationService$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/permissions/impl/NotificationPermissionController;)Lcom/onesignal/core/internal/application/IApplicationService;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/permissions/impl/NotificationPermissionController$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]