from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CoreModule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/CoreModule"
    __javaconstructor__ = [("()V", False)]
    register = JavaMethod("(Lcom/onesignal/common/services/ServiceBuilder;)V")

class BuildConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/BuildConfig"
    __javaconstructor__ = [("()V", False)]
    DEBUG = JavaStaticField("Z")
    LIBRARY_PACKAGE_NAME = JavaStaticField("Ljava/lang/String;")
    BUILD_TYPE = JavaStaticField("Ljava/lang/String;")
    SDK_VERSION = JavaStaticField("Ljava/lang/String;")