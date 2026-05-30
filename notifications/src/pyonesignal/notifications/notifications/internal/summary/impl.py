from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationSummaryManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/summary/impl/NotificationSummaryManager"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/notifications/internal/data/INotificationRepository;Lcom/onesignal/notifications/internal/display/ISummaryNotificationDisplayer;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/notifications/internal/restoration/INotificationRestoreProcessor;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    updatePossibleDependentSummaryOnDismiss = JavaMethod("(ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    updateSummaryNotificationAfterChildRemoved = JavaMethod("(Ljava/lang/String;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    clearNotificationOnSummaryClick = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$restoreSummary = JavaStaticMethod("(Lcom/onesignal/notifications/internal/summary/impl/NotificationSummaryManager;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$internalUpdateSummaryNotificationAfterChildRemoved = JavaStaticMethod("(Lcom/onesignal/notifications/internal/summary/impl/NotificationSummaryManager;Ljava/lang/String;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")