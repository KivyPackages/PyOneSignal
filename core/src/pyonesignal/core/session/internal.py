from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class SessionManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/SessionManager"
    __javaconstructor__ = [("(Lcom/onesignal/session/internal/outcomes/IOutcomeEventsController;)V", False)]
    addOutcome = JavaMethod("(Ljava/lang/String;)V")
    addUniqueOutcome = JavaMethod("(Ljava/lang/String;)V")
    addOutcomeWithValue = JavaMethod("(Ljava/lang/String;F)V")
    access$get_outcomeController$p = JavaStaticMethod("(Lcom/onesignal/session/internal/SessionManager;)Lcom/onesignal/session/internal/outcomes/IOutcomeEventsController;")