from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class MisconfiguredNotificationsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/MisconfiguredNotificationsManager"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/MisconfiguredNotificationsManager$Companion;")
    getPermission = JavaMultipleMethod([("()Ljava/lang/Void;", False, False), ("()Z", False, False)])
    requestPermission = JavaMethod("(ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getCanRequestPermission = JavaMultipleMethod([("()Z", False, False), ("()Ljava/lang/Void;", False, False)])
    removeNotification = JavaMultipleMethod([("(I)Ljava/lang/Void;", False, False), ("(I)V", False, False)])
    removeGroupedNotifications = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/Void;", False, False), ("(Ljava/lang/String;)V", False, False)])
    clearAllNotifications = JavaMultipleMethod([("()V", False, False), ("()Ljava/lang/Void;", False, False)])
    addPermissionObserver = JavaMultipleMethod([("(Lcom/onesignal/notifications/IPermissionObserver;)V", False, False), ("(Lcom/onesignal/notifications/IPermissionObserver;)Ljava/lang/Void;", False, False)])
    removePermissionObserver = JavaMultipleMethod([("(Lcom/onesignal/notifications/IPermissionObserver;)Ljava/lang/Void;", False, False), ("(Lcom/onesignal/notifications/IPermissionObserver;)V", False, False)])
    addForegroundLifecycleListener = JavaMultipleMethod([("(Lcom/onesignal/notifications/INotificationLifecycleListener;)V", False, False), ("(Lcom/onesignal/notifications/INotificationLifecycleListener;)Ljava/lang/Void;", False, False)])
    removeForegroundLifecycleListener = JavaMultipleMethod([("(Lcom/onesignal/notifications/INotificationLifecycleListener;)V", False, False), ("(Lcom/onesignal/notifications/INotificationLifecycleListener;)Ljava/lang/Void;", False, False)])
    addClickListener = JavaMultipleMethod([("(Lcom/onesignal/notifications/INotificationClickListener;)V", False, False), ("(Lcom/onesignal/notifications/INotificationClickListener;)Ljava/lang/Void;", False, False)])
    removeClickListener = JavaMultipleMethod([("(Lcom/onesignal/notifications/INotificationClickListener;)V", False, False), ("(Lcom/onesignal/notifications/INotificationClickListener;)Ljava/lang/Void;", False, False)])

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/MisconfiguredNotificationsManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        access$getEXCEPTION = JavaStaticMethod("(Lcom/onesignal/notifications/internal/MisconfiguredNotificationsManager$Companion;)Ljava/lang/Exception;")