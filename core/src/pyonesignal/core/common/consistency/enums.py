from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IamFetchRywTokenKey(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/common/consistency/enums/IamFetchRywTokenKey"
    USER = JavaStaticField("Lcom/onesignal/common/consistency/enums/IamFetchRywTokenKey;")
    SUBSCRIPTION = JavaStaticField("Lcom/onesignal/common/consistency/enums/IamFetchRywTokenKey;")
    values = JavaStaticMethod("()[Lcom/onesignal/common/consistency/enums/IamFetchRywTokenKey;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/common/consistency/enums/IamFetchRywTokenKey;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    USER = JavaStaticField("Lcom/onesignal/common/consistency/enums/IamFetchRywTokenKey;")
    SUBSCRIPTION = JavaStaticField("Lcom/onesignal/common/consistency/enums/IamFetchRywTokenKey;")