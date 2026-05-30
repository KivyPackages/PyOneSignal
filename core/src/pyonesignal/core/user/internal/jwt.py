from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IJwtUpdateListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/jwt/IJwtUpdateListener"
    onJwtUpdated = JavaMethod("(Ljava/lang/String;)V")

class JwtRequirement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/jwt/JwtRequirement"
    Companion = JavaStaticField("Lcom/onesignal/user/internal/jwt/JwtRequirement$Companion;")
    UNKNOWN = JavaStaticField("Lcom/onesignal/user/internal/jwt/JwtRequirement;")
    NOT_REQUIRED = JavaStaticField("Lcom/onesignal/user/internal/jwt/JwtRequirement;")
    REQUIRED = JavaStaticField("Lcom/onesignal/user/internal/jwt/JwtRequirement;")
    values = JavaStaticMethod("()[Lcom/onesignal/user/internal/jwt/JwtRequirement;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/user/internal/jwt/JwtRequirement;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/internal/jwt/JwtRequirement$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        fromBoolean = JavaMethod("(Ljava/lang/Boolean;)Lcom/onesignal/user/internal/jwt/JwtRequirement;")
    UNKNOWN = JavaStaticField("Lcom/onesignal/user/internal/jwt/JwtRequirement;")
    NOT_REQUIRED = JavaStaticField("Lcom/onesignal/user/internal/jwt/JwtRequirement;")
    REQUIRED = JavaStaticField("Lcom/onesignal/user/internal/jwt/JwtRequirement;")

class JwtTokenStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/jwt/JwtTokenStore"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)V", False)]
    addUserJwtInvalidatedListener = JavaMethod("(Lcom/onesignal/IUserJwtInvalidatedListener;)V")
    removeUserJwtInvalidatedListener = JavaMethod("(Lcom/onesignal/IUserJwtInvalidatedListener;)V")
    getJwt = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    addInternalUpdateListener = JavaMethod("(Lcom/onesignal/user/internal/jwt/IJwtUpdateListener;)V")
    removeInternalUpdateListener = JavaMethod("(Lcom/onesignal/user/internal/jwt/IJwtUpdateListener;)V")
    putJwt = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    invalidateJwt = JavaMethod("(Ljava/lang/String;)V")
    pruneToExternalIds = JavaMethod("(Ljava/util/Set;)V")
    access$getPublicInvalidatedListeners$p = JavaStaticMethod("(Lcom/onesignal/user/internal/jwt/JwtTokenStore;)Lcom/onesignal/common/events/EventProducer;")