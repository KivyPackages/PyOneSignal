from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ADMMessageHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/services/ADMMessageHandler"
    __javaconstructor__ = [("()V", False)]

class ADMMessageHandlerJob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/services/ADMMessageHandlerJob"
    __javaconstructor__ = [("()V", False)]

class HmsMessageServiceOneSignal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/services/HmsMessageServiceOneSignal"
    __javaconstructor__ = [("()V", False)]
    onMessageReceived = JavaMethod("(Lcom/huawei/hms/push/RemoteMessage;)V")
    onNewToken = JavaMultipleMethod([("(Ljava/lang/String;Landroid/os/Bundle;)V", False, False), ("(Ljava/lang/String;)V", False, False)])