from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IUserManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/IUserManager"
    getPushSubscription = JavaMethod("()Lcom/onesignal/user/subscriptions/IPushSubscription;")
    getOnesignalId = JavaMethod("()Ljava/lang/String;")
    getExternalId = JavaMethod("()Ljava/lang/String;")
    setLanguage = JavaMethod("(Ljava/lang/String;)V")
    addAlias = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    addAliases = JavaMethod("(Ljava/util/Map;)V")
    removeAlias = JavaMethod("(Ljava/lang/String;)V")
    removeAliases = JavaMethod("(Ljava/util/Collection;)V")
    addEmail = JavaMethod("(Ljava/lang/String;)V")
    removeEmail = JavaMethod("(Ljava/lang/String;)V")
    addSms = JavaMethod("(Ljava/lang/String;)V")
    removeSms = JavaMethod("(Ljava/lang/String;)V")
    addTag = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    addTags = JavaMethod("(Ljava/util/Map;)V")
    removeTag = JavaMethod("(Ljava/lang/String;)V")
    removeTags = JavaMethod("(Ljava/util/Collection;)V")
    getTags = JavaMethod("()Ljava/util/Map;")
    addObserver = JavaMethod("(Lcom/onesignal/user/state/IUserStateObserver;)V")
    removeObserver = JavaMethod("(Lcom/onesignal/user/state/IUserStateObserver;)V")
    trackEvent = JavaMethod("(Ljava/lang/String;Ljava/util/Map;)V")

    class DefaultImpls(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/user/IUserManager$DefaultImpls"
        trackEvent$default = JavaStaticMethod("(Lcom/onesignal/user/IUserManager;Ljava/lang/String;Ljava/util/Map;ILjava/lang/Object;)V")

class UserModule(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/UserModule"
    __javaconstructor__ = [("()V", False)]
    register = JavaMethod("(Lcom/onesignal/common/services/ServiceBuilder;)V")