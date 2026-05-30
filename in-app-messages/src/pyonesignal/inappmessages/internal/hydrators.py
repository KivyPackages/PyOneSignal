from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class InAppHydrator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/hydrators/InAppHydrator"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/time/ITime;Lcom/onesignal/user/internal/properties/PropertiesModelStore;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/inAppMessages/internal/hydrators/InAppHydrator$Companion;")
    hydrateIAMMessageContent = JavaMethod("(Lorg/json/JSONObject;)Lcom/onesignal/inAppMessages/internal/InAppMessageContent;")
    hydrateIAMMessages = JavaMethod("(Lorg/json/JSONArray;)Ljava/util/List;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/inAppMessages/internal/hydrators/InAppHydrator$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]