from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class OneSignalHmsEventBridge(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/bridges/OneSignalHmsEventBridge"
    INSTANCE = JavaStaticField("Lcom/onesignal/notifications/bridges/OneSignalHmsEventBridge;")
    HMS_TTL_KEY = JavaStaticField("Ljava/lang/String;")
    HMS_SENT_TIME_KEY = JavaStaticField("Ljava/lang/String;")
    onMessageReceived = JavaMethod("(Landroid/content/Context;Lcom/huawei/hms/push/RemoteMessage;)V")
    onNewToken = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/String;Landroid/os/Bundle;)V", False, False), ("(Landroid/content/Context;Ljava/lang/String;)V", False, False)])