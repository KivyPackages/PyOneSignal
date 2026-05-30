from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IUserStateObserver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/state/IUserStateObserver"
    onUserStateChange = JavaMethod("(Lcom/onesignal/user/state/UserChangedState;)V")

class UserChangedState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/state/UserChangedState"
    __javaconstructor__ = [("(Lcom/onesignal/user/state/UserState;)V", False)]
    getCurrent = JavaMethod("()Lcom/onesignal/user/state/UserState;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")

class UserState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/state/UserState"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    getOnesignalId = JavaMethod("()Ljava/lang/String;")
    getExternalId = JavaMethod("()Ljava/lang/String;")
    toJSONObject = JavaMethod("()Lorg/json/JSONObject;")