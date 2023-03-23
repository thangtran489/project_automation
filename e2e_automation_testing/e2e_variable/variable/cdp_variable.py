from datetime import timedelta
from typing import Any, Optional, Union

# import variablefile
from robot.api.deco import library
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


@library
class TitleSegment:
    def __init__(self):
        self.live_segment = "Live Segment"
        self.historical_segment = "Historical Segment"
        self.live_and_historical_segment = "Live Segment with Historical Backfill"


@library
class ConditionName:
    def __init__(self):
        self.funnel_event = "Performed a Funnel of Events"
        self.performed_event = "Performed an Event"
        self.part_segment = "Part of a Segment"
        self.trait = "Have a Trait"
        self.ptrait = "Have a p-Trait"
