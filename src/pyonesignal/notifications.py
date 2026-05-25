from ._bridge import is_android, JOneSignal
from .listeners import _NotificationClickListener, _ForegroundLifecycleListener


class NotificationsManager:
    """Manages notification permissions and lifecycle events."""

    def __init__(self):
        self._click_listener = None
        self._foreground_listener = None

    @property
    def _notif(self):
        return JOneSignal.getNotifications() if is_android else None

    def request_permission(self, fallback_to_settings: bool = True):
        """Prompts the Android 13+ Push Permission dialog."""
        if is_android:
            from jnius import autoclass
            JContinue = autoclass("com.onesignal.Continue")
            self._notif.requestPermission(fallback_to_settings, JContinue.none())

    def has_permission(self) -> bool:
        """Returns True if the user has granted OS-level push permissions."""
        if is_android:
            return self._notif.getPermission()
        return False

    def clear_all(self):
        """Clears all OneSignal notifications from the device tray."""
        if is_android:
            self._notif.clearAll()

    def set_click_listener(self, callback):
        """
        Callback signature: def on_click(notification_id: str, action_id: str, data_json: str)
        """
        if not is_android:
            return
        self.remove_click_listener()  # Prevent duplicates
        self._click_listener = _NotificationClickListener(callback)
        self._notif.addClickListener(self._click_listener)

    def remove_click_listener(self):
        if is_android and self._click_listener:
            self._notif.removeClickListener(self._click_listener)
            self._click_listener = None

    def set_foreground_listener(self, callback):
        """
        Callback signature: def on_foreground(notification_id: str, body: str, title: str)
        """
        if not is_android:
            return
        self.remove_foreground_listener()
        self._foreground_listener = _ForegroundLifecycleListener(callback)
        self._notif.addForegroundLifecycleListener(self._foreground_listener)

    def remove_foreground_listener(self):
        if is_android and self._foreground_listener:
            self._notif.removeForegroundLifecycleListener(self._foreground_listener)
            self._foreground_listener = None
