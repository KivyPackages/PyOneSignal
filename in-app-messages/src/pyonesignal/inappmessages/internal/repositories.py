from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IInAppRepository(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/repositories/IInAppRepository"
    cleanCachedInAppMessages = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    listInAppMessages = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    saveInAppMessage = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")