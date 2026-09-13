"""Provider adapter layer: one interface, swappable backends (Gemini, Azure OpenAI).

Design decision: swapping providers should mean editing this file only.
Trade-off accepted: no provider-specific niche features.
"""

from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        ...


class GeminiProvider(LLMProvider):
    def generate(self, prompt: str, **kwargs) -> str:
        # TODO(day 15): wire up Gemini client.
        raise NotImplementedError("GeminiProvider.generate: not implemented yet (day 15)")


class AzureOpenAIProvider(LLMProvider):
    def generate(self, prompt: str, **kwargs) -> str:
        # TODO: wire up Azure OpenAI client.
        raise NotImplementedError("AzureOpenAIProvider.generate: not implemented yet")


def get_provider(name: str) -> LLMProvider:
    providers = {
        "gemini": GeminiProvider,
        "azure_openai": AzureOpenAIProvider,
    }
    if name not in providers:
        raise ValueError(f"unknown provider: {name}")
    return providers[name]()
