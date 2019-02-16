import requests
from bs4 import BeautifulSoup
import pandas as pd
job_no = 0
url = "https://boston.craigslist.org/d/education-teaching/search/edu"
npo_jobs = {}
while True:

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    jobs = soup.find_all("p", {"class": "result-info"})

    for job in jobs:
        title = job.find("a", {"class": "result-title hdrlnk"}).text
        location_tag = job.find("span", {"class": "result-hood"})
        location = location_tag.text if location_tag else "N/A"
        time_tag = job.find("time", {"class": "result-date"})
        time = time_tag.text if time_tag else "N/A"
        link = job.find("a", {"class": "result-title hdrlnk"}).get("href")
        job_response = requests.get(link)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data, "html.parser")
        job_description_tag = job_soup.find('section', {'id': 'postingbody'})
        job_description = job_description_tag.text if job_description_tag else "N/A"
        job_attributes_tag = job_soup.find('p', {'class': 'attrgroup'})
        job_attributes = job_attributes_tag.text if job_attributes_tag else "N/A"
        job_no += 1
        npo_jobs[job_no] = [title, location, time, link, job_attributes, job_description]
        print("Job Title--", title)
        print("\n"
              "---------------------------------------------------------------------------------------------------------\n")

    url_tag = soup.find("a", {"title": "next page"})
    if url_tag.get('href'):
        url = 'https://boston.craigslist.org' + soup.find("a", {"title": "next page"}).get("href")
    else:
        break


print("Total Number of jobs {}".format(str(job_no)))
npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['Job Title', 'Location', 'Data', 'Link', 'Job Attibutes', 'Job Descripts'])
print(npo_jobs_df.head())
npo_jobs_df.to_csv('npo_jobs.csv')