---
title: Measuring the performance of your application code
source: https://docs.kanzi.com/4.1.0/en/working-with/performance-profiling/profiling-application-code.html
---

# Measuring the performance of your application code


The Kanzi performance profiling system enables you to measure the performance of your Kanzi application. Kanzi profiles all main loop tasks with the `MainLoopProfiler`, including custom tasks that you add.

Here you can find out how to measure the performance of your code in your Kanzi application. To measure the performance of different parts of Kanzi Engine during application startup and the tasks that Kanzi runs in the main loop, use the performance profilers in the Profiling build. See Measuring the performance of Kanzi Engine.

To measure the performance of your application code you can:

- Create your own performance profiling categories. See Creating performance profiling categories.
- Measure the performance of any function or scope. See Measuring the performance of scopes and Measuring the performance of functions.
- Log performance profiling data. See Logging application code performance profiling data.

## Creating performance profiling categories


To group the performance measurements of functions and scopes, create your own performance profiling categories.

To create a performance profiling category, use the `ProfilingMacros::kzProfilingCreateCategory` macro to define the category and the `ProfilingMacros::kzProfilingRegisterCategory` macro to register the category.

For example:

```
// Define a performance profiling category MY_PROFILING_CATEGORY.
// Set the compile-time state of the category to enabled, name the category ``MyProfilingCategory``,
// and set the sample buffer size of the category to 200.
#define MY_PROFILING_CATEGORY kzProfilingCreateCategory(KZ_PROFILING_ENABLED_CATEGORY, "MyProfilingCategory", 200)
// Register the performance profiling category MY_PROFILING_CATEGORY and set its initial runtime state to enabled.
// The runtime state of a performance profiling category controls whether profilers in the category collect samples.
// You can control the runtime state of performance profiling categories in the application configuration.
kzProfilingRegisterCategory(MY_PROFILING_CATEGORY, KZ_PROFILING_ENABLED_CATEGORY);

```


See ProfilingCategoryFilter.

You can use the performance profiling category you created to profile the performance of:

- Scopes. See Measuring the performance of scopes.
- Functions. See Measuring the performance of functions.

## Measuring the performance of scopes


You can use Kanzi profiling macros to measure the execution time of any scope in your application code:

- `ProfilingMacros::kzProfileScope` profiles the execution time of a scope.
- `ProfilingMacros::kzProfileScopeExtended` profiles the execution time of a scope using a custom profiler registry and sample buffer size.


To measure the performance of a scope:

1.

(Optional) Create your own performance profiling category. See Creating performance profiling categories.

If you do not want to create a performance profiling category, you can use the Generic category `ProfilingMacros::KZ_PROFILING_CATEGORY_GENERIC`.
2.

In the beginning of the scope the performance of which you want to measure, call the `ProfilingMacros::kzProfileScope` macro.

The `ProfilingMacros::kzProfileScope` macro creates a profiler and registers the profiler in the Default Profiler Registry. Every time the scope is entered, Kanzi adds to the profiler a new sample which includes the time spent executing this scope.

For example, to measure the execution time of the `if (!m_interpolationActive)` block in the Scroll view example:

```
// Activate interpolation playback by adding it to the code.
if (!m_interpolationActive)
{
    // kzProfileScope() measures the time it takes to execute this scope.
    // The profiler created by kzProfileScope() is assigned to the KZ_PROFILING_CATEGORY_GENERIC category and registered in the Default Profiler Registry.
    // The name of the profiler is "Activate interpolation playback".
    // Every time this scope is entered, that is when "!m_interpolationActive" is true, Kanzi adds a new sample to the profiler.
    kzProfileScope(KZ_PROFILING_CATEGORY_GENERIC, "Activate interpolation playback");
    getDomain()->getRootTimelineClock()->addTimelinePlayback(m_interpolationPlayback);
    m_interpolationActive = true;
}

```

3.

Log the performance profiling data. See Logging Kanzi Engine performance profiling data.

For example, when you exit the application, the Kanzi logger collects data from all function and scope profilers.
4.

Build and run your application. See Deploying Kanzi applications.


Kanzi writes the performance measurement information to the log.

```
info:profiling> Generic::Activate interpolation playback:
info:profiling>   Total duration [ns]: 34279
info:profiling>   Number of intervals: 1
info:profiling>   Average duration [ns]: 34279
info:profiling>   Longest duration [ns]: 34279
info:profiling>   Shortest duration [ns]: 34279

```

## Measuring the performance of functions


You can use the `ProfilingMacros::kzProfileFunction` macro to measure the execution time of functions in your application code.

To measure the performance of a function:

1.

(Optional) Create your own performance profiling category. See Creating performance profiling categories.

If you do not want to create a performance profiling category, you can use the Generic category `ProfilingMacros::KZ_PROFILING_CATEGORY_GENERIC`.
2.

In the beginning of the function the performance of which you want to measure, call the `ProfilingMacros::kzProfileFunction` macro.

The `ProfilingMacros::kzProfileFunction` macro creates in this function a static profiler and registers the profiler in the Default Profiler Registry. Every time the function is called, Kanzi adds to the profiler a new sample which includes the time spent executing this function.

For example, to measure the performance of scrolling in the Scroll view example, call the `ProfilingMacros::kzProfileFunction` macro in the handler for the `ScrollViewConcept::ScrolledMessage` message.

```
// Handler for the ScrollView3D::ScrolledMessage message from the Scroll View node.
// Updates input values for the zoom animation.
auto scrollToken = m_scrollView->addMessageHandler(ScrollView3D::ScrolledMessage, [this](ScrollView3D::ScrollMessageArguments& messageArguments) {
    // kzProfileFunction() measures the time it takes to execute the function.
    // The profiler created by kzProfileFunction() is assigned to the KZ_PROFILING_CATEGORY_GENERIC category and registered in the Default Profiler Registry.
    // The name of the profiler is provided by the compiler and includes the name of this function. See KZ_PROFILING_THIS_FUNCTION_NAME.
    // Every time the function is called, Kanzi adds a new sample to the profiler.
    kzProfileFunction(KZ_PROFILING_CATEGORY_GENERIC);

    ...
}

```

3.

Log the performance profiling data. See Logging Kanzi Engine performance profiling data.

For example, when you exit the application, the Kanzi logger collects data from all function and scope profilers.
4.

Build and run your application. See Deploying Kanzi applications.


Kanzi writes the performance measurement information to the log.

In the log **Number of intervals** shows how many times the function was called.

```
info:profiling> Generic::auto __thiscall ScrollViewApplication::onProjectLoaded::<lambda_921241ce020d51bc4ca5a6d3e6fa81a0>::operator ()(class kanzi::ScrollViewConcept::ScrollMessageArguments &) const:
info:profiling>   Total duration [ns]: 962007
info:profiling>   Number of intervals: 273
info:profiling>   Average duration [ns]: 3523
info:profiling>   Longest duration [ns]: 47407
info:profiling>   Shortest duration [ns]: 1823

```

## Logging application code performance profiling data


To analyze the performance of your application code, log the performance profiling data. You can log per-sample and summary data from the profilers that you create and from profiler registries. See Logging Kanzi Engine performance profiling data.
