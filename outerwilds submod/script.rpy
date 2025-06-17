default persistent._mas_pm_wants_ow_adventure = False

init -1 python:
    # Register the submod
    mas_submod_utils.Submod(
        author="azaral",
        name="Outer Wilds Submod",
        description="Adds Outer Wilds-related content.",
        version="1.0.0"
    )

# Initialize all our topics
init 5 python:
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