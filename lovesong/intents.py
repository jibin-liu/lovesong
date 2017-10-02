from responses import build_response, build_speechlet_response
from responses import build_audio_play_response, build_audio_stop_response
import audio_player


def dispatch(intent_name, intent_request, session):
    """
    dispatch event based on request_type

    Inputs:
    - intent_name: string, in the choice of:
                   'PlayIntent',
                   'AMAZON.CancelIntent',
                   'AMAZON.StopIntent',
                   'AMAZON.HelpIntent',
                   'AMAZON.PauseIntent'
    - intent_request: dict, input request
    - session: dict, input session

    Returns:
    response dictionary
    """
    if intent_name == 'AMAZON.HelpIntent':
        return get_welcome_response()
    elif intent_name in ('AMAZON.CancelIntent', 'AMAZON.StopIntent'):
        return handle_session_end_request()
    elif intent_name == 'AMAZON.PauseIntent':
        return audio_player.stop()
    elif intent_name == 'AMAZON.ResumeIntent':
        return audio_player.play(intent_request, session)
    elif intent_name == 'PlayIntent':
        return audio_player.play(intent_request, session)
    else:
        raise ValueError('Unknown intent name: {}'.format(intent_name))


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Simply say play to start playing songs."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Sorry I didn't get that. Simply say play to start playing songs."
    should_end_session = False
    speechlet_response = build_speechlet_response(card_title, speech_output,
                                                  reprompt_text, should_end_session)

    return build_response(session_attributes, speechlet_response)


def handle_session_end_request():
    session_attributes = {}

    should_end_session = True
    speechlet_response = build_speechlet_response("End Session", "", "",
                                                  should_end_session)
    return build_response(session_attributes, speechlet_response)
