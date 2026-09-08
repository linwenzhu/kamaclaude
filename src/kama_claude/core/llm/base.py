from __future__ import annotations

from typing import Protocol

from kama_claude.core.events.bus import EventBus
from kama_claude.core.llm.types import LlmResponse


class LLMProvider(Protocol):
    async def chat(
        self,
        messages: list[dict[str, object]],
        tool_schemas: list[dict[str, object]],
        bus: EventBus,
        run_id: str,
    ) -> LlmResponse: ...