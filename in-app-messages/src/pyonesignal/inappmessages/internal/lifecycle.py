from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IInAppLifecycleEventHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/lifecycle/IInAppLifecycleEventHandler"
    onMessageWillDisplay = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")
    onMessageWasDisplayed = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")
    onMessageActionOccurredOnPreview = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/inAppMessages/internal/InAppMessageClickResult;)V")
    onMessageActionOccurredOnMessage = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/inAppMessages/internal/InAppMessageClickResult;)V")
    onMessagePageChanged = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/inAppMessages/internal/InAppMessagePage;)V")
    onMessageWillDismiss = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")
    onMessageWasDismissed = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")

class IInAppLifecycleService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/lifecycle/IInAppLifecycleService"
    messageWasDismissed = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")
    messageActionOccurredOnPreview = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/inAppMessages/internal/InAppMessageClickResult;)V")
    messageWillDisplay = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")
    messageWasDisplayed = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")
    messageActionOccurredOnMessage = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/inAppMessages/internal/InAppMessageClickResult;)V")
    messagePageChanged = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/inAppMessages/internal/InAppMessagePage;)V")
    messageWillDismiss = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")