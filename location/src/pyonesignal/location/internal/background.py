from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LocationBackgroundService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/background/LocationBackgroundService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/location/ILocationManager;Lcom/onesignal/location/internal/preferences/ILocationPreferencesService;Lcom/onesignal/location/internal/capture/ILocationCapturer;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    getScheduleBackgroundRunIn = JavaMethod("()Ljava/lang/Long;")
    backgroundRun = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")