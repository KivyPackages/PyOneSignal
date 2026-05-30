from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NewRecordsState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/operations/impl/states/NewRecordsState"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/time/ITime;Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    add = JavaMethod("(Ljava/lang/String;)V")
    canAccess = JavaMethod("(Ljava/lang/String;)Z")
    isInMissingRetryWindow = JavaMethod("(Ljava/lang/String;)Z")