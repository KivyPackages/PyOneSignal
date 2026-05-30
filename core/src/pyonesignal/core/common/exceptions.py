from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class BackendException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/exceptions/BackendException"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/Integer;)V", False), ("(ILjava/lang/String;Ljava/lang/Integer;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    getRetryAfterSeconds = JavaMethod("()Ljava/lang/Integer;")
    getStatusCode = JavaMethod("()I")
    getResponse = JavaMethod("()Ljava/lang/String;")

class MainThreadException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/exceptions/MainThreadException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]