from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ILocationCapturer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/capture/ILocationCapturer"
    getLocationCoarse = JavaMethod("()Z")
    setLocationCoarse = JavaMethod("(Z)V")
    captureLastLocation = JavaMethod("()V")