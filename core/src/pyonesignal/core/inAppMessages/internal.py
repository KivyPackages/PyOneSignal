from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class MisconfiguredIAMManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/MisconfiguredIAMManager"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/inAppMessages/internal/MisconfiguredIAMManager$Companion;")
    removeLifecycleListener = JavaMultipleMethod([("(Lcom/onesignal/inAppMessages/IInAppMessageLifecycleListener;)Ljava/lang/Void;", False, False), ("(Lcom/onesignal/inAppMessages/IInAppMessageLifecycleListener;)V", False, False)])
    getPaused = JavaMethod("()Z")
    setPaused = JavaMethod("(Z)V")
    addTrigger = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Void;", False, False)])
    addTriggers = JavaMultipleMethod([("(Ljava/util/Map;)Ljava/lang/Void;", False, False), ("(Ljava/util/Map;)V", False, False)])
    removeTrigger = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/Void;", False, False), ("(Ljava/lang/String;)V", False, False)])
    removeTriggers = JavaMultipleMethod([("(Ljava/util/Collection;)V", False, False), ("(Ljava/util/Collection;)Ljava/lang/Void;", False, False)])
    clearTriggers = JavaMultipleMethod([("()V", False, False), ("()Ljava/lang/Void;", False, False)])
    addLifecycleListener = JavaMultipleMethod([("(Lcom/onesignal/inAppMessages/IInAppMessageLifecycleListener;)Ljava/lang/Void;", False, False), ("(Lcom/onesignal/inAppMessages/IInAppMessageLifecycleListener;)V", False, False)])
    addClickListener = JavaMultipleMethod([("(Lcom/onesignal/inAppMessages/IInAppMessageClickListener;)Ljava/lang/Void;", False, False), ("(Lcom/onesignal/inAppMessages/IInAppMessageClickListener;)V", False, False)])
    removeClickListener = JavaMultipleMethod([("(Lcom/onesignal/inAppMessages/IInAppMessageClickListener;)Ljava/lang/Void;", False, False), ("(Lcom/onesignal/inAppMessages/IInAppMessageClickListener;)V", False, False)])

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/inAppMessages/internal/MisconfiguredIAMManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        access$getEXCEPTION = JavaStaticMethod("(Lcom/onesignal/inAppMessages/internal/MisconfiguredIAMManager$Companion;)Ljava/lang/Exception;")