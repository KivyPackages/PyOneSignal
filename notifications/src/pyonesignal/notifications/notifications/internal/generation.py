from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationGenerationProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/generation/INotificationGenerationProcessor"
    processNotificationData = JavaMethod("(Landroid/content/Context;ILorg/json/JSONObject;ZJLkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class INotificationGenerationWorkManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/generation/INotificationGenerationWorkManager"
    beginEnqueueingWork = JavaMethod("(Landroid/content/Context;Ljava/lang/String;ILorg/json/JSONObject;JZZ)Z")