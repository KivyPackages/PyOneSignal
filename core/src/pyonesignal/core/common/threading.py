from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class OneSignalDispatchers(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/threading/OneSignalDispatchers"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/threading/OneSignalDispatchers;")
    BASE_THREAD_NAME = JavaStaticField("Ljava/lang/String;")
    getDefault = JavaMethod("()Lkotlinx/coroutines/CoroutineDispatcher;")
    getIO = JavaMethod("()Lkotlinx/coroutines/CoroutineDispatcher;")
    getSerialIO = JavaMethod("()Lkotlinx/coroutines/CoroutineDispatcher;")
    launchOnIO = JavaMethod("(Lkotlin/jvm/functions/Function1;)Lkotlinx/coroutines/Job;")
    launchOnDefault = JavaMethod("(Lkotlin/jvm/functions/Function1;)Lkotlinx/coroutines/Job;")
    launchOnSerialIO = JavaMethod("(Lkotlin/jvm/functions/Function1;)Lkotlinx/coroutines/Job;")
    prewarm = JavaMethod("()V")
    resetPrewarmForTest$com_onesignal_core = JavaMethod("()V")
    getPerformanceMetrics$com_onesignal_core = JavaMethod("()Ljava/lang/String;")
    getStatus$com_onesignal_core = JavaMethod("()Ljava/lang/String;")
    executorStatus$com_onesignal_core = JavaMethod("(Ljava/lang/String;Lkotlin/jvm/functions/Function0;)Ljava/lang/String;")
    scopeStatus$com_onesignal_core = JavaMethod("(Ljava/lang/String;Lkotlin/jvm/functions/Function0;)Ljava/lang/String;")
    access$getIoExecutor = JavaStaticMethod("(Lcom/onesignal/common/threading/OneSignalDispatchers;)Ljava/util/concurrent/ThreadPoolExecutor;")
    access$getDefaultExecutor = JavaStaticMethod("(Lcom/onesignal/common/threading/OneSignalDispatchers;)Ljava/util/concurrent/ThreadPoolExecutor;")
    access$getSerialIOExecutor = JavaStaticMethod("(Lcom/onesignal/common/threading/OneSignalDispatchers;)Ljava/util/concurrent/ExecutorService;")
    access$getIOScope = JavaStaticMethod("(Lcom/onesignal/common/threading/OneSignalDispatchers;)Lkotlinx/coroutines/CoroutineScope;")
    access$getDefaultScope = JavaStaticMethod("(Lcom/onesignal/common/threading/OneSignalDispatchers;)Lkotlinx/coroutines/CoroutineScope;")
    access$getSerialIOScope = JavaStaticMethod("(Lcom/onesignal/common/threading/OneSignalDispatchers;)Lkotlinx/coroutines/CoroutineScope;")

class ThreadUtilsKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/threading/ThreadUtilsKt"
    suspendifyOnMain = JavaStaticMethod("(Lkotlin/jvm/functions/Function1;)V")
    launchOnIO = JavaStaticMethod("(Lkotlin/jvm/functions/Function1;)Lkotlinx/coroutines/Job;")
    launchOnDefault = JavaStaticMethod("(Lkotlin/jvm/functions/Function1;)Lkotlinx/coroutines/Job;")
    suspendifyOnIO = JavaMultipleMethod([("(Lkotlin/jvm/functions/Function1;Lkotlin/jvm/functions/Function0;)V", True, False), ("(Lkotlin/jvm/functions/Function1;)V", True, False)])
    suspendifyWithCompletion = JavaStaticMethod("(ZLkotlin/jvm/functions/Function1;Lkotlin/jvm/functions/Function0;)V")
    suspendifyOnIO$default = JavaStaticMethod("(Lkotlin/jvm/functions/Function1;Lkotlin/jvm/functions/Function0;ILjava/lang/Object;)V")
    suspendifyOnDefault = JavaStaticMethod("(Lkotlin/jvm/functions/Function1;)V")
    suspendifyOnSerialIO = JavaStaticMethod("(Lkotlin/jvm/functions/Function1;)V")
    runOnSerialIOIfBackgroundThreading = JavaStaticMethod("(Lkotlin/jvm/functions/Function0;)V")
    suspendifyWithCompletion$default = JavaStaticMethod("(ZLkotlin/jvm/functions/Function1;Lkotlin/jvm/functions/Function0;ILjava/lang/Object;)V")
    suspendifyWithErrorHandling = JavaStaticMethod("(ZLkotlin/jvm/functions/Function1;Lkotlin/jvm/functions/Function1;Lkotlin/jvm/functions/Function0;)V")
    suspendifyWithErrorHandling$default = JavaStaticMethod("(ZLkotlin/jvm/functions/Function1;Lkotlin/jvm/functions/Function1;Lkotlin/jvm/functions/Function0;ILjava/lang/Object;)V")

class ThreadingMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/threading/ThreadingMode"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/threading/ThreadingMode;")
    setUseBackgroundThreading = JavaMethod("(Z)V")
    updateUseBackgroundThreading = JavaMethod("(ZLjava/lang/String;)V")
    getUseBackgroundThreading = JavaMethod("()Z")

class Waiter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/threading/Waiter"
    __javaconstructor__ = [("()V", False)]
    wake = JavaMethod("()V")
    waitForWake = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class WaiterWithValue(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/threading/WaiterWithValue"
    __javaconstructor__ = [("()V", False)]
    wake = JavaMethod("(Ljava/lang/Object;)V")
    waitForWake = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")