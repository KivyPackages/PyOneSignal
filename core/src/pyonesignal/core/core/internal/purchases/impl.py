from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class TrackGooglePurchase(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/purchases/impl/TrackGooglePurchase"
    __javaconstructor__ = [("(Lcom/onesignal/core/internal/application/IApplicationService;Lcom/onesignal/core/internal/preferences/IPreferencesService;Lcom/onesignal/core/internal/operations/IOperationRepo;Lcom/onesignal/core/internal/config/ConfigModelStore;Lcom/onesignal/user/internal/identity/IdentityModelStore;)V", False)]
    Companion = JavaStaticField("Lcom/onesignal/core/internal/purchases/impl/TrackGooglePurchase$Companion;")
    start = JavaMethod("()V")
    access$setIapEnabled$cp = JavaStaticMethod("(I)V")
    access$setMIInAppBillingService$p = JavaStaticMethod("(Lcom/onesignal/core/internal/purchases/impl/TrackGooglePurchase;Ljava/lang/Object;)V")
    access$queryBoughtItems = JavaStaticMethod("(Lcom/onesignal/core/internal/purchases/impl/TrackGooglePurchase;)V")
    access$getIapEnabled$cp = JavaStaticMethod("()I")
    access$setIInAppBillingServiceClass$cp = JavaStaticMethod("(Ljava/lang/Class;)V")
    onFocus = JavaMethod("(Z)V")
    onUnfocused = JavaMethod("()V")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/core/internal/purchases/impl/TrackGooglePurchase$Companion"
        __javaconstructor__ = [("(Lkotlin/jvm/internal/DefaultConstructorMarker;)V", False)]
        canTrack = JavaMethod("(Landroid/content/Context;)Z")
        access$getGetSkuDetailsMethod = JavaStaticMethod("(Lcom/onesignal/core/internal/purchases/impl/TrackGooglePurchase$Companion;Ljava/lang/Class;)Ljava/lang/reflect/Method;")
        access$getGetPurchasesMethod = JavaStaticMethod("(Lcom/onesignal/core/internal/purchases/impl/TrackGooglePurchase$Companion;Ljava/lang/Class;)Ljava/lang/reflect/Method;")
        access$getAsInterfaceMethod = JavaStaticMethod("(Lcom/onesignal/core/internal/purchases/impl/TrackGooglePurchase$Companion;Ljava/lang/Class;)Ljava/lang/reflect/Method;")