import intents
import audio_player


def dispatch(request_type, request, session_or_context):
    """
    dispatch event based on request_type

    Inputs:
    - request_type: string, in the choice of 'new', launch', 'intent', 'end'.
    - request: dict, input request
    - session_or_context: dict, input session_or_context

    Returns:
    None
    """
    if request_type == 'new':
        return on_session_started(request, session_or_context)
    elif request_type == 'launch':
        return on_launch(request, session_or_context)
    elif request_type == 'intent':
        return on_intent(request, session_or_context)
    elif request_type == 'audio_player':
        return on_audio_palyer(request, session_or_context)
    elif request_type == 'end':
        return on_session_ended(request, session_or_context)
    else:
        raise ValueError('Unknown request type: {}'.format(request_type))


def on_session_started(session_started_request, session):
    """ Called when the session starts """
    applicationId = session['application']['applicationId']
    print("event.session.application.applicationId=" + applicationId)


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch
    return intents.get_welcome_response()


def on_intent(intent_request, session):
    """ called when the user specifies an intent for this skill """
    intent = intent_request['intent']
    intent_name = intent['name']

    # Dispatch to the skill handlers
    return intents.dispatch(intent_name, intent, session)


def on_audio_palyer(audio_request, session):
    audio_request_type = audio_request['type'].split('.')[1]

    # Dispatch to the audio player handlers
    return audio_player.dispatch(audio_request_type, audio_request, session)


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    # add cleanup logic here
    return intents.handle_session_end_request()
