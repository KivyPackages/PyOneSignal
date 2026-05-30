from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class HttpClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/impl/HttpClient"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/http/impl/IHttpConnectionFactory;Lcom/onesignal/core/internal/preferences/IPreferencesService;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/core/internal/time/ITime;Lcom/onesignal/core/internal/device/IInstallIdService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/http/impl/HttpClient$Companion;")
    patch = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    get = JavaMethod("(Ljava/lang/String;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    put = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    delete = JavaMethod("(Ljava/lang/String;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    post = JavaMethod("(Ljava/lang/String;Lorg/json/JSONObject;Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$get_prefs$p = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;)Lcom/onesignal/core/internal/preferences/IPreferencesService;")
    access$makeRequest = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;Ljava/lang/String;Ljava/lang/String;Lorg/json/JSONObject;ILcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$makeRequestIODispatcher = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;Ljava/lang/String;Ljava/lang/String;Lorg/json/JSONObject;ILcom/onesignal/core/internal/http/impl/OptionalHeaders;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$get_connectionFactory$p = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;)Lcom/onesignal/core/internal/http/impl/IHttpConnectionFactory;")
    access$get_installIdService$p = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;)Lcom/onesignal/core/internal/device/IInstallIdService;")
    access$logHTTPSent = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;Ljava/lang/String;Ljava/net/URL;Lorg/json/JSONObject;Ljava/util/Map;)V")
    access$retryAfterFromResponse = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;Ljava/net/HttpURLConnection;)Ljava/lang/Integer;")
    access$retryLimitFromResponse = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;Ljava/net/HttpURLConnection;)Ljava/lang/Integer;")
    access$get_time$p = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;)Lcom/onesignal/core/internal/time/ITime;")
    access$getDelayNewRequestsUntil$p = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;)J")
    access$setDelayNewRequestsUntil$p = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;J)V")
    access$get_configModelStore$p = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/HttpClient;)Lcom/onesignal/core/internal/config/ConfigModelStore;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/http/impl/HttpClient$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class HttpClientKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/impl/HttpClientKt"
    HTTP_SDK_VERSION_HEADER_KEY = JavaStaticField("Ljava/lang/String;")
    getHTTP_SDK_VERSION_HEADER_VALUE = JavaStaticMethod("()Ljava/lang/String;")

class HttpConnectionFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/impl/HttpConnectionFactory"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    newHttpURLConnection = JavaMethod("(Ljava/lang/String;)Ljava/net/HttpURLConnection;")

class IHttpConnectionFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/impl/IHttpConnectionFactory"
    newHttpURLConnection = JavaMethod("(Ljava/lang/String;)Ljava/net/HttpURLConnection;")

class OptionalHeaders(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/impl/OptionalHeaders"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Integer;Ljava/lang/Long;Ljava/lang/String;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Integer;Ljava/lang/Long;Ljava/lang/String;)V", False)]
    copy$default = JavaStaticMethod("(Lcom/onesignal/core/internal/http/impl/OptionalHeaders;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Integer;Ljava/lang/Long;Ljava/lang/String;ILjava/lang/Object;)Lcom/onesignal/core/internal/http/impl/OptionalHeaders;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    copy = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Integer;Ljava/lang/Long;Ljava/lang/String;)Lcom/onesignal/core/internal/http/impl/OptionalHeaders;")
    component1 = JavaMethod("()Ljava/lang/String;")
    component2 = JavaMethod("()Ljava/lang/String;")
    getRetryCount = JavaMethod("()Ljava/lang/Integer;")
    getSessionDuration = JavaMethod("()Ljava/lang/Long;")
    getCacheKey = JavaMethod("()Ljava/lang/String;")
    getJwt = JavaMethod("()Ljava/lang/String;")
    component3 = JavaMethod("()Ljava/lang/Integer;")
    component4 = JavaMethod("()Ljava/lang/Long;")
    component5 = JavaMethod("()Ljava/lang/String;")
    getRywToken = JavaMethod("()Ljava/lang/String;")

class TLS12SocketFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/http/impl/TLS12SocketFactory"
    __javaconstructor__ = [("(Ljavax/net/ssl/SSLSocketFactory;)V", False)]
    getSslSocketFactory = JavaMethod("()Ljavax/net/ssl/SSLSocketFactory;")
    setSslSocketFactory = JavaMethod("(Ljavax/net/ssl/SSLSocketFactory;)V")
    getDefaultCipherSuites = JavaMethod("()[Ljava/lang/String;")
    getSupportedCipherSuites = JavaMethod("()[Ljava/lang/String;")
    createSocket = JavaMultipleMethod([("(Ljava/net/InetAddress;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;ILjava/net/InetAddress;I)Ljava/net/Socket;", False, False), ("()Ljava/net/Socket;", False, False), ("(Ljava/net/Socket;Ljava/lang/String;IZ)Ljava/net/Socket;", False, False), ("(Ljava/lang/String;I)Ljava/net/Socket;", False, False)])