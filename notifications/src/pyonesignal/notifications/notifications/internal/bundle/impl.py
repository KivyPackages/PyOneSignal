from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationBundleProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/bundle/impl/NotificationBundleProcessor"
    __javaconstructor__ = [("(Lcom/onesignal/notifications/internal/generation/INotificationGenerationWorkManager;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/bundle/impl/NotificationBundleProcessor$Companion;")
    PUSH_ADDITIONAL_DATA_KEY = JavaStaticField("Ljava/lang/String;")
    PUSH_MINIFIED_BUTTONS_LIST = JavaStaticField("Ljava/lang/String;")
    PUSH_MINIFIED_BUTTON_ID = JavaStaticField("Ljava/lang/String;")
    PUSH_MINIFIED_BUTTON_TEXT = JavaStaticField("Ljava/lang/String;")
    PUSH_MINIFIED_BUTTON_ICON = JavaStaticField("Ljava/lang/String;")
    DEFAULT_ACTION = JavaStaticField("Ljava/lang/String;")
    processBundleFromReceiver = JavaMethod("(Landroid/content/Context;Landroid/os/Bundle;)Lcom/onesignal/notifications/internal/bundle/INotificationBundleProcessor$ProcessedBundleResult;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/bundle/impl/NotificationBundleProcessor$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]