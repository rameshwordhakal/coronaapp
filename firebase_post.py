from firebase import firebase
import firebase_admin
from firebase_admin import credentials, firestore
import datetime, pytz
from mar29 import countries

cred = credentials.Certificate("../covid-19-firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
db_collection = db.collection(u'statistics')

for country_dict in countries:
  post_dict = {}
  if 'total_cases' in country_dict:
    post_dict['total_cases'] = country_dict['total_cases']
  if 'new_cases' in country_dict:
    post_dict['new_cases'] = country_dict['new_cases']
  if 'total_deaths' in country_dict:
    post_dict['total_deaths'] = country_dict['total_deaths']
  if 'new_deaths' in country_dict:
    post_dict['new_deaths'] = country_dict['new_deaths']
  if 'total_recovered' in country_dict:
    post_dict['total_recovered'] = country_dict['total_recovered']
  if 'active_cases' in country_dict:
    post_dict['active_cases'] = country_dict['active_cases']
  if 'serious_cases' in country_dict:
    post_dict['serious_cases'] = country_dict['serious_cases']
  # if 'tot_cases' in country_dict:
  #   post_dict['tot_cases'] = country_dict['tot_cases']

  db_document = db_collection.document(country_dict['country'])
  db_document.set(post_dict)
  
  print(country_dict['country'] + " successfully written to database.")