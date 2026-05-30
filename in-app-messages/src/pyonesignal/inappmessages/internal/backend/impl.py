from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class InAppBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/backend/impl/InAppBackendService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/http/IHttpClient;Lcom/onesignal/core/internal/device/IDeviceService;Lcom/onesignal/inAppMessages/internal/hydrators/InAppHydrator;)V", False)]
    getIAMData = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getIAMPreviewData = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendIAMImpression = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$get_deviceService$p = JavaStaticMethod("(Lcom/onesignal/inAppMessages/internal/backend/impl/InAppBackendService;)Lcom/onesignal/core/internal/device/IDeviceService;")
    access$attemptFetchWithRetries = JavaStaticMethod("(Lcom/onesignal/inAppMessages/internal/backend/impl/InAppBackendService;Ljava/lang/String;Lcom/onesignal/common/consistency/RywData;Lkotlin/jvm/functions/Function0;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$fetchInAppMessagesWithoutRywToken = JavaStaticMethod("(Lcom/onesignal/inAppMessages/internal/backend/impl/InAppBackendService;Ljava/lang/String;Lkotlin/jvm/functions/Function0;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    listInAppMessages = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/common/consistency/RywData;Lkotlin/jvm/functions/Function0;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    listInAppMessagesIv = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/common/consistency/RywData;Lkotlin/jvm/functions/Function0;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendIAMPageImpression = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendIAMClick = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class InAppBackendServiceKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/backend/impl/InAppBackendServiceKt"