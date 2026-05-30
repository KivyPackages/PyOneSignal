from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ConsistencyManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/consistency/impl/ConsistencyManager"
    __javaconstructor__ = [("()V", False)]
    setRywData = JavaMethod("(Ljava/lang/String;Lcom/onesignal/common/consistency/models/IConsistencyKeyEnum;Lcom/onesignal/common/consistency/RywData;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getRywDataFromAwaitableCondition = JavaMethod("(Lcom/onesignal/common/consistency/models/ICondition;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    resolveConditionsWithID = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")