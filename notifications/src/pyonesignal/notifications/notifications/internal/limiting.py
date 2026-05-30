from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationLimitManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/limiting/INotificationLimitManager"
    clearOldestOverLimit = JavaMethod("(ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class Constants(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/limiting/INotificationLimitManager$Constants"
        INSTANCE = JavaStaticField("Lcom/onesignal/notifications/internal/limiting/INotificationLimitManager$Constants;")
        getMaxNumberOfNotifications = JavaMethod("()I")