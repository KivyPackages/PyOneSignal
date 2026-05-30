from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IntentGeneratorForAttachingToNotifications(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/display/impl/IntentGeneratorForAttachingToNotifications"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    getContext = JavaMethod("()Landroid/content/Context;")
    getNewActionPendingIntent = JavaMethod("(ILandroid/content/Intent;)Landroid/app/PendingIntent;")
    getNewBaseIntent = JavaMethod("(I)Landroid/content/Intent;")

class NotificationDisplayBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/display/impl/NotificationDisplayBuilder"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/notifications/internal/channels/INotificationChannelManager;)V", False)]
    getTitle = JavaMethod("(Lorg/json/JSONObject;)Ljava/lang/CharSequence;")
    getDefaultLargeIcon = JavaMethod("()Landroid/graphics/Bitmap;")
    getDefaultSmallIconId = JavaMethod("()I")
    getGroupAlertBehavior = JavaMethod("()I")
    getNewDismissActionPendingIntent = JavaMethod("(ILandroid/content/Intent;)Landroid/app/PendingIntent;")
    getNewBaseDismissIntent = JavaMethod("(I)Landroid/content/Intent;")
    getBaseOneSignalNotificationBuilder = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;)Lcom/onesignal/notifications/internal/display/impl/NotificationDisplayBuilder$OneSignalNotificationBuilder;")
    removeNotifyOptions = JavaMethod("(Landroidx/core/app/NotificationCompat$Builder;)V")
    addXiaomiSettings = JavaMethod("(Lcom/onesignal/notifications/internal/display/impl/NotificationDisplayBuilder$OneSignalNotificationBuilder;Landroid/app/Notification;)V")
    addNotificationActionButtons = JavaMethod("(Lorg/json/JSONObject;Lcom/onesignal/notifications/internal/display/impl/IntentGeneratorForAttachingToNotifications;Landroidx/core/app/NotificationCompat$Builder;ILjava/lang/String;)V")

    class OneSignalNotificationBuilder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/display/impl/NotificationDisplayBuilder$OneSignalNotificationBuilder"
        __javaconstructor__ = [("()V", False)]
        getCompatBuilder = JavaMethod("()Landroidx/core/app/NotificationCompat$Builder;")
        setCompatBuilder = JavaMethod("(Landroidx/core/app/NotificationCompat$Builder;)V")
        getHasLargeIcon = JavaMethod("()Z")
        setHasLargeIcon = JavaMethod("(Z)V")

class NotificationDisplayer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/display/impl/NotificationDisplayer"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/notifications/internal/limiting/INotificationLimitManager;Lcom/onesignal/notifications/internal/display/ISummaryNotificationDisplayer;Lcom/onesignal/notifications/internal/display/INotificationDisplayBuilder;)V", False)]
    isRunningOnMainThreadCheck = JavaMethod("()Lkotlin/Unit;")
    access$showNotification = JavaStaticMethod("(Lcom/onesignal/notifications/internal/display/impl/NotificationDisplayer;Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    displayNotification = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class SummaryNotificationDisplayer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/display/impl/SummaryNotificationDisplayer"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/notifications/internal/data/INotificationRepository;Lcom/onesignal/notifications/internal/display/INotificationDisplayBuilder;)V", False)]
    createSingleNotificationBeforeSummaryBuilder = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Landroidx/core/app/NotificationCompat$Builder;)Landroid/app/Notification;")
    updateSummaryNotification = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    createGenericPendingIntentsForGroup = JavaMethod("(Landroidx/core/app/NotificationCompat$Builder;Lcom/onesignal/notifications/internal/display/impl/IntentGeneratorForAttachingToNotifications;Lorg/json/JSONObject;Ljava/lang/String;I)V")
    createGrouplessSummaryNotification = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lcom/onesignal/notifications/internal/display/impl/IntentGeneratorForAttachingToNotifications;IILkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    createSummaryNotification = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lcom/onesignal/notifications/internal/display/impl/NotificationDisplayBuilder$OneSignalNotificationBuilder;ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")