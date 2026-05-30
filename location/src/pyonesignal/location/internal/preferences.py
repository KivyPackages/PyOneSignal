from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ILocationPreferencesService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/preferences/ILocationPreferencesService"
    getLastLocationTime = JavaMethod("()J")
    setLastLocationTime = JavaMethod("(J)V")