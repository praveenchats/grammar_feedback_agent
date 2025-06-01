from typing import Dict, Any
from .analyzer import grammar_check

def grammar_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Node that performs grammar analysis on the input text.

    Args:
        state (Dict[str, Any]): The state dictionary containing 'text'.

    Returns:
        Dict[str, Any]: The updated state with grammar suggestions.
    """
    text = state["text"]
    suggestions = grammar_check(text)
    state["grammar"] = suggestions
    return state