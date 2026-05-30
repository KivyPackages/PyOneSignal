from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationSummaryManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/summary/INotificationSummaryManager"
    updatePossibleDependentSummaryOnDismiss = JavaMethod("(ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    updateSummaryNotificationAfterChildRemoved = JavaMethod("(Ljava/lang/String;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    clearNotificationOnSummaryClick = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")