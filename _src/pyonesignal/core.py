from ._bridge import is_android, JOneSignal, Context, JString, Logger
from .user import UserManager
from .push import PushManager
from .notifications import NotificationsManager


class PyOneSignal:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PyOneSignal, cls).__new__(cls)
            cls._instance._setup()
        return cls._instance

    def _setup(self):
        self.is_initialized = False
        self.User = UserManager()
        self.Push = PushManager()
        self.Notifications = NotificationsManager()

    def initialize(self, app_id: str):
        """Initializes the OneSignal SDK. Must be called once at app startup."""
        if self.is_initialized:
            Logger.warning("PyOneSignal: Already initialized.")
            return

        if is_android:
            try:
                JOneSignal.initWithContext(Context, JString(app_id))
                self.is_initialized = True
                Logger.info("PyOneSignal: Initialization successful.")
            except Exception as e:
                Logger.error(f"PyOneSignal: Failed to initialize. {e}")
        else:
            self.is_initialized = True

    def set_consent_required(self, required: bool):
        """Delays SDK initialization until user consent is given (GDPR compliance)."""
        if is_android:
            JOneSignal.setConsentRequired(required)

    def set_consent_given(self, given: bool):
        """Provides the consent to proceed with SDK operations."""
        if is_android:
            JOneSignal.setConsentGiven(given)
