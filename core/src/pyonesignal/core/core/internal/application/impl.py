from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ApplicationService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/application/impl/ApplicationService"
    __javaconstructor__ = [("()V", False)]
    getAppContext = JavaMethod("()Landroid/content/Context;")
    start = JavaMethod("(Landroid/content/Context;)V")
    setCurrent = JavaMethod("(Landroid/app/Activity;)V")
    onActivityCreated = JavaMethod("(Landroid/app/Activity;Landroid/os/Bundle;)V")
    onActivityStarted = JavaMethod("(Landroid/app/Activity;)V")
    onActivityResumed = JavaMethod("(Landroid/app/Activity;)V")
    onActivityPaused = JavaMethod("(Landroid/app/Activity;)V")
    onActivitySaveInstanceState = JavaMethod("(Landroid/app/Activity;Landroid/os/Bundle;)V")
    onActivityDestroyed = JavaMethod("(Landroid/app/Activity;)V")
    onGlobalLayout = JavaMethod("()V")
    decorViewReady = JavaMethod("(Landroid/app/Activity;Ljava/lang/Runnable;)V")
    access$onOrientationChanged = JavaStaticMethod("(Lcom/onesignal/core/internal/application/impl/ApplicationService;ILandroid/app/Activity;)V")
    addActivityLifecycleHandler = JavaMethod("(Lcom/onesignal/core/internal/application/IActivityLifecycleHandler;)V")
    getCurrent = JavaMethod("()Landroid/app/Activity;")
    isInForeground = JavaMethod("()Z")
    getEntryState = JavaMethod("()Lcom/onesignal/core/internal/application/AppEntryAction;")
    setEntryState = JavaMethod("(Lcom/onesignal/core/internal/application/AppEntryAction;)V")
    waitUntilSystemConditionsAvailable = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    waitUntilActivityReady = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    removeActivityLifecycleHandler = JavaMethod("(Lcom/onesignal/core/internal/application/IActivityLifecycleHandler;)V")
    addApplicationLifecycleHandler = JavaMethod("(Lcom/onesignal/core/internal/application/IApplicationLifecycleHandler;)V")
    removeApplicationLifecycleHandler = JavaMethod("(Lcom/onesignal/core/internal/application/IApplicationLifecycleHandler;)V")
    onActivityStopped = JavaMethod("(Landroid/app/Activity;)V")

class ISystemConditionHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/application/impl/ISystemConditionHandler"
    systemConditionChanged = JavaMethod("()V")