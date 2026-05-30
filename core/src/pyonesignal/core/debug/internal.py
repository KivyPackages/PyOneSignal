from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DebugManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/debug/internal/DebugManager"
    __javaconstructor__ = [("()V", False)]
    getLogLevel = JavaMethod("()Lcom/onesignal/debug/LogLevel;")
    setLogLevel = JavaMethod("(Lcom/onesignal/debug/LogLevel;)V")
    getAlertLevel = JavaMethod("()Lcom/onesignal/debug/LogLevel;")
    setAlertLevel = JavaMethod("(Lcom/onesignal/debug/LogLevel;)V")
    addLogListener = JavaMethod("(Lcom/onesignal/debug/ILogListener;)V")
    removeLogListener = JavaMethod("(Lcom/onesignal/debug/ILogListener;)V")