from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FCMParamsObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/FCMParamsObject"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    getProjectId = JavaMethod("()Ljava/lang/String;")
    getAppId = JavaMethod("()Ljava/lang/String;")
    getApiKey = JavaMethod("()Ljava/lang/String;")

class IFeatureFlagsBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/IFeatureFlagsBackendService"
    fetchRemoteFeatureFlags = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class IParamsBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/IParamsBackendService"
    fetchParams = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class InfluenceParamsObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/InfluenceParamsObject"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/Integer;Ljava/lang/Integer;Ljava/lang/Integer;Ljava/lang/Integer;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False), ("(Ljava/lang/Integer;Ljava/lang/Integer;Ljava/lang/Integer;Ljava/lang/Integer;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;)V", False)]
    isDirectEnabled = JavaMethod("()Ljava/lang/Boolean;")
    isIndirectEnabled = JavaMethod("()Ljava/lang/Boolean;")
    isUnattributedEnabled = JavaMethod("()Ljava/lang/Boolean;")
    getIndirectNotificationAttributionWindow = JavaMethod("()Ljava/lang/Integer;")
    getNotificationLimit = JavaMethod("()Ljava/lang/Integer;")
    getIndirectIAMAttributionWindow = JavaMethod("()Ljava/lang/Integer;")
    getIamLimit = JavaMethod("()Ljava/lang/Integer;")

class ParamsObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/ParamsObject"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Boolean;Ljava/lang/Boolean;Lorg/json/JSONArray;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Long;Lcom/onesignal/core/internal/backend/InfluenceParamsObject;Lcom/onesignal/core/internal/backend/FCMParamsObject;Lcom/onesignal/core/internal/backend/RemoteLoggingParamsObject;)V", False), ("(Ljava/lang/String;Ljava/lang/Boolean;Ljava/lang/Boolean;Lorg/json/JSONArray;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Boolean;Ljava/lang/Long;Lcom/onesignal/core/internal/backend/InfluenceParamsObject;Lcom/onesignal/core/internal/backend/FCMParamsObject;Lcom/onesignal/core/internal/backend/RemoteLoggingParamsObject;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    getGoogleProjectNumber = JavaMethod("()Ljava/lang/String;")
    setGoogleProjectNumber = JavaMethod("(Ljava/lang/String;)V")
    getEnterprise = JavaMethod("()Ljava/lang/Boolean;")
    setEnterprise = JavaMethod("(Ljava/lang/Boolean;)V")
    getUseIdentityVerification = JavaMethod("()Ljava/lang/Boolean;")
    setUseIdentityVerification = JavaMethod("(Ljava/lang/Boolean;)V")
    getNotificationChannels = JavaMethod("()Lorg/json/JSONArray;")
    setNotificationChannels = JavaMethod("(Lorg/json/JSONArray;)V")
    getFirebaseAnalytics = JavaMethod("()Ljava/lang/Boolean;")
    setFirebaseAnalytics = JavaMethod("(Ljava/lang/Boolean;)V")
    getRestoreTTLFilter = JavaMethod("()Ljava/lang/Boolean;")
    setRestoreTTLFilter = JavaMethod("(Ljava/lang/Boolean;)V")
    getClearGroupOnSummaryClick = JavaMethod("()Ljava/lang/Boolean;")
    setClearGroupOnSummaryClick = JavaMethod("(Ljava/lang/Boolean;)V")
    getReceiveReceiptEnabled = JavaMethod("()Ljava/lang/Boolean;")
    setReceiveReceiptEnabled = JavaMethod("(Ljava/lang/Boolean;)V")
    getUnsubscribeWhenNotificationsDisabled = JavaMethod("()Ljava/lang/Boolean;")
    setUnsubscribeWhenNotificationsDisabled = JavaMethod("(Ljava/lang/Boolean;)V")
    getLocationShared = JavaMethod("()Ljava/lang/Boolean;")
    setLocationShared = JavaMethod("(Ljava/lang/Boolean;)V")
    getRequiresUserPrivacyConsent = JavaMethod("()Ljava/lang/Boolean;")
    setRequiresUserPrivacyConsent = JavaMethod("(Ljava/lang/Boolean;)V")
    getOpRepoExecutionInterval = JavaMethod("()Ljava/lang/Long;")
    setOpRepoExecutionInterval = JavaMethod("(Ljava/lang/Long;)V")
    getInfluenceParams = JavaMethod("()Lcom/onesignal/core/internal/backend/InfluenceParamsObject;")
    setInfluenceParams = JavaMethod("(Lcom/onesignal/core/internal/backend/InfluenceParamsObject;)V")
    getFcmParams = JavaMethod("()Lcom/onesignal/core/internal/backend/FCMParamsObject;")
    setFcmParams = JavaMethod("(Lcom/onesignal/core/internal/backend/FCMParamsObject;)V")
    getRemoteLoggingParams = JavaMethod("()Lcom/onesignal/core/internal/backend/RemoteLoggingParamsObject;")
    getDisableGMSMissingPrompt = JavaMethod("()Ljava/lang/Boolean;")
    setDisableGMSMissingPrompt = JavaMethod("(Ljava/lang/Boolean;)V")

class RemoteFeatureFlagsFetchOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/RemoteFeatureFlagsFetchOutcome"
    __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class Success(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/backend/RemoteFeatureFlagsFetchOutcome$Success"
        __javaconstructor__ = [("(Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;)V", False)]
        copy$default = JavaStaticMethod("(Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsFetchOutcome$Success;Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;ILjava/lang/Object;)Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsFetchOutcome$Success;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")
        copy = JavaMethod("(Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;)Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsFetchOutcome$Success;")
        component1 = JavaMethod("()Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;")
        getResult = JavaMethod("()Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;")

    class Unavailable(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/backend/RemoteFeatureFlagsFetchOutcome$Unavailable"
        INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsFetchOutcome$Unavailable;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")

class RemoteFeatureFlagsResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/RemoteFeatureFlagsResult"
    __javaconstructor__ = [("(Ljava/util/List;Lkotlinx/serialization/json/JsonObject;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult$Companion;")
    copy$default = JavaStaticMethod("(Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;Ljava/util/List;Lkotlinx/serialization/json/JsonObject;ILjava/lang/Object;)Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    copy = JavaMethod("(Ljava/util/List;Lkotlinx/serialization/json/JsonObject;)Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;")
    component1 = JavaMethod("()Ljava/util/List;")
    component2 = JavaMethod("()Lkotlinx/serialization/json/JsonObject;")
    getMetadata = JavaMethod("()Lkotlinx/serialization/json/JsonObject;")
    getEnabledKeys = JavaMethod("()Ljava/util/List;")
    access$getEMPTY$cp = JavaStaticMethod("()Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/backend/RemoteFeatureFlagsResult$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        getEMPTY = JavaMethod("()Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;")

class RemoteLoggingParamsObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/RemoteLoggingParamsObject"
    __javaconstructor__ = [("()V", False), ("(Lcom/onesignal/debug/LogLevel;ZILkotlin/jvm/internal/DefaultConstructorMarker;)V", False), ("(Lcom/onesignal/debug/LogLevel;Z)V", False)]
    isEnabled = JavaMethod("()Z")
    getLogLevel = JavaMethod("()Lcom/onesignal/debug/LogLevel;")