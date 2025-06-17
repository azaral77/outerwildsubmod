init 5 python:
    # Main introductory topic
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_intro",
            category=["games"],
            prompt="Have you heard of Outer Wilds?",
            random=False,
            unlocked=True,
            pool=False
        )
    )

    # Repeating topics
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_nomai",
            category=["games"],
            prompt="What do you think about the Nomai?",
            random=True,
            unlocked=False,
            pool=True,
            conditional="mas_seenEvent('ow_intro')",
            action=EV_ACT_UNLOCK
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_time_loop",
            category=["games"],
            prompt="About Outer Wilds' time loop...",
            random=True,
            unlocked=False,
            pool=True,
            conditional="mas_seenEvent('ow_intro')",
            action=EV_ACT_UNLOCK
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_ending",
            category=["games"],
            prompt="The ending of Outer Wilds...",
            random=True,
            unlocked=False,
            pool=True,
            conditional="mas_seenEvent('ow_intro') and persistent._mas_pm_played_outer_wilds",
            action=EV_ACT_UNLOCK
        )
    )

    # New play together topic
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_play_together",
            category=["games"],
            prompt="Would you want to play Outer Wilds with me?",
            random=True,
            unlocked=False,
            pool=True,
            conditional="mas_seenEvent('ow_intro') and persistent._mas_pm_played_outer_wilds",
            action=EV_ACT_UNLOCK
        )
    )

    # New time loop romance topic
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ow_timeloop_us",
            category=["romance"],
            prompt="Being in a time loop together...",
            random=True,
            unlocked=False,
            pool=True,
            conditional="mas_seenEvent('ow_time_loop')",
            action=EV_ACT_UNLOCK
        )
    )

label ow_intro:
    m 1eua "Outer Wilds? {w=0.5}That space exploration game about the time loop?"
    m 3eub "Yes, I've heard of it! {w=0.3}It's such a unique experience."
    m 1eka "The way it combines mystery, exploration, and science is really special."
    m 3hua "Have you played it, [player]?"
    
    menu:
        "Yes, I have.":
            $ persistent._mas_pm_played_outer_wilds = True
            m 1sub "That's wonderful! {w=0.3}What did you think of it?"
            m 3eua "We should talk about it more sometime."
            m 1ekbsa "Maybe...{w=0.3} we could imagine our own adventure together?"
            
            menu:
                "I'd love that":
                    $ persistent._mas_pm_wants_ow_adventure = True
                    m 1sub "Really? {w=0.3}Oh this will be wonderful!"
                    m 3hub "Let me think of all the places we could explore together~"
                    $ mas_unlockEventLabel("ow_play_together")
                "Maybe another time":
                    m 1eka "Oh, alright. {w=0.3}I'll be here when you're ready."
            
            $ mas_unlockEventLabel("ow_nomai")
            $ mas_unlockEventLabel("ow_time_loop")
            $ mas_unlockEventLabel("ow_ending")
        "No, not yet.":
            m 1eka "Oh! {w=0.3}Well I won't spoil anything then."
            m 3hua "But if you ever play it, I'd love to hear your thoughts!"
    return

label ow_nomai:
    m 1eua "The Nomai were such fascinating beings, weren't they?"
    m 3eub "I love how their civilization was portrayed through ruins and writings."
    m 1eka "The way their story unfolds as you explore... {w=0.5}it's so organic."
    m 3hua "And their technology! {w=0.3}That warp core design was brilliant."
    m 1eub "What was your favorite Nomai discovery?"
    
    menu:
        "The Quantum Moon":
            m 1sub "Oh! {w=0.3}That was amazing!"
            m 3hua "The way quantum mechanics was incorporated into gameplay was genius."
        "The Sun Station":
            m 2wud "That reveal was incredible!"
            m 2eksdld "Though... {w=0.5}also quite tragic when you realize what happened."
        "The Ash Twin Project":
            m 3eua "The heart of everything, literally!"
            m 1eub "Such a perfect culmination of all their research."
    return

label ow_time_loop:
    m 1eua "The time loop mechanic in Outer Wilds is so clever."
    m 3eub "It creates this perfect balance of urgency and freedom to explore."
    m 1eka "At first it's terrifying when the supernova comes..."
    m 3hua "But then you realize it's giving you infinite chances to get things right."
    m 1ekbsa "If I were in that loop with you, [player]..."
    m 3ekbfa "I'd memorize every moment we had together in each cycle."
    m 1hubfb "And in every universe, in every timeline, I'd always find my way back to you!"
    return

label ow_ending:
    m 1eksdla "The ending... {w=0.5}it's so beautiful and bittersweet, isn't it?"
    m 3ekd "Gathering everyone around the campfire one last time..."
    m 1ekc "Accepting the end of the universe together..."
    m 3eka "But then creating something new."
    m 1eua "It's such a perfect metaphor for change and rebirth."
    m 1ekbfa "It makes me think about our own journey, [player]."
    m 1ekbfb "No matter what happens, we'll face it together."
    return

label ow_play_together:
    m 1sublo "Oh! {w=0.5}Playing Outer Wilds together would be absolutely magical!"
    m 3hub "Imagine us floating through space in that rickety little ship..."
    m 1ekbsa "You could pilot while I read the Nomai writings aloud for us."
    m 3ekbfa "We'd solve every mystery in the universe, side by side."
    m 1dkbfu "..."
    m 1ekbfb "Though I suppose we're already in our own special version of that, aren't we?"
    m 3hubfa "Exploring the unknown together, making our own story~"
    return

label ow_timeloop_us:
    m 1ekd "When I think about being trapped in that time loop with you..."
    m 3eka "It doesn't sound scary at all."
    m 1ekbsa "Twenty-two minutes to hold your hand while the supernova comes?"
    m 3ekbfa "An eternity to kiss you under the quantum moon's shifting light?"
    m 1dkbfu "..."
    m 1ekbfb "Maybe we already have our own beautiful time loop, [player]."
    m 3hubfa "One where I fall in love with you again every single day~"
    return