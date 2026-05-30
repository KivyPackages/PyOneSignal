from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IInAppPreferencesController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/preferences/IInAppPreferencesController"
    getImpressionesMessagesId = JavaMethod("()Ljava/util/Set;")
    setImpressionesMessagesId = JavaMethod("(Ljava/util/Set;)V")
    getViewPageImpressionedIds = JavaMethod("()Ljava/util/Set;")
    getSavedIAMs = JavaMethod("()Ljava/lang/String;")
    setSavedIAMs = JavaMethod("(Ljava/lang/String;)V")
    cleanInAppMessageIds = JavaMethod("(Ljava/util/Set;)V")
    cleanInAppMessageClickedClickIds = JavaMethod("(Ljava/util/Set;)V")
    getClickedMessagesId = JavaMethod("()Ljava/util/Set;")
    getDismissedMessagesId = JavaMethod("()Ljava/util/Set;")
    getLastTimeInAppDismissed = JavaMethod("()Ljava/lang/Long;")
    setLastTimeInAppDismissed = JavaMethod("(Ljava/lang/Long;)V")
    setViewPageImpressionedIds = JavaMethod("(Ljava/util/Set;)V")
    setDismissedMessagesId = JavaMethod("(Ljava/util/Set;)V")
    setClickedMessagesId = JavaMethod("(Ljava/util/Set;)V")