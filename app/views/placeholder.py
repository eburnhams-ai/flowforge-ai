from components.empty_state import empty_state
from components.hero import hero


def render_placeholder(title: str, subtitle: str) -> None:
    hero(title, subtitle)
    empty_state(
        "Tool shell ready",
        "This page is connected to the FlowForge Core shell. The tool logic will be added after the UI foundation is finished.",
    )
