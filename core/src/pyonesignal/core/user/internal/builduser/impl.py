from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RebuildUserService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/builduser/impl/RebuildUserService"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    getRebuildOperationsIfCurrentUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/util/List;")