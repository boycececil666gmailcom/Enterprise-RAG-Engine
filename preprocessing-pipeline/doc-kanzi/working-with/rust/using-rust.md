---
title: Rust
source: https://docs.kanzi.com/4.1.0/en/working-with/rust/using-rust.html
---

# Rust

The Kanzi Rust API provides ready-made, rich, idiomatic bindings to the Kanzi Engine C++ API, enabling you to use the Kanzi Engine in your Rust applications.

This version covers an initial subset of the most commonly used features.
**Note:** As this is a prerelease of the Kanzi Rust API, some functionality, workflow, and the API is likely to change in future releases.
Your feedback is very important to us. To submit your feedback, use this [feedback form](https://docs.kanzi.com/feedback/v1/forms/feedback-feature.html?featureId=KanziRustAPI&featureTitle=the%20Kanzi%20Rust%20API&productArea=studio).
This topic provides an overview of creating a Rust based project in Kanzi Studio. For detailed steps on configuring your environment for Rust, including Examples and full API reference documentation, see the [Kanzi Rust API](https://docs.kanzi.com/rust/latest-4-0-rust/overview.html) documentation.
## Setting up environment for Kanzi Rust API

Before you can use Kanzi Rust API in your Kanzi application, you must install and configure your environment. See [Setting up environment for Kanzi Rust API](https://docs.kanzi.com/rust/latest-4-0-rust/setting-up.html#setting-up-environment-for-kzrust).
## Create new Rust based project in Kanzi Studio

In the Kanzi Studio New Project window:

1.

Set Template to:

  - Application with Rust API to create a Kanzi application with the application logic written in Rust language.
  - Application with Rust plugin to create a Kanzi application with the Kanzi data source plugin written in Rust language.

2.

Click Create.

Kanzi Studio creates a project with the application code boilerplate written in linked extendable C++ and Rust parts.

See how to [Build a Kanzi Rust application](https://docs.kanzi.com/rust/latest-4-0-rust/using-rust-in-application.html#build-a-k-rust-application) or [Build a Kanzi Engine Rust plugin](https://docs.kanzi.com/rust/latest-4-0-rust/using-rust-plugins.html#build-a-kr-rust-plugin).

Kanzi Rust API application templates also come with ready-made Visual Studio Code launch and task configs.
