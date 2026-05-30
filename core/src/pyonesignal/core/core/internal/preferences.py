from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IPreferencesService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/preferences/IPreferencesService"
    getString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    getInt = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Integer;)Ljava/lang/Integer;")
    getLong = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;)Ljava/lang/Long;")
    saveString = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V")
    getStringSet = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)Ljava/util/Set;")
    saveBool = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Boolean;)V")
    saveLong = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;)V")
    getBool = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Boolean;)Ljava/lang/Boolean;")
    saveInt = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Integer;)V")
    saveStringSet = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;)V")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/preferences/IPreferencesService$DefaultImpls"
        getString$default = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/IPreferencesService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ILjava/lang/Object;)Ljava/lang/String;")
        getInt$default = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/IPreferencesService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Integer;ILjava/lang/Object;)Ljava/lang/Integer;")
        getStringSet$default = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/IPreferencesService;Ljava/lang/String;Ljava/lang/String;Ljava/util/Set;ILjava/lang/Object;)Ljava/util/Set;")
        getLong$default = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/IPreferencesService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;ILjava/lang/Object;)Ljava/lang/Long;")
        getBool$default = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/IPreferencesService;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Boolean;ILjava/lang/Object;)Ljava/lang/Boolean;")

class PreferenceOneSignalKeys(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/preferences/PreferenceOneSignalKeys"
    INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/preferences/PreferenceOneSignalKeys;")
    PREFS_LEGACY_APP_ID = JavaStaticField("Ljava/lang/String;")
    PREFS_LEGACY_PLAYER_ID = JavaStaticField("Ljava/lang/String;")
    PREFS_LEGACY_USER_SYNCVALUES = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_LAST_LOCATION_TIME = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_LOCATION_SHARED = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_JWT_TOKENS = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_USER_RESOLVED_PERMISSION_PREFIX = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_ETAG_PREFIX = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_INSTALL_ID = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_HTTP_CACHE_PREFIX = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_UNATTRIBUTED_UNIQUE_OUTCOME_EVENTS_SENT = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_CACHED_IAMS = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_DISMISSED_IAMS = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_IMPRESSIONED_IAMS = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_CLICKED_CLICK_IDS_IAMS = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_PAGE_IMPRESSIONED_IAMS = JavaStaticField("Ljava/lang/String;")
    PREFS_OS_IAM_LAST_DISMISSED_TIME = JavaStaticField("Ljava/lang/String;")
    MODEL_STORE_PREFIX = JavaStaticField("Ljava/lang/String;")

class PreferencePlayerPurchasesKeys(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/preferences/PreferencePlayerPurchasesKeys"
    INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/preferences/PreferencePlayerPurchasesKeys;")
    PREFS_PURCHASE_TOKENS = JavaStaticField("Ljava/lang/String;")
    PREFS_EXISTING_PURCHASES = JavaStaticField("Ljava/lang/String;")

class PreferenceStoreFix(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/preferences/PreferenceStoreFix"
    INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/preferences/PreferenceStoreFix;")
    ensureNoObfuscatedPrefStore = JavaMethod("(Landroid/content/Context;)V")

class PreferenceStores(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/preferences/PreferenceStores"
    INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/preferences/PreferenceStores;")
    ONESIGNAL = JavaStaticField("Ljava/lang/String;")
    PLAYER_PURCHASES = JavaStaticField("Ljava/lang/String;")

class PreferencesExtensionV4Kt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/preferences/PreferencesExtensionV4Kt"
    getLegacyAppId = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)Ljava/lang/String;")
    getLegacyPlayerId = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)Ljava/lang/String;")
    getLegacyUserSyncValues = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)Ljava/lang/String;")
    clearLegacyPlayerId = JavaStaticMethod("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)V")