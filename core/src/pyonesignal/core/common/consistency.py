from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IamFetchReadyCondition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/consistency/IamFetchReadyCondition"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/common/consistency/IamFetchReadyCondition$Companion;")
    ID = JavaStaticField("Ljava/lang/String;")
    getId = JavaMethod("()Ljava/lang/String;")
    isMet = JavaMethod("(Ljava/util/Map;)Z")
    getRywData = JavaMethod("(Ljava/util/Map;)Lcom/onesignal/common/consistency/RywData;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/common/consistency/IamFetchReadyCondition$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class RywData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/consistency/RywData"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Long;)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    copy = JavaMethod("(Ljava/lang/String;Ljava/lang/Long;)Lcom/onesignal/common/consistency/RywData;")
    getRywToken = JavaMethod("()Ljava/lang/String;")
    getRywDelay = JavaMethod("()Ljava/lang/Long;")
    component1 = JavaMethod("()Ljava/lang/String;")
    component2 = JavaMethod("()Ljava/lang/Long;")
    copy$default = JavaStaticMethod("(Lcom/onesignal/common/consistency/RywData;Ljava/lang/String;Ljava/lang/Long;ILjava/lang/Object;)Lcom/onesignal/common/consistency/RywData;")