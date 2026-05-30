from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class InAppMessagesModule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/InAppMessagesModule"
    __javaconstructor__ = [("()V", False)]
    register = JavaMethod("(Lcom/onesignal/common/services/ServiceBuilder;)V")