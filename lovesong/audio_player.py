from responses import build_response
from responses import build_audio_play_response, build_audio_stop_response

"""
need to save the state of audio player (use pickle?), with the infomation about
token, url, and offset

probably need a class?
"""


def dispatch(audio_play_type, audio_request, session):
    """
    dispatch event based on request_type

    Inputs:
    - intent_name: string, in the choice of:
                   'PlaybackStopped',

    - intent_request: dict, input request
    - session: dict, input session

    Returns:
    response dictionary
    """
    if audio_play_type == 'PlaybackStopped':
        return stop()


def play(intent_request, session):
    """ user provides bus information for tracking """
    # for now just hard-coded
    session_attributes = {}

    audio_item = {
        "stream": {
            "token": "12345",
            "url": "https://s3-us-west-1.amazonaws.com/love-songs/Marry+Me.mp3",
            "offsetInMilliseconds": 0
        }
    }

    audio_response = build_audio_play_response('AudioPlayer.Play',
                                               'REPLACE_ALL',
                                               audio_item)

    return build_response(session_attributes, audio_response)


def stop():
    return build_response({}, build_audio_stop_response())
