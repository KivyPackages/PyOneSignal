from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class AdwHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/AdwHomeBadger"
    __javaconstructor__ = [("()V", False)]
    INTENT_UPDATE_COUNTER = JavaStaticField("Ljava/lang/String;")
    PACKAGENAME = JavaStaticField("Ljava/lang/String;")
    CLASSNAME = JavaStaticField("Ljava/lang/String;")
    COUNT = JavaStaticField("Ljava/lang/String;")
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class ApexHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/ApexHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class AsusHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/AsusHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class DefaultBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/DefaultBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class EverythingMeHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/EverythingMeHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class HuaweiHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/HuaweiHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class LGHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/LGHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class NewHtcHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/NewHtcHomeBadger"
    __javaconstructor__ = [("()V", False)]
    INTENT_UPDATE_SHORTCUT = JavaStaticField("Ljava/lang/String;")
    INTENT_SET_NOTIFICATION = JavaStaticField("Ljava/lang/String;")
    PACKAGENAME = JavaStaticField("Ljava/lang/String;")
    COUNT = JavaStaticField("Ljava/lang/String;")
    EXTRA_COMPONENT = JavaStaticField("Ljava/lang/String;")
    EXTRA_COUNT = JavaStaticField("Ljava/lang/String;")
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class NovaHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/NovaHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class OPPOHomeBader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/OPPOHomeBader"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class SamsungHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/SamsungHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class SonyHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/SonyHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class VivoHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/VivoHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class XiaomiHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/XiaomiHomeBadger"
    __javaconstructor__ = [("()V", False)]
    INTENT_ACTION = JavaStaticField("Ljava/lang/String;")
    EXTRA_UPDATE_APP_COMPONENT_NAME = JavaStaticField("Ljava/lang/String;")
    EXTRA_UPDATE_APP_MSG_TEXT = JavaStaticField("Ljava/lang/String;")
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")

class ZukHomeBadger(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/notifications/internal/badges/impl/shortcutbadger/impl/ZukHomeBadger"
    __javaconstructor__ = [("()V", False)]
    getSupportLaunchers = JavaMethod("()Ljava/util/List;")
    executeBadge = JavaMethod("(Landroid/content/Context;Landroid/content/ComponentName;I)V")