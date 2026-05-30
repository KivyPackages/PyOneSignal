from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IInAppMessage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessage"
    getMessageId = JavaMethod("()Ljava/lang/String;")

class IInAppMessageClickEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessageClickEvent"
    getMessage = JavaMethod("()Lcom/onesignal/inAppMessages/IInAppMessage;")
    getResult = JavaMethod("()Lcom/onesignal/inAppMessages/IInAppMessageClickResult;")

class IInAppMessageClickListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessageClickListener"
    onClick = JavaMethod("(Lcom/onesignal/inAppMessages/IInAppMessageClickEvent;)V")

class IInAppMessageClickResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessageClickResult"
    getUrl = JavaMethod("()Ljava/lang/String;")
    getActionId = JavaMethod("()Ljava/lang/String;")
    getUrlTarget = JavaMethod("()Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")
    getClosingMessage = JavaMethod("()Z")

class IInAppMessageDidDismissEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessageDidDismissEvent"
    getMessage = JavaMethod("()Lcom/onesignal/inAppMessages/IInAppMessage;")

class IInAppMessageDidDisplayEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessageDidDisplayEvent"
    getMessage = JavaMethod("()Lcom/onesignal/inAppMessages/IInAppMessage;")

class IInAppMessageLifecycleListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessageLifecycleListener"
    onWillDisplay = JavaMethod("(Lcom/onesignal/inAppMessages/IInAppMessageWillDisplayEvent;)V")
    onDidDisplay = JavaMethod("(Lcom/onesignal/inAppMessages/IInAppMessageDidDisplayEvent;)V")
    onWillDismiss = JavaMethod("(Lcom/onesignal/inAppMessages/IInAppMessageWillDismissEvent;)V")
    onDidDismiss = JavaMethod("(Lcom/onesignal/inAppMessages/IInAppMessageDidDismissEvent;)V")

class IInAppMessageWillDismissEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessageWillDismissEvent"
    getMessage = JavaMethod("()Lcom/onesignal/inAppMessages/IInAppMessage;")

class IInAppMessageWillDisplayEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessageWillDisplayEvent"
    getMessage = JavaMethod("()Lcom/onesignal/inAppMessages/IInAppMessage;")

class IInAppMessagesManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/IInAppMessagesManager"
    removeLifecycleListener = JavaMethod("(Lcom/onesignal/inAppMessages/IInAppMessageLifecycleListener;)V")
    getPaused = JavaMethod("()Z")
    setPaused = JavaMethod("(Z)V")
    addTrigger = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    addTriggers = JavaMethod("(Ljava/util/Map;)V")
    removeTrigger = JavaMethod("(Ljava/lang/String;)V")
    removeTriggers = JavaMethod("(Ljava/util/Collection;)V")
    clearTriggers = JavaMethod("()V")
    addLifecycleListener = JavaMethod("(Lcom/onesignal/inAppMessages/IInAppMessageLifecycleListener;)V")
    addClickListener = JavaMethod("(Lcom/onesignal/inAppMessages/IInAppMessageClickListener;)V")
    removeClickListener = JavaMethod("(Lcom/onesignal/inAppMessages/IInAppMessageClickListener;)V")

class InAppMessageActionUrlType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/InAppMessageActionUrlType"
    Companion = JavaStaticField("Lcom/onesignal/inAppMessages/InAppMessageActionUrlType$Companion;")
    IN_APP_WEBVIEW = JavaStaticField("Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")
    BROWSER = JavaStaticField("Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")
    REPLACE_CONTENT = JavaStaticField("Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")
    toString = JavaMethod("()Ljava/lang/String;")
    values = JavaStaticMethod("()[Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    access$getText$p = JavaStaticMethod("(Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;)Ljava/lang/String;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/inAppMessages/InAppMessageActionUrlType$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        fromString = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")
    IN_APP_WEBVIEW = JavaStaticField("Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")
    BROWSER = JavaStaticField("Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")
    REPLACE_CONTENT = JavaStaticField("Lcom/onesignal/inAppMessages/InAppMessageActionUrlType;")