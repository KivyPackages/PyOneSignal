from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CacheKeys(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/CacheKeys"
    INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/http/CacheKeys;")
    GET_TAGS = JavaStaticField("Ljava/lang/String;")
    REMOTE_PARAMS = JavaStaticField("Ljava/lang/String;")

class HttpResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/HttpResponse"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/Throwable;Ljava/lang/Integer;Ljava/lang/Integer;)V", False), ("(ILjava/lang/String;Ljava/lang/Throwable;Ljava/lang/Integer;Ljava/lang/Integer;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    getRetryAfterSeconds = JavaMethod("()Ljava/lang/Integer;")
    getStatusCode = JavaMethod("()I")
    isSuccess = JavaMethod("()Z")
    getThrowable = JavaMethod("()Ljava/lang/Throwable;")
    getRetryLimit = JavaMethod("()Ljava/lang/Integer;")
    isClientError = JavaMethod("()Z")
    getPayload = JavaMethod("()Ljava/lang/String;")

class IHttpClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/IHttpClient"
    patch = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    get = JavaMethod("(Ljava/lang/String;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    delete = JavaMethod("(Ljava/lang/String;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    post = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/http/IHttpClient$DefaultImpls"
        put$default = JavaStaticMethod("(Lcom/onesignal/core/internal/http/IHttpClient;Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        patch$default = JavaStaticMethod("(Lcom/onesignal/core/internal/http/IHttpClient;Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        post$default = JavaStaticMethod("(Lcom/onesignal/core/internal/http/IHttpClient;Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        delete$default = JavaStaticMethod("(Lcom/onesignal/core/internal/http/IHttpClient;Ljava/lang/String;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        get$default = JavaStaticMethod("(Lcom/onesignal/core/internal/http/IHttpClient;Ljava/lang/String;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")

class OneSignalService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/OneSignalService"
    INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/http/OneSignalService;")
    ONESIGNAL_API_BASE_URL = JavaStaticField("Ljava/lang/String;")