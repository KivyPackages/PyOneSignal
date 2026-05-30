from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IModule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/modules/IModule"
    register = JavaMethod("(Lcom/onesignal/common/services/ServiceBuilder;)V")