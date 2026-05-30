from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ILanguageContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/language/ILanguageContext"
    setLanguage = JavaMethod("(Ljava/lang/String;)V")
    getLanguage = JavaMethod("()Ljava/lang/String;")