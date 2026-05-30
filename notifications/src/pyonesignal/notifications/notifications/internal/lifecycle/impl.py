from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationLifecycleService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/lifecycle/impl/NotificationLifecycleService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/time/ITime;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/session/internal/influence/IInfluenceManager;Lcom/onesignal/user/internal/subscriptions/ISubscriptionManager;Lcom/onesignal/core/internal/device/IDeviceService;Lcom/onesignal/notifications/internal/backend/INotificationBackendService;Lcom/onesignal/notifications/internal/receivereceipt/IReceiveReceiptWorkManager;Lcom/onesignal/notifications/internal/analytics/IAnalyticsTracker;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/lifecycle/impl/NotificationLifecycleService$Companion;")
    addExternalForegroundLifecycleListener = JavaMethod("(Lcom/onesignal/notifications/INotificationLifecycleListener;)V")
    removeExternalForegroundLifecycleListener = JavaMethod("(Lcom/onesignal/notifications/INotificationLifecycleListener;)V")
    addExternalClickListener = JavaMethod("(Lcom/onesignal/notifications/INotificationClickListener;)V")
    removeExternalClickListener = JavaMethod("(Lcom/onesignal/notifications/INotificationClickListener;)V")
    setupNotificationServiceExtension = JavaMethod("(Landroid/content/Context;)V")
    access$confirmNotificationOpened = JavaStaticMethod("(Lcom/onesignal/notifications/internal/lifecycle/impl/NotificationLifecycleService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    openDestinationActivity = JavaMethod("(Landroid/app/Activity;Lorg/json/JSONArray;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    canReceiveNotification = JavaMethod("(Lorg/json/JSONObject;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    setInternalNotificationLifecycleCallback = JavaMethod("(Lcom/onesignal/notifications/internal/lifecycle/INotificationLifecycleCallback;)V")
    externalRemoteNotificationReceived = JavaMethod("(Lcom/onesignal/notifications/INotificationReceivedEvent;)V")
    externalNotificationWillShowInForeground = JavaMethod("(Lcom/onesignal/notifications/INotificationWillDisplayEvent;)V")
    notificationReceived = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    canOpenNotification = JavaMethod("(Landroid/app/Activity;Lorg/json/JSONObject;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    notificationOpened = JavaMethod("(Landroid/app/Activity;Lorg/json/JSONArray;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/lifecycle/impl/NotificationLifecycleService$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]