from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class InAppHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/common/InAppHelper"
    INSTANCE = JavaStaticField("Lcom/onesignal/inAppMessages/internal/common/InAppHelper;")
    variantIdForMessage = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/core/internal/language/ILanguageContext;)Ljava/lang/String;")

class OneSignalChromeTab(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/common/OneSignalChromeTab"
    INSTANCE = JavaStaticField("Lcom/onesignal/inAppMessages/internal/common/OneSignalChromeTab;")
    open$com_onesignal_inAppMessages = JavaMethod("(Ljava/lang/String;ZLandroid/content/Context;)Z")