from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationChannelManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/channels/INotificationChannelManager"
    createNotificationChannel = JavaMethod("(Lcom/onesignal/notifications/internal/common/NotificationGenerationJob;)Ljava/lang/String;")
    processChannelList = JavaMethod("(Lorg/json/JSONArray;)V")