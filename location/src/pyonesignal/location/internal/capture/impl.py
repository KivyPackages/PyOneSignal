from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LocationCapturer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/capture/impl/LocationCapturer"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/time/ITime;Lcom/onesignal/location/internal/preferences/ILocationPreferencesService;Lcom/onesignal/user/internal/properties/PropertiesModelStore;Lcom/onesignal/location/internal/controller/ILocationController;)V", False)]
    getLocationCoarse = JavaMethod("()Z")
    setLocationCoarse = JavaMethod("(Z)V")
    captureLastLocation = JavaMethod("()V")
    onLocationChanged = JavaMethod("(Landroid/location/Location;)V")