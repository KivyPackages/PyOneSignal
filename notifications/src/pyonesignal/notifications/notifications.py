from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationsModule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/NotificationsModule"
    __javaconstructor__ = [("()V", False)]
    register = JavaMethod("(Lcom/onesignal/common/services/ServiceBuilder;)V")