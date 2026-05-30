from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ModelStoreListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/listeners/ModelStoreListener"
    __javaconstructor__ = [("(Lcom/onesignal/common/modeling/IModelStore;Lcom/onesignal/core/internal/operations/IOperationRepo;)V", False)]
    bootstrap = JavaMethod("()V")
    close = JavaMethod("()V")
    onModelAdded = JavaMethod("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V")
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")
    onModelRemoved = JavaMethod("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V")
    getAddOperation = JavaMethod("(Lcom/onesignal/common/modeling/Model;)Lcom/onesignal/core/internal/operations/Operation;")
    getUpdateOperation = JavaMethod("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)Lcom/onesignal/core/internal/operations/Operation;")
    getRemoveOperation = JavaMethod("(Lcom/onesignal/common/modeling/Model;)Lcom/onesignal/core/internal/operations/Operation;")

class SingletonModelStoreListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/core/internal/operations/listeners/SingletonModelStoreListener"
    __javaconstructor__ = [("(Lcom/onesignal/common/modeling/ISingletonModelStore;Lcom/onesignal/core/internal/operations/IOperationRepo;)V", False)]
    bootstrap = JavaMethod("()V")
    close = JavaMethod("()V")
    onModelUpdated = JavaMethod("(Lcom/onesignal/common/modeling/ModelChangedArgs;Ljava/lang/String;)V")
    onModelReplaced = JavaMethod("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;)V")
    getUpdateOperation = JavaMethod("(Lcom/onesignal/common/modeling/Model;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;Ljava/lang/Object;)Lcom/onesignal/core/internal/operations/Operation;")
    getReplaceOperation = JavaMethod("(Lcom/onesignal/common/modeling/Model;)Lcom/onesignal/core/internal/operations/Operation;")