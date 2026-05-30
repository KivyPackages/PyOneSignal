from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class BroadcastHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/util/BroadcastHelper"
    __javaconstructor__ = [("()V", False)]
    resolveBroadcast = JavaStaticMethod("(Landroid/content/Context;Landroid/content/Intent;)Ljava/util/List;")
    canResolveBroadcast = JavaStaticMethod("(Landroid/content/Context;Landroid/content/Intent;)Z")
    sendIntentExplicitly = JavaStaticMethod("(Landroid/content/Context;Landroid/content/Intent;)V")

class CloseHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/util/CloseHelper"
    __javaconstructor__ = [("()V", False)]
    close = JavaStaticMethod("(Landroid/database/Cursor;)V")
    closeQuietly = JavaStaticMethod("(Ljava/io/Closeable;)V")