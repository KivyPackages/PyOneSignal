from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IPushRegistrator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/registration/IPushRegistrator"
    registerForPush = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class RegisterResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/registration/IPushRegistrator$RegisterResult"
        __javaconstructor__ = [("(Ljava/lang/String;Lcom/onesignal/user/internal/subscriptions/SubscriptionStatus;)V", False)]
        getId = JavaMethod("()Ljava/lang/String;")
        getStatus = JavaMethod("()Lcom/onesignal/user/internal/subscriptions/SubscriptionStatus;")