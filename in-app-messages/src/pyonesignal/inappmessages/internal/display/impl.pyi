from typing import Any, ClassVar, overload
from android.app.Activity import Activity
from internal.InAppMessage import InAppMessage
from internal.InAppMessageContent import InAppMessageContent
from internal.backend.IInAppBackendService import IInAppBackendService
from internal.lifecycle.IInAppLifecycleService import IInAppLifecycleService
from internal.prompt.IInAppMessagePromptFactory import IInAppMessagePromptFactory
from pyonesignal.core.internal.application.IApplicationService import IApplicationService
from pyonesignal.core.internal.config.ConfigModelStore import ConfigModelStore
from pyonesignal.core.internal.language.ILanguageContext import ILanguageContext
from pyonesignal.core.internal.time.ITime import ITime

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class IInfluenceManager:
    """Forward declaration for ``com.onesignal.session.internal.influence.IInfluenceManager``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('com.onesignal.session.internal.influence.IInfluenceManager')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.
    """
    ...
class Continuation:
    """Forward declaration for ``kotlin.coroutines.Continuation``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.coroutines.Continuation')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/coroutines/Continuation/
    """
    ...
class DefaultConstructorMarker:
    """Forward declaration for ``kotlin.jvm.internal.DefaultConstructorMarker``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by jni-wrap. At runtime pyjnius will hand you a
    live ``autoclass('kotlin.jvm.internal.DefaultConstructorMarker')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/jvm/internal/DefaultConstructorMarker/
    """
    ...

class InAppDisplayer:
    Companion: ClassVar[Any]
    def __init__(self, p0: IApplicationService, p1: IInAppLifecycleService, p2: IInAppMessagePromptFactory, p3: IInAppBackendService, p4: IInfluenceManager, p5: ConfigModelStore, p6: ILanguageContext, p7: ITime) -> None: ...
    def displayPreviewMessage(self, p0: str, p1: Continuation) -> Any: ...
    def displayMessage(self, p0: InAppMessage, p1: Continuation) -> Any: ...
    def dismissCurrentInAppMessage(self) -> None: ...
    @staticmethod
    def access$showMessageContent(p0: "InAppDisplayer", p1: InAppMessage, p2: InAppMessageContent, p3: Continuation) -> Any: ...
    @staticmethod
    def access$initInAppMessage(p0: "InAppDisplayer", p1: Activity, p2: InAppMessage, p3: InAppMessageContent, p4: Continuation) -> Any: ...

    class Companion:
        def __init__(self, p0: DefaultConstructorMarker) -> None: ...

from typing import Any, ClassVar, overload
from android.view.View import View

class OSPopupWindow:
    INPUT_METHOD_FROM_FOCUSABLE: ClassVar[int]
    INPUT_METHOD_NEEDED: ClassVar[int]
    INPUT_METHOD_NOT_NEEDED: ClassVar[int]
    def __init__(self, p0: View, p1: int, p2: int, p3: bool, p4: Any) -> None: ...
    def setWasDismissedManually(self, p0: bool) -> None: ...
    def dismiss(self) -> None: ...
    def getWasDismissedManually(self) -> bool: ...

    class PopupWindowListener:
        def onDismiss(self, p0: bool) -> None: ...

from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.util.Property import Property

