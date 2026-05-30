from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ICondition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/consistency/models/ICondition"
    getId = JavaMethod("()Ljava/lang/String;")
    isMet = JavaMethod("(Ljava/util/Map;)Z")
    getRywData = JavaMethod("(Ljava/util/Map;)Lcom/onesignal/common/consistency/RywData;")

class IConsistencyKeyEnum(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/consistency/models/IConsistencyKeyEnum"

class IConsistencyManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/consistency/models/IConsistencyManager"
    setRywData = JavaMethod("(Ljava/lang/String;Lcom/onesignal/common/consistency/models/IConsistencyKeyEnum;Lcom/onesignal/common/consistency/RywData;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getRywDataFromAwaitableCondition = JavaMethod("(Lcom/onesignal/common/consistency/models/ICondition;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    resolveConditionsWithID = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")