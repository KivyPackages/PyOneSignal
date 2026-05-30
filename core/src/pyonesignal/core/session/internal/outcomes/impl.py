from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class CachedUniqueOutcome(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/CachedUniqueOutcome"
    __javaconstructor__ = [("(Ljava/lang/String;Lcom/onesignal/session/internal/influence/InfluenceChannel;)V", False)]
    getChannel = JavaMethod("()Lcom/onesignal/session/internal/influence/InfluenceChannel;")
    getInfluenceId = JavaMethod("()Ljava/lang/String;")

class CachedUniqueOutcomeTable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/CachedUniqueOutcomeTable"
    INSTANCE = JavaStaticField("Lcom/onesignal/session/internal/outcomes/impl/CachedUniqueOutcomeTable;")
    ID = JavaStaticField("Ljava/lang/String;")
    TABLE_NAME_V2 = JavaStaticField("Ljava/lang/String;")
    TABLE_NAME = JavaStaticField("Ljava/lang/String;")
    TABLE_NAME_V1 = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NOTIFICATION_ID = JavaStaticField("Ljava/lang/String;")
    COLUMN_CHANNEL_INFLUENCE_ID = JavaStaticField("Ljava/lang/String;")
    COLUMN_CHANNEL_TYPE = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NAME = JavaStaticField("Ljava/lang/String;")

class IOutcomeEventsBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/IOutcomeEventsBackendService"
    sendOutcomeEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Boolean;Lcom/onesignal/session/internal/outcomes/impl/OutcomeEvent;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class IOutcomeEventsPreferences(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/IOutcomeEventsPreferences"
    getUnattributedUniqueOutcomeEventsSentByChannel = JavaMethod("()Ljava/util/Set;")
    setUnattributedUniqueOutcomeEventsSentByChannel = JavaMethod("(Ljava/util/Set;)V")

class IOutcomeEventsRepository(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/IOutcomeEventsRepository"
    deleteOldOutcomeEvent = JavaMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventParams;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    saveUniqueOutcomeEventParams = JavaMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventParams;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getNotCachedUniqueInfluencesForOutcome = JavaMethod("(Ljava/lang/String;Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getAllEventsToSend = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    saveOutcomeEvent = JavaMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventParams;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    cleanCachedUniqueOutcomeEventNotifications = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class OutcomeConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeConstants"
    INSTANCE = JavaStaticField("Lcom/onesignal/session/internal/outcomes/impl/OutcomeConstants;")
    OUTCOME_ID = JavaStaticField("Ljava/lang/String;")
    OUTCOME_SOURCES = JavaStaticField("Ljava/lang/String;")
    WEIGHT = JavaStaticField("Ljava/lang/String;")
    TIMESTAMP = JavaStaticField("Ljava/lang/String;")
    SESSION_TIME = JavaStaticField("Ljava/lang/String;")
    DIRECT = JavaStaticField("Ljava/lang/String;")
    INDIRECT = JavaStaticField("Ljava/lang/String;")
    NOTIFICATION_IDS = JavaStaticField("Ljava/lang/String;")
    IAM_IDS = JavaStaticField("Ljava/lang/String;")

class OutcomeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEvent"
    __javaconstructor__ = [("(Lcom/onesignal/session/internal/influence/InfluenceType;Lorg/json/JSONArray;Ljava/lang/String;JJF)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/session/internal/outcomes/impl/OutcomeEvent$Companion;")
    getTimestamp = JavaMethod("()J")
    getSession = JavaMethod("()Lcom/onesignal/session/internal/influence/InfluenceType;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getNotificationIds = JavaMethod("()Lorg/json/JSONArray;")
    getSessionTime = JavaMethod("()J")
    getWeight = JavaMethod("()F")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEvent$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        fromOutcomeEventParamstoOutcomeEvent = JavaMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventParams;)Lcom/onesignal/session/internal/outcomes/impl/OutcomeEvent;")

class OutcomeEventParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEventParams"
    __javaconstructor__ = [("(Ljava/lang/String;Lcom/onesignal/session/internal/outcomes/impl/OutcomeSource;FJJ)V", False)]
    getTimestamp = JavaMethod("()J")
    isUnattributed = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getSessionTime = JavaMethod("()J")
    getWeight = JavaMethod("()F")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    getOutcomeId = JavaMethod("()Ljava/lang/String;")
    getOutcomeSource = JavaMethod("()Lcom/onesignal/session/internal/outcomes/impl/OutcomeSource;")
    setWeight = JavaMethod("(F)V")
    setSessionTime = JavaMethod("(J)V")
    setTimestamp = JavaMethod("(J)V")

class OutcomeEventsBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEventsBackendService"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/http/IHttpClient;)V", False)]
    sendOutcomeEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Boolean;Lcom/onesignal/session/internal/outcomes/impl/OutcomeEvent;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class OutcomeEventsController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEventsController"
    __javaconstructor__ = [("(Lcom/onesignal/session/internal/session/ISessionService;Lcom/onesignal/session/internal/influence/IInfluenceManager;Lcom/onesignal/session/internal/outcomes/impl/IOutcomeEventsRepository;Lcom/onesignal/session/internal/outcomes/impl/IOutcomeEventsPreferences;Lcom/onesignal/session/internal/outcomes/impl/IOutcomeEventsBackendService;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/user/internal/identity/IdentityModelStore;Lcom/onesignal/user/internal/subscriptions/ISubscriptionManager;Lcom/onesignal/core/internal/device/IDeviceService;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    start = JavaMethod("()V")
    access$sendSavedOutcomes = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsController;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$get_outcomeEventsCache$p = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsController;)Lcom/onesignal/session/internal/outcomes/impl/IOutcomeEventsRepository;")
    access$sendSavedOutcomeEvent = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsController;Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventParams;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$sendUniqueOutcomeEvent = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsController;Ljava/lang/String;Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$sendAndCreateOutcomeEvent = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsController;Ljava/lang/String;FJLjava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$getUniqueIds = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsController;Ljava/lang/String;Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    access$requestMeasureOutcomeEvent = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsController;Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventParams;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendUniqueOutcomeEvent = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendSessionEndOutcomeEvent = JavaMethod("(JLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendOutcomeEvent = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendOutcomeEventWithValue = JavaMethod("(Ljava/lang/String;FLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    onSessionStarted = JavaMethod("()V")
    onSessionActive = JavaMethod("()V")
    onSessionEnded = JavaMethod("(J)V")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEventsController$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")
        $EnumSwitchMapping$1 = JavaStaticField("[I")

class OutcomeEventsPreferences(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEventsPreferences"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/preferences/IPreferencesService;)V", False)]
    getUnattributedUniqueOutcomeEventsSentByChannel = JavaMethod("()Ljava/util/Set;")
    setUnattributedUniqueOutcomeEventsSentByChannel = JavaMethod("(Ljava/util/Set;)V")

class OutcomeEventsRepository(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEventsRepository"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/database/IDatabaseProvider;)V", False)]
    access$get_databaseProvider$p = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsRepository;)Lcom/onesignal/core/internal/database/IDatabaseProvider;")
    access$getNotificationInfluenceSource = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsRepository;Lcom/onesignal/session/internal/influence/InfluenceType;Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;Ljava/lang/String;)Lcom/onesignal/session/internal/outcomes/impl/OutcomeSource;")
    access$getIAMInfluenceSource = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsRepository;Lcom/onesignal/session/internal/influence/InfluenceType;Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;Ljava/lang/String;Lcom/onesignal/session/internal/outcomes/impl/OutcomeSource;)Lcom/onesignal/session/internal/outcomes/impl/OutcomeSource;")
    access$addIdsToListFromSource = JavaStaticMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsRepository;Ljava/util/List;Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;)V")
    deleteOldOutcomeEvent = JavaMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventParams;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    saveUniqueOutcomeEventParams = JavaMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventParams;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getNotCachedUniqueInfluencesForOutcome = JavaMethod("(Ljava/lang/String;Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getAllEventsToSend = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    saveOutcomeEvent = JavaMethod("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventParams;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    cleanCachedUniqueOutcomeEventNotifications = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEventsRepository$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")

class OutcomeEventsTable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeEventsTable"
    INSTANCE = JavaStaticField("Lcom/onesignal/session/internal/outcomes/impl/OutcomeEventsTable;")
    ID = JavaStaticField("Ljava/lang/String;")
    TABLE_NAME = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NOTIFICATION_IDS = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_IAM_IDS = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_SESSION = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NOTIFICATION_INFLUENCE_TYPE = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_IAM_INFLUENCE_TYPE = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_NAME = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_WEIGHT = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_TIMESTAMP = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_PARAMS = JavaStaticField("Ljava/lang/String;")
    COLUMN_NAME_SESSION_TIME = JavaStaticField("Ljava/lang/String;")

class OutcomeSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeSource"
    __javaconstructor__ = [("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    setDirectBody = JavaMultipleMethod([("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;)Lcom/onesignal/session/internal/outcomes/impl/OutcomeSource;", False, False), ("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;)V", False, False)])
    setIndirectBody = JavaMultipleMethod([("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;)Lcom/onesignal/session/internal/outcomes/impl/OutcomeSource;", False, False), ("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;)V", False, False)])
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    getDirectBody = JavaMethod("()Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;")
    getIndirectBody = JavaMethod("()Lcom/onesignal/session/internal/outcomes/impl/OutcomeSourceBody;")

class OutcomeSourceBody(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeSourceBody"
    __javaconstructor__ = [("(Lorg/json/JSONArray;)V", False), ("()V", False), ("(Lorg/json/JSONArray;Lorg/json/JSONArray;)V", False), ("(Lorg/json/JSONArray;Lorg/json/JSONArray;ILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    getNotificationIds = JavaMethod("()Lorg/json/JSONArray;")
    getInAppMessagesIds = JavaMethod("()Lorg/json/JSONArray;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")
    setInAppMessagesIds = JavaMethod("(Lorg/json/JSONArray;)V")
    setNotificationIds = JavaMethod("(Lorg/json/JSONArray;)V")

class OutcomeTableProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomeTableProvider"
    __javaconstructor__ = [("()V", False)]
    upgradeOutcomeTableRevision1To2 = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    upgradeOutcomeTableRevision2To3 = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    upgradeCacheOutcomeTableRevision1To2 = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    upgradeOutcomeTableRevision3To4 = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")

class OutcomesDbContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/impl/OutcomesDbContract"
    INSTANCE = JavaStaticField("Lcom/onesignal/session/internal/outcomes/impl/OutcomesDbContract;")
    OUTCOME_EVENT_TABLE = JavaStaticField("Ljava/lang/String;")
    CACHE_UNIQUE_OUTCOME_TABLE = JavaStaticField("Ljava/lang/String;")
    CACHE_UNIQUE_OUTCOME_COLUMN_CHANNEL_INFLUENCE_ID = JavaStaticField("Ljava/lang/String;")
    CACHE_UNIQUE_OUTCOME_COLUMN_CHANNEL_TYPE = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_OUTCOME_ENTRIES_V1 = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_OUTCOME_ENTRIES_V2 = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_OUTCOME_ENTRIES_V3 = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_OUTCOME_ENTRIES_V4 = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_UNIQUE_OUTCOME_ENTRIES_V1 = JavaStaticField("Ljava/lang/String;")
    SQL_CREATE_UNIQUE_OUTCOME_ENTRIES_V2 = JavaStaticField("Ljava/lang/String;")