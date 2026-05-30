from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ExecutionResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/ExecutionResponse"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/operations/ExecutionResult;Ljava/util/Map;Ljava/util/List;Ljava/lang/Integer;)V", False), ("(Lcom/onesignal/core/internal/operations/ExecutionResult;Ljava/util/Map;Ljava/util/List;Ljava/lang/Integer;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    getRetryAfterSeconds = JavaMethod("()Ljava/lang/Integer;")
    getOperations = JavaMethod("()Ljava/util/List;")
    getIdTranslations = JavaMethod("()Ljava/util/Map;")
    getResult = JavaMethod("()Lcom/onesignal/core/internal/operations/ExecutionResult;")

class ExecutionResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/ExecutionResult"
    SUCCESS = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    SUCCESS_STARTING_ONLY = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_RETRY = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_NORETRY = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_UNAUTHORIZED = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_CONFLICT = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_PAUSE_OPREPO = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    values = JavaStaticMethod("()[Lcom/onesignal/core/internal/operations/ExecutionResult;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/operations/ExecutionResult;")
    SUCCESS = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    SUCCESS_STARTING_ONLY = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_RETRY = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_NORETRY = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_UNAUTHORIZED = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_CONFLICT = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")
    FAIL_PAUSE_OPREPO = JavaStaticField("Lcom/onesignal/core/internal/operations/ExecutionResult;")

class GroupComparisonType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/GroupComparisonType"
    CREATE = JavaStaticField("Lcom/onesignal/core/internal/operations/GroupComparisonType;")
    ALTER = JavaStaticField("Lcom/onesignal/core/internal/operations/GroupComparisonType;")
    NONE = JavaStaticField("Lcom/onesignal/core/internal/operations/GroupComparisonType;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    values = JavaStaticMethod("()[Lcom/onesignal/core/internal/operations/GroupComparisonType;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/operations/GroupComparisonType;")
    CREATE = JavaStaticField("Lcom/onesignal/core/internal/operations/GroupComparisonType;")
    ALTER = JavaStaticField("Lcom/onesignal/core/internal/operations/GroupComparisonType;")
    NONE = JavaStaticField("Lcom/onesignal/core/internal/operations/GroupComparisonType;")

class IOperationExecutor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/IOperationExecutor"
    execute = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getOperations = JavaMethod("()Ljava/util/List;")

class IOperationRepo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/IOperationRepo"
    enqueue = JavaMethod("(Lcom/onesignal/core/internal/operations/Operation;Z)V")
    enqueueAndWait = JavaMethod("(Lcom/onesignal/core/internal/operations/Operation;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    containsInstanceOf = JavaMethod("(Lkotlin/reflect/KClass;)Z")
    awaitInitialized = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    forceExecuteOperations = JavaMethod("()V")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/operations/IOperationRepo$DefaultImpls"
        enqueue$default = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/core/internal/operations/Operation;ZILjava/lang/Object;)V")
        enqueueAndWait$default = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/core/internal/operations/Operation;ZLkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")

class IOperationRepoKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/IOperationRepoKt"
    containsInstanceOf = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/IOperationRepo;)Z")

class Operation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/Operation"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getExternalId = JavaMethod("()Ljava/lang/String;")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getRequiresJwt = JavaMethod("()Z")
    setExternalId$com_onesignal_core = JavaMethod("(Ljava/lang/String;)V")
    getApplyToRecordId = JavaMethod("()Ljava/lang/String;")
    getCreateComparisonKey = JavaMethod("()Ljava/lang/String;")
    getModifyComparisonKey = JavaMethod("()Ljava/lang/String;")
    getGroupComparisonType = JavaMethod("()Lcom/onesignal/core/internal/operations/GroupComparisonType;")
    getCanStartExecute = JavaMethod("()Z")
    translateIds = JavaMethod("(Ljava/util/Map;)V")