class OSWebView:
    RENDERER_PRIORITY_BOUND: ClassVar[int]
    RENDERER_PRIORITY_IMPORTANT: ClassVar[int]
    RENDERER_PRIORITY_WAIVED: ClassVar[int]
    SCHEME_GEO: ClassVar[str]
    SCHEME_MAILTO: ClassVar[str]
    SCHEME_TEL: ClassVar[str]
    FOCUS_AFTER_DESCENDANTS: ClassVar[int]
    FOCUS_BEFORE_DESCENDANTS: ClassVar[int]
    FOCUS_BLOCK_DESCENDANTS: ClassVar[int]
    LAYOUT_MODE_CLIP_BOUNDS: ClassVar[int]
    LAYOUT_MODE_OPTICAL_BOUNDS: ClassVar[int]
    PERSISTENT_ALL_CACHES: ClassVar[int]
    PERSISTENT_ANIMATION_CACHE: ClassVar[int]
    PERSISTENT_NO_CACHE: ClassVar[int]
    PERSISTENT_SCROLLING_CACHE: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_AUTO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_NO: ClassVar[int]
    ACCESSIBILITY_DATA_SENSITIVE_YES: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_ASSERTIVE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_NONE: ClassVar[int]
    ACCESSIBILITY_LIVE_REGION_POLITE: ClassVar[int]
    ALPHA: ClassVar[Property]
    AUTOFILL_FLAG_INCLUDE_NOT_IMPORTANT_VIEWS: ClassVar[int]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DATE: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_DAY: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_MONTH: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_EXPIRATION_YEAR: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_NUMBER: ClassVar[str]
    AUTOFILL_HINT_CREDIT_CARD_SECURITY_CODE: ClassVar[str]
    AUTOFILL_HINT_EMAIL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_NAME: ClassVar[str]
    AUTOFILL_HINT_PASSWORD: ClassVar[str]
    AUTOFILL_HINT_PHONE: ClassVar[str]
    AUTOFILL_HINT_POSTAL_ADDRESS: ClassVar[str]
    AUTOFILL_HINT_POSTAL_CODE: ClassVar[str]
    AUTOFILL_HINT_USERNAME: ClassVar[str]
    AUTOFILL_TYPE_DATE: ClassVar[int]
    AUTOFILL_TYPE_LIST: ClassVar[int]
    AUTOFILL_TYPE_NONE: ClassVar[int]
    AUTOFILL_TYPE_TEXT: ClassVar[int]
    AUTOFILL_TYPE_TOGGLE: ClassVar[int]
    CONTENT_SENSITIVITY_AUTO: ClassVar[int]
    CONTENT_SENSITIVITY_NOT_SENSITIVE: ClassVar[int]
    CONTENT_SENSITIVITY_SENSITIVE: ClassVar[int]
    DRAG_FLAG_ACCESSIBILITY_ACTION: ClassVar[int]
    DRAG_FLAG_GLOBAL: ClassVar[int]
    DRAG_FLAG_GLOBAL_PERSISTABLE_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_PREFIX_URI_PERMISSION: ClassVar[int]
    DRAG_FLAG_GLOBAL_SAME_APPLICATION: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_READ: ClassVar[int]
    DRAG_FLAG_GLOBAL_URI_WRITE: ClassVar[int]
    DRAG_FLAG_HIDE_CALLING_TASK_ON_DRAG_START: ClassVar[int]
    DRAG_FLAG_OPAQUE: ClassVar[int]
    DRAG_FLAG_START_INTENT_SENDER_ON_UNHANDLED_DRAG: ClassVar[int]
    DRAWING_CACHE_QUALITY_AUTO: ClassVar[int]
    DRAWING_CACHE_QUALITY_HIGH: ClassVar[int]
    DRAWING_CACHE_QUALITY_LOW: ClassVar[int]
    FIND_VIEWS_WITH_CONTENT_DESCRIPTION: ClassVar[int]
    FIND_VIEWS_WITH_TEXT: ClassVar[int]
    FOCUSABLE: ClassVar[int]
    FOCUSABLES_ALL: ClassVar[int]
    FOCUSABLES_TOUCH_MODE: ClassVar[int]
    FOCUSABLE_AUTO: ClassVar[int]
    FOCUS_BACKWARD: ClassVar[int]
    FOCUS_DOWN: ClassVar[int]
    FOCUS_FORWARD: ClassVar[int]
    FOCUS_LEFT: ClassVar[int]
    FOCUS_RIGHT: ClassVar[int]
    FOCUS_UP: ClassVar[int]
    GONE: ClassVar[int]
    HAPTIC_FEEDBACK_ENABLED: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_AUTO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_NO_HIDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_ACCESSIBILITY_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_AUTO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES: ClassVar[int]
    IMPORTANT_FOR_AUTOFILL_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_AUTO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_NO_EXCLUDE_DESCENDANTS: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES: ClassVar[int]
    IMPORTANT_FOR_CONTENT_CAPTURE_YES_EXCLUDE_DESCENDANTS: ClassVar[int]
    INVISIBLE: ClassVar[int]
    KEEP_SCREEN_ON: ClassVar[int]
    LAYER_TYPE_HARDWARE: ClassVar[int]
    LAYER_TYPE_NONE: ClassVar[int]
    LAYER_TYPE_SOFTWARE: ClassVar[int]
    LAYOUT_DIRECTION_INHERIT: ClassVar[int]
    LAYOUT_DIRECTION_LOCALE: ClassVar[int]
    LAYOUT_DIRECTION_LTR: ClassVar[int]
    LAYOUT_DIRECTION_RTL: ClassVar[int]
    MEASURED_HEIGHT_STATE_SHIFT: ClassVar[int]
    MEASURED_SIZE_MASK: ClassVar[int]
    MEASURED_STATE_MASK: ClassVar[int]
    MEASURED_STATE_TOO_SMALL: ClassVar[int]
    NOT_FOCUSABLE: ClassVar[int]
    NO_ID: ClassVar[int]
    OVER_SCROLL_ALWAYS: ClassVar[int]
    OVER_SCROLL_IF_CONTENT_SCROLLS: ClassVar[int]
    OVER_SCROLL_NEVER: ClassVar[int]
    REQUESTED_FRAME_RATE_CATEGORY_DEFAULT: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_HIGH: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_LOW: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NORMAL: ClassVar[float]
    REQUESTED_FRAME_RATE_CATEGORY_NO_PREFERENCE: ClassVar[float]
    ROTATION: ClassVar[Property]
    ROTATION_X: ClassVar[Property]
    ROTATION_Y: ClassVar[Property]
    SCALE_X: ClassVar[Property]
    SCALE_Y: ClassVar[Property]
    SCREEN_STATE_OFF: ClassVar[int]
    SCREEN_STATE_ON: ClassVar[int]
    SCROLLBARS_INSIDE_INSET: ClassVar[int]
    SCROLLBARS_INSIDE_OVERLAY: ClassVar[int]
    SCROLLBARS_OUTSIDE_INSET: ClassVar[int]
    SCROLLBARS_OUTSIDE_OVERLAY: ClassVar[int]
    SCROLLBAR_POSITION_DEFAULT: ClassVar[int]
    SCROLLBAR_POSITION_LEFT: ClassVar[int]
    SCROLLBAR_POSITION_RIGHT: ClassVar[int]
    SCROLL_AXIS_HORIZONTAL: ClassVar[int]
    SCROLL_AXIS_NONE: ClassVar[int]
    SCROLL_AXIS_VERTICAL: ClassVar[int]
    SCROLL_CAPTURE_HINT_AUTO: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE: ClassVar[int]
    SCROLL_CAPTURE_HINT_EXCLUDE_DESCENDANTS: ClassVar[int]
    SCROLL_CAPTURE_HINT_INCLUDE: ClassVar[int]
    SCROLL_INDICATOR_BOTTOM: ClassVar[int]
    SCROLL_INDICATOR_END: ClassVar[int]
    SCROLL_INDICATOR_LEFT: ClassVar[int]
    SCROLL_INDICATOR_RIGHT: ClassVar[int]
    SCROLL_INDICATOR_START: ClassVar[int]
    SCROLL_INDICATOR_TOP: ClassVar[int]
    SOUND_EFFECTS_ENABLED: ClassVar[int]
    STATUS_BAR_HIDDEN: ClassVar[int]
    STATUS_BAR_VISIBLE: ClassVar[int]
    SYSTEM_UI_FLAG_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE: ClassVar[int]
    SYSTEM_UI_FLAG_IMMERSIVE_STICKY: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION: ClassVar[int]
    SYSTEM_UI_FLAG_LAYOUT_STABLE: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LIGHT_STATUS_BAR: ClassVar[int]
    SYSTEM_UI_FLAG_LOW_PROFILE: ClassVar[int]
    SYSTEM_UI_FLAG_VISIBLE: ClassVar[int]
    SYSTEM_UI_LAYOUT_FLAGS: ClassVar[int]
    TEXT_ALIGNMENT_CENTER: ClassVar[int]
    TEXT_ALIGNMENT_GRAVITY: ClassVar[int]
    TEXT_ALIGNMENT_INHERIT: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_END: ClassVar[int]
    TEXT_ALIGNMENT_TEXT_START: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_END: ClassVar[int]
    TEXT_ALIGNMENT_VIEW_START: ClassVar[int]
    TEXT_DIRECTION_ANY_RTL: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_LTR: ClassVar[int]
    TEXT_DIRECTION_FIRST_STRONG_RTL: ClassVar[int]
    TEXT_DIRECTION_INHERIT: ClassVar[int]
    TEXT_DIRECTION_LOCALE: ClassVar[int]
    TEXT_DIRECTION_LTR: ClassVar[int]
    TEXT_DIRECTION_RTL: ClassVar[int]
    TRANSLATION_X: ClassVar[Property]
    TRANSLATION_Y: ClassVar[Property]
    TRANSLATION_Z: ClassVar[Property]
    VISIBLE: ClassVar[int]
    X: ClassVar[Property]
    Y: ClassVar[Property]
    Z: ClassVar[Property]
    def __init__(self, p0: Context) -> None: ...
    def computeScroll(self) -> None: ...
    def overScrollBy(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: bool) -> bool: ...
    def scrollTo(self, p0: int, p1: int) -> None: ...

from typing import Any, ClassVar, overload
from android.animation.ValueAnimator import ValueAnimator
from android.view.View import View
from android.view.animation.Animation import Animation
from android.view.animation.Interpolator import Interpolator

class OneSignalAnimate:
    INSTANCE: ClassVar["OneSignalAnimate"]
    def animateViewByTranslation(self, p0: View, p1: float, p2: float, p3: int, p4: Interpolator, p5: Any) -> Animation: ...
    def animateViewSmallToLarge(self, p0: View, p1: int, p2: Interpolator, p3: Any) -> Animation: ...
    def animateViewColor(self, p0: View, p1: int, p2: int, p3: int, p4: Any) -> ValueAnimator: ...

from typing import Any, ClassVar, overload

class OneSignalBounceInterpolator:
    def __init__(self, p0: float, p1: float) -> None: ...
    def getInterpolation(self, p0: float) -> float: ...

