from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DatabaseCursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/database/impl/DatabaseCursor"
    __javaconstructor__ = [("(Landroid/database/Cursor;)V", False)]
    getInt = JavaMethod("(Ljava/lang/String;)I")
    getLong = JavaMethod("(Ljava/lang/String;)J")
    getFloat = JavaMethod("(Ljava/lang/String;)F")
    getCount = JavaMethod("()I")
    getString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    moveToNext = JavaMethod("()Z")
    getOptString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    moveToFirst = JavaMethod("()Z")
    getOptFloat = JavaMethod("(Ljava/lang/String;)Ljava/lang/Float;")
    getOptLong = JavaMethod("(Ljava/lang/String;)Ljava/lang/Long;")
    getOptInt = JavaMethod("(Ljava/lang/String;)Ljava/lang/Integer;")

class DatabaseProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/database/impl/DatabaseProvider"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;)V", False)]
    getOs = JavaMethod("()Lcom/onesignal/core/internal/database/IDatabase;")

class OSDatabase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/database/impl/OSDatabase"
    __javaconstructor__ = [("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeTableProvider;Landroid/content/Context;I)V", False), ("(Lcom/onesignal/session/internal/outcomes/impl/OutcomeTableProvider;Landroid/content/Context;IILkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/database/impl/OSDatabase$Companion;")
    DEFAULT_TTL_IF_NOT_IN_PAYLOAD = JavaStaticField("I")
    update = JavaMethod("(Ljava/lang/String;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")
    insert = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/content/ContentValues;)V")
    delete = JavaMethod("(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)V")
    query = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/jvm/functions/Function1;)V")
    onCreate = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;)V")
    insertOrThrow = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/content/ContentValues;)V")
    onUpgrade = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;II)V")
    onDowngrade = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;II)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/database/impl/OSDatabase$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

class OneSignalDbContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/database/impl/OneSignalDbContract"
    __javaconstructor__ = [("()V", False)]

    class InAppMessageTable(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/database/impl/OneSignalDbContract$InAppMessageTable"
        INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/database/impl/OneSignalDbContract$InAppMessageTable;")
        TABLE_NAME = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_MESSAGE_ID = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_DISPLAY_QUANTITY = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_LAST_DISPLAY = JavaStaticField("Ljava/lang/String;")
        COLUMN_CLICK_IDS = JavaStaticField("Ljava/lang/String;")
        COLUMN_DISPLAYED_IN_SESSION = JavaStaticField("Ljava/lang/String;")
        _COUNT = JavaStaticField("Ljava/lang/String;")
        _ID = JavaStaticField("Ljava/lang/String;")

    class NotificationTable(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/database/impl/OneSignalDbContract$NotificationTable"
        INSTANCE = JavaStaticField("Lcom/onesignal/core/internal/database/impl/OneSignalDbContract$NotificationTable;")
        TABLE_NAME = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_NOTIFICATION_ID = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_ANDROID_NOTIFICATION_ID = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_GROUP_ID = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_COLLAPSE_ID = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_IS_SUMMARY = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_OPENED = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_DISMISSED = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_TITLE = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_MESSAGE = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_CREATED_TIME = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_EXPIRE_TIME = JavaStaticField("Ljava/lang/String;")
        COLUMN_NAME_FULL_DATA = JavaStaticField("Ljava/lang/String;")
        INDEX_CREATE_NOTIFICATION_ID = JavaStaticField("Ljava/lang/String;")
        INDEX_CREATE_ANDROID_NOTIFICATION_ID = JavaStaticField("Ljava/lang/String;")
        INDEX_CREATE_GROUP_ID = JavaStaticField("Ljava/lang/String;")
        INDEX_CREATE_COLLAPSE_ID = JavaStaticField("Ljava/lang/String;")
        INDEX_CREATE_CREATED_TIME = JavaStaticField("Ljava/lang/String;")
        INDEX_CREATE_EXPIRE_TIME = JavaStaticField("Ljava/lang/String;")
        _COUNT = JavaStaticField("Ljava/lang/String;")
        _ID = JavaStaticField("Ljava/lang/String;")