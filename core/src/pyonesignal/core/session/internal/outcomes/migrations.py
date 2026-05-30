from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class RemoveInvalidSessionTimeRecords(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/migrations/RemoveInvalidSessionTimeRecords"
    INSTANCE = JavaStaticField("Lcom/onesignal/session/internal/outcomes/migrations/RemoveInvalidSessionTimeRecords;")
    run = JavaMethod("(Lcom/onesignal/core/internal/database/IDatabaseProvider;)V")