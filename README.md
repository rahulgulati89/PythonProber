# PythonProber

The following page talks about a solution in python designed to monitor internet urls and provide Prometheus metrics. The solution is supposed to run on kubernetes cluster. Metrics from the python app should be exposed to prometheus and dashboard for the same can be built using grafana.

Prometheus and grafana can be installed using prometheus operator helm charts.

## Getting started
You will need the following software to run this program
* Python 3.X
* Install requirements.txt file.

Once the dependencies are installed, we can build a new docker image containing the python logic which probes URL's `https://httpstat.us/200` and `https://httpstat.us/503` and gets the status code and response time. The code and unit test for this python application are available under `pythonprober` directory in this github repo. 


## Executing

To execute this, we need to build a docker image using the following command. Make sure that following command is being ran from the directory containing the `Dockerfile`.

`docker build -t pythonprober .`

This should build the image with `latest` tag and store it in your docker repository. Once this image is build, we can use the same container image and deploy that from our kubernetes deployment.

The kubernetes cluster containing multiple components can be deployed using following command. The kubernetes deployment yaml file is also present in the same folder with the name `python-prober-deployment.yml`. We can run the following command to deploy different components running container image generated in above step.

`kubectl apply -f python-prober-deployment.yml`

If all goes well, you should see output of above command like this

`
serviceaccount/ish-pythonprober unchanged
service/ish-pythonprober unchanged
deployment.apps/ish-pythonprober unchanged
ingress.networking.k8s.io/ish-pythonprober created
servicemonitor.monitoring.coreos.com/ish-pythonprober unchanged
pod/ish-pythonprober-test-connection unchanged
`
Additionally, we can check our pods using below command. Note that all the pods are deployed in default namespace. 

`kubectl get pods`

`
NAME                                  READY   STATUS      RESTARTS   AGE
ish-pythonprober-796c97db44-n2f2m     1/1     Running     13         77m
`

The metrics should be visible on prometheus and grafana dashboard for those metrics should look like below. Note that we have used `guages` in prometheus metrics to track these metrics. The 2 metrics display the response time in milliseconds and the status codes(200 or 503).

![alt text](https://github.com/rahulgulati89/PythonProber/blob/main/Dashboard1.png)
![alt text](https://github.com/rahulgulati89/PythonProber/blob/main/Dashboard2.png)
