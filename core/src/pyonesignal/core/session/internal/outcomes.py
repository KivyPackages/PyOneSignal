from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IOutcomeEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/IOutcomeEvent"
    getTimestamp = JavaMethod("()J")
    getSession = JavaMethod("()Lcom/onesignal/session/internal/influence/InfluenceType;")
    getName = JavaMethod("()Ljava/lang/String;")
    getNotificationIds = JavaMethod("()Lorg/json/JSONArray;")
    getSessionTime = JavaMethod("()J")
    getWeight = JavaMethod("()F")

class IOutcomeEventsController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/session/internal/outcomes/IOutcomeEventsController"
    sendUniqueOutcomeEvent = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendSessionEndOutcomeEvent = JavaMethod("(JLkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendOutcomeEvent = JavaMethod("(Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;")
    sendOutcomeEventWithValue = JavaMethod("(Ljava/lang/String;FLkotlin/coroutines/Continuation;)Ljava/lang/Object;")