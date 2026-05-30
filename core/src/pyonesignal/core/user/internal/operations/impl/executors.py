from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CustomEventOperationExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/CustomEventOperationExecutor"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/customEvents/ICustomEventBackendService;Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/device/IDeviceService;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/executors/CustomEventOperationExecutor$Companion;")
    CUSTOM_EVENT = JavaStaticField("Ljava/lang/String;")
    execute = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getOperations = JavaMethod("()Ljava/util/List;")
    access$getDeviceService$p = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/CustomEventOperationExecutor;)Lcom/onesignal/core/internal/device/IDeviceService;")
    access$getApplicationService$p = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/CustomEventOperationExecutor;)Lcom/onesignal/core/internal/application/IApplicationService;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/CustomEventOperationExecutor$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/CustomEventOperationExecutor$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")

class ExecutorsIvExtensionsKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/ExecutorsIvExtensionsKt"
    resolveBackendParams = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/Operation;Ljava/lang/String;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;)Lcom/onesignal/user/internal/operations/impl/executors/IvBackendParams;")
    resolveIvBackendParams = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/Operation;Ljava/lang/String;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Z)Lcom/onesignal/user/internal/operations/impl/executors/IvBackendParams;")
    resolveIvJwt = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/Operation;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Z)Ljava/lang/String;")
    shouldFailLoginUserFromSubscription = JavaStaticMethod("(Z)Z")
    resolveJwt = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/Operation;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;)Ljava/lang/String;")

class IdentityOperationExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/IdentityOperationExecutor"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/backend/IIdentityBackendService;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/builduser/IRebuildUserService;Lcom/onesignal/user/internal/operations/impl/states/NewRecordsState;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/executors/IdentityOperationExecutor$Companion;")
    SET_ALIAS = JavaStaticField("Ljava/lang/String;")
    DELETE_ALIAS = JavaStaticField("Ljava/lang/String;")
    execute = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getOperations = JavaMethod("()Ljava/util/List;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/IdentityOperationExecutor$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/IdentityOperationExecutor$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")

class IvBackendParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/IvBackendParams"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/executors/IvBackendParams$Companion;")
    copy$default = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/IvBackendParams;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ILjava/lang/Object;)Lcom/onesignal/user/internal/operations/impl/executors/IvBackendParams;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    copy = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lcom/onesignal/user/internal/operations/impl/executors/IvBackendParams;")
    getAliasLabel = JavaMethod("()Ljava/lang/String;")
    getAliasValue = JavaMethod("()Ljava/lang/String;")
    component1 = JavaMethod("()Ljava/lang/String;")
    component2 = JavaMethod("()Ljava/lang/String;")
    getJwt = JavaMethod("()Ljava/lang/String;")
    component3 = JavaMethod("()Ljava/lang/String;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/IvBackendParams$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        legacyFor = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/user/internal/operations/impl/executors/IvBackendParams;")

class LoginUserFromSubscriptionOperationExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/LoginUserFromSubscriptionOperationExecutor"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/backend/ISubscriptionBackendService;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/executors/LoginUserFromSubscriptionOperationExecutor$Companion;")
    LOGIN_USER_FROM_SUBSCRIPTION_USER = JavaStaticField("Ljava/lang/String;")
    execute = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$loginUser = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/LoginUserFromSubscriptionOperationExecutor;Lcom/onesignal/user/internal/operations/LoginUserFromSubscriptionOperation;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getOperations = JavaMethod("()Ljava/util/List;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/LoginUserFromSubscriptionOperationExecutor$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/LoginUserFromSubscriptionOperationExecutor$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")

class LoginUserOperationExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/LoginUserOperationExecutor"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/operations/impl/executors/IdentityOperationExecutor;Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/device/IDeviceService;Lcom/onesignal/user/internal/backend/IUserBackendService;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/core/internal/language/ILanguageContext;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;Lcom/onesignal/common/consistency/models/IConsistencyManager;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/executors/LoginUserOperationExecutor$Companion;")
    LOGIN_USER = JavaStaticField("Ljava/lang/String;")
    execute = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$loginUser = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/LoginUserOperationExecutor;Lcom/onesignal/user/internal/operations/LoginUserOperation;Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$createUser = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/LoginUserOperationExecutor;Lcom/onesignal/user/internal/operations/LoginUserOperation;Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getOperations = JavaMethod("()Ljava/util/List;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/LoginUserOperationExecutor$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/LoginUserOperationExecutor$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")
        $EnumSwitchMapping$1 = JavaStaticField("[I")
        $EnumSwitchMapping$2 = JavaStaticField("[I")

class PropertyOperationHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/PropertyOperationHelper"
    INSTANCE = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/executors/PropertyOperationHelper;")
    createPropertiesFromOperation = JavaMultipleMethod([("(Lcom/onesignal/user/internal/operations/SetTagOperation;Lcom/onesignal/user/internal/backend/PropertiesObject;)Lcom/onesignal/user/internal/backend/PropertiesObject;", False, False), ("(Lcom/onesignal/user/internal/operations/SetPropertyOperation;Lcom/onesignal/user/internal/backend/PropertiesObject;)Lcom/onesignal/user/internal/backend/PropertiesObject;", False, False), ("(Lcom/onesignal/user/internal/operations/DeleteTagOperation;Lcom/onesignal/user/internal/backend/PropertiesObject;)Lcom/onesignal/user/internal/backend/PropertiesObject;", False, False)])

class RefreshUserOperationExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/RefreshUserOperationExecutor"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/backend/IUserBackendService;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/user/internal/builduser/IRebuildUserService;Lcom/onesignal/user/internal/operations/impl/states/NewRecordsState;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/executors/RefreshUserOperationExecutor$Companion;")
    REFRESH_USER = JavaStaticField("Ljava/lang/String;")
    execute = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$getUser = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/RefreshUserOperationExecutor;Lcom/onesignal/user/internal/operations/RefreshUserOperation;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getOperations = JavaMethod("()Ljava/util/List;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/RefreshUserOperationExecutor$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/RefreshUserOperationExecutor$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")
        $EnumSwitchMapping$1 = JavaStaticField("[I")

class SubscriptionOperationExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/SubscriptionOperationExecutor"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/backend/ISubscriptionBackendService;Lcom/onesignal/core/internal/device/IDeviceService;Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/user/internal/builduser/IRebuildUserService;Lcom/onesignal/user/internal/operations/impl/states/NewRecordsState;Lcom/onesignal/common/consistency/models/IConsistencyManager;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/executors/SubscriptionOperationExecutor$Companion;")
    CREATE_SUBSCRIPTION = JavaStaticField("Ljava/lang/String;")
    UPDATE_SUBSCRIPTION = JavaStaticField("Ljava/lang/String;")
    DELETE_SUBSCRIPTION = JavaStaticField("Ljava/lang/String;")
    TRANSFER_SUBSCRIPTION = JavaStaticField("Ljava/lang/String;")
    execute = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getOperations = JavaMethod("()Ljava/util/List;")
    access$updateExistingSubscriptionFromCreate = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/SubscriptionOperationExecutor;Lcom/onesignal/user/internal/operations/CreateSubscriptionOperation;Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$createSubscription = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/SubscriptionOperationExecutor;Lcom/onesignal/user/internal/operations/CreateSubscriptionOperation;Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$updateSubscription = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/SubscriptionOperationExecutor;Lcom/onesignal/user/internal/operations/UpdateSubscriptionOperation;Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$transferSubscription = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/SubscriptionOperationExecutor;Lcom/onesignal/user/internal/operations/TransferSubscriptionOperation;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$deleteSubscription = JavaStaticMethod("(Lcom/onesignal/user/internal/operations/impl/executors/SubscriptionOperationExecutor;Lcom/onesignal/user/internal/operations/DeleteSubscriptionOperation;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/SubscriptionOperationExecutor$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/SubscriptionOperationExecutor$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")
        $EnumSwitchMapping$1 = JavaStaticField("[I")

class UpdateUserOperationExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/UpdateUserOperationExecutor"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/backend/IUserBackendService;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/user/internal/builduser/IRebuildUserService;Lcom/onesignal/user/internal/operations/impl/states/NewRecordsState;Lcom/onesignal/common/consistency/models/IConsistencyManager;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/operations/impl/executors/UpdateUserOperationExecutor$Companion;")
    SET_TAG = JavaStaticField("Ljava/lang/String;")
    DELETE_TAG = JavaStaticField("Ljava/lang/String;")
    SET_PROPERTY = JavaStaticField("Ljava/lang/String;")
    TRACK_SESSION_START = JavaStaticField("Ljava/lang/String;")
    TRACK_SESSION_END = JavaStaticField("Ljava/lang/String;")
    TRACK_PURCHASE = JavaStaticField("Ljava/lang/String;")
    execute = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getOperations = JavaMethod("()Ljava/util/List;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/UpdateUserOperationExecutor$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/operations/impl/executors/UpdateUserOperationExecutor$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")