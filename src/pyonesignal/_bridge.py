import sys
import logging

logger = logging.getLogger("PyOneSignal")
if not logger.handlers:
    logging.basicConfig(level=logging.INFO)

is_android = hasattr(sys, "getandroidapilevel") or sys.platform == "android"

if is_android:
    from jnius import autoclass, PythonJavaClass, java_method

    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Context = PythonActivity.mActivity.getApplicationContext()

    JOneSignal = autoclass("com.onesignal.OneSignal")
    JString = autoclass("java.lang.String")

else:
    logger.warning(
        "PyOneSignal: Running off-device. Java bridge disabled. Methods will pass silently."
    )
    Context = None
    JOneSignal = None
    JString = None

    class PythonJavaClass:
        pass

    def java_method(*args, **kwargs):
        def decorator(func):
            return func
        return decorator

    def autoclass(*args, **kwargs):
        return None