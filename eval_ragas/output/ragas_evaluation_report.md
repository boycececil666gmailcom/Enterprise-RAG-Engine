# RAGAS Pipeline Evaluation Report

### 📊 RAGAS Evaluation Summary

| Metric | Score |
| :--- | :--- |
| **faithfulness** | `0.0000` |
| **answer_relevancy** | `nan` |
| **context_precision** | `0.0000` |
| **context_recall** | `0.0000` |

## Detailed Sample Results

```csv
user_input,retrieved_contexts,response,reference,faithfulness,answer_relevancy,context_precision,context_recall
What is Animations best practices in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Animations best practices]

To create more efficient animations:

- Remove the keyframes that do not affect the precision of an animation.
- Remove the Animation Data channels that do not animate anything.
- Avoid excessive use of bezier interpolation between keyframes, because bezier interpolation is more expensive than linear, step, and smooth step interpolation.
- After you import an animation that is heavily sampled, check whether the keyframes are using Bezier interpolation. To significantly reduce the CPU workload, select all keyframes and use linear interpolation. This rarely has an impact on the visual quality of the animation.
- To dynamically change the size of text in a Text Block node, use the Scale property field of either Render Transformation or Layout Transformation properties, instead of the Font Size property. For example, use this approach when you want to animate the size of text in a Text Block node. When you use the Font Size property to dynamically scale the text, Kanzi creates multiple textures for different font sizes and does not release them from the memory.
**Tip:** In the Kanzi Studio Node Tree window, an indicator next to a node shows when a State Manager, Binding, Data Source Binding, or an Animation overrides the values of some properties in that node.
To navigate to the source of the override in the Kanzi Studio project, right-click the override indicator and select the source you wish to navigate to from the context menu.",0.0,,0.0,0.0
What is Animations best practices in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Animations best practices]

To create more efficient animations:

- Remove the keyframes that do not affect the precision of an animation.
- Remove the Animation Data channels that do not animate anything.
- Avoid excessive use of bezier interpolation between keyframes, because bezier interpolation is more expensive than linear, step, and smooth step interpolation.
- After you import an animation that is heavily sampled, check whether the keyframes are using Bezier interpolation. To significantly reduce the CPU workload, select all keyframes and use linear interpolation. This rarely has an impact on the visual quality of the animation.
- To dynamically change the size of text in a Text Block node, use the Scale property field of either Render Transformation or Layout Transformation properties, instead of the Font Size property. For example, use this approach when you want to animate the size of text in a Text Block node. When you use the Font Size property to dynamically scale the text, Kanzi creates multiple textures for different font sizes and does not release them from the memory.
**Tip:** In the Kanzi Studio Node Tree window, an indicator next to a node shows when a State Manager, Binding, Data Source Binding, or an Animation overrides the values of some properties in that node.
To navigate to the source of the override in the Kanzi Studio project, right-click the override indicator and select the source you wish to navigate to from the context menu.",,,0.0,0.0
What is Removing redundant Animation Data channels in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Removing redundant Animation Data channels]

Whether importing animations from a third-party tool or creating them in Kanzi, animations sometimes contain Animation Data resources that do not animate anything. For example, when you add a keyframe for a Render Transformation by dragging the property from the Properties to the Animation Clip Editor, Kanzi adds an Animation Data resource for all property attributes, even if they have not changed.

Note that the static values in Animation Data resources have higher precedence than the local property values of the node. When you delete a channel with a static value, the local value becomes effective. Because sometimes even static values (Animation Data resources without any keyframes) contain valid information and are needed, consider cleaning up unnecessary animation information on a case by case basis.

To remove the redundant Animation Data resources:

1.

In the Library select Animations > Animation Clips and select your animation clip.
2.

Right-click the animation clip for which you want to remove the redundant Animation Data resources and select Delete Animations with One or Zero Effective Keyframes.

These images show the same Animation Clip before and after removing the Animation Data resources without effective animations.",0.0,,0.0,0.0
What is Removing redundant Animation Data channels in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Removing redundant Animation Data channels]

Whether importing animations from a third-party tool or creating them in Kanzi, animations sometimes contain Animation Data resources that do not animate anything. For example, when you add a keyframe for a Render Transformation by dragging the property from the Properties to the Animation Clip Editor, Kanzi adds an Animation Data resource for all property attributes, even if they have not changed.

Note that the static values in Animation Data resources have higher precedence than the local property values of the node. When you delete a channel with a static value, the local value becomes effective. Because sometimes even static values (Animation Data resources without any keyframes) contain valid information and are needed, consider cleaning up unnecessary animation information on a case by case basis.

To remove the redundant Animation Data resources:

1.

In the Library select Animations > Animation Clips and select your animation clip.
2.

Right-click the animation clip for which you want to remove the redundant Animation Data resources and select Delete Animations with One or Zero Effective Keyframes.

These images show the same Animation Clip before and after removing the Animation Data resources without effective animations.",,,0.0,0.0
What is Removing redundant Animation Data channels in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Removing redundant Animation Data channels]

Whether importing animations from a third-party tool or creating them in Kanzi, animations sometimes contain Animation Data resources that do not animate anything. For example, when you add a keyframe for a Render Transformation by dragging the property from the Properties to the Animation Clip Editor, Kanzi adds an Animation Data resource for all property attributes, even if they have not changed.

Note that the static values in Animation Data resources have higher precedence than the local property values of the node. When you delete a channel with a static value, the local value becomes effective. Because sometimes even static values (Animation Data resources without any keyframes) contain valid information and are needed, consider cleaning up unnecessary animation information on a case by case basis.

To remove the redundant Animation Data resources:

1.

In the Library select Animations > Animation Clips and select your animation clip.
2.

Right-click the animation clip for which you want to remove the redundant Animation Data resources and select Delete Animations with One or Zero Effective Keyframes.

These images show the same Animation Clip before and after removing the Animation Data resources without effective animations.",0.0,,0.0,0.0
What is Removing redundant Animation Data channels in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Removing redundant Animation Data channels]

Whether importing animations from a third-party tool or creating them in Kanzi, animations sometimes contain Animation Data resources that do not animate anything. For example, when you add a keyframe for a Render Transformation by dragging the property from the Properties to the Animation Clip Editor, Kanzi adds an Animation Data resource for all property attributes, even if they have not changed.

Note that the static values in Animation Data resources have higher precedence than the local property values of the node. When you delete a channel with a static value, the local value becomes effective. Because sometimes even static values (Animation Data resources without any keyframes) contain valid information and are needed, consider cleaning up unnecessary animation information on a case by case basis.

To remove the redundant Animation Data resources:

1.

In the Library select Animations > Animation Clips and select your animation clip.
2.

Right-click the animation clip for which you want to remove the redundant Animation Data resources and select Delete Animations with One or Zero Effective Keyframes.

These images show the same Animation Clip before and after removing the Animation Data resources without effective animations.",0.0,,0.0,0.0
What is Removing redundant keyframes in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Removing redundant keyframes]

Sometimes animations contain more keyframes than necessary. Kanzi provides an easy way to optimize animation data, which results in a significantly smaller number of keyframes, often without losing the animation precision at all. For example, in the animation shown here there are too many keyframes than is needed for most purposes.

To remove the redundant keyframes:

1.

In the Library > Animations > Animation Clips select your animation clip.
2.

Right-click the animation you want to optimize and select Optimize Animations.
3.

In the Threshold value dialog box enter the threshold value for the keyframe removal and click OK.

Value 0.1 is a good starting point. This removes all keyframes with a delta value smaller than 0.1. Try different values for your animation, because using another value can optimize your animation even more.

If you want to make sure no information is lost, use 0.

This image shows the example animation after removing all keyframes with a delta value smaller than 0.1.",0.0,,0.0,0.0
What is Removing redundant keyframes in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Removing redundant keyframes]

Sometimes animations contain more keyframes than necessary. Kanzi provides an easy way to optimize animation data, which results in a significantly smaller number of keyframes, often without losing the animation precision at all. For example, in the animation shown here there are too many keyframes than is needed for most purposes.

To remove the redundant keyframes:

1.

In the Library > Animations > Animation Clips select your animation clip.
2.

Right-click the animation you want to optimize and select Optimize Animations.
3.

In the Threshold value dialog box enter the threshold value for the keyframe removal and click OK.

Value 0.1 is a good starting point. This removes all keyframes with a delta value smaller than 0.1. Try different values for your animation, because using another value can optimize your animation even more.

If you want to make sure no information is lost, use 0.

This image shows the example animation after removing all keyframes with a delta value smaller than 0.1.",0.0,,0.0,0.0
What is Removing redundant keyframes in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Removing redundant keyframes]

Sometimes animations contain more keyframes than necessary. Kanzi provides an easy way to optimize animation data, which results in a significantly smaller number of keyframes, often without losing the animation precision at all. For example, in the animation shown here there are too many keyframes than is needed for most purposes.

To remove the redundant keyframes:

1.

In the Library > Animations > Animation Clips select your animation clip.
2.

Right-click the animation you want to optimize and select Optimize Animations.
3.

In the Threshold value dialog box enter the threshold value for the keyframe removal and click OK.

Value 0.1 is a good starting point. This removes all keyframes with a delta value smaller than 0.1. Try different values for your animation, because using another value can optimize your animation even more.

If you want to make sure no information is lost, use 0.

This image shows the example animation after removing all keyframes with a delta value smaller than 0.1.",0.0,,0.0,0.0
What is Removing redundant keyframes in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Removing redundant keyframes]

Sometimes animations contain more keyframes than necessary. Kanzi provides an easy way to optimize animation data, which results in a significantly smaller number of keyframes, often without losing the animation precision at all. For example, in the animation shown here there are too many keyframes than is needed for most purposes.

To remove the redundant keyframes:

1.

In the Library > Animations > Animation Clips select your animation clip.
2.

Right-click the animation you want to optimize and select Optimize Animations.
3.

In the Threshold value dialog box enter the threshold value for the keyframe removal and click OK.

Value 0.1 is a good starting point. This removes all keyframes with a delta value smaller than 0.1. Try different values for your animation, because using another value can optimize your animation even more.

If you want to make sure no information is lost, use 0.

This image shows the example animation after removing all keyframes with a delta value smaller than 0.1.",0.0,,0.0,0.0
What is Best practices in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Best practices]

When creating applications for embedded and mobile devices, even seemingly small details can have significant impact on the performance of your Kanzi application on target devices. Kanzi graphics pipeline is optimized to allow 60 frames per second for 3D instrument clusters and human-machine interfaces. Use the best practices covered in this section of documentation to create optimal Kanzi applications for your target hardware.

Even though Kanzi provides many ways that enable you to create applications that consume less memory, CPU and GPU capacity, and device battery, how you create your application has a large impact on its efficiency.",0.0,,0.0,0.0
What is Best practices in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Best practices]

When creating applications for embedded and mobile devices, even seemingly small details can have significant impact on the performance of your Kanzi application on target devices. Kanzi graphics pipeline is optimized to allow 60 frames per second for 3D instrument clusters and human-machine interfaces. Use the best practices covered in this section of documentation to create optimal Kanzi applications for your target hardware.

Even though Kanzi provides many ways that enable you to create applications that consume less memory, CPU and GPU capacity, and device battery, how you create your application has a large impact on its efficiency.",0.0,,0.0,0.0
How to use Thread safety in Best practices?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Best practices > Thread safety]

Kanzi is thread-agnostic and does not guarantee thread safety. To make your Kanzi application code thread-safe:

- Do not call Kanzi functions from custom threads unless the API documentation specifies that you can call the function from any thread.
- Synchronize between threads all access to shared data.",0.0,,0.0,0.0
How to use Thread safety in Best practices?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Best practices > Thread safety]

Kanzi is thread-agnostic and does not guarantee thread safety. To make your Kanzi application code thread-safe:

- Do not call Kanzi functions from custom threads unless the API documentation specifies that you can call the function from any thread.
- Synchronize between threads all access to shared data.",0.0,,0.0,0.0
How to use Pay attention to the log messages in Best practices?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Best practices > Pay attention to the log messages]

Kanzi prints warnings and errors to the Kanzi Studio Log window and the Kanzi debug console to help you find the problems and bottlenecks in your Kanzi application. Pay careful attention to these messages. To ensure that your Kanzi application works correctly and performs optimally on your target platform, resolve all the issues shown in the warnings and errors. Even seemingly unimportant warnings can have a significant impact on the loading times and performance of your Kanzi application. For example, see Adjusting the data size.",0.0,,0.0,0.0
How to use Use the Kanzi Command Prompt in Best practices?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Best practices > Use the Kanzi Command Prompt]

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.

See Using the Kanzi Command Prompt.",0.0,,0.0,0.0
How to use Use the Kanzi Command Prompt in Best practices?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Best practices > Use the Kanzi Command Prompt]

The Kanzi Command Prompt opens the Windows Command Prompt with the Kanzi environment variables set for the version of Kanzi for which you open a Kanzi Command Prompt.

Use the Kanzi Command Prompt to access Kanzi utilities and build tools, such as Gradle and CMake, without using absolute paths or setting environment variables.

See Using the Kanzi Command Prompt.",0.0,,0.0,0.0
How to use Kanzi best practices in Best practices?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Best practices > Kanzi best practices]

Here you can find the information about best practices when working with Kanzi.  [](start-up-time.html)

Performance   [](animations/animations-best-practices.html)

Animations   [](images-and-textures/images-and-textures-best-practices.html)

Images   [](meshes/meshes-best-practices.html)

Meshes   [](rendering/rendering-best-practices.html)

Rendering   [](shaders/shaders-best-practices.html)

Shaders   [](using-kanzi-command-prompt.html)

Kanzi Command Prompt   [](../working-with/projects/cleaning-up-a-project.html)

Cleaning projects",0.0,,0.0,0.0
How to use Kanzi best practices in Best practices?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Best practices > Kanzi best practices]

Here you can find the information about best practices when working with Kanzi.  [](start-up-time.html)

Performance   [](animations/animations-best-practices.html)

Animations   [](images-and-textures/images-and-textures-best-practices.html)

Images   [](meshes/meshes-best-practices.html)

Meshes   [](rendering/rendering-best-practices.html)

Rendering   [](shaders/shaders-best-practices.html)

Shaders   [](using-kanzi-command-prompt.html)

Kanzi Command Prompt   [](../working-with/projects/cleaning-up-a-project.html)

Cleaning projects",0.0,,0.0,0.0
What is Adjusting the data size in Kanzi?,['Error'],Error executing RAG pipeline via HTTP API.,"[Document Context: Adjusting the data size]

When you use the correct data sizes for images, textures and shaders you reduce the memory requirements. Adjust the data size to reflect the requirements of your application:

- If the screen resolution of the target devices is low, make sure the texels of the texture match the pixels of the target screen. For example, when you have a 50 by 40 pixels textured button on a screen 320 by 200 pixels, the optimal size of the texture that returns the best quality is a 50 by 40 pixels texture. You can combine image downscaling with image compression. Try to find a compromise between required visual quality and application performance. See Compressing textures.
- You have to have a really good reason to use textures larger than 1024 pixels. If texture is 1024 pixels wide or high and contains a repeating pattern, extract the smallest repeating pattern and in the texture set the Wrap Mode to Repeat.
- The memory required by a texture corresponds directly to the texture format you use. For example, an 8-bit grayscale texture requires 8 bits for each pixel, whereas RGBA8 requires four 8-bit channels (32 bits for each pixel).
- Make sure that all faces of a cubemap texture use images of the same size and format. When the size and format of the images in a cubemap texture do not match, Kanzi uses the default cubemap texture.

For example, for all faces of a cubemap texture use images that are 256 by 256 pixels large and are 8-bit grayscale.

When the size and format of the images in a cubemap texture do not match, Kanzi Studio uses red type to mark such textures.
- Use mipmaps to create a set of downscaled sublevels from a large texture. Mipmaps increase the GPU memory use by one third, but improve the performance when the full texture does not have to be sampled. Use mipmaps to improve the performance whenever you scale a textured node.

See Using mipmaps.

Avoid creating textures from very large images. For example, do not create tex",0.0,,0.0,0.0

```
