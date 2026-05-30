from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ILocationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/ILocationManager"
    requestPermission = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    isShared = JavaMethod("()Z")
    setShared = JavaMethod("(Z)V")