from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ICursor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/database/ICursor"
    getString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getInt = JavaMethod("(Ljava/lang/String;)I")
    getLong = JavaMethod("(Ljava/lang/String;)J")
    getFloat = JavaMethod("(Ljava/lang/String;)F")
    getCount = JavaMethod("()I")
    moveToNext = JavaMethod("()Z")
    getOptString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    moveToFirst = JavaMethod("()Z")
    getOptFloat = JavaMethod("(Ljava/lang/String;)Ljava/lang/Float;")
    getOptLong = JavaMethod("(Ljava/lang/String;)Ljava/lang/Long;")
    getOptInt = JavaMethod("(Ljava/lang/String;)Ljava/lang/Integer;")

class IDatabase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/database/IDatabase"
    query = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/jvm/functions/Function1;)V")
    update = JavaMethod("(Ljava/lang/String;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")
    insert = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/content/ContentValues;)V")
    delete = JavaMethod("(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)V")
    insertOrThrow = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/content/ContentValues;)V")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/database/IDatabase$DefaultImpls"
        query$default = JavaStaticMethod("(Lcom/onesignal/core/internal/database/IDatabase;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/jvm/functions/Function1;ILjava/lang/Object;)V")

class IDatabaseProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/database/IDatabaseProvider"
    getOs = JavaMethod("()Lcom/onesignal/core/internal/database/IDatabase;")