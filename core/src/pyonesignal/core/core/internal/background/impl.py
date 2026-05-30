from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class BackgroundManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/background/impl/BackgroundManager"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/time/ITime;Ljava/util/List;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/background/impl/BackgroundManager$Companion;")
    start = JavaMethod("()V")
    setNeedsJobReschedule = JavaMethod("(Z)V")
    cancelRunBackgroundServices = JavaMethod("()Z")
    runBackgroundServices = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getNeedsJobReschedule = JavaMethod("()Z")
    access$cancelSyncTask = JavaStaticMethod("(Lcom/onesignal/core/internal/background/impl/BackgroundManager;)V")
    access$scheduleBackground = JavaStaticMethod("(Lcom/onesignal/core/internal/background/impl/BackgroundManager;)V")
    access$setBackgroundSyncJob$p = JavaStaticMethod("(Lcom/onesignal/core/internal/background/impl/BackgroundManager;Lkotlinx/coroutines/Job;)V")
    access$getLock$p = JavaStaticMethod("(Lcom/onesignal/core/internal/background/impl/BackgroundManager;)Ljava/lang/Object;")
    access$get_backgroundServices$p = JavaStaticMethod("(Lcom/onesignal/core/internal/background/impl/BackgroundManager;)Ljava/util/List;")
    access$setNextScheduledSyncTimeMs$p = JavaStaticMethod("(Lcom/onesignal/core/internal/background/impl/BackgroundManager;J)V")
    onFocus = JavaMethod("(Z)V")
    onUnfocused = JavaMethod("()V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/background/impl/BackgroundManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]