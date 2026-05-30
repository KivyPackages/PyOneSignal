from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class OperationModelStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/impl/OperationModelStore"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)V", False)]
    create = JavaMultipleMethod([("(Lorg/json/JSONObject;)Lcom/onesignal/common/modeling/Model;", False, False), ("(Lorg/json/JSONObject;)Lcom/onesignal/core/internal/operations/Operation;", False, False)])
    loadOperations = JavaMethod("()V")

class OperationRepo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/impl/OperationRepo"
    __javaconstructor__ = [("(Ljava/util/List;Lcom/onesignal/core/internal/operations/impl/OperationModelStore;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/core/internal/time/ITime;Lcom/onesignal/user/internal/operations/impl/states/NewRecordsState;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/config/impl/IdentityVerificationService;)V", False)]
    enqueue = JavaMethod("(Lcom/onesignal/core/internal/operations/Operation;Z)V")
    start = JavaMethod("()V")
    enqueueAndWait = JavaMethod("(Lcom/onesignal/core/internal/operations/Operation;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    containsInstanceOf = JavaMethod("(Lkotlin/reflect/KClass;)Z")
    awaitInitialized = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    forceExecuteOperations = JavaMethod("()V")
    getQueue$com_onesignal_core = JavaMethod("()Ljava/util/List;")
    getNextOps$com_onesignal_core = JavaMethod("(I)Ljava/util/List;")
    executeOperations$com_onesignal_core = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    removeOperationsWithoutExternalId$com_onesignal_core = JavaMethod("()V")
    onJwtConfigHydrated$com_onesignal_core = JavaMethod("(Z)V")
    delayBeforeNextExecution = JavaMethod("(ILjava/lang/Integer;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    delayForPostCreate = JavaMethod("(JLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    loadSavedOperations$com_onesignal_core = JavaMethod("()V")
    access$processQueueForever = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/impl/OperationRepo;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$getEnqueueIntoBucket$p = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/impl/OperationRepo;)I")
    access$waitForNewOperationAndExecutionInterval = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/impl/OperationRepo;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$getWaiter$p = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/impl/OperationRepo;)Lcom/onesignal/common/threading/WaiterWithValue;")
    access$getRetryWaiter$p = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/impl/OperationRepo;)Lcom/onesignal/common/threading/WaiterWithValue;")

    class LoopWaiterMessage(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/operations/impl/OperationRepo$LoopWaiterMessage"
        __javaconstructor__ = [("(ZJ)V", False), ("(ZJILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        getPreviousWaitedTime = JavaMethod("()J")
        getForce = JavaMethod("()Z")

    class OperationQueueItem(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/operations/impl/OperationRepo$OperationQueueItem"
        __javaconstructor__ = [("(Lcom/onesignal/core/internal/operations/Operation;Lcom/onesignal/common/threading/WaiterWithValue;II)V", False), ("(Lcom/onesignal/core/internal/operations/Operation;Lcom/onesignal/common/threading/WaiterWithValue;IIILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        toString = JavaMethod("()Ljava/lang/String;")
        getOperation = JavaMethod("()Lcom/onesignal/core/internal/operations/Operation;")
        getWaiter = JavaMethod("()Lcom/onesignal/common/threading/WaiterWithValue;")
        setWaiter = JavaMethod("(Lcom/onesignal/common/threading/WaiterWithValue;)V")
        getRetries = JavaMethod("()I")
        setRetries = JavaMethod("(I)V")
        getBucket = JavaMethod("()I")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/operations/impl/OperationRepo$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")

class OperationRepoIvExtensionsKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/impl/OperationRepoIvExtensionsKt"
    handleFailUnauthorized = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/impl/OperationRepo;Lcom/onesignal/core/internal/operations/impl/OperationRepo$OperationQueueItem;Ljava/util/List;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Z)Z")
    hasValidJwtIfRequired = JavaStaticMethod("(Lcom/onesignal/core/internal/operations/impl/OperationRepo;Lcom/onesignal/user/internal/jwt/JwtTokenStore;Lcom/onesignal/core/internal/operations/Operation;Z)Z")