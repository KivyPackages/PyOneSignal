from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CustomEventBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/customEvents/impl/CustomEventBackendService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/http/IHttpClient;)V", False)]
    sendCustomEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;JLjava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/customEvents/impl/CustomEventMetadata;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class CustomEventController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/customEvents/impl/CustomEventController"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/core/internal/time/ITime;Lcom/onesignal/core/internal/operations/IOperationRepo;)V", False)]
    sendCustomEvent = JavaMethod("(Ljava/lang/String;Ljava/util/Map;)V")

class CustomEventMetadata(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/customEvents/impl/CustomEventMetadata"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/user/internal/customEvents/impl/CustomEventMetadata$Companion;")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    getAppVersion = JavaMethod("()Ljava/lang/String;")
    getDeviceModel = JavaMethod("()Ljava/lang/String;")
    getDeviceType = JavaMethod("()Ljava/lang/String;")
    getSdk = JavaMethod("()Ljava/lang/String;")
    getDeviceOS = JavaMethod("()Ljava/lang/String;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/customEvents/impl/CustomEventMetadata$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]