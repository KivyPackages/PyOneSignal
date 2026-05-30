from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ITime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/time/ITime"
    getCurrentTimeMillis = JavaMethod("()J")
    getProcessUptimeMillis = JavaMethod("()J")