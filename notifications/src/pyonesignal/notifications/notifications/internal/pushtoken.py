from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IPushTokenManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/pushtoken/IPushTokenManager"
    retrievePushToken = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class PushTokenManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/pushtoken/PushTokenManager"
    __javaconstructor__ = [("(Lcom/onesignal/notifications/internal/registration/IPushRegistrator;Lcom/onesignal/core/internal/device/IDeviceService;)V", False)]
    getPushTokenStatus = JavaMethod("()Lcom/onesignal/user/internal/subscriptions/SubscriptionStatus;")
    setPushTokenStatus = JavaMethod("(Lcom/onesignal/user/internal/subscriptions/SubscriptionStatus;)V")
    getPushToken = JavaMethod("()Ljava/lang/String;")
    setPushToken = JavaMethod("(Ljava/lang/String;)V")
    retrievePushToken = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/pushtoken/PushTokenManager$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")

class PushTokenResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/pushtoken/PushTokenResponse"
    __javaconstructor__ = [("(Ljava/lang/String;Lcom/onesignal/user/internal/subscriptions/SubscriptionStatus;)V", False)]
    getToken = JavaMethod("()Ljava/lang/String;")
    getStatus = JavaMethod("()Lcom/onesignal/user/internal/subscriptions/SubscriptionStatus;")