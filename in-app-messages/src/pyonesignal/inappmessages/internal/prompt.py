from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IInAppMessagePromptFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/prompt/IInAppMessagePromptFactory"
    createPrompt = JavaMethod("(Ljava/lang/String;)Lcom/onesignal/inAppMessages/internal/prompt/impl/InAppMessagePrompt;")

class InAppMessagePromptTypes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/inAppMessages/internal/prompt/InAppMessagePromptTypes"
    INSTANCE = JavaStaticField("Lcom/onesignal/inAppMessages/internal/prompt/InAppMessagePromptTypes;")
    PUSH_PROMPT_KEY = JavaStaticField("Ljava/lang/String;")
    LOCATION_PROMPT_KEY = JavaStaticField("Ljava/lang/String;")