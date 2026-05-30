from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class InAppStateService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/state/InAppStateService"
    __javaconstructor__ = [("()V", False)]
    setPaused = JavaMethod("(Z)V")
    getPaused = JavaMethod("()Z")
    getInAppMessageIdShowing = JavaMethod("()Ljava/lang/String;")
    getLastTimeInAppDismissed = JavaMethod("()Ljava/lang/Long;")
    setLastTimeInAppDismissed = JavaMethod("(Ljava/lang/Long;)V")
    setInAppMessageIdShowing = JavaMethod("(Ljava/lang/String;)V")
    getCurrentPrompt = JavaMethod("()Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt;")
    setCurrentPrompt = JavaMethod("(Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt;)V")