from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IdentityBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/impl/IdentityBackendService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/http/IHttpClient;)V", False)]
    deleteAlias = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    setAlias = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/util/Map;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class JSONConverter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/impl/JSONConverter"
    INSTANCE = JavaStaticField("Lcom/onesignal/user/internal/backend/impl/JSONConverter;")
    convertToCreateUserResponse = JavaMethod("(Lorg/json/JSONObject;)Lcom/onesignal/user/internal/backend/CreateUserResponse;")
    convertToJSON = JavaMultipleMethod([("(Ljava/util/List;)Lorg/json/JSONArray;", False, False), ("(Lcom/onesignal/user/internal/backend/SubscriptionObject;)Lorg/json/JSONObject;", False, False), ("(Lcom/onesignal/user/internal/backend/PropertiesObject;)Lorg/json/JSONObject;", False, False), ("(Lcom/onesignal/user/internal/backend/PropertiesDeltasObject;)Lorg/json/JSONObject;", False, False)])

class SubscriptionBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/impl/SubscriptionBackendService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/http/IHttpClient;)V", False)]
    deleteSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    updateSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/backend/SubscriptionObject;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    createSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/backend/SubscriptionObject;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getIdentityFromSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    transferSubscription = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class UserBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/backend/impl/UserBackendService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/http/IHttpClient;)V", False)]
    getUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    createUser = JavaMethod("(Ljava/lang/String;Ljava/util/Map;Ljava/util/List;Ljava/util/Map;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    updateUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/backend/PropertiesObject;ZLcom/onesignal/user/internal/backend/PropertiesDeltasObject;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")