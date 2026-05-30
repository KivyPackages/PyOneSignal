from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RequestPermissionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/permissions/impl/RequestPermissionService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;)V", False)]
    startPrompt = JavaMethod("(ZLjava/lang/String;Ljava/lang/String;Ljava/lang/Class;)V")
    registerAsCallback = JavaMethod("(Ljava/lang/String;Lcom/onesignal/core/internal/permissions/IRequestPermissionService$PermissionCallback;)V")
    setFallbackToSettings = JavaMethod("(Z)V")
    access$get_application$p = JavaStaticMethod("(Lcom/onesignal/core/internal/permissions/impl/RequestPermissionService;)Lcom/onesignal/core/internal/application/IApplicationService;")
    setWaiting = JavaMethod("(Z)V")
    getWaiting = JavaMethod("()Z")
    setShouldShowRequestPermissionRationaleBeforeRequest = JavaMethod("(Z)V")
    getCallback = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/permissions/IRequestPermissionService$PermissionCallback;")
    getFallbackToSettings = JavaMethod("()Z")
    getShouldShowRequestPermissionRationaleBeforeRequest = JavaMethod("()Z")