from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IdentityModel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/identity/IdentityModel"
    __javaconstructor__ = [("()V", False)]
    remove = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;)Ljava/lang/String;", False, False)])
    get = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;)Ljava/lang/String;", False, False)])
    containsValue = JavaMultipleMethod([("(Ljava/lang/Object;)Z", False, False), ("(Ljava/lang/String;)Z", False, False)])
    getOrDefault = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/Object;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    getOnesignalId = JavaMethod("()Ljava/lang/String;")
    getExternalId = JavaMethod("()Ljava/lang/String;")
    setExternalId = JavaMethod("(Ljava/lang/String;)V")
    setOnesignalId = JavaMethod("(Ljava/lang/String;)V")

class IdentityModelStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/identity/IdentityModelStore"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)V", False)]

class IdentityModelStoreKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/identity/IdentityModelStoreKt"
    IDENTITY_NAME_SPACE = JavaStaticField("Ljava/lang/String;")
    hasOneSignalId = JavaStaticMethod("(Lcom/onesignal/user/internal/identity/IdentityModelStore;)Z")