from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IAMLifecycleService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/lifecycle/impl/IAMLifecycleService"
    __javaconstructor__ = [("()V", False)]
    messageActionOccurredOnPreview = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/inAppMessages/internal/InAppMessageClickResult;)V")
    messageWillDisplay = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")
    messageWasDisplayed = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")
    messageActionOccurredOnMessage = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/inAppMessages/internal/InAppMessageClickResult;)V")
    messagePageChanged = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Lcom/onesignal/inAppMessages/internal/InAppMessagePage;)V")
    messageWillDismiss = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")
    messageWasDismissed = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)V")