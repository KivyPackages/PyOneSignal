from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationLifecycleCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/lifecycle/INotificationLifecycleCallback"
    canReceiveNotification = JavaMethod("(Lorg/json/JSONObject;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    canOpenNotification = JavaMethod("(Landroid/app/Activity;Lorg/json/JSONObject;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class INotificationLifecycleService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/lifecycle/INotificationLifecycleService"
    addExternalForegroundLifecycleListener = JavaMethod("(Lcom/onesignal/notifications/INotificationLifecycleListener;)V")
    removeExternalForegroundLifecycleListener = JavaMethod("(Lcom/onesignal/notifications/INotificationLifecycleListener;)V")
    addExternalClickListener = JavaMethod("(Lcom/onesignal/notifications/INotificationClickListener;)V")
    removeExternalClickListener = JavaMethod("(Lcom/onesignal/notifications/INotificationClickListener;)V")
    canReceiveNotification = JavaMethod("(Lorg/json/JSONObject;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    setInternalNotificationLifecycleCallback = JavaMethod("(Lcom/onesignal/notifications/internal/lifecycle/INotificationLifecycleCallback;)V")
    externalRemoteNotificationReceived = JavaMethod("(Lcom/onesignal/notifications/INotificationReceivedEvent;)V")
    externalNotificationWillShowInForeground = JavaMethod("(Lcom/onesignal/notifications/INotificationWillDisplayEvent;)V")
    notificationReceived = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    canOpenNotification = JavaMethod("(Landroid/app/Activity;Lorg/json/JSONObject;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    notificationOpened = JavaMethod("(Landroid/app/Activity;Lorg/json/JSONArray;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")