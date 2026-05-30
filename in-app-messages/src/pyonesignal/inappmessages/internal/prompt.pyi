from typing import Any, ClassVar, overload
from internal.prompt.impl.InAppMessagePrompt import InAppMessagePrompt

class IInAppMessagePromptFactory:
    def createPrompt(self, p0: str) -> InAppMessagePrompt: ...

from typing import Any, ClassVar, overload

class InAppMessagePromptTypes:
    INSTANCE: ClassVar["InAppMessagePromptTypes"]
    PUSH_PROMPT_KEY: ClassVar[str]
    LOCATION_PROMPT_KEY: ClassVar[str]

