from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Time(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/time/impl/Time"
    __javaconstructor__ = [("()V", False)]
    getCurrentTimeMillis = JavaMethod("()J")
    getProcessUptimeMillis = JavaMethod("()J")