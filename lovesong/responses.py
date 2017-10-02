def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': response
    }


def build_audio_play_response(directive_type, play_behavior, audio_item):
    return {
        'directives': [
            {
                'type': directive_type,
                'playBehavior': play_behavior,
                'audioItem': audio_item
            }
        ]
    }


def build_audio_stop_response():
    return {
        'directives': [
            {
                'type': 'AudioPlayer.Stop'
            }
        ]
    }
