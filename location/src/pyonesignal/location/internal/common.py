from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LocationConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/common/LocationConstants"
    INSTANCE = JavaStaticField("Lcom/onesignal/location/internal/common/LocationConstants;")
    TIME_FOREGROUND_SEC = JavaStaticField("J")
    TIME_BACKGROUND_SEC = JavaStaticField("J")
    FOREGROUND_UPDATE_TIME_MS = JavaStaticField("J")
    BACKGROUND_UPDATE_TIME_MS = JavaStaticField("J")
    ANDROID_FINE_LOCATION_PERMISSION_STRING = JavaStaticField("Ljava/lang/String;")
    ANDROID_COARSE_LOCATION_PERMISSION_STRING = JavaStaticField("Ljava/lang/String;")
    ANDROID_BACKGROUND_LOCATION_PERMISSION_STRING = JavaStaticField("Ljava/lang/String;")

class LocationPoint(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/common/LocationPoint"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/Integer;")
    getLat = JavaMethod("()Ljava/lang/Double;")
    setLog = JavaMethod("(Ljava/lang/Double;)V")
    getBg = JavaMethod("()Ljava/lang/Boolean;")
    setBg = JavaMethod("(Ljava/lang/Boolean;)V")
    setLat = JavaMethod("(Ljava/lang/Double;)V")
    getLog = JavaMethod("()Ljava/lang/Double;")
    getAccuracy = JavaMethod("()Ljava/lang/Float;")
    setAccuracy = JavaMethod("(Ljava/lang/Float;)V")
    setType = JavaMethod("(Ljava/lang/Integer;)V")
    setTimeStamp = JavaMethod("(Ljava/lang/Long;)V")
    getTimeStamp = JavaMethod("()Ljava/lang/Long;")

class LocationUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/location/internal/common/LocationUtils"
    INSTANCE = JavaStaticField("Lcom/onesignal/location/internal/common/LocationUtils;")
    hasGMSLocationLibrary = JavaMethod("()Z")
    hasHMSLocationLibrary = JavaMethod("()Z")
    hasLocationPermission = JavaMethod("(Landroid/content/Context;)Z")