from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class NotificationQueryHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/data/impl/NotificationQueryHelper"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    recentUninteractedWithNotificationsWhere = JavaMethod("()Ljava/lang/StringBuilder;")

class NotificationRepository(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/data/impl/NotificationRepository"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/notifications/internal/data/INotificationQueryHelper;Lcom/onesignal/core/internal/database/IDatabaseProvider;Lcom/onesignal/core/internal/time/ITime;Lcom/onesignal/notifications/internal/badges/IBadgeCountUpdater;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/notifications/internal/data/impl/NotificationRepository$Companion;")
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
    access$get_time$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/data/impl/NotificationRepository;)Lcom/onesignal/core/internal/time/ITime;")
    access$get_databaseProvider$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/data/impl/NotificationRepository;)Lcom/onesignal/core/internal/database/IDatabaseProvider;")
    access$get_applicationService$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/data/impl/NotificationRepository;)Lcom/onesignal/core/internal/application/IApplicationService;")
    access$get_badgeCountUpdater$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/data/impl/NotificationRepository;)Lcom/onesignal/notifications/internal/badges/IBadgeCountUpdater;")
    access$internalMarkAsDismissed = JavaStaticMethod("(Lcom/onesignal/notifications/internal/data/impl/NotificationRepository;I)Z")
    access$get_queryHelper$p = JavaStaticMethod("(Lcom/onesignal/notifications/internal/data/impl/NotificationRepository;)Lcom/onesignal/notifications/internal/data/INotificationQueryHelper;")
    access$getCOLUMNS_FOR_LIST_NOTIFICATIONS$cp = JavaStaticMethod("()[Ljava/lang/String;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/notifications/internal/data/impl/NotificationRepository$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        getCOLUMNS_FOR_LIST_NOTIFICATIONS = JavaMethod("()[Ljava/lang/String;")