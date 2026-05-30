from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IMigrationRecovery(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/migrations/IMigrationRecovery"
    isInBadState = JavaMethod("()Z")
    recover = JavaMethod("()V")
    recoveryMessage = JavaMethod("()Ljava/lang/String;")

class MigrationRecovery(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/migrations/MigrationRecovery"
    __javaconstructor__ = [("()V", False)]
    start = JavaMethod("()V")

class RecoverConfigPushSubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/migrations/RecoverConfigPushSubscription"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;)V", False)]
    isInBadState = JavaMethod("()Z")
    recover = JavaMethod("()V")
    recoveryMessage = JavaMethod("()Ljava/lang/String;")
    getActivePushSubscription = JavaMethod("()Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;")
    access$get_subscriptionModelStore$p = JavaStaticMethod("(Lcom/onesignal/user/internal/migrations/RecoverConfigPushSubscription;)Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;")

class RecoverFromDroppedLoginBug(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/migrations/RecoverFromDroppedLoginBug"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    access$get_operationRepo$p = JavaStaticMethod("(Lcom/onesignal/user/internal/migrations/RecoverFromDroppedLoginBug;)Lcom/onesignal/core/internal/operations/IOperationRepo;")
    access$isInBadState = JavaStaticMethod("(Lcom/onesignal/user/internal/migrations/RecoverFromDroppedLoginBug;)Z")
    access$get_identityModelStore$p = JavaStaticMethod("(Lcom/onesignal/user/internal/migrations/RecoverFromDroppedLoginBug;)Lcom/onesignal/user/internal/identity/IdentityModelStore;")
    access$recoverByAddingBackDroppedLoginOperation = JavaStaticMethod("(Lcom/onesignal/user/internal/migrations/RecoverFromDroppedLoginBug;)V")
    start = JavaMethod("()V")