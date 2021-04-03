import json
import re
import webbrowser
import pprint
import datetime
from tabulate import tabulate
from urllib.request import urlopen
from bs4 import BeautifulSoup
now = datetime.datetime.now()
result = []
#tags = [ "google-cloud-platform"]
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

def find_bad_qn(a,tag):#       tags = "google-cloud-platform+or+firebase+or+google-cloud-firestore+or+google-cloud-functions"
        url="https://stackoverflow.com/questions/tagged/"+tag+"?page="+str(a)+"&sort=newest&filters=NoAnswers&edited=true"
        html = urlopen(url)
        bsObj = BeautifulSoup(html,"html5lib")
        que= bsObj.find_all("div", class_="question-summary")
        for div in que:
                vote=int(div.find('span').text.split(' ')[0])
                link=div.a.get('href')
                name=div.a.text
                date1=div.find('span', class_="relativetime")["title"]
                date = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%SZ')
                timeper = datetime.timedelta(days = 3)
                if(vote<0 and (now-date)<timeper and not bool(re.search('(\[on hold\]|\[duplicate\]|\[closed\])$', name))):
                        elem = {'link': link, 'vote': vote, 'date':format(date)}
                        result.append(elem)
for tag in tags:
        for i in range(1,3):
                try:
                        find_bad_qn(i,tag)
                except Exception as e:
                        print("exception")
                        print(e)
                        i=7
                        continue

for qn in result:
        qn['link']="https://stackoverflow.com"+qn['link']
result= sorted(result, key=lambda x: x['date'], reverse=False)
result = sorted(result, key=lambda x: x['vote'], reverse=False)
result1 = []
for par in result:
        if par in result1:
                print("repetido")
        else:
                result1.append(par)

print(tabulate(result, tablefmt="html"))
print(tabulate(result1))
