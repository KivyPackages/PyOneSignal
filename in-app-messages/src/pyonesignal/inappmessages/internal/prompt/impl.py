from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class InAppMessageLocationPrompt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/prompt/impl/InAppMessageLocationPrompt"
    __javaconstructor__ = [("(Lcom/onesignal/location/ILocationManager;)V", False)]
    getPromptKey = JavaMethod("()Ljava/lang/String;")
    handlePrompt = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class InAppMessagePrompt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt"
    __javaconstructor__ = [("()V", False)]
    getPromptKey = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    hasPrompted = JavaMethod("()Z")
    setPrompted = JavaMethod("(Z)V")
    handlePrompt = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class OSPromptActionCompletionCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$OSPromptActionCompletionCallback"
        onCompleted = JavaMethod("(Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;)V")

    class PromptActionResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult"
        PERMISSION_GRANTED = JavaStaticField("Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")
        PERMISSION_DENIED = JavaStaticField("Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")
        LOCATION_PERMISSIONS_MISSING_MANIFEST = JavaStaticField("Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")
        ERROR = JavaStaticField("Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")
        values = JavaStaticMethod("()[Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")
        getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
        PERMISSION_GRANTED = JavaStaticField("Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")
        PERMISSION_DENIED = JavaStaticField("Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")
        LOCATION_PERMISSIONS_MISSING_MANIFEST = JavaStaticField("Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")
        ERROR = JavaStaticField("Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt$PromptActionResult;")

class InAppMessagePromptFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePromptFactory"
    __javaconstructor__ = [("(Lcom/onesignal/notifications/INotificationsManager;Lcom/onesignal/location/ILocationManager;)V", False)]
    createPrompt = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt;")

class InAppMessagePushPrompt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePushPrompt"
    __javaconstructor__ = [("(Lcom/onesignal/notifications/INotificationsManager;)V", False)]
    getPromptKey = JavaMethod("()Ljava/lang/String;")
    handlePrompt = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")