from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationIntentExtras(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/open/impl/NotificationIntentExtras"
    __javaconstructor__ = [("(Lorg/json/JSONArray;Lorg/json/JSONObject;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    copy = JavaMethod("(Lorg/json/JSONArray;Lorg/json/JSONObject;)Lcom/onesignal/notifications/internal/open/impl/NotificationIntentExtras;")
    getDataArray = JavaMethod("()Lorg/json/JSONArray;")
    setDataArray = JavaMethod("(Lorg/json/JSONArray;)V")
    getJsonData = JavaMethod("()Lorg/json/JSONObject;")
    setJsonData = JavaMethod("(Lorg/json/JSONObject;)V")
    component1 = JavaMethod("()Lorg/json/JSONArray;")
    component2 = JavaMethod("()Lorg/json/JSONObject;")
    copy$default = JavaStaticMethod("(Lcom/onesignal/notifications/internal/open/impl/NotificationIntentExtras;Lorg/json/JSONArray;Lorg/json/JSONObject;ILjava/lang/Object;)Lcom/onesignal/notifications/internal/open/impl/NotificationIntentExtras;")

class NotificationOpenedProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/open/impl/NotificationOpenedProcessor"
    __javaconstructor__ = [("(Lcom/onesignal/notifications/internal/summary/INotificationSummaryManager;Lcom/onesignal/notifications/internal/data/INotificationRepository;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/notifications/internal/lifecycle/INotificationLifecycleService;)V", False)]
    processFromContext = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$processIntent = JavaStaticMethod("(Lcom/onesignal/notifications/internal/open/impl/NotificationOpenedProcessor;Landroid/content/Context;Landroid/content/Intent;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$processToOpenIntent = JavaStaticMethod("(Lcom/onesignal/notifications/internal/open/impl/NotificationOpenedProcessor;Landroid/content/Context;Landroid/content/Intent;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$addChildNotifications = JavaStaticMethod("(Lcom/onesignal/notifications/internal/open/impl/NotificationOpenedProcessor;Lorg/json/JSONArray;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$markNotificationsConsumed = JavaStaticMethod("(Lcom/onesignal/notifications/internal/open/impl/NotificationOpenedProcessor;Landroid/content/Context;Landroid/content/Intent;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$clearStatusBarNotifications = JavaStaticMethod("(Lcom/onesignal/notifications/internal/open/impl/NotificationOpenedProcessor;Landroid/content/Context;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class NotificationOpenedProcessorHMS(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/open/impl/NotificationOpenedProcessorHMS"
    __javaconstructor__ = [("(Lcom/onesignal/notifications/internal/lifecycle/INotificationLifecycleService;)V", False)]
    access$handleProcessJsonOpenData = JavaStaticMethod("(Lcom/onesignal/notifications/internal/open/impl/NotificationOpenedProcessorHMS;Landroid/app/Activity;Lorg/json/JSONObject;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    handleHMSNotificationOpenIntent = JavaMethod("(Landroid/app/Activity;Landroid/content/Intent;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")