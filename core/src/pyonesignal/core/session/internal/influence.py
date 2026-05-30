from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IInfluenceManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/influence/IInfluenceManager"
    onNotificationReceived = JavaMethod("(Ljava/lang/String;)V")
    onInAppMessageDisplayed = JavaMethod("(Ljava/lang/String;)V")
    onDirectInfluenceFromIAM = JavaMethod("(Ljava/lang/String;)V")
    getInfluences = JavaMethod("()Ljava/util/List;")
    onDirectInfluenceFromNotification = JavaMethod("(Ljava/lang/String;)V")
    onInAppMessageDismissed = JavaMethod("()V")

class Influence(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/influence/Influence"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Lcom/onesignal/session/internal/influence/InfluenceChannel;Lcom/onesignal/session/internal/influence/InfluenceType;Lorg/json/JSONArray;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/session/internal/influence/Influence$Companion;")
    INFLUENCE_CHANNEL = JavaStaticField("Ljava/lang/String;")
    INFLUENCE_TYPE = JavaStaticField("Ljava/lang/String;")
    INFLUENCE_IDS = JavaStaticField("Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    copy = JavaMethod("()Lcom/onesignal/session/internal/influence/Influence;")
    setIds = JavaMethod("(Lorg/json/JSONArray;)V")
    getInfluenceType = JavaMethod("()Lcom/onesignal/session/internal/influence/InfluenceType;")
    getIds = JavaMethod("()Lorg/json/JSONArray;")
    setInfluenceType = JavaMethod("(Lcom/onesignal/session/internal/influence/InfluenceType;)V")
    getInfluenceChannel = JavaMethod("()Lcom/onesignal/session/internal/influence/InfluenceChannel;")
    getDirectId = JavaMethod("()Ljava/lang/String;")
    toJSONString = JavaMethod("()Ljava/lang/String;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/session/internal/influence/Influence$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class InfluenceChannel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/influence/InfluenceChannel"
    Companion = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceChannel$Companion;")
    IAM = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceChannel;")
    NOTIFICATION = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceChannel;")
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaStaticMethod("()[Lcom/onesignal/session/internal/influence/InfluenceChannel;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/session/internal/influence/InfluenceChannel;")
    equalsName = JavaMethod("(Ljava/lang/String;)Z")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/session/internal/influence/InfluenceChannel;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/session/internal/influence/InfluenceChannel$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        fromString = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/session/internal/influence/InfluenceChannel;")
    IAM = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceChannel;")
    NOTIFICATION = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceChannel;")

class InfluenceType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/influence/InfluenceType"
    Companion = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceType$Companion;")
    DIRECT = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceType;")
    INDIRECT = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceType;")
    UNATTRIBUTED = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceType;")
    DISABLED = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceType;")
    values = JavaStaticMethod("()[Lcom/onesignal/session/internal/influence/InfluenceType;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/session/internal/influence/InfluenceType;")
    isDirect = JavaMethod("()Z")
    isAttributed = JavaMethod("()Z")
    isIndirect = JavaMethod("()Z")
    isUnattributed = JavaMethod("()Z")
    isDisabled = JavaMethod("()Z")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    fromString = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/session/internal/influence/InfluenceType;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/session/internal/influence/InfluenceType$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        fromString = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/session/internal/influence/InfluenceType;")
    DIRECT = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceType;")
    INDIRECT = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceType;")
    UNATTRIBUTED = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceType;")
    DISABLED = JavaStaticField("Lcom/onesignal/session/internal/influence/InfluenceType;")