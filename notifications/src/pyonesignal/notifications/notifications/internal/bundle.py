from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationBundleProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/bundle/INotificationBundleProcessor"
    processBundleFromReceiver = JavaMethod("(Landroid/content/Context;Landroid/os/Bundle;)Lcom/onesignal/notifications/internal/bundle/INotificationBundleProcessor$ProcessedBundleResult;")

    class ProcessedBundleResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/bundle/INotificationBundleProcessor$ProcessedBundleResult"
        __javaconstructor__ = [("()V", False)]
        isProcessed = JavaMethod("()Z")
        isWorkManagerProcessing = JavaMethod("()Z")
        setWorkManagerProcessing = JavaMethod("(Z)V")
        setOneSignalPayload = JavaMethod("(Z)V")
        setDeniedByLifecycleCallback = JavaMethod("(Z)V")