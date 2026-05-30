from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ICustomEventBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/customEvents/ICustomEventBackendService"
    sendCustomEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;JLjava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/customEvents/impl/CustomEventMetadata;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/customEvents/ICustomEventBackendService$DefaultImpls"
        sendCustomEvent$default = JavaStaticMethod("(Lcom/onesignal/user/internal/customEvents/ICustomEventBackendService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;JLjava/lang/String;Ljava/lang/String;Lcom/onesignal/user/internal/customEvents/impl/CustomEventMetadata;Ljava/lang/String;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")

class ICustomEventController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/customEvents/ICustomEventController"
    sendCustomEvent = JavaMethod("(Ljava/lang/String;Ljava/util/Map;)V")