def slots_creation_entrypoint():
    import slots

    slot_creation_functions = [
        function
        for func_name, function in slots.__dict__.items()
        if func_name.startswith("make") and func_name.endswith("slot")
    ]

    for function in slot_creation_functions:
        function()


def intents_creation_entrypoint():
    import intents

    for func_name, function in intents.__dict__.items():
        if func_name.startswith("make") and func_name.endswith("intent"):
            function()


def bot_creation_entrypoint():
    import bot

    for func_name, function in bot.__dict__.items():
        if func_name.startswith("make") and func_name.endswith("bot"):
            function()


if __name__ == "__main__":
    slots_creation_entrypoint()
    intents_creation_entrypoint()
    bot_creation_entrypoint()
