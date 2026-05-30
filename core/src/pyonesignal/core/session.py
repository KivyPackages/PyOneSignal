from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ISessionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/ISessionManager"
    addOutcome = JavaMethod("(Ljava/lang/String;)V")
    addUniqueOutcome = JavaMethod("(Ljava/lang/String;)V")
    addOutcomeWithValue = JavaMethod("(Ljava/lang/String;F)V")

class SessionModule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/SessionModule"
    __javaconstructor__ = [("()V", False)]
    register = JavaMethod("(Lcom/onesignal/common/services/ServiceBuilder;)V")