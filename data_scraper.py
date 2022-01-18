from codecs import strict_errors
from os import strerror
import time
from selenium import webdriver
import mysql.connector
import requests
from lxml import html

from date_time_converter import *
from pixel_locations import *

browser = webdriver.Chrome()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS ryerson_incident_database")
mycursor.execute("USE ryerson_incident_database")

#USE THIS TO CLEAR TABLE
#mycursor.execute("DROP TABLE incidents")

mycursor.execute("CREATE TABLE IF NOT EXISTS incidents (id INTEGER AUTO_INCREMENT PRIMARY KEY, date_uploaded VARCHAR(255), incident_date INTEGER, incident_time VARCHAR(255), reported_date VARCHAR(255), reported_time VARCHAR(255), location VARCHAR(255), incident_type VARCHAR(255), hyperlinks VARCHAR(255), incident_details TEXT, suspect_descriptions TEXT, top_pixels INTEGER, left_pixels INTEGER)")

target_url = "https://www.ryerson.ca/community-safety-security/security-incidents/list-of-security-incidents/"

browser.get(target_url)

#find total number of pages to scrape

page_numbers = []

for datum in browser.find_elements_by_xpath("//li/a[@data-page]"):
    page_numbers.append(datum.get_attribute("data-page"))

print(page_numbers)

#TEMPORARY TO CUT DOWN ON TIME
page_numbers = page_numbers[0:1]
print(page_numbers)

date_uploaded = []
incident_date = []
incident_time = []
reported_date = []
reported_time = []
location = []
incident_type = []
hyperlinks = []
incident_details = []
suspect_descriptions = []
top_pixels = []
left_pixels = []

duplicate_flag = False

sql = "SELECT MAX(date_uploaded) FROM incidents"
mycursor.execute(sql)
latest_date_uploaded_tuple = mycursor.fetchall()

print(latest_date_uploaded_tuple[0])

try:
    latest_date_uploaded = "".join(latest_date_uploaded_tuple[0])
except:
    latest_date_uploaded = "None"
  
print(latest_date_uploaded)

for i in range(len(page_numbers)):

    for entry in browser.find_elements_by_xpath("//div[@class=' date']"):

        date = date_converter(entry.get_attribute("innerHTML"))

        if date == latest_date_uploaded:
            duplicate_flag = True
            final_list_length = len(date_uploaded)

            print(date)
            print(duplicate_flag)
            print(final_list_length)

            break

        if date == "":
            date = "N/A"

        date_uploaded.append(date)
    
    for entry in browser.find_elements_by_xpath("//div[@class=' dateOfIncident']"):
        temp = entry.get_attribute("innerHTML")
        temp_list_1 = temp.split("</span>")
        temp_list_2 = temp_list_1[1].split(" at ")

        if int(date_converter(temp_list_2[0])) != "":
            incident_date.append(int(date_converter(temp_list_2[0])))
        else:
            incident_date.append("N/A")

        if time_converter(temp_list_2[1]) != "":
            incident_time.append(time_converter(temp_list_2[1]))
        else:
            incident_time.append("N/A")
                    
    for entry in browser.find_elements_by_xpath("//div[@class=' location']"):
        temp = entry.get_attribute("innerHTML")
        temp_list_1 = temp.split("</span>")

        if temp_list_1[1] != "":
            results = assign_names_pixels(temp_list_1[1])
            location.append(results[0])
            top_pixels.append(results[1])
            left_pixels.append(results[2])
        else:
            location.append("N/A")
            top_pixels.append(0)
            left_pixels.append(0)

    for entry in browser.find_elements_by_xpath("//a[@class=' title']"):
        temp = entry.get_attribute("innerHTML")
        temp_list_1 = temp.split("</div>")

        incident_type.append(temp_list_1[1])
        hyperlinks.append(entry.get_attribute("href"))

    if i != len(page_numbers) - 1:
        button_path = browser.find_element_by_xpath(f"//li/a[@data-page = {page_numbers[i + 1]}]")
        button_path.click()

    if duplicate_flag:
        incident_date = incident_date[0 : final_list_length]
        incident_time = incident_time[0 : final_list_length]
        location = location[0 : final_list_length]
        incident_type = incident_type[0 : final_list_length]
        hyperlinks = hyperlinks[0 : final_list_length]
        top_pixels = top_pixels[0 : final_list_length]
        left_pixels = left_pixels[0 : final_list_length]
        break   

    if len(date_uploaded) == len(incident_date) == len(incident_time) == len(location) == len(incident_type) == len(hyperlinks):
        time.sleep(3)
        continue
    else:
        print("There is a discrepancy on page " + page_numbers[i])
        break

    #print(date_uploaded)
    #print(incident_date)
    #print(incident_time)
    #print(reported_date)
    #print(reported_time)
    #print(location)
    #print(incident_type)
    #print(hyperlinks) 

