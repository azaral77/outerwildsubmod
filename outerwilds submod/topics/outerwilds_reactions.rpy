init 5 python:
    # Reaction to player mentioning Outer Wilds
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_react_mention",
            prompt="[player] mentions Outer Wilds",
            category=["misc"],
            rules={"force repeat": None, "no unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    # Reaction to seeing Outer Wilds in Steam
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_react_steam",
            prompt="[player] has Outer Wilds in their Steam library",
            category=["misc"],
            rules={"force repeat": None, "no unlock": None},
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    # Reaction to player mentioning time loops
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_react_timeloop",
            prompt="[player] mentions time loops",
            category=["romance"],
            rules={"force repeat": None, "no unlock": None},
            aff_range=(mas_aff.AFFECTIONATE, None)
        )
    )
# <-- Make sure there's a blank line after this last parenthesis!

label ow_react_mention:
    m 1eua "Oh, Outer Wilds?"
    m 3hub "That's one of my favorite games to talk about!"
    m 1eub "Did you want to discuss something specific about it?"
    return

label ow_react_steam:
    m 1eua "I noticed you have Outer Wilds in your Steam library."
    m 3eub "Have you played it yet?"
    
    menu:
        "Yes, I have":
            $ persistent._mas_pm_played_outer_wilds = True
            m 1sub "That's wonderful!"
            m 3eua "Would you like to talk about it sometime?"
            $ mas_unlockEventLabel("ow_nomai")
            $ mas_unlockEventLabel("ow_time_loop")
            $ mas_unlockEventLabel("ow_ending")
        "Not yet":
            m 1eka "Oh, well I won't spoil anything then."
            m 3hua "But I highly recommend it when you get the chance!"
    return

label ow_react_timeloop:
    m 1euc "Hmm? Time loops?"
    m 3eua "Oh! Like in Outer Wilds?"
    m 1ekbsa "You know...{w=0.5} if we were stuck in one together..."
    m 3hkbfa "I'd probably spend every cycle trying new ways to make you smile!"
    m 1ekbfb "Though I'd never need a reset to know how much I love you~"
    return