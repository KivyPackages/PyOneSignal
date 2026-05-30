from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ILocationPermissionChangedHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/permissions/ILocationPermissionChangedHandler"
    onLocationPermissionChanged = JavaMethod("(Z)V")

class LocationPermissionController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/permissions/LocationPermissionController"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/permissions/IRequestPermissionService;Lcom/onesignal/core/internal/application/IApplicationService;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/location/internal/permissions/LocationPermissionController$Companion;")
    start = JavaMethod("()V")
    subscribe = JavaMultipleMethod([("(Lcom/onesignal/location/internal/permissions/ILocationPermissionChangedHandler;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    prompt = JavaMethod("(ZLjava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$get_applicationService$p = JavaStaticMethod("(Lcom/onesignal/location/internal/permissions/LocationPermissionController;)Lcom/onesignal/core/internal/application/IApplicationService;")
    getHasSubscribers = JavaMethod("()Z")
    unsubscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/location/internal/permissions/ILocationPermissionChangedHandler;)V", False, False)])
    onAccept = JavaMethod("()V")
    onReject = JavaMethod("(Z)V")
    access$getCurrPermission$p = JavaStaticMethod("(Lcom/onesignal/location/internal/permissions/LocationPermissionController;)Ljava/lang/String;")
    access$getWaiter$p = JavaStaticMethod("(Lcom/onesignal/location/internal/permissions/LocationPermissionController;)Lcom/onesignal/common/threading/WaiterWithValue;")
    access$getEvents$p = JavaStaticMethod("(Lcom/onesignal/location/internal/permissions/LocationPermissionController;)Lcom/onesignal/common/events/EventProducer;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/location/internal/permissions/LocationPermissionController$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class NavigateToAndroidSettingsForLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/permissions/NavigateToAndroidSettingsForLocation"
    INSTANCE = JavaStaticField("Lcom/onesignal/location/internal/permissions/NavigateToAndroidSettingsForLocation;")
    show = JavaMethod("(Landroid/content/Context;)V")