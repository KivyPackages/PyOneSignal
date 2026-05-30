from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ActivityLifecycleHandlerBase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/application/ActivityLifecycleHandlerBase"
    __javaconstructor__ = [("()V", False)]
    onActivityStopped = JavaMethod("(Landroid/app/Activity;)V")
    onActivityAvailable = JavaMethod("(Landroid/app/Activity;)V")

class AppEntryAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/application/AppEntryAction"
    NOTIFICATION_CLICK = JavaStaticField("Lcom/onesignal/core/internal/application/AppEntryAction;")
    APP_OPEN = JavaStaticField("Lcom/onesignal/core/internal/application/AppEntryAction;")
    APP_CLOSE = JavaStaticField("Lcom/onesignal/core/internal/application/AppEntryAction;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    values = JavaStaticMethod("()[Lcom/onesignal/core/internal/application/AppEntryAction;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/application/AppEntryAction;")
    isNotificationClick = JavaMethod("()Z")
    isAppOpen = JavaMethod("()Z")
    isAppClose = JavaMethod("()Z")
    NOTIFICATION_CLICK = JavaStaticField("Lcom/onesignal/core/internal/application/AppEntryAction;")
    APP_OPEN = JavaStaticField("Lcom/onesignal/core/internal/application/AppEntryAction;")
    APP_CLOSE = JavaStaticField("Lcom/onesignal/core/internal/application/AppEntryAction;")

class ApplicationLifecycleHandlerBase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/application/ApplicationLifecycleHandlerBase"
    __javaconstructor__ = [("()V", False)]
    onFocus = JavaMethod("(Z)V")
    onUnfocused = JavaMethod("()V")

class IActivityLifecycleHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/application/IActivityLifecycleHandler"
    onActivityStopped = JavaMethod("(Landroid/app/Activity;)V")
    onActivityAvailable = JavaMethod("(Landroid/app/Activity;)V")

class IApplicationLifecycleHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/application/IApplicationLifecycleHandler"
    onFocus = JavaMethod("(Z)V")
    onUnfocused = JavaMethod("()V")

class IApplicationService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/application/IApplicationService"
    getAppContext = JavaMethod("()Landroid/content/Context;")
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