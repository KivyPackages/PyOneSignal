from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ITriggerController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/ITriggerController"
    isTriggerOnMessage = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Ljava/util/Collection;)Z")
    evaluateMessageTriggers = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)Z")
    messageHasOnlyDynamicTriggers = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)Z")

class ITriggerHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/ITriggerHandler"
    onTriggerCompleted = JavaMethod("(Ljava/lang/String;)V")
    onTriggerConditionChanged = JavaMethod("(Ljava/lang/String;)V")
    onTriggerChanged = JavaMethod("(Ljava/lang/String;)V")

class TriggerModel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/TriggerModel"
    __javaconstructor__ = [("()V", False)]
    getValue = JavaMethod("()Ljava/lang/Object;")
    getKey = JavaMethod("()Ljava/lang/String;")
    setValue = JavaMethod("(Ljava/lang/Object;)V")
    setKey = JavaMethod("(Ljava/lang/String;)V")

class TriggerModelStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/TriggerModelStore"
    __javaconstructor__ = [("()V", False)]