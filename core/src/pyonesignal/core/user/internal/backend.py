from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CreateUserResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/CreateUserResponse"
    __javaconstructor__ = [("(Ljava/util/Map;Lcom/onesignal/user/internal/backend/PropertiesObject;Ljava/util/List;Lcom/onesignal/common/consistency/RywData;)V", False), ("(Ljava/util/Map;Lcom/onesignal/user/internal/backend/PropertiesObject;Ljava/util/List;Lcom/onesignal/common/consistency/RywData;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    getProperties = JavaMethod("()Lcom/onesignal/user/internal/backend/PropertiesObject;")
    getIdentities = JavaMethod("()Ljava/util/Map;")
    getSubscriptions = JavaMethod("()Ljava/util/List;")
    getRywData = JavaMethod("()Lcom/onesignal/common/consistency/RywData;")

class IIdentityBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/IIdentityBackendService"
    setAlias = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    deleteAlias = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/backend/IIdentityBackendService$DefaultImpls"
        setAlias$default = JavaStaticMethod("(Lcom/onesignal/user/internal/backend/IIdentityBackendService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        deleteAlias$default = JavaStaticMethod("(Lcom/onesignal/user/internal/backend/IIdentityBackendService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")

class ISubscriptionBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/ISubscriptionBackendService"
    createSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/backend/SubscriptionObject;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getIdentityFromSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    deleteSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    updateSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/backend/SubscriptionObject;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    transferSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/backend/ISubscriptionBackendService$DefaultImpls"
        createSubscription$default = JavaStaticMethod("(Lcom/onesignal/user/internal/backend/ISubscriptionBackendService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/backend/SubscriptionObject;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        updateSubscription$default = JavaStaticMethod("(Lcom/onesignal/user/internal/backend/ISubscriptionBackendService;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/backend/SubscriptionObject;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        transferSubscription$default = JavaStaticMethod("(Lcom/onesignal/user/internal/backend/ISubscriptionBackendService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        deleteSubscription$default = JavaStaticMethod("(Lcom/onesignal/user/internal/backend/ISubscriptionBackendService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")

class IUserBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/IUserBackendService"
    createUser = JavaMethod("(Ljava/lang/String;Ljava/util/Map;Ljava/util/List;Ljava/util/Map;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    updateUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/backend/PropertiesObject;ZLcom/onesignal/user/internal/backend/PropertiesDeltasObject;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/backend/IUserBackendService$DefaultImpls"
        createUser$default = JavaStaticMethod("(Lcom/onesignal/user/internal/backend/IUserBackendService;Ljava/lang/String;Ljava/util/Map;Ljava/util/List;Ljava/util/Map;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        getUser$default = JavaStaticMethod("(Lcom/onesignal/user/internal/backend/IUserBackendService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        updateUser$default = JavaStaticMethod("(Lcom/onesignal/user/internal/backend/IUserBackendService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/backend/PropertiesObject;ZLcom/onesignal/user/internal/backend/PropertiesDeltasObject;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")

class IdentityConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/IdentityConstants"
    INSTANCE = JavaStaticField("Lcom/onesignal/user/internal/backend/IdentityConstants;")
    EXTERNAL_ID = JavaStaticField("Ljava/lang/String;")
    ONESIGNAL_ID = JavaStaticField("Ljava/lang/String;")

class PropertiesDeltasObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/PropertiesDeltasObject"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/Long;Ljava/lang/Integer;Ljava/math/BigDecimal;Ljava/util/List;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False), ("(Ljava/lang/Long;Ljava/lang/Integer;Ljava/math/BigDecimal;Ljava/util/List;)V", False)]
    getSessionCount = JavaMethod("()Ljava/lang/Integer;")
    getAmountSpent = JavaMethod("()Ljava/math/BigDecimal;")
    getPurchases = JavaMethod("()Ljava/util/List;")
    getSessionTime = JavaMethod("()Ljava/lang/Long;")
    getHasAtLeastOnePropertySet = JavaMethod("()Z")

class PropertiesObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/PropertiesObject"
    __javaconstructor__ = [("()V", False), ("(Ljava/util/Map;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Double;Ljava/lang/Double;)V", False), ("(Ljava/util/Map;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Double;Ljava/lang/Double;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    getCountry = JavaMethod("()Ljava/lang/String;")
    getTags = JavaMethod("()Ljava/util/Map;")
    getHasAtLeastOnePropertySet = JavaMethod("()Z")
    getTimezoneId = JavaMethod("()Ljava/lang/String;")
    getLatitude = JavaMethod("()Ljava/lang/Double;")
    getLongitude = JavaMethod("()Ljava/lang/Double;")
    getLanguage = JavaMethod("()Ljava/lang/String;")

class PurchaseObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/PurchaseObject"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/math/BigDecimal;)V", False)]
    getSku = JavaMethod("()Ljava/lang/String;")
    getIso = JavaMethod("()Ljava/lang/String;")
    getAmount = JavaMethod("()Ljava/math/BigDecimal;")

class SubscriptionObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/SubscriptionObject"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Lcom/onesignal/user/internal/backend/SubscriptionObjectType;Ljava/lang/String;Ljava/lang/Boolean;Ljava/lang/Integer;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Boolean;Ljava/lang/Integer;Ljava/lang/String;Ljava/lang/String;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False), ("(Ljava/lang/String;Lcom/onesignal/user/internal/backend/SubscriptionObjectType;Ljava/lang/String;Ljava/lang/Boolean;Ljava/lang/Integer;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Boolean;Ljava/lang/Integer;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getId = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    getNetType = JavaMethod("()Ljava/lang/Integer;")
    getAppVersion = JavaMethod("()Ljava/lang/String;")
    getNotificationTypes = JavaMethod("()Ljava/lang/Integer;")
    getEnabled = JavaMethod("()Ljava/lang/Boolean;")
    getRooted = JavaMethod("()Ljava/lang/Boolean;")
    getDeviceModel = JavaMethod("()Ljava/lang/String;")
    getToken = JavaMethod("()Ljava/lang/String;")
    getSdk = JavaMethod("()Ljava/lang/String;")
    getDeviceOS = JavaMethod("()Ljava/lang/String;")
    getCarrier = JavaMethod("()Ljava/lang/String;")

class SubscriptionObjectType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/SubscriptionObjectType"
    Companion = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType$Companion;")
    IOS_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    ANDROID_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    FIREOS_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    CHROME_EXTENSION = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    CHROME_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    WINDOWS_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    SAFARI_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    SAFARI_PUSH_LEGACY = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    FIREFOX_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    MACOS_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    EMAIL = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    HUAWEI_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    SMS = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    values = JavaStaticMethod("()[Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    getValue = JavaMethod("()Ljava/lang/String;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/backend/SubscriptionObjectType$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        fromString = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
        fromDeviceType = JavaMethod("(Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;)Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")

        class WhenMappings(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "com/onesignal/user/internal/backend/SubscriptionObjectType$Companion$WhenMappings"
            $EnumSwitchMapping$0 = JavaStaticField("[I")
    IOS_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    ANDROID_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    FIREOS_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    CHROME_EXTENSION = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    CHROME_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    WINDOWS_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    SAFARI_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    SAFARI_PUSH_LEGACY = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    FIREFOX_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    MACOS_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    EMAIL = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    HUAWEI_PUSH = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")
    SMS = JavaStaticField("Lcom/onesignal/user/internal/backend/SubscriptionObjectType;")