from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class INotificationQueryHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/data/INotificationQueryHelper"
    recentUninteractedWithNotificationsWhere = JavaMethod("()Ljava/lang/StringBuilder;")

class INotificationRepository(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/data/INotificationRepository"
    createSummaryNotification = JavaMethod("(ILjava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    createNotification = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ZZILjava/lang/String;Ljava/lang/String;JLjava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    doesNotificationExist = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getGroupId = JavaMethod("(ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getAndroidIdForGroup = JavaMethod("(Ljava/lang/String;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    getAndroidIdFromCollapseKey = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    listNotificationsForGroup = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    listNotificationsForOutstanding = JavaMethod("(Ljava/util/List;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    markAsConsumed = JavaMethod("(IZLjava/lang/String;ZLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    markAsDismissed = JavaMethod("(ILkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    markAsDismissedForGroup = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    markAsDismissedForOutstanding = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    clearOldestOverLimitFallback = JavaMethod("(IILkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    deleteExpiredNotifications = JavaMethod("(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/data/INotificationRepository$DefaultImpls"
        markAsConsumed$default = JavaStaticMethod("(Lcom/onesignal/notifications/internal/data/INotificationRepository;IZLjava/lang/String;ZLkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")
        listNotificationsForOutstanding$default = JavaStaticMethod("(Lcom/onesignal/notifications/internal/data/INotificationRepository;Ljava/util/List;Lkotlin/coroutines/Continuation;ILjava/lang/Object;)Ljava/lang/Object;")

    class NotificationData(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/data/INotificationRepository$NotificationData"
        __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;JLjava/lang/String;Ljava/lang/String;)V", False)]
        getMessage = JavaMethod("()Ljava/lang/String;")
        getId = JavaMethod("()Ljava/lang/String;")
        getTitle = JavaMethod("()Ljava/lang/String;")
        getAndroidId = JavaMethod("()I")
        getFullData = JavaMethod("()Ljava/lang/String;")
        getCreatedAt = JavaMethod("()J")