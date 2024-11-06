# app/context_manager.py

def manage_context(context, new_response):
    # Maintain simple conversation history for demonstration
    if context:
        return f"{context['context']} ... {new_response}"
    return new_response
