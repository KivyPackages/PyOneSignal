from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationGenerationProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/generation/impl/NotificationGenerationProcessor"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/notifications/internal/display/INotificationDisplayer;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/notifications/internal/data/INotificationRepository;Lcom/onesignal/notifications/internal/summary/INotificationSummaryManager;Lcom/onesignal/notifications/internal/lifecycle/INotificationLifecycleService;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    processNotificationData = JavaMethod("(Landroid/content/Context;ILorg/json/JSONObject;ZJLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$get_lifecycleService$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/generation/impl/NotificationGenerationProcessor;)Lcom/onesignal/notifications/internal/lifecycle/INotificationLifecycleService;")
    access$processHandlerResponse = JavaStaticMethod("(Lcom/onesignal/notifications/internal/generation/impl/NotificationGenerationProcessor;Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;ZZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$isDuplicateNotification = JavaStaticMethod("(Lcom/onesignal/notifications/internal/generation/impl/NotificationGenerationProcessor;Lcom/onesignal/notifications/internal/Notification;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$postProcessNotification = JavaStaticMethod("(Lcom/onesignal/notifications/internal/generation/impl/NotificationGenerationProcessor;Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;ZZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$saveNotification = JavaStaticMethod("(Lcom/onesignal/notifications/internal/generation/impl/NotificationGenerationProcessor;Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$markNotificationAsDismissed = JavaStaticMethod("(Lcom/onesignal/notifications/internal/generation/impl/NotificationGenerationProcessor;Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$processCollapseKey = JavaStaticMethod("(Lcom/onesignal/notifications/internal/generation/impl/NotificationGenerationProcessor;Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getCustomJSONObject = JavaMethod("(Lorg/json/JSONObject;)Lorg/json/JSONObject;")

class NotificationGenerationWorkManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/generation/impl/NotificationGenerationWorkManager"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/generation/impl/NotificationGenerationWorkManager$Companion;")
    beginEnqueueingWork = JavaMethod("(Landroid/content/Context;Ljava/lang/String;ILorg/json/JSONObject;JZZ)Z")
    access$getNotificationIds$cp = JavaStaticMethod("()Ljava/util/concurrent/ConcurrentHashMap;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/generation/impl/NotificationGenerationWorkManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        addNotificationIdProcessed = JavaMethod("(Ljava/lang/String;)Z")
        removeNotificationIdProcessed = JavaMethod("(Ljava/lang/String;)V")

    class NotificationGenerationWorker(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/generation/impl/NotificationGenerationWorkManager$NotificationGenerationWorker"
        __javaconstructor__ = [("(Landroid/content/Context;Landroidx/work/WorkerParameters;)V", False)]
        doWork = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")