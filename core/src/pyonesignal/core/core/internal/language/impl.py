from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LanguageContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/language/impl/LanguageContext"
    __javaconstructor__ = [("(Lcom/onesignal/user/internal/properties/PropertiesModelStore;)V", False)]
    setLanguage = JavaMethod("(Ljava/lang/String;)V")
    getLanguage = JavaMethod("()Ljava/lang/String;")

class LanguageProviderDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/language/impl/LanguageProviderDevice"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/language/impl/LanguageProviderDevice$Companion;")
    getLanguage = JavaMethod("()Ljava/lang/String;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/language/impl/LanguageProviderDevice$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]