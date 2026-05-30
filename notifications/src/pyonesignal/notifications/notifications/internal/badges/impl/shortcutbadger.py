from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Badger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/Badger"
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")

class ShortcutBadgeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/ShortcutBadgeException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Exception;)V", False)]

class ShortcutBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/ShortcutBadger"
    applyCountOrThrow = JavaStaticMethod("(Landroid/content/Context;I)V")
    applyCount = JavaStaticMethod("(Landroid/content/Context;I)Z")
    removeCount = JavaStaticMethod("(Landroid/content/Context;)Z")
    removeCountOrThrow = JavaStaticMethod("(Landroid/content/Context;)V")
    isBadgeCounterSupported = JavaStaticMethod("(Landroid/content/Context;)Z")
    applyNotification = JavaStaticMethod("(Landroid/content/Context;Landroid/app/Notification;I)V")