from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class GetIAMDataResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/backend/GetIAMDataResponse"
    __javaconstructor__ = [("(Lcom/onesignal/inAppMessages/internal/InAppMessageContent;Z)V", False)]
    getShouldRetry = JavaMethod("()Z")
    getContent = JavaMethod("()Lcom/onesignal/inAppMessages/internal/InAppMessageContent;")

class IInAppBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/backend/IInAppBackendService"
    getIAMData = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getIAMPreviewData = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendIAMImpression = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    listInAppMessages = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/common/consistency/RywData;Lkotlin/jvm/functions/Function0;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    listInAppMessagesIv = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/common/consistency/RywData;Lkotlin/jvm/functions/Function0;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendIAMPageImpression = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendIAMClick = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")