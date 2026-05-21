from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import mainthread

# Import your PyOneSignal singleton
from pyonesignal import onesignal

# Replace with your actual OneSignal App ID
ONESIGNAL_APP_ID = "YOUR-ONESIGNAL-APP-ID-HERE"

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15)

        self.status_label = Label(
            text="Waiting for Notifications...", 
            halign="center", 
            valign="middle",
            text_size=(400, None)
        )
        self.add_widget(self.status_label)

        btn_permission = Button(text="Request Push Permission", size_hint_y=0.2)
        btn_permission.bind(on_release=lambda x: onesignal.Notifications.request_permission())
        self.add_widget(btn_permission)

        btn_login = Button(text="Login as 'user_123'", size_hint_y=0.2)
        btn_login.bind(on_release=lambda x: onesignal.User.login("user_123"))
        self.add_widget(btn_login)

        btn_tag = Button(text="Add Tag (account_type: premium)", size_hint_y=0.2)
        btn_tag.bind(on_release=lambda x: onesignal.User.add_tags({"account_type": "premium"}))
        self.add_widget(btn_tag)

        btn_optout = Button(text="Opt Out of Push", size_hint_y=0.2)
        btn_optout.bind(on_release=lambda x: onesignal.Push.opt_out())
        self.add_widget(btn_optout)

    @mainthread
    def update_status(self, text):
        """Safely updates the UI from a background Java thread."""
        self.status_label.text = text


class MyApp(App):
    def build(self):
        self.layout = MainLayout()
        return self.layout

    def on_start(self):
        """Initialize OneSignal when the app fully starts."""

        # 1. Initialize the SDK
        onesignal.initialize(ONESIGNAL_APP_ID)

        # 2. Bind the event listeners
        onesignal.Notifications.set_click_listener(self.on_notification_clicked)
        onesignal.Notifications.set_foreground_listener(self.on_notification_received)

    def on_notification_clicked(self, notif_id, action_id, data_json):
        """Fires when the user taps a notification in the system tray."""
        msg = f"Notification Clicked!\nID: {notif_id}\nAction: {action_id}\nData: {data_json}"
        print(msg)
        # Update UI safely
        self.layout.update_status(msg)

    def on_notification_received(self, notif_id, body, title):
        """Fires when a notification arrives while the app is actively on screen."""
        msg = f"Foreground Notification!\nTitle: {title}\nBody: {body}"
        print(msg)
        # Update UI safely
        self.layout.update_status(msg)

if __name__ == '__main__':
    MyApp().run()