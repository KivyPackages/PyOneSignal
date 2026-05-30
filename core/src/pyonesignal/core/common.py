from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AndroidUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/AndroidUtils"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/AndroidUtils;")
    getRandomDelay = JavaMethod("(II)I")
    isStringNotEmpty = JavaMethod("(Ljava/lang/String;)Z")
    isActivityFullyReady = JavaMethod("(Landroid/app/Activity;)Z")
    isAndroidUserUnlocked = JavaMethod("(Landroid/content/Context;)Z")
    hasConfigChangeFlag = JavaMethod("(Landroid/app/Activity;I)Z")
    getAppVersion = JavaMethod("(Landroid/content/Context;)Ljava/lang/String;")
    getAndroidSDKInt = JavaMethod("()I")
    getManifestMeta = JavaMethod("(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;")
    getManifestMetaBundle = JavaMethod("(Landroid/content/Context;)Landroid/os/Bundle;")
    getManifestMetaBoolean = JavaMethod("(Landroid/content/Context;Ljava/lang/String;)Z")
    getResourceString = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    isValidResourceName = JavaMethod("(Ljava/lang/String;)Z")
    getRootCauseThrowable = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")
    getRootCauseMessage = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/String;")
    isRunningOnMainThread = JavaMethod("()Z")
    getTargetSdkVersion = JavaMethod("(Landroid/content/Context;)I")
    hasNotificationManagerCompat = JavaMethod("()Z")
    openURLInBrowser = JavaMultipleMethod([("(Landroid/content/Context;Landroid/net/Uri;)V", False, False), ("(Landroid/content/Context;Ljava/lang/String;)V", False, False)])
    openURLInBrowserIntent = JavaMethod("(Landroid/net/Uri;)Landroid/content/Intent;")
    hasPermission = JavaMethod("(Ljava/lang/String;ZLcom/onesignal/core/internal/application/IApplicationService;)Z")
    filterManifestPermissions = JavaMethod("(Ljava/util/List;Lcom/onesignal/core/internal/application/IApplicationService;)Ljava/util/List;")
    opaqueHasClass = JavaMethod("(Ljava/lang/Class;)Z")
    finishSafely = JavaMethod("(Landroid/app/Activity;)V")

    class SchemaType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/common/AndroidUtils$SchemaType"
        Companion = JavaStaticField("Lcom/onesignal/common/AndroidUtils$SchemaType$Companion;")
        DATA = JavaStaticField("Lcom/onesignal/common/AndroidUtils$SchemaType;")
        HTTPS = JavaStaticField("Lcom/onesignal/common/AndroidUtils$SchemaType;")
        HTTP = JavaStaticField("Lcom/onesignal/common/AndroidUtils$SchemaType;")
        values = JavaStaticMethod("()[Lcom/onesignal/common/AndroidUtils$SchemaType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/common/AndroidUtils$SchemaType;")
        getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
        access$getText$p = JavaStaticMethod("(Lcom/onesignal/common/AndroidUtils$SchemaType;)Ljava/lang/String;")

        class Companion(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "com/onesignal/common/AndroidUtils$SchemaType$Companion"
            __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
            fromString = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/common/AndroidUtils$SchemaType;")
        DATA = JavaStaticField("Lcom/onesignal/common/AndroidUtils$SchemaType;")
        HTTPS = JavaStaticField("Lcom/onesignal/common/AndroidUtils$SchemaType;")
        HTTP = JavaStaticField("Lcom/onesignal/common/AndroidUtils$SchemaType;")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/common/AndroidUtils$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")

class DateUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/DateUtils"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/DateUtils;")
    iso8601Format = JavaMethod("()Ljava/text/SimpleDateFormat;")

class IDManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/IDManager"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/IDManager;")
    LOCAL_PREFIX = JavaStaticField("Ljava/lang/String;")
    createLocalId = JavaMethod("()Ljava/lang/String;")
    isLocalId = JavaMethod("(Ljava/lang/String;)Z")

class JSONObjectExtensionsKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/JSONObjectExtensionsKt"
    toList = JavaStaticMethod("(Lorg/json/JSONArray;)Ljava/util/List;")
    toMap = JavaStaticMethod("(Lorg/json/JSONObject;)Ljava/util/Map;")
    putMap = JavaMultipleMethod([("(Lorg/json/JSONObject;Ljava/lang/String;Ljava/util/Map;)Lorg/json/JSONObject;", True, False), ("(Lorg/json/JSONObject;Ljava/util/Map;)Lorg/json/JSONObject;", True, False)])
    safeInt = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;)Ljava/lang/Integer;")
    safeLong = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;)Ljava/lang/Long;")
    safeDouble = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;)Ljava/lang/Double;")
    safeBool = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;)Ljava/lang/Boolean;")
    safeString = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;)Ljava/lang/String;")
    safeJSONObject = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;)Lorg/json/JSONObject;")
    expandJSONObject = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;Lkotlin/jvm/functions/Function1;)V")
    expandJSONArray = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;Lkotlin/jvm/functions/Function1;)Ljava/util/List;")
    putJSONObject = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;Lkotlin/jvm/functions/Function1;)Lorg/json/JSONObject;")
    putJSONArray = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;Ljava/util/List;Lkotlin/jvm/functions/Function1;)Lorg/json/JSONObject;")
    putSafe = JavaStaticMethod("(Lorg/json/JSONObject;Ljava/lang/String;Ljava/lang/Object;)Lorg/json/JSONObject;")

class JSONUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/JSONUtils"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/JSONUtils;")
    EXTERNAL_USER_ID = JavaStaticField("Ljava/lang/String;")
    toUnescapedEUIDString = JavaMethod("(Lorg/json/JSONObject;)Ljava/lang/String;")
    bundleAsJSONObject = JavaMethod("(Landroid/os/Bundle;)Lorg/json/JSONObject;")
    wrapInJsonArray = JavaMethod("(Lorg/json/JSONObject;)Lorg/json/JSONArray;")
    jsonStringToBundle = JavaMethod("(Ljava/lang/String;)Landroid/os/Bundle;")
    newStringMapFromJSONObject = JavaMethod("(Lorg/json/JSONObject;)Ljava/util/Map;")
    newStringSetFromJSONArray = JavaMethod("(Lorg/json/JSONArray;)Ljava/util/Set;")
    compareJSONArrays = JavaMethod("(Lorg/json/JSONArray;Lorg/json/JSONArray;)Z")
    normalizeType = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    isValidJsonObject = JavaMethod("(Ljava/lang/Object;)Z")
    mapToJson = JavaMethod("(Ljava/util/Map;)Lorg/json/JSONObject;")
    convertToJson = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")

class NetworkUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/NetworkUtils"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/NetworkUtils;")
    getResponseStatusType = JavaMethod("(I)Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
    setMaxNetworkRequestAttemptCount = JavaMethod("(I)V")
    getMaxNetworkRequestAttemptCount = JavaMethod("()I")

    class ResponseStatusType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/common/NetworkUtils$ResponseStatusType"
        INVALID = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        RETRYABLE = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        UNAUTHORIZED = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        MISSING = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        CONFLICT = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        values = JavaStaticMethod("()[Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
        INVALID = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        RETRYABLE = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        UNAUTHORIZED = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        MISSING = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")
        CONFLICT = JavaStaticField("Lcom/onesignal/common/NetworkUtils$ResponseStatusType;")

class OneSignalUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/OneSignalUtils"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/OneSignalUtils;")
    formatVersion$com_onesignal_core = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    isValidEmail = JavaMethod("(Ljava/lang/String;)Z")
    isValidPhoneNumber = JavaMethod("(Ljava/lang/String;)Z")
    getSdkVersion = JavaMethod("()Ljava/lang/String;")

class OneSignalWrapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/OneSignalWrapper"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/OneSignalWrapper;")
    getSdkVersion$annotations = JavaStaticMethod("()V")
    getSdkVersion = JavaStaticMethod("()Ljava/lang/String;")
    getSdkType = JavaStaticMethod("()Ljava/lang/String;")
    getSdkType$annotations = JavaStaticMethod("()V")
    setSdkVersion = JavaStaticMethod("(Ljava/lang/String;)V")
    setSdkType = JavaStaticMethod("(Ljava/lang/String;)V")

class PIIHasher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/PIIHasher"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/PIIHasher;")
    hash = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    isHashed = JavaMethod("(Ljava/lang/String;)Z")

class RootToolsInternalMethods(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/RootToolsInternalMethods"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/RootToolsInternalMethods;")
    isRooted = JavaMethod("()Z")

class TimeUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/TimeUtils"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/TimeUtils;")
    getTimeZoneOffset = JavaMethod("()I")
    getTimeZoneId = JavaMethod("()Ljava/lang/String;")

class ViewUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/ViewUtils"
    INSTANCE = JavaStaticField("Lcom/onesignal/common/ViewUtils;")
    dpToPx = JavaMethod("(I)I")
    getWindowHeight = JavaMethod("(Landroid/app/Activity;)I")
    getCutoutAndStatusBarInsets = JavaMethod("(Landroid/app/Activity;)[I")
    getFullbleedWindowWidth = JavaMethod("(Landroid/app/Activity;)I")
    getWindowWidth = JavaMethod("(Landroid/app/Activity;)I")