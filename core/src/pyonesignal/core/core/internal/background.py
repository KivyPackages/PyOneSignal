from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IBackgroundManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/background/IBackgroundManager"
    runBackgroundServices = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    cancelRunBackgroundServices = JavaMethod("()Z")
    getNeedsJobReschedule = JavaMethod("()Z")
    setNeedsJobReschedule = JavaMethod("(Z)V")

class IBackgroundService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/background/IBackgroundService"
    backgroundRun = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getScheduleBackgroundRunIn = JavaMethod("()Ljava/lang/Long;")