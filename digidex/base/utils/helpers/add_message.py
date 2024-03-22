from django.contrib import messages

def show_message(request, message, message_type):
    """
    Shows a message with a given level.
    message_type should be one of 'success', 'info', 'warning', 'error', or 'debug'.
    """
    levels = {
        'success': messages.SUCCESS,
        'info': messages.INFO,
        'warning': messages.WARNING,
        'error': messages.ERROR,
        'debug': messages.DEBUG,
    }

    if message_type in levels:
        messages.add_message(request, levels[message_type], message)
    else:
        raise ValueError("Invalid message type provided.")
