from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IdentityModelStoreListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/listeners/IdentityModelStoreListener"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    getUpdateOperation = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)Lcom/onesignal/core/internal/operations/Operation;", False, False), ("(Lcom/onesignal/user/internal/identity/IdentityModel;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)Lcom/onesignal/core/internal/operations/Operation;", False, False)])
    getReplaceOperation = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;)Lcom/onesignal/core/internal/operations/Operation;", False, False), ("(Lcom/onesignal/user/internal/identity/IdentityModel;)Lcom/onesignal/core/internal/operations/Operation;", False, False)])

class PropertiesModelStoreListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/listeners/PropertiesModelStoreListener"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/user/internal/identity/IdentityModelStore;)V", False)]
    getUpdateOperation = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)Lcom/onesignal/core/internal/operations/Operation;", False, False), ("(Lcom/onesignal/user/internal/properties/PropertiesModel;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)Lcom/onesignal/core/internal/operations/Operation;", False, False)])
    getReplaceOperation = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;)Lcom/onesignal/core/internal/operations/Operation;", False, False), ("(Lcom/onesignal/user/internal/properties/PropertiesModel;)Lcom/onesignal/core/internal/operations/Operation;", False, False)])

class SubscriptionModelStoreListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/listeners/SubscriptionModelStoreListener"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/listeners/SubscriptionModelStoreListener$Companion;")
    getAddOperation = JavaMultipleMethod([("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;)Lcom/onesignal/core/internal/operations/Operation;", False, False), ("(Lcom/onesignal/common/modeling/Model;)Lcom/onesignal/core/internal/operations/Operation;", False, False)])
    getUpdateOperation = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)Lcom/onesignal/core/internal/operations/Operation;", False, False), ("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)Lcom/onesignal/core/internal/operations/Operation;", False, False)])
    getRemoveOperation = JavaMultipleMethod([("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;)Lcom/onesignal/core/internal/operations/Operation;", False, False), ("(Lcom/onesignal/common/modeling/Model;)Lcom/onesignal/core/internal/operations/Operation;", False, False)])

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/listeners/SubscriptionModelStoreListener$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        getSubscriptionEnabledAndStatus = JavaMethod("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;)Lkotlin/Pair;")