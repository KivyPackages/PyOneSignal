from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ILocationController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/controller/ILocationController"
    start = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    stop = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getLastLocation = JavaMethod("()Landroid/location/Location;")

class ILocationUpdatedHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/controller/ILocationUpdatedHandler"
    onLocationChanged = JavaMethod("(Landroid/location/Location;)V")