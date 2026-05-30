from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LocationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/LocationManager"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/location/internal/capture/ILocationCapturer;Lcom/onesignal/location/internal/controller/ILocationController;Lcom/onesignal/location/internal/permissions/LocationPermissionController;Lcom/onesignal/core/internal/preferences/IPreferencesService;)V", False)]
    start = JavaMethod("()V")
    isShared = JavaMethod("()Z")
    setShared = JavaMethod("(Z)V")
    onLocationPermissionChanged = JavaMethod("(Z)V")
    requestPermission = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$startGetLocation = JavaStaticMethod("(Lcom/onesignal/location/internal/LocationManager;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$get_applicationService$p = JavaStaticMethod("(Lcom/onesignal/location/internal/LocationManager;)Lcom/onesignal/core/internal/application/IApplicationService;")
    access$get_capturer$p = JavaStaticMethod("(Lcom/onesignal/location/internal/LocationManager;)Lcom/onesignal/location/internal/capture/ILocationCapturer;")
    access$get_locationPermissionController$p = JavaStaticMethod("(Lcom/onesignal/location/internal/LocationManager;)Lcom/onesignal/location/internal/permissions/LocationPermissionController;")
    access$backgroundLocationPermissionLogic = JavaStaticMethod("(Lcom/onesignal/location/internal/LocationManager;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")