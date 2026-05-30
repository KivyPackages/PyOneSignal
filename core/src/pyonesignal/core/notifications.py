from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class BackgroundImageLayout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/BackgroundImageLayout"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getImage = JavaMethod("()Ljava/lang/String;")
    getTitleTextColor = JavaMethod("()Ljava/lang/String;")
    getBodyTextColor = JavaMethod("()Ljava/lang/String;")

class IActionButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/IActionButton"
    getIcon = JavaMethod("()Ljava/lang/String;")
    getText = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()Ljava/lang/String;")

class IDisplayableMutableNotification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/IDisplayableMutableNotification"

class IDisplayableNotification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/IDisplayableNotification"
    display = JavaMethod("()V")

class IMutableNotification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/IMutableNotification"
    setExtender = JavaMethod("(Landroidx/core/app/NotificationCompat$Extender;)V")

class INotification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/INotification"
    getTtl = JavaMethod("()I")
    getAndroidNotificationId = JavaMethod("()I")
    getNotificationId = JavaMethod("()Ljava/lang/String;")
    getTemplateName = JavaMethod("()Ljava/lang/String;")
    getTemplateId = JavaMethod("()Ljava/lang/String;")
    getBody = JavaMethod("()Ljava/lang/String;")
    getAdditionalData = JavaMethod("()Lorg/json/JSONObject;")
    getSmallIcon = JavaMethod("()Ljava/lang/String;")
    getLargeIcon = JavaMethod("()Ljava/lang/String;")
    getBigPicture = JavaMethod("()Ljava/lang/String;")
    getSmallIconAccentColor = JavaMethod("()Ljava/lang/String;")
    getLaunchURL = JavaMethod("()Ljava/lang/String;")
    getSound = JavaMethod("()Ljava/lang/String;")
    getLedColor = JavaMethod("()Ljava/lang/String;")
    getLockScreenVisibility = JavaMethod("()I")
    getGroupKey = JavaMethod("()Ljava/lang/String;")
    getGroupMessage = JavaMethod("()Ljava/lang/String;")
    getActionButtons = JavaMethod("()Ljava/util/List;")
    getFromProjectNumber = JavaMethod("()Ljava/lang/String;")
    getBackgroundImageLayout = JavaMethod("()Lcom/onesignal/notifications/BackgroundImageLayout;")
    getCollapseId = JavaMethod("()Ljava/lang/String;")
    getSentTime = JavaMethod("()J")
    getGroupedNotifications = JavaMethod("()Ljava/util/List;")
    getRawPayload = JavaMethod("()Ljava/lang/String;")
    getTitle = JavaMethod("()Ljava/lang/String;")
    getPriority = JavaMethod("()I")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/INotification$DefaultImpls"
        getBackgroundImageLayout$annotations = JavaStaticMethod("()V")

class INotificationClickEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/INotificationClickEvent"
    getNotification = JavaMethod("()Lcom/onesignal/notifications/INotification;")
    getResult = JavaMethod("()Lcom/onesignal/notifications/INotificationClickResult;")

class INotificationClickListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/INotificationClickListener"
    onClick = JavaMethod("(Lcom/onesignal/notifications/INotificationClickEvent;)V")

class INotificationClickResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/INotificationClickResult"
    getUrl = JavaMethod("()Ljava/lang/String;")
    getActionId = JavaMethod("()Ljava/lang/String;")

class INotificationLifecycleListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/INotificationLifecycleListener"
    onWillDisplay = JavaMethod("(Lcom/onesignal/notifications/INotificationWillDisplayEvent;)V")

class INotificationReceivedEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/INotificationReceivedEvent"
    getContext = JavaMethod("()Landroid/content/Context;")
    preventDefault = JavaMultipleMethod([("(Z)V", False, False), ("()V", False, False)])
    getNotification = JavaMethod("()Lcom/onesignal/notifications/IDisplayableMutableNotification;")

class INotificationServiceExtension(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/INotificationServiceExtension"
    onNotificationReceived = JavaMethod("(Lcom/onesignal/notifications/INotificationReceivedEvent;)V")

class INotificationWillDisplayEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/INotificationWillDisplayEvent"
    preventDefault = JavaMultipleMethod([("()V", False, False), ("(Z)V", False, False)])
    getNotification = JavaMethod("()Lcom/onesignal/notifications/IDisplayableNotification;")

class INotificationsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/INotificationsManager"
    getCanRequestPermission = JavaMethod("()Z")
    requestPermission = JavaMethod("(ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    removeNotification = JavaMethod("(I)V")
    removeGroupedNotifications = JavaMethod("(Ljava/lang/String;)V")
    clearAllNotifications = JavaMethod("()V")
    addPermissionObserver = JavaMethod("(Lcom/onesignal/notifications/IPermissionObserver;)V")
    removePermissionObserver = JavaMethod("(Lcom/onesignal/notifications/IPermissionObserver;)V")
    addForegroundLifecycleListener = JavaMethod("(Lcom/onesignal/notifications/INotificationLifecycleListener;)V")
    removeForegroundLifecycleListener = JavaMethod("(Lcom/onesignal/notifications/INotificationLifecycleListener;)V")
    addClickListener = JavaMethod("(Lcom/onesignal/notifications/INotificationClickListener;)V")
    removeClickListener = JavaMethod("(Lcom/onesignal/notifications/INotificationClickListener;)V")
    getPermission = JavaMethod("()Z")

class IPermissionObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/IPermissionObserver"
    onNotificationPermissionChange = JavaMethod("(Z)V")