for j in range(len(hyperlinks)):
    page = requests.get(hyperlinks[j])
    page_HTML = html.fromstring(page.content)

    print(hyperlinks[j])

    details_as_list = page_HTML.xpath("//div[@class = 'incidentdetails']/p/text()")

    descriptions_as_list = page_HTML.xpath("//div[@class = 'description']/p/text()")

    reported_date_as_list = page_HTML.xpath("//div[@class = 'datereported']/text()")

    if len(reported_date_as_list) > 0:
        temp = reported_date_as_list[0].replace(u"\xa0", u"")
        temp_list_1 = temp.split("y, ")
        temp_list_2 = temp_list_1[1].split(" at ")

        reported_date.append(date_converter(temp_list_2[0]))
        reported_time.append(time_converter(temp_list_2[1]))
    else:
        reported_date.append("N/A")
        reported_time.append("N/A")

    try:
        details_as_list_cleaned = details_as_list[0].replace(u"\xa0", u"")
    except:
        details_as_list_cleaned = "No details provided."

    try:
        descriptions_as_list_cleaned = descriptions_as_list[0].replace(u"\xa0", u"")
    except:
        descriptions_as_list_cleaned = "No suspect description(s) provided."

    incident_details.append(details_as_list_cleaned)
    suspect_descriptions.append(descriptions_as_list_cleaned)

    time.sleep(1)

"""
print(date_uploaded[0])
print(incident_date[0])
print(incident_time[0])
print(reported_date[0])
print(reported_time[0])
print(location[0])
print(incident_type[0])
print(hyperlinks[0])
print(incident_details[0])
print(suspect_descriptions[0])
"""

if len(date_uploaded) == len(incident_date) == len(incident_time) == len(reported_date) == len(reported_time) == len(location) == len(incident_type) == len(hyperlinks) == len(incident_details) == len(suspect_descriptions) == len(top_pixels) == len(left_pixels):
    for i in range(len(date_uploaded)):
        sql = "INSERT INTO incidents (date_uploaded, incident_date, incident_time, reported_date, reported_time, location, incident_type, hyperlinks, incident_details, suspect_descriptions, top_pixels, left_pixels) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (date_uploaded[i], incident_date[i], incident_time[i], reported_date[i], reported_time[i], location[i], incident_type[i], hyperlinks[i], incident_details[i], suspect_descriptions[i], top_pixels[i], left_pixels[i])
        mycursor.execute(sql, val)

    mydb.commit()

    sql = "SELECT * FROM incidents ORDER BY incident_date, incident_time"
    #sql = "SELECT DISTINCT location from incidents"
    mycursor.execute(sql)

    result = mycursor.fetchall()

    for x in result:
        print(x)
else:
    print("An error has occurred while scraping.")
    print(str(len(date_uploaded)) + " " +  str(len(incident_date)) + " " + str(len(incident_time)) + " " + str(len(reported_date)) + " " + str(len(reported_time)) + " " + str(len(location)) + " " + str(len(incident_type)) + " " + str(len(hyperlinks)) + " " + str(len(incident_details)) + " " + str(len(suspect_descriptions)) + " " + str(len(top_pixels)) + " " + str(len(left_pixels)))