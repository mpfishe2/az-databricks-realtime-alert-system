# Azure Databricks Real-Time Alert System

## What is this repository?

This repository is for this blog post on CodeMinusTears.com:  
https://codeminustears.com/2019/03/23/real-time-alerting-databricks/  
  
It showcasing how you can use a Structured Streaming Pipeline in Azure Databricks to route anomalous data or alert you to various conditions or issues that you set up monitoring for by using an Azure Event Hub and a Azure Logic App.  
  
The end result is a pipleine that filters out anomalous data in a real-time stream of data and sends a email with the anomalous data.

## Table of Contents

|Name|Purpose|
|---|---|
|`senderApp\sender.py`|Python App that emulates a stream of data|
|`InstallAzureEventHubsSparkConnector.docx`|Word Document that explains how to install the Micrsoft Event Hub Spark Connector|
|`SetUpLogicAppForAlerting.docx`|Word Document that explains how to set up for the Logic App for this demo|
|`Real-Time Alerting.ipynb`|IPYNB file for the demo and for import into Databricks|
|`Real-Time Alerting.py`|Source File for the Databricks Notebook for this demo|

## How to use this repository

There is a thorough walkthrough and explanation of how to set up this solution that can be found in this link.
  
### General Steps

1. Clone this repository to your local Machine
2. Deploy an Azure Event Hub Namespace and create two event hubs within the namespace called **ingestion** and **alerting**
3. Deploy an Azure Databricks workspace
4. Import the notebook to your Databricks workspace
5. Fill in the Event Hub Configuration details
6. Run the notebook on the cluster
7. Go to the **sender.py** file and fill in the Event Hub configuration details
8. Run the python file using `python sender.py` in a Command Prompt or Bash Terminal
9. Deploy an Azure Logic App
10. Follow the instructions in the SetUpLogicAppForAlerting.docx
11. See emails pop into your inbox (could generate a lot of emails, create a filter rule!)