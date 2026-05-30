from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LocationPreferencesService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/preferences/impl/LocationPreferencesService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)V", False)]
    getLastLocationTime = JavaMethod("()J")
    setLastLocationTime = JavaMethod("(J)V")