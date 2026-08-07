---
title: Data sources
source: https://docs.kanzi.com/4.1.0/en/working-with/data-sources/data-sources.html
---

# Data sources

Use data sources to separate the user interface from the application data and to remove the dependencies between a Kanzi Studio project and the application code which define the Kanzi application.

Kanzi allows you to define the format and structure of your data source by defining a Kanzi Engine data source plugin.

When you use a data source in a Kanzi application you bind the values of properties and property fields to data that comes from a data source. This binding establishes a connection between a node or a resource and the application data. When data in the data source changes, the nodes and resources which are bound to the data reflect the change in the data.

A typical use case is to bind the properties of nodes in your cluster or IVI system to data from a data source provided by a server to which your application connects. For example, your Kanzi application can use data sources to get data such as speed, RPM, and fuel information, address book entries, album and song information, navigation information, and so on.

Learn how to define and use data sources in your Kanzi applications by completing the data sources tutorial. See Tutorial: Get application data from a data source.
