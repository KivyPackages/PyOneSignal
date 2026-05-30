from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DynamicTriggerController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/impl/DynamicTriggerController"
    __javaconstructor__ = [("(Lcom/onesignal/inAppMessages/internal/state/InAppStateService;Lcom/onesignal/session/internal/session/ISessionService;Lcom/onesignal/core/internal/time/ITime;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/inAppMessages/internal/triggers/impl/DynamicTriggerController$Companion;")
    dynamicTriggerShouldFire = JavaMethod("(Lcom/onesignal/inAppMessages/internal/Trigger;)Z")
    getEvents = JavaMethod("()Lcom/onesignal/common/events/EventProducer;")
    access$getScheduledMessages$p = JavaStaticMethod("(Lcom/onesignal/inAppMessages/internal/triggers/impl/DynamicTriggerController;)Ljava/util/List;")
    subscribe = JavaMultipleMethod([("(Lcom/onesignal/inAppMessages/internal/triggers/ITriggerHandler;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    unsubscribe = JavaMultipleMethod([("(Ljava/lang/Object;)V", False, False), ("(Lcom/onesignal/inAppMessages/internal/triggers/ITriggerHandler;)V", False, False)])
    getHasSubscribers = JavaMethod("()Z")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/impl/DynamicTriggerController$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/impl/DynamicTriggerController$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")
        $EnumSwitchMapping$1 = JavaStaticField("[I")

class DynamicTriggerTimer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/impl/DynamicTriggerTimer"
    INSTANCE = JavaStaticField("Lcom/onesignal/inAppMessages/internal/triggers/impl/DynamicTriggerTimer;")
    scheduleTrigger = JavaMethod("(Ljava/util/TimerTask;Ljava/lang/String;J)V")

class TriggerController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/impl/TriggerController"
    __javaconstructor__ = [("(Lcom/onesignal/inAppMessages/internal/triggers/TriggerModelStore;Lcom/onesignal/inAppMessages/internal/triggers/impl/DynamicTriggerController;)V", False)]
    onModelAdded = JavaMultipleMethod([("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/inAppMessages/internal/triggers/TriggerModel;Ljava/lang/String;)V", False, False)])
    onModelRemoved = JavaMultipleMethod([("(Lcom/onesignal/inAppMessages/internal/triggers/TriggerModel;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False)])
    getTriggers = JavaMethod("()Ljava/util/concurrent/ConcurrentHashMap;")
    subscribe = JavaMultipleMethod([("(Lcom/onesignal/inAppMessages/internal/triggers/ITriggerHandler;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    unsubscribe = JavaMultipleMethod([("(Lcom/onesignal/inAppMessages/internal/triggers/ITriggerHandler;)V", False, False), ("(Ljava/lang/Object;)V", False, False)])
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")
    isTriggerOnMessage = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;Ljava/util/Collection;)Z")
    evaluateMessageTriggers = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)Z")
    messageHasOnlyDynamicTriggers = JavaMethod("(Lcom/onesignal/inAppMessages/internal/InAppMessage;)Z")
    getHasSubscribers = JavaMethod("()Z")

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/inAppMessages/internal/triggers/impl/TriggerController$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")