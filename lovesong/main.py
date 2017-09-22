from events import EventHandler


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    event_handler = EventHandler()
    request, session = event['request'], event['session']

    if event['session']['new']:
        event_handler.dispatch('new', request, session)

    if event['request']['type'] == "LaunchRequest":
        return event_handler.dispatch('launch', request, session)
    elif event['request']['type'] == "IntentRequest":
        return event_handler.dispatch('intent', request, session)
    elif event['request']['type'] == "SessionEndedRequest":
        return event_handler.dispatch('end', request, session)


if __name__ == "__main__":
    import json
    event = json.loads("""{
          "session": {
            "new": true,
            "sessionId": "SessionId.9c7f8652-4e46-4616-b3a6-320eac6d0e57",
            "application": {
              "applicationId": "amzn1.ask.skill.94942d5c-03ad-4efc-80ea-9f8b33ac7426"
            },
            "attributes": {},
            "user": {
              "userId": "amzn1.ask.account.AGIX4LSXCAHJM7EDNJMLXGUNPPU4WWNP5R2VKPSUA37Z5CSIZLD4YML3CQT2OSZGDUHL3M6USWCXE7HHPNQWQCEL5G6XEYZMRG6GKANNTNEZPACN662BHOCZH2ZBHPIH6B232UBSXHR5L445PLO4YZXP3J6VTA4BRQIRDDQYEZ6TQKSGZ2BN7FJM4QNJVCV4G2544BRZ54KP4IQ"
            }
          },
          "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.1d9e326a-1ac2-4982-b3f8-3b39b4a8d7ef",
            "intent": {
              "name": "PlayIntent",
              "slots": {}
            },
            "locale": "en-US",
            "timestamp": "2017-09-22T06:17:54Z"
          },
          "context": {
            "AudioPlayer": {
              "playerActivity": "IDLE"
            },
            "System": {
              "application": {
                "applicationId": "amzn1.ask.skill.94942d5c-03ad-4efc-80ea-9f8b33ac7426"
              },
              "user": {
                "userId": "amzn1.ask.account.AGIX4LSXCAHJM7EDNJMLXGUNPPU4WWNP5R2VKPSUA37Z5CSIZLD4YML3CQT2OSZGDUHL3M6USWCXE7HHPNQWQCEL5G6XEYZMRG6GKANNTNEZPACN662BHOCZH2ZBHPIH6B232UBSXHR5L445PLO4YZXP3J6VTA4BRQIRDDQYEZ6TQKSGZ2BN7FJM4QNJVCV4G2544BRZ54KP4IQ"
              },
              "device": {
                "supportedInterfaces": {}
              }
            }
          },
          "version": "1.0"
        }""")

    lambda_handler(event, None)
