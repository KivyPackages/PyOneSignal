from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ConfigModelStoreListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/config/impl/ConfigModelStoreListener"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/core/internal/backend/IParamsBackendService;Lcom/onesignal/user/internal/subscriptions/ISubscriptionManager;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/config/impl/ConfigModelStoreListener$Companion;")
    start = JavaMethod("()V")
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")
    onModelReplaced = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/core/internal/config/ConfigModel;Ljava/lang/String;)V", False, False)])
    access$get_paramsBackendService$p = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/ConfigModelStoreListener;)Lcom/onesignal/core/internal/backend/IParamsBackendService;")
    access$get_configModelStore$p = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/ConfigModelStoreListener;)Lcom/onesignal/core/internal/config/ConfigModelStore;")
    access$get_subscriptionManager$p = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/ConfigModelStoreListener;)Lcom/onesignal/user/internal/subscriptions/ISubscriptionManager;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/config/impl/ConfigModelStoreListener$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class FeatureFlagsRefreshService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/config/impl/FeatureFlagsRefreshService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/core/internal/backend/IFeatureFlagsBackendService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/config/impl/FeatureFlagsRefreshService$Companion;")
    start = JavaMethod("()V")
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")
    onModelReplaced = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/core/internal/config/ConfigModel;Ljava/lang/String;)V", False, False)])
    onFocus = JavaMethod("(Z)V")
    onUnfocused = JavaMethod("()V")
    getRefreshIntervalMs$com_onesignal_core = JavaMethod("()J")
    setRefreshIntervalMs$com_onesignal_core = JavaMethod("(J)V")
    access$restartForegroundPolling = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/FeatureFlagsRefreshService;)V")
    access$getPollJob$p = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/FeatureFlagsRefreshService;)Lkotlinx/coroutines/Job;")
    access$setPollJob$p = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/FeatureFlagsRefreshService;Lkotlinx/coroutines/Job;)V")
    access$setPollingAppId$p = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/FeatureFlagsRefreshService;Ljava/lang/String;)V")
    access$fetchAndApply = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/FeatureFlagsRefreshService;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$getApplicationService$p = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/FeatureFlagsRefreshService;)Lcom/onesignal/core/internal/application/IApplicationService;")
    access$getConfigModelStore$p = JavaStaticMethod("(Lcom/onesignal/core/internal/config/impl/FeatureFlagsRefreshService;)Lcom/onesignal/core/internal/config/ConfigModelStore;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/config/impl/FeatureFlagsRefreshService$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class IdentityVerificationService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/config/impl/IdentityVerificationService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/features/IFeatureManager;Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    start = JavaMethod("()V")
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")
    onModelReplaced = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/core/internal/config/ConfigModel;Ljava/lang/String;)V", False, False)])
    getIvBehaviorActive = JavaMethod("()Z")
    getNewCodePathsRun = JavaMethod("()Z")
    setOnJwtConfigHydratedHandler = JavaMethod("(Lkotlin/jvm/functions/Function1;)V")