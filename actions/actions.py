# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
import os

#from google_trans_new import google_translator

class ActionLanguageSearch(Action):

    def name(self) -> Text:
        return "action_lang_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data_path = os.path.join("data", "cldf-datasets-wals-014143f", "cldf", "languages.csv")
        wals_data = pd.read_csv(data_path)

        data_path2 = os.path.join("data", "cldf-datasets-wals-014143f", "raw", "walslanguage.csv")
        wals_data2 = pd.read_csv(data_path2)

        data_path3 = os.path.join("data", "cldf-datasets-wals-014143f", "raw", "countrylanguage.csv")
        wals_data3 = pd.read_csv(data_path3)

        data_path4 = os.path.join("data", "cldf-datasets-wals-014143f", "raw", "country.csv")
        wals_data4 = pd.read_csv(data_path4)

        entities = list(tracker.get_latest_entity_values("language"))
        print(entities)

        if len(entities) > 0:
            query_lang = entities.pop()
            # translator = google_translator()
            # query_lang = str(translator.translate(query_lang, lang_tgt='en'))

            #query_lang = str(google_translate(query_lang))
            # query_lang = query_lang.lower().capitalize().strip()

            query_lang = query_lang.lower().capitalize()
            print(query_lang)
            
            out_row = wals_data[wals_data["Name"] == query_lang].to_dict("records")
            print(out_row)
            out_row2 = wals_data2[wals_data2["ascii_name"] == query_lang.lower()].to_dict("records")
            #print(out_row2[0]["pk"])
            out_row3 = wals_data3[wals_data3["language_pk"] == out_row2[0]["pk"]].to_dict("records")
            print(out_row3)
            out_row4 = wals_data4[wals_data4["pk"] == out_row3[0]["country_pk"]].to_dict("records")
            print(out_row4)

            if len(out_row) > 0:
                out_row = out_row[0]
                #out_text = "Language %s belongs to the Family %s\n with Genus as %s\n and has ISO code %s" % (out_row["Name"], out_row["Family"], out_row["Genus"], out_row["ISO_codes"])
                out_text = "भाषा %s जिसका WALS कोड %s,जीनस %s ,\n  परिवार %s\n से संबंधित है,और इसमें ISO कोड %s है| \n क्या जानकारी उपयोगी थी दोस्त?" % (out_row["Name"], out_row["ID"], out_row["Family"], out_row["Genus"], out_row["ISO_codes"])
                dispatcher.utter_message(text = out_text)
            else:
                dispatcher.utter_message(text = "माफ़ करना! हमारे पास %s भाषा के रिकॉर्ड नहीं हैं " % query_lang)

        return []


class ActionCountrySearch(Action):

    def name(self) -> Text:
        return "action_country_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data_path = os.path.join("data", "cldf-datasets-wals-014143f", "cldf", "languages.csv")
        wals_data = pd.read_csv(data_path)

        data_path2 = os.path.join("data", "cldf-datasets-wals-014143f", "raw", "walslanguage.csv")
        wals_data2 = pd.read_csv(data_path2)

        data_path3 = os.path.join("data", "cldf-datasets-wals-014143f", "raw", "countrylanguage.csv")
        wals_data3 = pd.read_csv(data_path3)

        data_path4 = os.path.join("data", "cldf-datasets-wals-014143f", "raw", "country.csv")
        wals_data4 = pd.read_csv(data_path4)

        entities = list(tracker.get_latest_entity_values("language"))
        print(entities)

        if len(entities) > 0:
            query_lang = entities.pop()
            # translator = google_translator()
            #query_lang = translator.translate(query_lang, lang_tgt='en')

            # query_lang = str(translator.translate(query_lang, lang_tgt='en'))

            #query_lang = str(google_translate(query_lang))
            # query_lang = query_lang.lower().capitalize().strip()

            query_lang = query_lang.lower().capitalize()
            print(query_lang)
            
            out_row = wals_data[wals_data["Name"] == query_lang].to_dict("records")
            print(out_row)
            out_row2 = wals_data2[wals_data2["ascii_name"] == query_lang.lower()].to_dict("records")
            #print(out_row2[0]["pk"])
            out_row3 = wals_data3[wals_data3["language_pk"] == out_row2[0]["pk"]].to_dict("records")
            print(out_row3)
            out_row4 = wals_data4[wals_data4["pk"] == out_row3[0]["country_pk"]].to_dict("records")
            print(out_row4)

            if len(out_row) > 0:
                out_row = out_row[0]
                out_text = "%s भाषा %s देश में बोली जाती है | \n क्या जानकारी उपयोगी थी दोस्त?" % (out_row["Name"], out_row4[0]["name"])
                dispatcher.utter_message(text = out_text)
            else:
                dispatcher.utter_message(text = "माफ़ करना! हमारे पास %s भाषा के रिकॉर्ड नहीं हैं" % query_lang)

        return []


class ActionMacroareaSearch(Action):

    def name(self) -> Text:
        return "action_macroarea_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        data_path = os.path.join("data", "cldf-datasets-wals-014143f", "cldf", "languages.csv")
        wals_data = pd.read_csv(data_path)

        data_path2 = os.path.join("data", "cldf-datasets-wals-014143f", "raw", "walslanguage.csv")
        wals_data2 = pd.read_csv(data_path2)

        entities = list(tracker.get_latest_entity_values("language"))
        print(entities)

        if len(entities) > 0:
            query_lang = entities.pop()
            # translator = google_translator()
            #query_lang = translator.translate(query_lang, lang_tgt='en')

            # query_lang = str(translator.translate(query_lang, lang_tgt='en'))

            #query_lang = str(google_translate(query_lang))
            # query_lang = query_lang.lower().capitalize().strip()

            query_lang = query_lang.lower().capitalize()
            print(query_lang)
            
            out_row = wals_data[wals_data["Name"] == query_lang].to_dict("records")
            print(out_row)
            out_row2 = wals_data2[wals_data2["ascii_name"] == query_lang.lower()].to_dict("records")

            if len(out_row) > 0:
                out_row = out_row[0]
                out_text = "%s भाषा का मैक्रोएरा %s है | \n क्या जानकारी उपयोगी थी दोस्त?" % (out_row["Name"], out_row2[0]["macroarea"])
                dispatcher.utter_message(text = out_text)
            else:
                dispatcher.utter_message(text = "माफ़ करना! हमारे पास %s भाषा के रिकॉर्ड नहीं हैं" % query_lang)

        return []