from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class InAppRepository(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/repositories/impl/InAppRepository"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/database/IDatabaseProvider;Lcom/onesignal/core/internal/time/ITime;Lcom/onesignal/inAppMessages/internal/preferences/IInAppPreferencesController;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/inAppMessages/internal/repositories/impl/InAppRepository$Companion;")
    IAM_CACHE_DATA_LIFETIME = JavaStaticField("J")
    access$get_databaseProvider$p = JavaStaticMethod("(Lcom/onesignal/inAppMessages/internal/repositories/impl/InAppRepository;)Lcom/onesignal/core/internal/database/IDatabaseProvider;")
    listInAppMessages = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    saveInAppMessage = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$get_time$p = JavaStaticMethod("(Lcom/onesignal/inAppMessages/internal/repositories/impl/InAppRepository;)Lcom/onesignal/core/internal/time/ITime;")
    access$get_prefs$p = JavaStaticMethod("(Lcom/onesignal/inAppMessages/internal/repositories/impl/InAppRepository;)Lcom/onesignal/inAppMessages/internal/preferences/IInAppPreferencesController;")
    cleanCachedInAppMessages = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/inAppMessages/internal/repositories/impl/InAppRepository$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]