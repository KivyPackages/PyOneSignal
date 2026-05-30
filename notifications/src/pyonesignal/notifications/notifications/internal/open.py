from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationOpenedProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/open/INotificationOpenedProcessor"
    processFromContext = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class INotificationOpenedProcessorHMS(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/open/INotificationOpenedProcessorHMS"
    handleHMSNotificationOpenIntent = JavaMethod("(Landroid/app/Activity;Landroid/content/Intent;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")