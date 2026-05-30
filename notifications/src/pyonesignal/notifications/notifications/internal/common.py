from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class GenerateNotificationOpenIntent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/GenerateNotificationOpenIntent"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/Intent;Z)V", False)]
    getIntentVisible = JavaMethod("()Landroid/content/Intent;")

class GenerateNotificationOpenIntentFromPushPayload(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/GenerateNotificationOpenIntentFromPushPayload"
    INSTANCE = JavaStaticField("Lcom/onesignal/notifications/internal/common/GenerateNotificationOpenIntentFromPushPayload;")
    create = JavaMethod("(Landroid/content/Context;Lorg/json/JSONObject;)Lcom/onesignal/notifications/internal/common/GenerateNotificationOpenIntent;")

class NotificationConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/NotificationConstants"
    INSTANCE = JavaStaticField("Lcom/onesignal/notifications/internal/common/NotificationConstants;")
    EXTENSION_SERVICE_META_DATA_TAG_NAME = JavaStaticField("Ljava/lang/String;")
    DEFAULT_TTL_IF_NOT_IN_PAYLOAD = JavaStaticField("I")
    PUSH_ADDITIONAL_DATA_KEY = JavaStaticField("Ljava/lang/String;")
    GOOGLE_SENT_TIME_KEY = JavaStaticField("Ljava/lang/String;")
    GOOGLE_TTL_KEY = JavaStaticField("Ljava/lang/String;")
    HMS_TTL_KEY = JavaStaticField("Ljava/lang/String;")
    HMS_SENT_TIME_KEY = JavaStaticField("Ljava/lang/String;")
    GENERATE_NOTIFICATION_BUNDLE_KEY_ACTION_ID = JavaStaticField("Ljava/lang/String;")
    IAM_PREVIEW_KEY = JavaStaticField("Ljava/lang/String;")
    BUNDLE_KEY_ANDROID_NOTIFICATION_ID = JavaStaticField("Ljava/lang/String;")
    BUNDLE_KEY_ONESIGNAL_DATA = JavaStaticField("Ljava/lang/String;")

class NotificationFormatHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/NotificationFormatHelper"
    INSTANCE = JavaStaticField("Lcom/onesignal/notifications/internal/common/NotificationFormatHelper;")
    PAYLOAD_OS_ROOT_CUSTOM = JavaStaticField("Ljava/lang/String;")
    PAYLOAD_OS_NOTIFICATION_ID = JavaStaticField("Ljava/lang/String;")
    isOneSignalIntent = JavaMethod("(Landroid/content/Intent;)Z")
    isOneSignalBundle = JavaMethod("(Landroid/os/Bundle;)Z")
    getOSNotificationIdFromJson = JavaMethod("(Lorg/json/JSONObject;)Ljava/lang/String;")

class NotificationGenerationJob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/NotificationGenerationJob"
    __javaconstructor__ = [("(Lcom/onesignal/notifications/internal/Notification;Lorg/json/JSONObject;)V", False), ("(Lorg/json/JSONObject;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getNotification = JavaMethod("()Lcom/onesignal/notifications/internal/Notification;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getJsonPayload = JavaMethod("()Lorg/json/JSONObject;")
    setJsonPayload = JavaMethod("(Lorg/json/JSONObject;)V")
    setRestoring = JavaMethod("(Z)V")
    isNotificationToDisplay = JavaMethod("()Z")
    setNotificationToDisplay = JavaMethod("(Z)V")
    getShownTimeStamp = JavaMethod("()Ljava/lang/Long;")
    setShownTimeStamp = JavaMethod("(Ljava/lang/Long;)V")
    getOverriddenBodyFromExtender = JavaMethod("()Ljava/lang/CharSequence;")
    setOverriddenBodyFromExtender = JavaMethod("(Ljava/lang/CharSequence;)V")
    getOverriddenTitleFromExtender = JavaMethod("()Ljava/lang/CharSequence;")
    setOverriddenTitleFromExtender = JavaMethod("(Ljava/lang/CharSequence;)V")
    getOverriddenSound = JavaMethod("()Landroid/net/Uri;")
    setOverriddenSound = JavaMethod("(Landroid/net/Uri;)V")
    getOverriddenFlags = JavaMethod("()Ljava/lang/Integer;")
    setOverriddenFlags = JavaMethod("(Ljava/lang/Integer;)V")
    getOrgFlags = JavaMethod("()Ljava/lang/Integer;")
    setOrgFlags = JavaMethod("(Ljava/lang/Integer;)V")
    getOrgSound = JavaMethod("()Landroid/net/Uri;")
    setOrgSound = JavaMethod("(Landroid/net/Uri;)V")
    hasExtender = JavaMethod("()Z")
    getApiNotificationId = JavaMethod("()Ljava/lang/String;")
    getAndroidId = JavaMethod("()I")
    getBody = JavaMethod("()Ljava/lang/CharSequence;")
    getAdditionalData = JavaMethod("()Lorg/json/JSONObject;")
    isRestoring = JavaMethod("()Z")

class NotificationHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/NotificationHelper"
    INSTANCE = JavaStaticField("Lcom/onesignal/notifications/internal/common/NotificationHelper;")
    GROUPLESS_SUMMARY_KEY = JavaStaticField("Ljava/lang/String;")
    GROUPLESS_SUMMARY_ID = JavaStaticField("I")
    areNotificationsEnabled$default = JavaStaticMethod("(Lcom/onesignal/notifications/internal/common/NotificationHelper;Landroid/content/Context;Ljava/lang/String;ILjava/lang/Object;)Z")
    getGrouplessNotifsCount = JavaMethod("(Landroid/content/Context;)I")
    getActiveGrouplessNotifications = JavaMethod("(Landroid/content/Context;)Ljava/util/ArrayList;")
    assignGrouplessNotifications = JavaMethod("(Landroid/content/Context;Ljava/util/ArrayList;)V")
    getCampaignNameFromNotification = JavaMethod("(Lcom/onesignal/notifications/INotification;)Ljava/lang/String;")
    generateNotificationOpenedResult$com_onesignal_notifications = JavaMethod("(Lorg/json/JSONArray;Lcom/onesignal/core/internal/time/ITime;)Lcom/onesignal/notifications/internal/NotificationClickEvent;")
    getNotificationIdFromFCMJson = JavaMethod("(Lorg/json/JSONObject;)Ljava/lang/String;")
    getNotificationManager = JavaMethod("(Landroid/content/Context;)Landroid/app/NotificationManager;")
    parseVibrationPattern = JavaMethod("(Lorg/json/JSONObject;)[J")
    getSoundUri = JavaMethod("(Landroid/content/Context;Ljava/lang/String;)Landroid/net/Uri;")
    getCustomJSONObject = JavaMethod("(Lorg/json/JSONObject;)Lorg/json/JSONObject;")
    areNotificationsEnabled = JavaMethod("(Landroid/content/Context;Ljava/lang/String;)Z")
    getActiveNotifications = JavaMethod("(Landroid/content/Context;)[Landroid/service/notification/StatusBarNotification;")
    isGroupSummary = JavaMethod("(Landroid/service/notification/StatusBarNotification;)Z")

class NotificationPriorityMapper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/NotificationPriorityMapper"
    INSTANCE = JavaStaticField("Lcom/onesignal/notifications/internal/common/NotificationPriorityMapper;")
    toAndroidImportance = JavaMethod("(I)I")
    isHighPriority = JavaMethod("(I)Z")
    toAndroidPriority = JavaMethod("(I)I")

class OSNotificationOpenAppSettings(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/OSNotificationOpenAppSettings"
    INSTANCE = JavaStaticField("Lcom/onesignal/notifications/internal/common/OSNotificationOpenAppSettings;")
    getShouldOpenActivity = JavaMethod("(Landroid/content/Context;)Z")
    getSuppressLaunchURL = JavaMethod("(Landroid/content/Context;)Z")

class OSNotificationOpenBehaviorFromPushPayload(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/OSNotificationOpenBehaviorFromPushPayload"
    __javaconstructor__ = [("(Landroid/content/Context;Lorg/json/JSONObject;)V", False)]
    getUri = JavaMethod("()Landroid/net/Uri;")
    getShouldOpenApp = JavaMethod("()Z")

class OSWorkManagerHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/common/OSWorkManagerHelper"
    INSTANCE = JavaStaticField("Lcom/onesignal/notifications/internal/common/OSWorkManagerHelper;")
    getInstance = JavaMethod("(Landroid/content/Context;)Landroidx/work/WorkManager;")