from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LocationModule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/LocationModule"
    __javaconstructor__ = [("()V", False)]
    register = JavaMethod("(Lcom/onesignal/common/services/ServiceBuilder;)V")