from ._bridge import is_android, JOneSignal, JString, Logger


class UserManager:
    """Manages user state, aliases, tags, emails, and SMS."""

    @property
    def _user(self):
        return JOneSignal.getUser() if is_android else None

    def login(self, external_id: str):
        """Logs the user in with your backend's user ID."""
        if is_android:
            JOneSignal.login(JString(external_id))
            Logger.info(f"PyOneSignal: Logged in as {external_id}")

    def logout(self):
        """Logs the user out, reverting to an anonymous user."""
        if is_android:
            JOneSignal.logout()
            Logger.info("PyOneSignal: Logged out.")

    def add_tag(self, key: str, value: str):
        """Adds a single data tag to the user."""
        if is_android:
            self._user.addTag(JString(key), JString(value))

    def add_tags(self, tags: dict):
        """Adds multiple tags from a Python dictionary."""
        for k, v in tags.items():
            self.add_tag(str(k), str(v))

    def remove_tag(self, key: str):
        """Removes a single tag."""
        if is_android:
            self._user.removeTag(JString(key))

    def add_email(self, email: str):
        """Adds an email address to the current user."""
        if is_android:
            self._user.addEmail(JString(email))

    def remove_email(self, email: str):
        """Removes an email address from the current user."""
        if is_android:
            self._user.removeEmail(JString(email))
