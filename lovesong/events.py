from intents import IntentHandler


class EventHandler(object):
    """ class that handles events """
    def __init__(self):
        """ constructor """
        return

    def dispatch(self, request_type, request, session):
        """
        dispatch event based on request_type

        Inputs:
        - request_type: string, in the choice of 'new', launch', 'intent', 'end'.
        - request: dict, input request
        - session: dict, input session

        Returns:
        None
        """
        if request_type == 'new':
            self.on_session_started(request, session)
        elif request_type == 'launch':
            self.on_launch(request, session)
        elif request_type == 'intent':
            self.on_intent(request, session)
        elif request_type == 'end':
            self.on_session_ended(request, session)
        else:
            raise ValueError('Unknown request type: {}'.format(request_type))

    def on_session_started(self, session_started_request, session):
        """ Called when the session starts """
        return

    def on_launch(self, launch_request, session):
        """ Called when the user launches the skill without specifying what they
        want
        """
        # Dispatch to your skill's launch
        intent_handler = IntentHandler()
        intent_handler.get_welcome_response()

    def on_intent(self, intent_request, session):
        """ called when the user specifies an intent for this skill """
        intent = intent_request['intent']
        intent_name = intent_request['intent']['name']

        # Dispatch to the skill handlers
        intent_handler = IntentHandler()
        intent_handler.dispatch(intent_name, intent, session)

    def on_session_ended(self, session_ended_request, session):
        """ Called when the user ends the session.
        Is not called when the skill returns should_end_session=true
        """
        # add cleanup logic here
        intent_handler = IntentHandler()
        intent_handler.handle_session_end_request()
