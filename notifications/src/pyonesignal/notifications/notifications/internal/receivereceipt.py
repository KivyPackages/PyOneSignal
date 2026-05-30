from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IReceiveReceiptProcessor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/receivereceipt/IReceiveReceiptProcessor"
    sendReceiveReceipt = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

class IReceiveReceiptWorkManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/receivereceipt/IReceiveReceiptWorkManager"
    enqueueReceiveReceipt = JavaMethod("(Ljava/lang/String;)V")