from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IBadgeCountUpdater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/IBadgeCountUpdater"
    update = JavaMethod("()V")
    updateCount = JavaMethod("(I)V")