from responses import build_response, build_speechlet_response, build_audio_response


class IntentHandler(object):
    """ class that handles intent requests """
    def __init__(self):
        """ constructor """
        return

    def dispatch(self, intent_name, intent_request, session):
        """
        dispatch event based on request_type

        Inputs:
        - intent_name: string, in the choice of:
                       'PlayIntent',
                       'AMAZON.CancelIntent',
                       'AMAZON.StopIntent',
                       'AMAZON.HelpIntent'
        - intent_request: dict, input request
        - session: dict, input session

        Returns:
        response dictionary
        """
        if intent_name == 'AMAZON.HelpIntent':
            self.get_welcome_response()
        elif intent_name in ('AMAZON.CancelIntent' or 'AMAZON.StopIntent'):
            self.handle_session_end_request(intent_request, session)
        elif intent_name == 'PlayIntent':
            self.play_songs(intent_request, session)
        else:
            raise ValueError('Unknown intent name: {}'.format(intent_name))

    def get_welcome_response(self):
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

    def play_songs(self, intent_request, session):
        """ user provides bus information for tracking """
        # for now just hard-coded and assume my own bus
        session_attributes = {}

        audio_item = {
            "stream": {
                "token": "12345",
                "url": "https://s3-us-west-1.amazonaws.com/love-songs/Marry+Me.mp3",
                "offsetInMilliseconds": 0
            }
        }

        audio_response = build_audio_response('AudioPlayer.Play', 'REPLACE_ALL',
                                              audio_item)

        return build_response(session_attributes, audio_response)

    def handle_session_end_request(self):
        card_title = "Session Ended"
        speech_output = "Bye, love you"
        should_end_session = True
        speechlet_response = build_speechlet_response(card_title, speech_output,
                                                      None, should_end_session)
        return build_response({}, speechlet_response)
