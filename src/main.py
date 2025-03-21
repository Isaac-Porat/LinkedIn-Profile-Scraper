import os
import requests
from dotenv import load_dotenv
import pandas as pd
from LinkedInProfile import LinkedInProfile

load_dotenv()
PROXYCURL_API = os.getenv("PROXYCURL_API")

headers = {'Authorization': 'Bearer ' + PROXYCURL_API}

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

params = {
    'linkedin_profile_url': 'https://www.linkedin.com/in/tyfrankel/',
    'extra': 'exclude',
    'github_profile_id': 'exclude',
    'facebook_profile_id': 'exclude',
    'twitter_profile_id': 'exclude',
    'personal_contact_number': 'exclude',
    'personal_email': 'exclude',
    'inferred_salary': 'exclude',
    'skills': 'exclude',
    'use_cache': 'if-recent',
    'fallback_to_cache': 'on-error',
}
try:
    response = requests.get(api_endpoint, params=params, headers=headers)
    response.raise_for_status()  

    if response.status_code == 200:
        response_data = response.json()
    elif response.status_code == 404:
        print("Profile not found.")
        response_data = {}
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")

response_data = response.json()

profile = LinkedInProfile.from_dict(response_data)

profile_folder = f"../data/{profile.full_name.replace(' ', '_')}"
os.makedirs(profile_folder, exist_ok=True)

if profile.profile_pic_url:
    profile_pic_response = requests.get(profile.profile_pic_url)
    if profile_pic_response.status_code == 200:
        with open(os.path.join(profile_folder, 'profile_pic.jpg'), 'wb') as f:
            f.write(profile_pic_response.content)

if profile.background_cover_image_url:
    background_cover_response = requests.get(profile.background_cover_image_url)
    if background_cover_response.status_code == 200:
        with open(os.path.join(profile_folder, 'background_cover.jpg'), 'wb') as f:
            f.write(background_cover_response.content)

profile_data = {
    "First Name": profile.first_name,
    "Last Name": profile.last_name,
    "Full Name": profile.full_name,
    "Headline": profile.headline,
    "Summary": profile.summary,
    "City": profile.city,
    "State": profile.state,
    "Country": profile.country,
    "Country Full Name": profile.country_full_name,
    "Occupation": profile.occupation,
    "Connections": profile.connections,
    "Profile Pic URL": profile.profile_pic_url,
    "Background Cover Image URL": profile.background_cover_image_url,
    "Public Identifier": profile.public_identifier,
    "Certifications": [cert.name for cert in profile.certifications],
    "Education": [edu.school for edu in profile.education],
    "Experiences": [exp.company for exp in profile.experiences],
    "Activities": [act.title for act in profile.activities],
    "Projects": [proj.title for proj in profile.projects],
    "Follower Count": profile.follower_count,
    "Accomplishment Courses": profile.accomplishment_courses,
    "Accomplishment Honors Awards": profile.accomplishment_honors_awards,
    "Accomplishment Organisations": profile.accomplishment_organisations,
    "Accomplishment Patents": profile.accomplishment_patents,
    "Accomplishment Publications": profile.accomplishment_publications,
    "Accomplishment Test Scores": profile.accomplishment_test_scores,
    "Articles": profile.articles,
    "Groups": profile.groups,
    "People Also Viewed": profile.people_also_viewed,
    "Volunteer Work": profile.volunteer_work,
}

df = pd.DataFrame([profile_data])

try:
    df.to_excel('../data/linkedin_profile_data.xlsx', index=False)
except Exception as e:
    print(f"An error occurred while saving to Excel: {e}")








