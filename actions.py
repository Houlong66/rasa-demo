from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk.forms import FormAction

import os
import requests
import datetime
import json

LOCATION_DIR = os.path.join(os.path.dirname(
    __file__), "data/lookup/location")
with open(LOCATION_DIR, "r", encoding="utf-8") as f:
    LOCATION_LIST = f.read().split()

VALID_DATES = ["今天", "明天", "后天"]

WEATHER_URL = "https://api.seniverse.com/v3/weather/daily.json"
WEATHER_KEY = "ShPXZfvJpV50RreWx"

CHITCHAT_URL = "http://api.qingyunke.com/api.php"
CHITCHAT_KEY = "free"

NEWS_URL = "http://v.juhe.cn/toutiao/index"
NEWS_KEY = "f8a1db86c30c46f1d487a422c75ed4b4"

def _text_to_date(date: Text):
    today = datetime.datetime.now()
    one_day = datetime.timedelta(days=1)

    if date == "今天":
        result_date = today.date()
    elif date == '明天':
        result_date = (today + one_day).date()
    elif date == "后天":
        result_date = (today + one_day*2).date()
    else:
        return None
    return result_date.isoformat()


class ActionChitchat(Action):
    def name(self) -> Text:
        return "action_chitchat"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_state = tracker.current_state()
        params_dict = {
            "key": CHITCHAT_KEY,
            "appid": 0,
            "msg": current_state["latest_message"]["text"]
        }
        request_result = requests.get(CHITCHAT_URL, params=params_dict).json()
        dispatcher.utter_message(request_result["content"])

class ActionResetAll(Action):
    """
    重置所有slot的action
    """

    def name(self) -> Text:
        return "action_reset_all"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [AllSlotsReset()]


class WeatherForm(FormAction):
    """
    查询的天气的表单
    必填的slot: [location, date]
    """

    def name(self) -> Text:
        return "weather_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["location", "date"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []

    def validate_date(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """验证date"""

        if value in VALID_DATES:
            return {"date": value}
        else:
            dispatcher.utter_message(template="utter_wrong_date")
            return {"date": None}

    def validate_location(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """验证location"""
        if value in LOCATION_LIST:
            return {"location": value}
        else:
            dispatcher.utter_message(template="utter_wrong_location")
            return {"location": None}


class SearchWeather(Action):
    def name(self) -> Text:
        return "search_weather"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("正在查询……")

        location = tracker.get_slot("location")
        date = tracker.get_slot("date")

        result_date = _text_to_date(date)
        # 检查时间有没有转换成功
        if not result_date:
            message = "抱歉，提供的时间有误"
            dispatcher.utter_message(message)
            return []

        request_result = requests.get(WEATHER_URL, params={
            "key": WEATHER_KEY,
            "location": location
        }, timeout=5).json()

        request_status = request_result.get("status", None)
        # 当请求接口有误时，会返回status字段，若没有则正常
        if request_status:
            message = "抱歉，天气查询接口有误"
            dispatcher.utter_message(message)
            return []

        request_daily = request_result["results"][0]["daily"]
        request_weather = [
            one for one in request_daily if one["date"] == result_date][0]
        message = "{}{}的天气：{}，{}，{}-{}度"
        dispatcher.utter_message(message.format(location, date, result_date,
                                                request_weather["text_day"], request_weather["low"], request_weather["high"]))
        return []

class ActionReportNews(Action):
    def name(self) -> Text:
        return "action_report_news"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        params_dict = {"key": NEWS_KEY}
        request_result = requests.get(NEWS_URL, params=params_dict).json()
        result = request_result.get("result", None)
        if not result:
            dispatcher.utter_message("新闻查询接口有误")
            return []
        result_data = result["data"]
        message = "\n".join(["{}. {}:\n{}".format(index+1, item["title"], item["url"]) for (index,item) in enumerate(result_data)])
        dispatcher.utter_message(message)
        return []