from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DeviceRegistrationListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/listeners/DeviceRegistrationListener"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/notifications/internal/channels/INotificationChannelManager;Lcom/onesignal/notifications/internal/pushtoken/IPushTokenManager;Lcom/onesignal/notifications/INotificationsManager;Lcom/onesignal/user/internal/subscriptions/ISubscriptionManager;)V", False)]
    start = JavaMethod("()V")
    onNotificationPermissionChange = JavaMethod("(Z)V")
    access$get_pushTokenManager$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/listeners/DeviceRegistrationListener;)Lcom/onesignal/notifications/internal/pushtoken/IPushTokenManager;")
    onModelReplaced = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/core/internal/config/ConfigModel;Ljava/lang/String;)V", False, False)])
    onSubscriptionRemoved = JavaMethod("(Lcom/onesignal/user/subscriptions/ISubscription;)V")
    onSubscriptionAdded = JavaMethod("(Lcom/onesignal/user/subscriptions/ISubscription;)V")
    onSubscriptionChanged = JavaMethod("(Lcom/onesignal/user/subscriptions/ISubscription;Lcom/onesignal/common/modeling/ModelChangedArgs;)V")
    access$get_notificationsManager$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/listeners/DeviceRegistrationListener;)Lcom/onesignal/notifications/INotificationsManager;")
    access$get_subscriptionManager$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/listeners/DeviceRegistrationListener;)Lcom/onesignal/user/internal/subscriptions/ISubscriptionManager;")
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")