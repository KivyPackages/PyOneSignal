from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class PropertiesModel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/properties/PropertiesModel"
    __javaconstructor__ = [("()V", False)]
    getCountry = JavaMethod("()Ljava/lang/String;")
    getOnesignalId = JavaMethod("()Ljava/lang/String;")
    setLanguage = JavaMethod("(Ljava/lang/String;)V")
    getTags = JavaMethod("()Lcom/onesignal/common/modeling/MapModel;")
    setCountry = JavaMethod("(Ljava/lang/String;)V")
    getTimezone = JavaMethod("()Ljava/lang/String;")
    getLocationLatitude = JavaMethod("()Ljava/lang/Double;")
    setLocationLatitude = JavaMethod("(Ljava/lang/Double;)V")
    getLocationLongitude = JavaMethod("()Ljava/lang/Double;")
    setLocationLongitude = JavaMethod("(Ljava/lang/Double;)V")
    getLocationAccuracy = JavaMethod("()Ljava/lang/Float;")
    setLocationAccuracy = JavaMethod("(Ljava/lang/Float;)V")
    getLocationType = JavaMethod("()Ljava/lang/Integer;")
    setLocationType = JavaMethod("(Ljava/lang/Integer;)V")
    getLocationBackground = JavaMethod("()Ljava/lang/Boolean;")
    setLocationBackground = JavaMethod("(Ljava/lang/Boolean;)V")
    getLocationTimestamp = JavaMethod("()Ljava/lang/Long;")
    setLocationTimestamp = JavaMethod("(Ljava/lang/Long;)V")
    setTimezone = JavaMethod("(Ljava/lang/String;)V")
    setOnesignalId = JavaMethod("(Ljava/lang/String;)V")
    getLanguage = JavaMethod("()Ljava/lang/String;")

class PropertiesModelStore(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/properties/PropertiesModelStore"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)V", False)]