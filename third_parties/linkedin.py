import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False)  :
    """scrape information from LinkedIn profiles,
    Manually scrape the infromation from the LinkedIn profile"""
    
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/WzLaughez/be2062fd2acfe89841abc001ab7b9d78/raw/ef687804921464cd0fddffc38636ee8f1a17d60e/Fariz_ramadhan,json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10
        )
    
    data = response.json()

    
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/muhammad-fariz-b90839226/",
            mock=True
        )
    )