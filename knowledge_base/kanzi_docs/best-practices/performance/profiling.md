---
title: Measuring application performance
source: https://docs.kanzi.com/4.1.0/en/best-practices/performance/profiling.html
---

# Measuring application performance

The Kanzi performance profiling system enables you to measure the performance of your Kanzi application. You can measure the performance of:

- Different parts of Kanzi Engine during application startup and runtime. See Measuring the performance of Kanzi Engine.
- Your Kanzi application code. See Measuring the performance of your application code.
- Resource loading and deployment. See Measuring the loading and deployment time of resources.

You can use:

- **Profilers** to measure the performance of different parts of Kanzi Engine during application startup and runtime, and of your own application code. The Profiling build comes with several performance profilers. See Performance profiling categories in the Profiling build.
- **Profiling categories** to group profilers and to determine which profilers you want to enable. When you want to group the performance measurements of your own functions and scopes, create your own categories. See Performance profiling categories in the Profiling build and Creating performance profiling categories.
- **Profiling macros** to create and configure profiling categories and profilers. This way you can measure the performance of any function or scope. See Measuring the performance of scopes, Measuring the performance of functions.
- Performance HUD to show performance profiling graphs for the main loop tasks. See Showing the performance measurement graphs in the Performance HUD.
