from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ADMMessageReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/receivers/ADMMessageReceiver"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/receivers/ADMMessageReceiver$Companion;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/receivers/ADMMessageReceiver$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class BootUpReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/receivers/BootUpReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")

class FCMBroadcastReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/receivers/FCMBroadcastReceiver"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/receivers/FCMBroadcastReceiver$Companion;")
    access$setSuccessfulResultCode = JavaStaticMethod("(Lcom/onesignal/notifications/receivers/FCMBroadcastReceiver;)V")
    access$setAbort = JavaStaticMethod("(Lcom/onesignal/notifications/receivers/FCMBroadcastReceiver;)V")
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/receivers/FCMBroadcastReceiver$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        access$isFCMMessage = JavaStaticMethod("(Lcom/onesignal/notifications/receivers/FCMBroadcastReceiver$Companion;Landroid/content/Intent;)Z")

class NotificationDismissReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/receivers/NotificationDismissReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")

class UpgradeReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/receivers/UpgradeReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")