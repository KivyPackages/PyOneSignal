from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class MisconfiguredLocationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/MisconfiguredLocationManager"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/location/internal/MisconfiguredLocationManager$Companion;")
    requestPermission = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    isShared = JavaMethod("()Z")
    setShared = JavaMethod("(Z)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/location/internal/MisconfiguredLocationManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        access$getEXCEPTION = JavaStaticMethod("(Lcom/onesignal/location/internal/MisconfiguredLocationManager$Companion;)Ljava/lang/Exception;")