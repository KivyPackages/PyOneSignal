from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationPermissionChangedHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/permissions/INotificationPermissionChangedHandler"
    onNotificationPermissionChanged = JavaMethod("(Z)V")

class INotificationPermissionController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/permissions/INotificationPermissionController"
    prompt = JavaMethod("(ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getCanRequestPermission = JavaMethod("()Z")