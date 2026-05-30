from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IBackgroundManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/background/IBackgroundManager"
    setNeedsJobReschedule = JavaMethod("(Z)V")
    cancelRunBackgroundServices = JavaMethod("()Z")
    runBackgroundServices = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getNeedsJobReschedule = JavaMethod("()Z")

class IBackgroundService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/background/IBackgroundService"
    backgroundRun = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getScheduleBackgroundRunIn = JavaMethod("()Ljava/lang/Long;")