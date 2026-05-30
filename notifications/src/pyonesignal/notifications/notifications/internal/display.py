from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationDisplayBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/display/INotificationDisplayBuilder"
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

class INotificationDisplayer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/display/INotificationDisplayer"
    displayNotification = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class ISummaryNotificationDisplayer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/display/ISummaryNotificationDisplayer"
    createSingleNotificationBeforeSummaryBuilder = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Landroidx/core/app/NotificationCompat$Builder;)Landroid/app/Notification;")
    updateSummaryNotification = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    createGenericPendingIntentsForGroup = JavaMethod("(Landroidx/core/app/NotificationCompat$Builder;Lcom/onesignal/notifications/internal/display/impl/IntentGeneratorForAttachingToNotifications;Lorg/json/JSONObject;Ljava/lang/String;I)V")
    createGrouplessSummaryNotification = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lcom/onesignal/notifications/internal/display/impl/IntentGeneratorForAttachingToNotifications;IILkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    createSummaryNotification = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lcom/onesignal/notifications/internal/display/impl/NotificationDisplayBuilder$OneSignalNotificationBuilder;ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")