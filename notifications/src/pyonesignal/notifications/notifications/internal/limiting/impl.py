from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationLimitManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/limiting/impl/NotificationLimitManager"
    __javaconstructor__ = [("(Lcom/onesignal/notifications/internal/data/INotificationRepository;Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/notifications/internal/summary/INotificationSummaryManager;)V", False)]
    clearOldestOverLimit = JavaMethod("(ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$clearOldestOverLimitStandard = JavaStaticMethod("(Lcom/onesignal/notifications/internal/limiting/impl/NotificationLimitManager;ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")