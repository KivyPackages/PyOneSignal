from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SessionListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/session/impl/SessionListener"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/session/internal/session/ISessionService;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/session/internal/outcomes/IOutcomeEventsController;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/session/internal/session/impl/SessionListener$Companion;")
    SECONDS_IN_A_DAY = JavaStaticField("J")
    start = JavaMethod("()V")
    access$get_outcomeEventsController$p = JavaStaticMethod("(Lcom/onesignal/session/internal/session/impl/SessionListener;)Lcom/onesignal/session/internal/outcomes/IOutcomeEventsController;")
    onSessionStarted = JavaMethod("()V")
    onSessionActive = JavaMethod("()V")
    onSessionEnded = JavaMethod("(J)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/session/internal/session/impl/SessionListener$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class SessionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/session/impl/SessionService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/session/internal/session/SessionModelStore;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    access$handleOnFocus = JavaStaticMethod("(Lcom/onesignal/session/internal/session/impl/SessionService;ZJ)V")
    access$handleOnUnfocused = JavaStaticMethod("(Lcom/onesignal/session/internal/session/impl/SessionService;J)V")
    bootstrap = JavaMethod("()V")
    start = JavaMethod("()V")
    getStartTime = JavaMethod("()J")
    getHasSubscribers = JavaMethod("()Z")
    subscribe = JavaMultipleMethod([("(Lcom/onesignal/session/internal/session/ISessionLifecycleHandler;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    unsubscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/session/internal/session/ISessionLifecycleHandler;)V", False, False)])
    backgroundRun = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getScheduleBackgroundRunIn = JavaMethod("()Ljava/lang/Long;")
    onFocus = JavaMethod("(Z)V")
    onUnfocused = JavaMethod("()V")