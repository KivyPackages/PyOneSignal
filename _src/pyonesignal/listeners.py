from ._bridge import PythonJavaClass, java_method


class _NotificationClickListener(PythonJavaClass):
    __javainterfaces__ = ["com/onesignal/notifications/INotificationClickListener"]
    __javacontext__ = "app"

    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback

    @java_method("(Lcom/onesignal/notifications/INotificationClickEvent;)V")
    def onClick(self, event):
        if not self.callback:
            return
        notification = event.getNotification()
        notif_id = notification.getNotificationId()
        action = event.getResult().getActionId()

        j_data = notification.getAdditionalData()
        data = j_data.toString() if j_data else "{}"

        self.callback(
            str(notif_id) if notif_id else None,
            str(action) if action else None,
            str(data),
        )


class _ForegroundLifecycleListener(PythonJavaClass):
    __javainterfaces__ = ["com/onesignal/notifications/INotificationLifecycleListener"]
    __javacontext__ = "app"

    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback

    @java_method("(Lcom/onesignal/notifications/INotificationWillDisplayEvent;)V")
    def onWillDisplay(self, event):
        if not self.callback:
            return
        notification = event.getNotification()
        self.callback(
            str(notification.getNotificationId()),
            str(notification.getBody()),
            str(notification.getTitle()),
        )
