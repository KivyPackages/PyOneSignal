from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AppIdResolution(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/AppIdResolution"
    __javaconstructor__ = [("(Ljava/lang/String;ZZ)V", False)]
    copy$default = JavaStaticMethod("(Lcom/onesignal/user/internal/AppIdResolution;Ljava/lang/String;ZZILjava/lang/Object;)Lcom/onesignal/user/internal/AppIdResolution;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    copy = JavaMethod("(Ljava/lang/String;ZZ)Lcom/onesignal/user/internal/AppIdResolution;")
    component1 = JavaMethod("()Ljava/lang/String;")
    component2 = JavaMethod("()Z")
    getAppId = JavaMethod("()Ljava/lang/String;")
    component3 = JavaMethod("()Z")
    getFailed = JavaMethod("()Z")
    getForceCreateUser = JavaMethod("()Z")

class AppIdResolutionKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/AppIdResolutionKt"
    resolveAppId = JavaStaticMethod("(Ljava/lang/String;Lcom/onesignal/core/internal/config/ConfigModel;Lcom/onesignal/core/internal/preferences/IPreferencesService;)Lcom/onesignal/user/internal/AppIdResolution;")

class EmailSubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/EmailSubscription"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;)V", False)]
    getEmail = JavaMethod("()Ljava/lang/String;")

class LoginHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/LoginHelper"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/UserSwitcher;Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/core/internal/config/ConfigModel;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Ljava/lang/Object;)V", False)]
    switchUser$com_onesignal_core = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lcom/onesignal/user/internal/LoginHelper$LoginEnqueueContext;")
    switchUser$com_onesignal_core$default = JavaStaticMethod("(Lcom/onesignal/user/internal/LoginHelper;Ljava/lang/String;Ljava/lang/String;ILjava/lang/Object;)Lcom/onesignal/user/internal/LoginHelper$LoginEnqueueContext;")
    enqueueLogin$com_onesignal_core = JavaMethod("(Lcom/onesignal/user/internal/LoginHelper$LoginEnqueueContext;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class LoginEnqueueContext(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/LoginHelper$LoginEnqueueContext"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
        copy$default = JavaStaticMethod("(Lcom/onesignal/user/internal/LoginHelper$LoginEnqueueContext;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ILjava/lang/Object;)Lcom/onesignal/user/internal/LoginHelper$LoginEnqueueContext;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        copy = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lcom/onesignal/user/internal/LoginHelper$LoginEnqueueContext;")
        getExternalId = JavaMethod("()Ljava/lang/String;")
        component1 = JavaMethod("()Ljava/lang/String;")
        component2 = JavaMethod("()Ljava/lang/String;")
        getAppId = JavaMethod("()Ljava/lang/String;")
        component3 = JavaMethod("()Ljava/lang/String;")
        component4 = JavaMethod("()Ljava/lang/String;")
        getNewIdentityOneSignalId = JavaMethod("()Ljava/lang/String;")
        getExistingOneSignalId = JavaMethod("()Ljava/lang/String;")

class LogoutHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/LogoutHelper"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/UserSwitcher;Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/core/internal/config/ConfigModel;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;Ljava/lang/Object;)V", False)]
    switchUser$com_onesignal_core = JavaMethod("()Lcom/onesignal/user/internal/LogoutHelper$LogoutEnqueueContext;")
    enqueueLogout$com_onesignal_core = JavaMethod("(Lcom/onesignal/user/internal/LogoutHelper$LogoutEnqueueContext;)V")

    class LogoutEnqueueContext(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/LogoutHelper$LogoutEnqueueContext"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        copy$default = JavaStaticMethod("(Lcom/onesignal/user/internal/LogoutHelper$LogoutEnqueueContext;Ljava/lang/String;Ljava/lang/String;ILjava/lang/Object;)Lcom/onesignal/user/internal/LogoutHelper$LogoutEnqueueContext;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        copy = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Lcom/onesignal/user/internal/LogoutHelper$LogoutEnqueueContext;")
        component1 = JavaMethod("()Ljava/lang/String;")
        component2 = JavaMethod("()Ljava/lang/String;")
        getAppId = JavaMethod("()Ljava/lang/String;")
        getNewOnesignalId = JavaMethod("()Ljava/lang/String;")

class LogoutHelperIvExtensionsKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/LogoutHelperIvExtensionsKt"
    switchUserIv = JavaStaticMethod("(Lcom/onesignal/user/internal/UserSwitcher;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Lcom/onesignal/core/internal/config/ConfigModel;Z)Z")

class PushSubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/PushSubscription"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;)V", False)]
    optOut = JavaMethod("()V")
    addObserver = JavaMethod("(Lcom/onesignal/user/subscriptions/IPushSubscriptionObserver;)V")
    removeObserver = JavaMethod("(Lcom/onesignal/user/subscriptions/IPushSubscriptionObserver;)V")
    optIn = JavaMethod("()V")
    getToken = JavaMethod("()Ljava/lang/String;")
    getOptedIn = JavaMethod("()Z")
    getChangeHandlersNotifier = JavaMethod("()Lcom/onesignal/common/events/EventProducer;")
    getSavedState = JavaMethod("()Lcom/onesignal/user/subscriptions/PushSubscriptionState;")
    refreshState = JavaMethod("()Lcom/onesignal/user/subscriptions/PushSubscriptionState;")

class SmsSubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/SmsSubscription"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;)V", False)]
    getNumber = JavaMethod("()Ljava/lang/String;")

class Subscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/Subscription"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;)V", False)]
    getId = JavaMethod("()Ljava/lang/String;")
    getModel = JavaMethod("()Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;")

class UninitializedPushSubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/UninitializedPushSubscription"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/UninitializedPushSubscription$Companion;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/UninitializedPushSubscription$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        createFakePushSub = JavaMethod("()Lcom/onesignal/user/internal/subscriptions/SubscriptionModel;")

class UserManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/UserManager"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/subscriptions/ISubscriptionManager;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/user/internal/customEvents/ICustomEventController;Lcom/onesignal/core/internal/language/ILanguageContext;)V", False)]
    getPushSubscription = JavaMethod("()Lcom/onesignal/user/subscriptions/IPushSubscription;")
    getOnesignalId = JavaMethod("()Ljava/lang/String;")
    getExternalId = JavaMethod("()Ljava/lang/String;")
    setLanguage = JavaMethod("(Ljava/lang/String;)V")
    addAlias = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    addAliases = JavaMethod("(Ljava/util/Map;)V")
    removeAlias = JavaMethod("(Ljava/lang/String;)V")
    removeAliases = JavaMethod("(Ljava/util/Collection;)V")
    addEmail = JavaMethod("(Ljava/lang/String;)V")
    removeEmail = JavaMethod("(Ljava/lang/String;)V")
    addSms = JavaMethod("(Ljava/lang/String;)V")
    removeSms = JavaMethod("(Ljava/lang/String;)V")
    addTag = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    addTags = JavaMethod("(Ljava/util/Map;)V")
    removeTag = JavaMethod("(Ljava/lang/String;)V")
    removeTags = JavaMethod("(Ljava/util/Collection;)V")
    getTags = JavaMethod("()Ljava/util/Map;")
    addObserver = JavaMethod("(Lcom/onesignal/user/state/IUserStateObserver;)V")
    removeObserver = JavaMethod("(Lcom/onesignal/user/state/IUserStateObserver;)V")
    trackEvent = JavaMethod("(Ljava/lang/String;Ljava/util/Map;)V")
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")
    onModelReplaced = JavaMultipleMethod([("(Lcom/onesignal/user/internal/identity/IdentityModel;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False)])
    getAliases = JavaMethod("()Ljava/util/Map;")
    getSubscriptions = JavaMethod("()Lcom/onesignal/user/internal/subscriptions/SubscriptionList;")
    getChangeHandlersNotifier = JavaMethod("()Lcom/onesignal/common/events/EventProducer;")

class UserSwitcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/UserSwitcher"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/preferences/IPreferencesService;Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/common/services/ServiceProvider;Lcom/onesignal/common/IDManager;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Lcom/onesignal/core/internal/config/ConfigModel;Lcom/onesignal/common/OneSignalUtils;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/common/AndroidUtils;Lkotlin/jvm/functions/Function0;)V", False), ("(Lcom/onesignal/core/internal/preferences/IPreferencesService;Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/common/services/ServiceProvider;Lcom/onesignal/common/IDManager;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Lcom/onesignal/core/internal/config/ConfigModel;Lcom/onesignal/common/OneSignalUtils;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/common/AndroidUtils;Lkotlin/jvm/functions/Function0;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    initUser = JavaMethod("(Z)V")
    createAndSwitchToNewUser = JavaMethod("(ZLkotlin/jvm/functions/Function2;)V")
    createAndSwitchToNewUser$default = JavaStaticMethod("(Lcom/onesignal/user/internal/UserSwitcher;ZLkotlin/jvm/functions/Function2;ILjava/lang/Object;)V")
    createPushSubscriptionFromLegacySync = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/config/ConfigModel;Lcom/onesignal/user/internal/subscriptions/SubscriptionModelStore;Landroid/content/Context;)Z")