from ._bridge import is_android, JOneSignal, Logger


class PushManager:
    """Manages device push notification subscriptions (Opt-in / Opt-out)."""

    @property
    def _sub(self):
        return JOneSignal.getUser().getPushSubscription() if is_android else None

    def opt_in(self):
        """Explicitly opts the user in to push notifications."""
        if is_android:
            self._sub.optIn()
            Logger.info("PyOneSignal: Opted IN to push.")

    def opt_out(self):
        """Explicitly opts the user out of push notifications."""
        if is_android:
            self._sub.optOut()
            Logger.info("PyOneSignal: Opted OUT of push.")

    def get_id(self) -> str:
        """Returns the OneSignal Push Subscription ID."""
        if is_android:
            sub_id = self._sub.getId()
            return str(sub_id) if sub_id else ""
        return ""

    def get_token(self) -> str:
        """Returns the underlying FCM/GCM device token."""
        if is_android:
            token = self._sub.getToken()
            return str(token) if token else ""
        return ""

    def is_opted_in(self) -> bool:
        """Checks if the user is currently opted in."""
        if is_android:
            return self._sub.getOptedIn()
        return False
