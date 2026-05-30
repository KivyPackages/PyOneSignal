from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FusedLocationApiWrapperImpl(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/controller/impl/FusedLocationApiWrapperImpl"
    __javaconstructor__ = [("()V", False)]
    getLastLocation = JavaMethod("(Lcom/google/android/gms/common/api/GoogleApiClient;)Landroid/location/Location;")
    cancelLocationUpdates = JavaMethod("(Lcom/google/android/gms/common/api/GoogleApiClient;Lcom/google/android/gms/location/LocationListener;)V")
    requestLocationUpdates = JavaMethod("(Lcom/google/android/gms/common/api/GoogleApiClient;Lcom/google/android/gms/location/LocationRequest;Lcom/google/android/gms/location/LocationListener;)V")

class GmsLocationController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/controller/impl/GmsLocationController"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/location/internal/controller/impl/IFusedLocationApiWrapper;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/location/internal/controller/impl/GmsLocationController$Companion;")
    start = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    stop = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    subscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/location/internal/controller/ILocationUpdatedHandler;)V", False, False)])
    access$get_applicationService$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;)Lcom/onesignal/core/internal/application/IApplicationService;")
    getLastLocation = JavaMethod("()Landroid/location/Location;")
    getHasSubscribers = JavaMethod("()Z")
    unsubscribe = JavaMultipleMethod([("(Lcom/onesignal/location/internal/controller/ILocationUpdatedHandler;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    access$getStartStopMutex$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;)Lkotlinx/coroutines/sync/Mutex;")
    access$getGoogleApiClient$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;)Lcom/onesignal/location/internal/controller/impl/GoogleApiClientCompatProxy;")
    access$getLastLocation$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;)Landroid/location/Location;")
    access$getEvent$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;)Lcom/onesignal/common/events/EventProducer;")
    access$setLocationAndFire = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;Landroid/location/Location;)V")
    access$getLocationHandlerThread$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;)Lcom/onesignal/location/internal/controller/impl/GmsLocationController$LocationHandlerThread;")
    access$get_fusedLocationApiWrapper$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;)Lcom/onesignal/location/internal/controller/impl/IFusedLocationApiWrapper;")
    access$setLocationUpdateListener$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;Lcom/onesignal/location/internal/controller/impl/GmsLocationController$LocationUpdateListener;)V")
    access$setGoogleApiClient$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/GmsLocationController;Lcom/onesignal/location/internal/controller/impl/GoogleApiClientCompatProxy;)V")
    access$getAPI_FALLBACK_TIME$cp = JavaStaticMethod("()I")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/location/internal/controller/impl/GmsLocationController$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        getAPI_FALLBACK_TIME = JavaMethod("()I")

    class LocationUpdateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/location/internal/controller/impl/GmsLocationController$LocationUpdateListener"
        __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/location/internal/controller/impl/GmsLocationController;Lcom/google/android/gms/common/api/GoogleApiClient;Lcom/onesignal/location/internal/controller/impl/IFusedLocationApiWrapper;)V", False)]
        onFocus = JavaMethod("(Z)V")
        onUnfocused = JavaMethod("()V")
        close = JavaMethod("()V")
        onLocationChanged = JavaMethod("(Landroid/location/Location;)V")

class GoogleApiClientCompatProxy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/controller/impl/GoogleApiClientCompatProxy"
    __javaconstructor__ = [("(Lcom/google/android/gms/common/api/GoogleApiClient;)V", False)]
    connect = JavaMethod("()V")
    blockingConnect = JavaMethod("()Lcom/google/android/gms/common/ConnectionResult;")
    disconnect = JavaMethod("()V")
    getRealInstance = JavaMethod("()Lcom/google/android/gms/common/api/GoogleApiClient;")

class HmsLocationController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/controller/impl/HmsLocationController"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;)V", False)]
    start = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    stop = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    subscribe = JavaMultipleMethod([("(Lcom/onesignal/location/internal/controller/ILocationUpdatedHandler;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    access$get_applicationService$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;)Lcom/onesignal/core/internal/application/IApplicationService;")
    getLastLocation = JavaMethod("()Landroid/location/Location;")
    getHasSubscribers = JavaMethod("()Z")
    unsubscribe = JavaMultipleMethod([("(Lcom/onesignal/location/internal/controller/ILocationUpdatedHandler;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    access$getStartStopMutex$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;)Lkotlinx/coroutines/sync/Mutex;")
    access$getLastLocation$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;)Landroid/location/Location;")
    access$getEvent$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;)Lcom/onesignal/common/events/EventProducer;")
    access$getLocationHandlerThread$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;)Lcom/onesignal/location/internal/controller/impl/HmsLocationController$LocationHandlerThread;")
    access$setLocationUpdateListener$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;Lcom/onesignal/location/internal/controller/impl/HmsLocationController$LocationUpdateListener;)V")
    access$setLastLocation$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;Landroid/location/Location;)V")
    access$getHmsFusedLocationClient$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;)Lcom/huawei/hms/location/FusedLocationProviderClient;")
    access$setHmsFusedLocationClient$p = JavaStaticMethod("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;Lcom/huawei/hms/location/FusedLocationProviderClient;)V")

    class LocationHandlerThread(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/location/internal/controller/impl/HmsLocationController$LocationHandlerThread"
        __javaconstructor__ = [("()V", False)]
        MIN_PRIORITY = JavaStaticField("I")
        NORM_PRIORITY = JavaStaticField("I")
        MAX_PRIORITY = JavaStaticField("I")
        getMHandler = JavaMethod("()Landroid/os/Handler;")
        setMHandler = JavaMethod("(Landroid/os/Handler;)V")

    class LocationUpdateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/location/internal/controller/impl/HmsLocationController$LocationUpdateListener"
        __javaconstructor__ = [("(Lcom/onesignal/location/internal/controller/impl/HmsLocationController;Lcom/onesignal/core/internal/application/IApplicationService;Lcom/huawei/hms/location/FusedLocationProviderClient;)V", False)]
        onFocus = JavaMethod("(Z)V")
        onUnfocused = JavaMethod("()V")
        close = JavaMethod("()V")
        onLocationResult = JavaMethod("(Lcom/huawei/hms/location/LocationResult;)V")

class IFusedLocationApiWrapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/controller/impl/IFusedLocationApiWrapper"
    getLastLocation = JavaMethod("(Lcom/google/android/gms/common/api/GoogleApiClient;)Landroid/location/Location;")
    cancelLocationUpdates = JavaMethod("(Lcom/google/android/gms/common/api/GoogleApiClient;Lcom/google/android/gms/location/LocationListener;)V")
    requestLocationUpdates = JavaMethod("(Lcom/google/android/gms/common/api/GoogleApiClient;Lcom/google/android/gms/location/LocationRequest;Lcom/google/android/gms/location/LocationListener;)V")

class NullLocationController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/controller/impl/NullLocationController"
    __javaconstructor__ = [("()V", False)]
    start = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    stop = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    subscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/location/internal/controller/ILocationUpdatedHandler;)V", False, False)])
    getLastLocation = JavaMethod("()Landroid/location/Location;")
    getHasSubscribers = JavaMethod("()Z")
    unsubscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/location/internal/controller/ILocationUpdatedHandler;)V", False, False)])