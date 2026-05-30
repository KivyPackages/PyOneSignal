from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ISessionLifecycleHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/session/ISessionLifecycleHandler"
    onSessionStarted = JavaMethod("()V")
    onSessionActive = JavaMethod("()V")
    onSessionEnded = JavaMethod("(J)V")

class ISessionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/session/ISessionService"
    getStartTime = JavaMethod("()J")

class SessionModel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/session/SessionModel"
    __javaconstructor__ = [("()V", False)]
    getStartTime = JavaMethod("()J")
    getSessionId = JavaMethod("()Ljava/lang/String;")
    setStartTime = JavaMethod("(J)V")
    setSessionId = JavaMethod("(Ljava/lang/String;)V")
    isValid = JavaMethod("()Z")
    setValid = JavaMethod("(Z)V")
    getFocusTime = JavaMethod("()J")
    setFocusTime = JavaMethod("(J)V")
    getActiveDuration = JavaMethod("()J")
    setActiveDuration = JavaMethod("(J)V")

class SessionModelStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/session/SessionModelStore"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)V", False)]