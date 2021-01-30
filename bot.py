import re


def make_MedicalCenterBot_bot():
    print("6a. Now I will read every intent in the intents file.")
    print(
        f"6b. We will now get the names straight from the module, transform them into dicts and print them."
    )
    bot_intents = [format_for_aws(intent_name) for intent_name in intent_names()]
    for intent in bot_intents:
        print(intent)


def format_for_aws(intent_name):
    return {"name": intent_name}


def intent_names():
    regex = r"make_([A-Za-z]+)_intent"
    import intents

    return [
        re.match(regex, intent_name).group(1)
        for intent_name in intents.__dict__
        if intent_name.startswith("make") and intent_name.endswith("intent")
    ]
