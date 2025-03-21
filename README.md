# LinkedIn Profile Scraper

A Python-based tool for scraping LinkedIn profiles to extract professional information.

## Project Overview

This project provides functionality to scrape LinkedIn profiles and extract structured data including:
- Basic profile information
- Work experience
- Education
- Skills
- Certifications
- And more

## Features

- Extract comprehensive profile information
- Structured data output (JSON)
- Configurable scraping parameters
- Rate limiting protection

## API

This project utilizes [Proxycurl's API](https://nubela.co/proxycurl/docs#people-api-person-profile-endpoint) to extract the LinkedIn profile data.


### Rate Limiting and Status Codes

- **Rate Limit Window**: 5 minutes
- **Trial Account Limit**: 2 requests every minute
- **Valid Request**: 1 credit
- **Successful Request**: 200 or 404

### Status Code Summary

| Status Code | Success | Description                                           |
|-------------|---------|-------------------------------------------------------|
| 400         | No      | Invalid parameters provided. Refer to the documentation and message body for more info |
| 401         | No      | Invalid API Key                                      |
| 403         | No      | You have run out of credits                          |
| 404         | Yes     | The requested resource (e.g: user profile, company) could not be found |
| 410         | No      | This API is deprecated                                |
| 429         | No      | Rate limited. Please retry                            |
| 500         | No      | There is an error with our API. Please contact us for assistance |
| 503         | No      | Enrichment failed, please retry.                     |

## License

GNU General Public License v3.0
