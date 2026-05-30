from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationBackendService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/backend/INotificationBackendService"
    updateNotificationAsReceived = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    updateNotificationAsOpened = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lcom/onesignal/core/internal/device/IDeviceService$DeviceType;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")