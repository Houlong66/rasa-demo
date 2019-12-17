## greet_story
* greet
    - utter_greet

## goodbye_story
* goodbye
    - utter_goodbye

## help_sotry
* help
    - utter_what_can_do

## chitchat_story
* chitchat
    - action_chitchat
* chitchat
	- action_chitchat
* chitchat
	- action_chitchat

## happy_path_all
* greet
    - utter_greet
* help
    - utter_what_can_do
* query_provider{"location":"广州", "date":"明天", "query_type":"天气"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name": "weather_form"}
    - form{"name": null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## happy_path_location
* query_provider{"location":"武汉", "query_type":"天气"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name": "weather_form"}
    - form{"name": null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## happy_path_date
* query_provider{"date":"今天", "query_type":"天气"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name": "weather_form"}
    - form{"name": null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## unhappy_path_date

* query_provider{"date":"明天","query_type":"天气"}
    - slot{"date":"明天"}
    - slot{"query_type":"天气"}
    - weather_form
    - slot{"requested_slot":"location"}
* goodbye
    - action_chitchat
    - weather_form
    - slot{"requested_slot":"location"}
* chitchat
	- action_chitchat
    - weather_form
    - slot{"requested_slot":"location"}
* inform{"location":"广州"}
    - slot{"location":"广州"}
    - weather_form
    - slot{"location":"广州"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## unhappy_path_location

* greet
    - utter_greet
* query_provider{"location":"广州","query_type":"天气"}
    - slot{"location":"广州"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"location":"广州"}
    - slot{"location":"广州"}
    - slot{"requested_slot":"date"}
* greet
	- action_chitchat
    - weather_form
    - slot{"requested_slot":"date"}
* chitchat
	- action_chitchat
    - slot{"location":"广州"}
    - slot{"query_type":"天气"}
    - weather_form
    - slot{"requested_slot":"date"}
* inform{"date":"明天"}
    - slot{"date":"明天"}
    - weather_form
    - slot{"date":"明天"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## new_unhappy_201912132134

* greet
    - utter_greet
* query_provider{"date":"明天","query_type":"天气"}
    - slot{"date":"明天"}
    - slot{"query_type":"天气"}
    - slot{"date":"明天"}
    - slot{"query_type":"天气"}
* goodbye
    - action_chitchat
    - weather_form
    - slot{"requested_slot":"location"}
* goodbye
    - action_chitchat
    - weather_form
    - slot{"requested_slot":"location"}
* inform{"location":"广州"}
    - slot{"location":"广州"}
    - weather_form
    - slot{"location":"广州"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* query_provider{"location":"北京","query_type":"天气"}
    - slot{"location":"北京"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"location":"北京"}
    - slot{"location":"北京"}
    - slot{"requested_slot":"date"}
* goodbye
    - action_chitchat
    - weather_form
    - slot{"requested_slot":"date"}
* inform{"date":"后天","location":"吧"}
    - slot{"date":"后天"}
    - slot{"location":"吧"}
    - weather_form
    - slot{"location":null}
    - slot{"date":"后天"}
    - slot{"requested_slot":"location"}
* inform{"location":"北京"}
    - slot{"location":"北京"}
    - weather_form
    - slot{"location":"北京"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## new_happy_201912132143

* greet
    - utter_greet
* query_provider{"location":"广州","query_type":"天气"}
    - slot{"location":"广州"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"location":"广州"}
    - slot{"location":"广州"}
    - slot{"requested_slot":"date"}
* inform{"date":"明天"}
    - slot{"date":"明天"}
    - weather_form
    - slot{"date":"明天"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* inform{"location":"北京"}
    - slot{"location":"北京"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"location":"北京"}
    - slot{"location":"北京"}
    - slot{"requested_slot":"date"}
* inform{"date":"后天"}
    - slot{"date":"后天"}
    - weather_form
    - slot{"date":"后天"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_greet
* query_provider{"date":"明天","query_type":"天气"}
    - slot{"date":"明天"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"date":"明天"}
    - slot{"date":"明天"}
    - slot{"requested_slot":"location"}
* inform{"location":"广州"}
    - slot{"location":"广州"}
    - weather_form
    - slot{"location":"广州"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## New Story

* query_provider{"location":"广州","query_type":"天气"}
    - slot{"location":"广州"}
    - slot{"query_type":"天气"}
    - weather_form
    - slot{"requested_slot":"date"}
* chitchat
    - action_chitchat
    - weather_form
    - slot{"requested_slot":"date"}
* chitchat
    - action_chitchat
    - weather_form
    - slot{"requested_slot":"date"}
* inform{"date":"明天"}
    - slot{"date":"明天"}
    - weather_form
    - slot{"date":"明天"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## New Story

* query_provider{"date":"明天","query_type":"天气"}
    - slot{"date":"明天"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"date":"明天"}
    - slot{"date":"明天"}
    - slot{"requested_slot":"location"}
* chitchat
    - action_chitchat
    - weather_form
    - slot{"requested_slot":"location"}
* inform{"location":"广州"}
    - slot{"location":"广州"}
    - weather_form
    - slot{"location":"广州"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* chitchat
    - utter_unkown
* query_provider{"location":"厦门","query_type":"天气"}
    - slot{"location":"厦门"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"location":"厦门"}
    - slot{"location":"厦门"}
    - slot{"requested_slot":"date"}
* inform{"date":"后天"}
    - slot{"date":"后天"}
    - weather_form
    - slot{"date":"后天"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_greet
* chitchat
    - action_chitchat
* chitchat
    - action_chitchat
* goodbye
    - utter_unkown
* goodbye
    - utter_goodbye

## New Story

* goodbye
    - utter_goodbye
* chitchat
    - action_chitchat
* goodbye
    - utter_unkown

## New Story

* query_provider{"date":"明天","query_type":"天气"}
    - slot{"date":"明天"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"date":"明天"}
    - slot{"date":"明天"}
    - slot{"requested_slot":"location"}
* chitchat
    - action_chitchat
    - weather_form
    - slot{"requested_slot":"location"}
* chitchat
    - action_chitchat
    - weather_form
    - slot{"requested_slot":"location"}
* inform{"location":"广州"}
    - slot{"location":"广州"}
    - weather_form
    - slot{"location":"广州"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* inform{"location":"北京"}
    - slot{"location":"北京"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"location":"北京"}
    - slot{"location":"北京"}
    - slot{"requested_slot":"date"}
* inform{"date":"后天"}
    - slot{"date":"后天"}
    - weather_form
    - slot{"date":"后天"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## New Story

* query_provider{"date":"明天","location":"北京","query_type":"天气"}
    - slot{"date":"明天"}
    - slot{"location":"北京"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"location":"北京"}
    - slot{"date":"明天"}
    - slot{"location":"北京"}
    - slot{"date":"明天"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* chitchat
    - action_chitchat
* chitchat
    - action_chitchat
* chitchat
    - action_chitchat

## news_story
* greet
    - utter_greet
* query_provider{"query_type":"新闻"}
	- slot{"query_type":"新闻"}
    - action_report_news
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## news_story
* query_provider{"query_type":"新闻"}
	- slot{"query_type":"新闻"}
    - action_report_news
    - action_reset_all
    - utter_more

## New Story

* query_provider{"date":"今天","query_type":"新闻"}
    - slot{"date":"今天"}
    - slot{"query_type":"新闻"}
    - action_report_news
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## New Story

* greet
    - utter_greet
* help
    - utter_what_can_do
* query_provider{"date":"今天","query_type":"新闻"}
    - slot{"date":"今天"}
    - slot{"query_type":"新闻"}
    - action_report_news
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye

## New Story

* query_provider{"date":"今天","query_type":"新闻"}
    - slot{"date":"今天"}
    - slot{"query_type":"新闻"}
    - action_report_news
    - action_reset_all
    - utter_more
* query_provider{"date":"今天","query_type":"天气"}
    - slot{"date":"今天"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"date":"今天"}
    - slot{"date":"今天"}
    - slot{"requested_slot":"location"}
* inform{"location":"广州"}
    - slot{"location":"广州"}
    - weather_form
    - slot{"location":"广州"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
* goodbye
    - utter_goodbye
