import time
import random
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
browser = webdriver.Firefox()

tags = ['apache-beam','app-engine-flexible','appengine-gradle-plugin','appengine-maven-plugin','bigtable','dialogflow-cx','dialogflow-es','gae-datastore','gce-persistent-disk','gcloud','gcloud-intellij','gcloud-java','gcloud-node','gcloud-python'
,'gcsfuse','gcutil','gke-networking','google-ai-platform','google-anthos','google-app-engine','google-artifact-registry','google-bigquery','google-cdn','google-cloud-api-gateway','google-cloud-armor','google-cloud-automl-nl'
,'google-cloud-bigtable','google-cloud-build','google-cloud-cdn','google-cloud-composer','google-cloud-data-fusion','google-cloud-data-transfer','google-cloud-dataflow','google-cloud-datalab','google-cloud-dataprep','google-cloud-dataproc'
,'google-cloud-datastore','google-cloud-debugger','google-cloud-dlp','google-cloud-dns','google-cloud-dotnet','google-cloud-eclipse','google-cloud-endpoints','google-cloud-filestore','google-cloud-firestore','google-cloud-functions'
,'google-cloud-http-load-balancer','google-cloud-intellij','google-cloud-interconnect','google-cloud-internal-load-balancer','google-cloud-iot','google-cloud-kms','google-cloud-logging','google-cloud-memorystore','google-cloud-ml','google-cloud-ml-data'
,'google-cloud-monitoring','google-cloud-network-load-balancer','google-cloud-networking','google-cloud-nl','google-cloud-platform','google-cloud-powershell','google-cloud-pubsub','google-cloud-python','google-cloud-router','google-cloud-run'
,'google-cloud-scheduler','google-cloud-sdk','google-cloud-shell','google-cloud-source-repos','google-cloud-spanner','google-cloud-speech','google-cloud-sql','google-cloud-storage','google-cloud-talent-solution','google-cloud-tasks'
,'google-cloud-tcp-proxy','google-cloud-tpu','google-cloud-trace','google-cloud-transcoder','google-cloud-vision','google-cloud-visualstudio','google-cloud-vpn','google-cloud-webrisk','google-compute-engine','google-container-builder'
,'google-container-os','google-container-registry','google-data-catalog','google-data-studio','google-deployment-manager','google-eclipse-plugin','google-genomics','google-hadoop','google-kubernetes-engine','google-natural-language','google-oauth'
,'google-persistent-disk','google-plugin-eclipse','google-prediction','google-stackdriver','google-translate','google-translation-api','google-workflows','gsutil','maven-gae-plugin','stackdriver','video-intelligence-api','firebase']


def login():
    browser.get('https://stackoverflow.com/users/login')
    email = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    email.send_keys("youremail")
    password.send_keys("yourpassword")
    browser.find_element_by_id("submit-button").click()
    time.sleep(2)

def upvoteqn(url):
    browser.get(url)
    browser.find_elements_by_class_name("vote-up-off")[0].click()


def select_page(a,tag):   
    url="https://stackoverflow.com/questions/tagged/"+tag+"?page="+str(a)+"&sort=votes"
    html = urlopen(url)
    bsObj = BeautifulSoup(html,"html5lib")
    que= bsObj.find_all("div", class_="question-summary")
    for div in que:
        link="https://stackoverflow.com"+div.a.get('href')
        result.append({'link': link})    

result = []
login()
s=random.randrange(1,100)
select_page(s)
for i in range(1,31):
    url=result[i]['link']
    print (url,s)
    upvoteqn(url)
