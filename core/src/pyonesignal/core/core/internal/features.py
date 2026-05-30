from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class FeatureActivationMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/features/FeatureActivationMode"
    IMMEDIATE = JavaStaticField("Lcom/onesignal/core/internal/features/FeatureActivationMode;")
    APP_STARTUP = JavaStaticField("Lcom/onesignal/core/internal/features/FeatureActivationMode;")
    values = JavaStaticMethod("()[Lcom/onesignal/core/internal/features/FeatureActivationMode;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/features/FeatureActivationMode;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    IMMEDIATE = JavaStaticField("Lcom/onesignal/core/internal/features/FeatureActivationMode;")
    APP_STARTUP = JavaStaticField("Lcom/onesignal/core/internal/features/FeatureActivationMode;")

class FeatureFlag(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/features/FeatureFlag"
    SDK_BACKGROUND_THREADING = JavaStaticField("Lcom/onesignal/core/internal/features/FeatureFlag;")
    SDK_IDENTITY_VERIFICATION = JavaStaticField("Lcom/onesignal/core/internal/features/FeatureFlag;")
    values = JavaStaticMethod("()[Lcom/onesignal/core/internal/features/FeatureFlag;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Lcom/onesignal/core/internal/features/FeatureFlag;")
    getKey = JavaMethod("()Ljava/lang/String;")
    getEntries = JavaStaticMethod("()Lkotlin/enums/EnumEntries;")
    getActivationMode = JavaMethod("()Lcom/onesignal/core/internal/features/FeatureActivationMode;")
    isEnabledIn = JavaMethod("(Ljava/util/Set;)Z")
    SDK_BACKGROUND_THREADING = JavaStaticField("Lcom/onesignal/core/internal/features/FeatureFlag;")
    SDK_IDENTITY_VERIFICATION = JavaStaticField("Lcom/onesignal/core/internal/features/FeatureFlag;")

class FeatureManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/features/FeatureManager"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/config/ConfigModelStore;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/features/FeatureManager$Companion;")
    isEnabled = JavaMethod("(Lcom/onesignal/core/internal/features/FeatureFlag;)Z")
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")
    onModelReplaced = JavaMultipleMethod([("(Lcom/onesignal/core/internal/config/ConfigModel;Ljava/lang/String;)V", False, False), ("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V", False, False)])
    enabledFeatureKeys = JavaMethod("()Ljava/util/List;")
    remoteFeatureFlagMetadata = JavaMethod("()Ljava/util/Map;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/features/FeatureManager$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]

    class WhenMappings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/features/FeatureManager$WhenMappings"
        $EnumSwitchMapping$0 = JavaStaticField("[I")
        $EnumSwitchMapping$1 = JavaStaticField("[I")

class IFeatureManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/features/IFeatureManager"
    isEnabled = JavaMethod("(Lcom/onesignal/core/internal/features/FeatureFlag;)Z")
    enabledFeatureKeys = JavaMethod("()Ljava/util/List;")
    remoteFeatureFlagMetadata = JavaMethod("()Ljava/util/Map;")