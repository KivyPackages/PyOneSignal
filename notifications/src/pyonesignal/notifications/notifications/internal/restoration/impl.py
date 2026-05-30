from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationRestoreProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/restoration/impl/NotificationRestoreProcessor"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/notifications/internal/generation/INotificationGenerationWorkManager;Lcom/onesignal/notifications/internal/data/INotificationRepository;Lcom/onesignal/notifications/internal/badges/IBadgeCountUpdater;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/restoration/impl/NotificationRestoreProcessor$Companion;")
    DEFAULT_TTL_IF_NOT_IN_PAYLOAD = JavaStaticField("I")
    process = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    processNotification = JavaMethod("(Lcom/onesignal/notifications/internal/data/INotificationRepository$NotificationData;ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/restoration/impl/NotificationRestoreProcessor$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class NotificationRestoreWorkManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/restoration/impl/NotificationRestoreWorkManager"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/restoration/impl/NotificationRestoreWorkManager$Companion;")
    beginEnqueueingWork = JavaMethod("(Landroid/content/Context;Z)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/restoration/impl/NotificationRestoreWorkManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class NotificationRestoreWorker(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/restoration/impl/NotificationRestoreWorkManager$NotificationRestoreWorker"
        __javaconstructor__ = [("(Landroid/content/Context;Landroidx/work/WorkerParameters;)V", False)]
        doWork = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")