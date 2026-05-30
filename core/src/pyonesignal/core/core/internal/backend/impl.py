from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FeatureFlagsBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/impl/FeatureFlagsBackendService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/http/IHttpClient;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/backend/impl/FeatureFlagsBackendService$Companion;")
    TURBINE_FEATURES_PLATFORM_ANDROID = JavaStaticField("Ljava/lang/String;")
    fetchRemoteFeatureFlags = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/backend/impl/FeatureFlagsBackendService$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        isValidFeaturesSdkVersionLabel = JavaMethod("(Ljava/lang/String;)Z")
        buildFeatureFlagsGetPath$com_onesignal_core = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")

class FeatureFlagsJsonParser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/impl/FeatureFlagsJsonParser"
    INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/backend/impl/FeatureFlagsJsonParser;")
    parseSuccessful = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;")
    getFormat = JavaMethod("()Lkotlinx/serialization/json/Json;")
    encodeMetadata = JavaMethod("(Lkotlinx/serialization/json/JsonObject;)Ljava/lang/String;")
    parseStoredMetadataMap = JavaMethod("(Ljava/lang/String;)Ljava/util/Map;")
    parse = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/backend/RemoteFeatureFlagsResult;")

class ParamsBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/impl/ParamsBackendService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/http/IHttpClient;)V", False)]
    fetchParams = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$processOutcomeJson = JavaStaticMethod("(Lcom/onesignal/core/internal/backend/impl/ParamsBackendService;Lorg/json/JSONObject;)Lcom/onesignal/core/internal/backend/InfluenceParamsObject;")

class TurbineSdkFeatureFlagsPath(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/backend/impl/TurbineSdkFeatureFlagsPath"
    INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/backend/impl/TurbineSdkFeatureFlagsPath;")
    isValidFeaturesSdkVersionLabel = JavaMethod("(Ljava/lang/String;)Z")
    buildGetPath = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    percentEncodePathSegmentUtf8$com_onesignal_core = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")