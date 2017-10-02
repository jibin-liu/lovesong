import events


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    request, session = event['request'], event.get('session')
    context = event.get('context')

    # new session
    if session is not None:
        if session['new']:
            events.dispatch('new', request, session)

    # handling request
    # user says open
    if event['request']['type'] == "LaunchRequest":
        return events.dispatch('launch', request, session)
    # user says play, stop, cancel, etc.
    elif event['request']['type'] == "IntentRequest":
        return events.dispatch('intent', request, session)
    # user says quit
    elif event['request']['type'] == "SessionEndedRequest":
        return events.dispatch('end', request, session)
    # AudioPlayer requests
    elif event['request']['type'].startswith("AudioPlayer"):
        return events.dispatch('audio_player', request, context)


if __name__ == "__main__":
    import json
    import sys
    from pprint import pprint

    event = json.load(open(sys.argv[1]))

    pprint(lambda_handler(event, None))
