from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IBootstrapService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/startup/IBootstrapService"
    bootstrap = JavaMethod("()V")

class IStartableService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/startup/IStartableService"
    start = JavaMethod("()V")

class StartupService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/startup/StartupService"
    __javaconstructor__ = [("(Lcom/onesignal/common/services/ServiceProvider;)V", False)]
    bootstrap = JavaMethod("()V")
    scheduleStart = JavaMethod("()V")
    access$getServices$p = JavaStaticMethod("(Lcom/onesignal/core/internal/startup/StartupService;)Lcom/onesignal/common/services/ServiceProvider;")