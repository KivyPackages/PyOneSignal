from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SubscriptionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/subscriptions/impl/SubscriptionManager"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/session/internal/session/ISessionService;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;)V", False)]
    getHasSubscribers = JavaMethod("()Z")
    subscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/user/internal/subscriptions/ISubscriptionChangedHandler;)V", False, False)])
    unsubscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/user/internal/subscriptions/ISubscriptionChangedHandler;)V", False, False)])
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")
    onModelAdded = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;Ljava/lang/String;)V", False, False)])
    onModelRemoved = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;Ljava/lang/String;)V", False, False)])
    onSessionStarted = JavaMethod("()V")
    onSessionActive = JavaMethod("()V")
    onSessionEnded = JavaMethod("(J)V")
    getSubscriptions = JavaMethod("()Lcom/onesignal/user/internal/subscriptions/SubscriptionList;")
    getPushSubscriptionModel = JavaMethod("()Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;")
    setSubscriptions = JavaMethod("(Lcom/onesignal/user/internal/subscriptions/SubscriptionList;)V")
    addEmailSubscription = JavaMethod("(Ljava/lang/String;)V")
    addOrUpdatePushSubscriptionToken = JavaMethod("(Ljava/lang/String;Lcom/onesignal/user/internal/subscriptions/SubscriptionStatus;)V")
    addSmsSubscription = JavaMethod("(Ljava/lang/String;)V")
    removeEmailSubscription = JavaMethod("(Ljava/lang/String;)V")
    removeSmsSubscription = JavaMethod("(Ljava/lang/String;)V")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/subscriptions/impl/SubscriptionManager$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")