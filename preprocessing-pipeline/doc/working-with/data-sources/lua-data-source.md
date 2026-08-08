---
title: Defining a data source using Lua
source: https://docs.kanzi.com/4.1.0/en/working-with/data-sources/lua-data-source.html
---

# Defining a data source using Lua

Use a Lua data source to define and simulate the external data dependencies of your application alongside your design in Kanzi Studio using the Lua programming language.
**Note:** The Lua Data Source in Kanzi Studio is an experimental feature, and your feedback is very important to us. To submit your feedback, use this [feedback form](https://docs.kanzi.com/feedback/v1/forms/feedback-feature.html?featureId=KanziLuaDataSource&featureTitle=the%20Kanzi%20Lua%20Data%20Source&productArea=studio).
## Creating a Lua data source

To create a Lua data source:

1.

In the Data Sources window click Create Data Source.
2.

In the Create Data Source window set:

  - Name to the name you want to use for this data source.
  - Data Source Type to the Kanzi.LuaDataSource.

Click OK.
3.

In the Data Sources window click  and set the value of the Lua Data Script property to the Lua data script which defines the data structure for your Lua Data Source.
4.

Create a Lua data script which returns the root data object.

Unlike regular Lua scripts which are used in Execute Lua Action, your Lua data script must return a root `DataObject` which contains the data definition for your Lua data source.
**Tip:** You can define data objects in the Lua data script as global variables, so that other scripts can easily access and modify the data.
For example:
```
-- Define a root data object, containing all the data.
local rootDataObject = DataObject:create("cluster", {
speed = 100,
rpm = 2300,
notifications = {
{ notification = "Service Due"},
{ notification = "Oil Change Needed"},
{ notification = "Dirty Air Filter"},
},
})
-- Store all data objects in a global table for easier access from simulation scripts.
globalData = {}
for child in rootDataObject:iterateChildren() do
globalData[child:getName()] = child
end
-- Return the root data object.
return rootDataObject
```
5.
In the Data Sources window click  next to the data source to create data objects from that data source.
After Lua Data Source executes your data script you can use the data object defined by it in your project. See Using data objects.

## Simulating your data

You can simulate data flow in your Kanzi Studio project using Execute Lua Action. See Using Lua on how to add the Lua logic into your application.
**Tip:** You can use a trigger condition to disable simulation in your application. See Adding conditions to a trigger.
For example:
1.
Define a new inheritable boolean property type in your Kanzi Studio project.
2.
Add this property to the root node of your project.
3.
Use the value of this property as a condition for the triggers that execute the simulation Lua scripts.
For example, use On Timer trigger to simulate data updates over time:
```
-- Initialize global timestamp variable for simulating data update over time.
if timestamp == nil then
timestamp = 0
end
-- Simulate speed and RPM changes.
local modifier = math.sin(timestamp)
local speed = math.floor(90 + modifier * 30)
local rpm = math.floor(2000 + modifier * 1000)
-- Use globally defined data table to simulate the data update.
if globalData then
globalData.speed:setValue(speed)
globalData.rpm:setValue(rpm)
end
-- Advance time.
timestamp = timestamp + 0.01
```
4.
In your application code, override the value of this property for the root node to disable the simulation scripts.
For example:
```
void onProjectLoaded() override
{
// Project file has been loaded from .kzb file.
// Project sets "DataSimulation.IsSimulation" property on a Root Node, which is used in triggers conditions to enable simulation scripts.
// To disable the simulation, set this property value to false on a Root Node.
DynamicPropertyType<bool> isSimulationProperty("DataSimulation.IsSimulation");
const auto rootNode = getScreen()->getChild(0);
kzAssert(rootNode);
// Disable data simulation.
rootNode->setProperty(isSimulationProperty, false);
}
```
5.
Use the Data Objects defined in your Lua script to provide the real data values from your application.
```
// Define a DataObjectList to provide actual list data.
class NotificationsDataObject : public DataObjectList
{
public:
...
// Follow the same data structure as the one you defined in Lua.
DataObjectSharedPtr getItemTemplate() override
{
auto item = DataObject::create(getDomain(), "item");
item->addChild(DataObjectString::create(getDomain(), "notification"));
return item;
}
};
```

```
void onProjectLoaded() override
{
    ...

    // Use data model defined by the Lua Data Source. Retrieve the Data Context from the Root Node.
    auto dataContext = dynamic_pointer_cast<DataContext>(rootNode->getProperty(DataContext::DataContextProperty));
    kzAssert(dataContext);

    // Store the data objects to update.
    m_speedData = dynamic_pointer_cast<DataObjectInt>(dataContext->lookupDataContext("speed"));
    kzAssert(m_speedData);

    m_rpmData = dynamic_pointer_cast<DataObjectInt>(dataContext->lookupDataContext("rpm"));
    kzAssert(m_rpmData);

    // For list data, replace the existing simulation data object list with the actual data object list.
    auto simulationNotificationsDataObject = dynamic_pointer_cast<DataObjectList>(dataContext->lookupDataContext("notifications"));
    kzAssert(simulationNotificationsDataObject);

    auto rootDataObject = dataContext->getData();
    kzAssert(rootDataObject);

    rootDataObject->removeChild(*simulationNotificationsDataObject);
    rootDataObject->addChild(notificationsData);

    // Notify that the data context has been modified.
    dataContext->notifyModified();

    getMainLoopScheduler().appendTask(UserStage, kzMakeFixedString("UpdateData"), MainLoopScheduler::TaskRecurrence::Recurring,
        [this](auto)
        {
            this->updateSpeedAndRPMData();
        }
    );
}

```
