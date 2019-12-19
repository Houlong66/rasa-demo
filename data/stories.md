## greet_story
* greet
    - utter_greet
    - utter_what_can_do

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
    - slot{"location":"广州"}
    - slot{"date":"明天"}
    - weather_form
    - form{"name": "weather_form"}
    - form{"name": null}
    - search_weather
    - action_reset_all
    - utter_more
    - action_restart

## happy_path_location
* query_provider{"location":"武汉", "query_type":"天气"}
    - slot{"query_type":"天气"}
    - slot{"location":"武汉"}
    - weather_form
    - form{"name": "weather_form"}
    - form{"name": null}
    - search_weather
    - action_reset_all
    - utter_more
    - action_restart

## happy_path_date
* query_provider{"date":"今天", "query_type":"天气"}
    - slot{"query_type":"天气"}
    - slot{"date":"今天"}
    - weather_form
    - form{"name": "weather_form"}
    - form{"name": null}
    - search_weather
    - action_reset_all
    - utter_more
    - action_restart

## unhappy_path_date

* query_provider{"date":"后天","query_type":"天气"}
    - slot{"query_type":"天气"}
    - slot{"date":"后天"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"date":"后天"}
    - slot{"date":"后天"}
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
    - action_restart

## unhappy_path_location

* query_provider{"location":"武汉","query_type":"天气"}
    - slot{"query_type":"天气"}
    - slot{"location":"武汉"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"location":"武汉"}
    - slot{"location":"武汉"}
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
    - action_restart

## very_unhappy_path

* query_provider{"location":"广州","query_type":"天气"}
    - slot{"query_type":"天气"}
    - slot{"location":"广州"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"location":"广州"}
    - slot{"location":"广州"}
    - slot{"requested_slot":"date"}
* chitchat
    - action_chitchat
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
* inform{"date":"今天"}
    - slot{"date":"今天"}
    - weather_form
    - slot{"date":"今天"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - search_weather
    - action_reset_all
    - utter_more
    - action_restart

## news_story

* query_provider{"date":"今天","query_type":"新闻"}
    - slot{"query_type":"新闻"}
    - slot{"date":"今天"}
    - action_report_news
    - action_reset_all
    - utter_more
    - action_restart

## news_greet_story

* greet
    - utter_greet
    - utter_what_can_do
* query_provider{"query_type":"新闻"}
    - slot{"query_type":"新闻"}
    - action_report_news
    - action_reset_all
    - utter_more
    - action_restart

## news_chitchat_story

* chitchat
    - action_chitchat
* query_provider{"date":"今天","query_type":"新闻"}
    - slot{"query_type":"新闻"}
    - slot{"date":"今天"}
    - action_report_news
    - action_reset_all
    - utter_more
    - action_restart

## goodbye_deactivate_story

* chitchat
    - action_chitchat
* query_provider{"date":"今天","query_type":"天气"}
    - slot{"date":"今天"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"date":"今天"}
    - slot{"date":"今天"}
    - slot{"requested_slot":"location"}
* goodbye
    - utter_goodbye
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_reset_all

## greet_deactivate_story

* chitchat
    - action_chitchat
* query_provider{"date":"今天","query_type":"天气"}
    - slot{"date":"今天"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"date":"今天"}
    - slot{"date":"今天"}
    - slot{"requested_slot":"location"}
* greet
    - utter_greet
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_reset_all

## weather_news_story

* chitchat
    - action_chitchat
* query_provider{"date":"今天","query_type":"天气"}
    - slot{"date":"今天"}
    - slot{"query_type":"天气"}
    - weather_form
    - form{"name":"weather_form"}
    - slot{"date":"今天"}
    - slot{"date":"今天"}
    - slot{"requested_slot":"location"}
    - slot{"date":"今天"}
    - slot{"query_type":"天气"}
* query_provider{"query_type":"新闻"}
    - slot{"query_type":"新闻"}
    - action_report_news
    - action_deactivate_form
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_reset_all
    - utter_more
    - action_restart
