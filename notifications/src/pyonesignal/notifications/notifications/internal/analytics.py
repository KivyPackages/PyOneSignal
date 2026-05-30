from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IAnalyticsTracker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/analytics/IAnalyticsTracker"
    trackReceivedEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    trackInfluenceOpenEvent = JavaMethod("()V")
    trackOpenedEvent = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")