from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class IRebuildUserService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/user/internal/builduser/IRebuildUserService"
    getRebuildOperationsIfCurrentUser = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/util/List;")