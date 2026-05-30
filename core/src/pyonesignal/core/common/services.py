from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IServiceBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/services/IServiceBuilder"
    register = JavaMultipleMethod([("(Ljava/lang/Object;)Lcom/onesignal/common/services/ServiceRegistration;", False, False), ("(Lkotlin/jvm/functions/Function1;)Lcom/onesignal/common/services/ServiceRegistration;", False, False), ("(Ljava/lang/Class;)Lcom/onesignal/common/services/ServiceRegistration;", False, False)])
    build = JavaMethod("()Lcom/onesignal/common/services/ServiceProvider;")

class IServiceProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/services/IServiceProvider"
    getService = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")
    getServiceOrNull = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")
    hasService = JavaMethod("(Ljava/lang/Class;)Z")
    getAllServices = JavaMethod("(Ljava/lang/Class;)Ljava/util/List;")

class ServiceBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/services/ServiceBuilder"
    __javaconstructor__ = [("()V", False)]
    register = JavaMultipleMethod([("(Ljava/lang/Object;)Lcom/onesignal/common/services/ServiceRegistration;", False, False), ("(Lkotlin/jvm/functions/Function1;)Lcom/onesignal/common/services/ServiceRegistration;", False, False), ("(Ljava/lang/Class;)Lcom/onesignal/common/services/ServiceRegistration;", False, False), ("()Lcom/onesignal/common/services/ServiceRegistration;", False, False)])
    build = JavaMethod("()Lcom/onesignal/common/services/ServiceProvider;")

class ServiceProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/services/ServiceProvider"
    __javaconstructor__ = [("(Ljava/util/List;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/common/services/ServiceProvider$Companion;")
    getService = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")
    getServiceOrNull = JavaMethod("(Ljava/lang/Class;)Ljava/lang/Object;")
    hasService = JavaMethod("(Ljava/lang/Class;)Z")
    getAllServices = JavaMethod("(Ljava/lang/Class;)Ljava/util/List;")
    hasService$com_onesignal_core = JavaMethod("()Z")
    getAllServices$com_onesignal_core = JavaMethod("()Ljava/util/List;")
    getService$com_onesignal_core = JavaMethod("()Ljava/lang/Object;")
    getServiceOrNull$com_onesignal_core = JavaMethod("()Ljava/lang/Object;")
    access$getIndent$cp = JavaStaticMethod("()Ljava/lang/String;")
    access$setIndent$cp = JavaStaticMethod("(Ljava/lang/String;)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/common/services/ServiceProvider$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        getIndent = JavaMethod("()Ljava/lang/String;")
        setIndent = JavaMethod("(Ljava/lang/String;)V")

class ServiceRegistration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/services/ServiceRegistration"
    __javaconstructor__ = [("()V", False)]
    resolve = JavaMethod("(Lcom/onesignal/common/services/IServiceProvider;)Ljava/lang/Object;")
    provides = JavaMultipleMethod([("(Ljava/lang/Class;)Lcom/onesignal/common/services/ServiceRegistration;", False, False), ("()Lcom/onesignal/common/services/ServiceRegistration;", False, False)])
    getServices = JavaMethod("()Ljava/util/Set;")

class ServiceRegistrationLambda(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/services/ServiceRegistrationLambda"
    __javaconstructor__ = [("(Lkotlin/jvm/functions/Function1;)V", False)]
    resolve = JavaMethod("(Lcom/onesignal/common/services/IServiceProvider;)Ljava/lang/Object;")

class ServiceRegistrationReflection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/services/ServiceRegistrationReflection"
    __javaconstructor__ = [("(Ljava/lang/Class;)V", False)]
    resolve = JavaMethod("(Lcom/onesignal/common/services/IServiceProvider;)Ljava/lang/Object;")

class ServiceRegistrationSingleton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/services/ServiceRegistrationSingleton"
    __javaconstructor__ = [("(Ljava/lang/Object;)V", False)]
    resolve = JavaMethod("(Lcom/onesignal/common/services/IServiceProvider;)Ljava/lang/Object;")