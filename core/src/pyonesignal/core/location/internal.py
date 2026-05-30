from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class MisconfiguredLocationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/MisconfiguredLocationManager"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/location/internal/MisconfiguredLocationManager$Companion;")
    isShared = JavaMethod("()Z")
    setShared = JavaMethod("(Z)V")
    requestPermission = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/location/internal/MisconfiguredLocationManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        access$getEXCEPTION = JavaStaticMethod("(Lcom/onesignal/location/internal/MisconfiguredLocationManager$Companion;)Ljava/lang/Exception;")