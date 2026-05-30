from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IEmailSubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/subscriptions/IEmailSubscription"
    getEmail = JavaMethod("()Ljava/lang/String;")

class IPushSubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/subscriptions/IPushSubscription"
    getOptedIn = JavaMethod("()Z")
    addObserver = JavaMethod("(Lcom/onesignal/user/subscriptions/IPushSubscriptionObserver;)V")
    removeObserver = JavaMethod("(Lcom/onesignal/user/subscriptions/IPushSubscriptionObserver;)V")
    optOut = JavaMethod("()V")
    optIn = JavaMethod("()V")
    getToken = JavaMethod("()Ljava/lang/String;")

class IPushSubscriptionObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/subscriptions/IPushSubscriptionObserver"
    onPushSubscriptionChange = JavaMethod("(Lcom/onesignal/user/subscriptions/PushSubscriptionChangedState;)V")

class ISmsSubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/subscriptions/ISmsSubscription"
    getNumber = JavaMethod("()Ljava/lang/String;")

class ISubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/subscriptions/ISubscription"
    getId = JavaMethod("()Ljava/lang/String;")

class PushSubscriptionChangedState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/subscriptions/PushSubscriptionChangedState"
    __javaconstructor__ = [("(Lcom/onesignal/user/subscriptions/PushSubscriptionState;Lcom/onesignal/user/subscriptions/PushSubscriptionState;)V", False)]
    getCurrent = JavaMethod("()Lcom/onesignal/user/subscriptions/PushSubscriptionState;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    getPrevious = JavaMethod("()Lcom/onesignal/user/subscriptions/PushSubscriptionState;")

class PushSubscriptionState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/subscriptions/PushSubscriptionState"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Z)V", False)]
    getOptedIn = JavaMethod("()Z")
    getId = JavaMethod("()Ljava/lang/String;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    getToken = JavaMethod("()Ljava/lang/String;")