from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class PreferencesService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/preferences/impl/PreferencesService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/preferences/impl/PreferencesService$Companion;")
    getInt = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Integer;)Ljava/lang/Integer;")
    getLong = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;)Ljava/lang/Long;")
    start = JavaMethod("()V")
    getString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    getStringSet = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)Ljava/util/Set;")
    getBool = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Boolean;)Ljava/lang/Boolean;")
    saveBool = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Boolean;)V")
    saveInt = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Integer;)V")
    saveLong = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;)V")
    saveStringSet = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)V")
    access$getPrefsToApply$p = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/impl/PreferencesService;)Ljava/util/Map;")
    access$getSharedPrefsByName = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/impl/PreferencesService;Ljava/lang/String;)Landroid/content/SharedPreferences;")
    access$getHasLoggedMissingAppContext$p = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/impl/PreferencesService;)Z")
    access$setHasLoggedMissingAppContext$p = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/impl/PreferencesService;Z)V")
    saveString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    access$get_time$p = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/impl/PreferencesService;)Lcom/onesignal/core/internal/time/ITime;")
    access$getWaiter$p = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/impl/PreferencesService;)Lcom/onesignal/common/threading/Waiter;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/preferences/impl/PreferencesService$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]