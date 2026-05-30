from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ReceiveReceiptProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/receivereceipt/impl/ReceiveReceiptProcessor"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/device/IDeviceService;Lcom/onesignal/notifications/internal/backend/INotificationBackendService;)V", False)]
    sendReceiveReceipt = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class ReceiveReceiptWorkManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/receivereceipt/impl/ReceiveReceiptWorkManager"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/user/internal/subscriptions/ISubscriptionManager;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/receivereceipt/impl/ReceiveReceiptWorkManager$Companion;")
    enqueueReceiveReceipt = JavaMethod("(Ljava/lang/String;)V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/receivereceipt/impl/ReceiveReceiptWorkManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class ReceiveReceiptWorker(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/receivereceipt/impl/ReceiveReceiptWorkManager$ReceiveReceiptWorker"
        __javaconstructor__ = [("(Landroid/content/Context;Landroidx/work/WorkerParameters;)V", False)]
        doWork = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")