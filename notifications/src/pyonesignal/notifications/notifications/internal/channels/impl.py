from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationChannelManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/channels/impl/NotificationChannelManager"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/language/ILanguageContext;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/channels/impl/NotificationChannelManager$Companion;")
    createNotificationChannel = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;)Ljava/lang/String;")
    processChannelList = JavaMethod("(Lorg/json/JSONArray;)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/channels/impl/NotificationChannelManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]