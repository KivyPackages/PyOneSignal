from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationRestoreProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/restoration/INotificationRestoreProcessor"
    process = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    processNotification = JavaMethod("(Lcom/onesignal/notifications/internal/data/INotificationRepository$NotificationData;ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/restoration/INotificationRestoreProcessor$DefaultImpls"
        processNotification$default = JavaStaticMethod("(Lcom/onesignal/notifications/internal/restoration/INotificationRestoreProcessor;Lcom/onesignal/notifications/internal/data/INotificationRepository$NotificationData;ILkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")

class INotificationRestoreWorkManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/restoration/INotificationRestoreWorkManager"
    beginEnqueueingWork = JavaMethod("(Landroid/content/Context;Z)V")