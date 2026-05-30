from typing import Any, ClassVar, overload
from internal.InAppMessage import InAppMessage
from pyonesignal.core.internal.language.ILanguageContext import ILanguageContext

class InAppHelper:
    INSTANCE: ClassVar["InAppHelper"]
    def variantIdForMessage(self, p0: InAppMessage, p1: ILanguageContext) -> str: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context

class OneSignalChromeTab:
    INSTANCE: ClassVar["OneSignalChromeTab"]
    def open$com_onesignal_inAppMessages(self, p0: str, p1: bool, p2: Context) -> bool: ...

