---
title: Creating animations and timelines using the Kanzi Engine API
source: https://docs.kanzi.com/4.1.0/en/working-with/animations/creating-animations-using-api.html
---

# Creating animations and timelines using the Kanzi Engine API


The Kanzi animation system consists of animations and timelines. Animations define how values of specific type change in time, and timelines map animations to the properties of objects you want to animate.

You can use the Kanzi Engine API to create animations and timelines:

- From-to animation defines from which to which value to change the value of a property. You can omit either of these values to animate either from the current value or to the current value of the property. From-to animations use an easing curve that defines the rate of change for the animation. You can use one of the easing curves that comes with Kanzi, or define your own.

To create from-to animations using the Kanzi Engine API, see Creating from-to animations using the Kanzi Engine API.
- Keyframe animation uses keyframes that define the property value and time at which the animation reaches that value. In Kanzi you can create linear, step, and BÃ©zier spline keyframes.

To create keyframe animations using the Kanzi Engine API, see Creating keyframe animations using the Kanzi Engine API.
- Property timeline applies an animation to a property of an object. For example, to change the layout size of an Image node, use the property timeline to animate the Layout Width and Layout Height properties of the node.

To create property timelines using the Kanzi Engine API, see Creating property timelines using the Kanzi Engine API.
- Property field timeline applies an animation to one or more fields of a property of an object. For example, you can use a separate animation for each color channel to change the color of the text in a Text Block node.

To create property field timelines using the Kanzi Engine API, see Creating property field timelines using the Kanzi Engine API.
- Parallel timeline allows you to group timelines which Kanzi plays at the same time. A parallel timeline ends when the animations in the last child timeline end. Use this timeline to organize collections of timelines and create a composition of timelines.

To create parallel timelines using the Kanzi Engine API, see Creating parallel timelines using the Kanzi Engine API.
- Timeline playback properties allow you to define how Kanzi plays timeline content. For example, you can set the speed, number of repetitions and playback direction of animations. See Configuring timelines using the Kanzi Engine API.

## Creating from-to animations using the Kanzi Engine API


From-to animation defines from which to which value to change the value of a property. You can omit either of these values to animate either from the current value or to the current value of the property. From-to animations use an easing curve that defines the rate of change for the animation. You can use one of the easing curves that comes with Kanzi, or define your own.

To create a from-to animation:

```
// Create a from-to animation that uses the linear easing function and is two seconds long.
// As a starting value, the animation takes the current value of the property in the node you want to animate.
// The animation sets the final value of the property in the node you animate to 200.
// You set which node this animation animates in the timeline.
FloatLinearFromToAnimationSharedPtr linearAnimation = FloatLinearFromToAnimation::create(domain, chrono::seconds(2), nullopt, 200.0f);

```


To animate a property value in a node using a from-to animation:

```
// Create a property timeline and apply the linearAnimation from-to animation to the Layout Width property
// to animate the width of the current node.
PropertyAnimationTimelineSharedPtr propertyTimeline = PropertyAnimationTimeline::create(domain, ".", Node::WidthProperty, linearAnimation);

```


To animate a property field value in a node using a from-to animation:

```
// Create a property field animation timeline and apply it to the Render Transformation property of the current node.
PropertyFieldAnimationTimelineSharedPtr propertyFieldTimeline = PropertyFieldAnimationTimeline::create(domain, ".", Node2D::RenderTransformationProperty);
// Scale the current node on the x axis by animating the Scale X property field of the Render Transformation property
// with the linearAnimation from-to animation.
propertyFieldTimeline->addEntry(PropertyFieldScaleX, linearAnimation);

```


To create a float from-to animation that uses the back easing curve and the ease out easing mode:

```
// Define the FloatBackFromToAnimation to use float values and Back easing function.
typedef FromToAnimation<float, BackEasingFunction> FloatBackFromToAnimation;
typedef shared_ptr<FloatBackFromToAnimation> FloatBackFromToAnimationSharedPtr;
// Create a from-to animation that uses the back easing function and is 5000 milliseconds long.
// The animation sets the starting value of the property in the node you want to animate to 100,
// and the final value of that property to 300.
FloatBackFromToAnimationSharedPtr backAnimation = FloatBackFromToAnimation::create(domain, chrono::milliseconds(5000), nullopt, 300.0f);
// Set the easing mode of the backAnimation from-to animation to Ease out.
backAnimation->setEasingMode(AnimationEaseOut);

```


To play an animation regardless of the timeline type:

```
// Create the playback context and the timeline playback for the node defined in the item2d.
SceneGraphTimelinePlaybackContext context(*item2d);
// Create the playback for the timeline defined in the propertyFieldTimeline.
TimelinePlaybackSharedPtr playback = propertyFieldTimeline->createPlayback(context);
// Start the animation.
domain->getRootTimelineClock()->addTimelinePlayback(playback);

```


For details, see the `FromToAnimation` class.
## Creating keyframe animations using the Kanzi Engine API


Keyframe animation uses keyframes that define the property value and time at which the animation reaches that value. In Kanzi you can create linear, step, and BÃ©zier spline keyframes.

To create a keyframe animation:

```
// Create a float keyframe animation.
FloatKeyframeAnimationSharedPtr keyframeAnimation = FloatKeyframeAnimation::create(domain);
// Create and add keyframes to the keyframe animation. This keyframe animation contains two linear keyframes.
// Create a linear keyframe at second 0 with the value 0.
keyframeAnimation->addLinearKeyframe(chrono::seconds::zero(), 0.0f);
// Create a linear keyframe at second 1 with the value 100.
keyframeAnimation->addLinearKeyframe(chrono::seconds(1), 100.0f);

```


To animate a property value in a node using a keyframe animation:

```
// Create a property timeline and apply the keyframeAnimation keyframe animation to the Layout Width property
// to animate the width of the current node.
PropertyAnimationTimelineSharedPtr propertyTimeline = PropertyAnimationTimeline::create(domain, ".", Node2D::WidthProperty, keyframeAnimation);

```


To animate a property field value in a node using a keyframe animation:

```
// Create a property field animation timeline and apply it to the Render Transformation property of the current node.
PropertyFieldAnimationTimelineSharedPtr propertyFieldTimeline = PropertyFieldAnimationTimeline::create(domain, ".", Node2D::RenderTransformationProperty);
// Rotate the current node by animating the Rotation Z property field of the Render Transformation property
// with the keyframeAnimation keyframe animation.
propertyFieldTimeline->addEntry(PropertyFieldRotationZ, keyframeAnimation);

```


To create a keyframe animation that uses Bezier keyframes to move an object on a sideways figure eight shaped path:

```
// Create two float keyframe animations: one to animate the object on the x axis,
// the other to animate the object on the y axis.
// Create float keyframe animation keyframeAnimationX that uses linear keyframes
// to animate the movement of the object on the x axis.
FloatKeyframeAnimationSharedPtr keyframeAnimationX = FloatKeyframeAnimation::create(domain);
// Create a linear keyframe at second 0 with the value 0.
keyframeAnimationX->addLinearKeyframe(chrono::seconds::zero(), 0.0f);
// Create a linear keyframe at second 4 with the value 4.
// At this keyframe the object reaches the furthest point on the x axis.
keyframeAnimationX->addLinearKeyframe(chrono::seconds(4), 4.0f);
// Create a linear keyframe at second 8 with the value 0.
// At this keyframe the object returns to the same position it had at the first keyframe.
keyframeAnimationX->addLinearKeyframe(chrono::seconds(8), 0.0f);

// Create float keyframe animation keyframeAnimationY that uses Bezier keyframes
// to animate the movement of the object on the y axis.
FloatKeyframeAnimationSharedPtr keyframeAnimationY = FloatKeyframeAnimation::create(domain);
// Create a linear keyframe at second 0 with the value 0. When you use Bezier keyframes,
// you can use any type of keyframe for the first keyframe, because you need this keyframe
// only to provide the information for the starting position.
keyframeAnimationY->addLinearKeyframe(chrono::seconds::zero(), 0.0f);
// Create a Bezier keyframe at second 4 with the value 0 and two control points.
// You use the control points to set the position of the keyframe.
keyframeAnimationY->addBezierKeyframe(chrono::seconds(4), 0.0f, Vector2(0.5f, 4.0f), Vector2(0.5f, -4.0f));
// Create a Bezier keyframe at second 8 with the value 0 and two control points.
// This keyframe uses the same control points, but because the keyframeAnimationX
// animation moves the object on the x axis back to its starting position, this keyframe
// is a mirror image of the previous keyframe.
keyframeAnimationY->addBezierKeyframe(chrono::seconds(8), 0.0f, Vector2(0.5f, 4.0f), Vector2(0.5f, -4.0f));

// Create a property field animation timeline and apply it to the Render Transformation property of the current node.
PropertyFieldAnimationTimelineSharedPtr timeline = PropertyFieldAnimationTimeline::create(domain, ".", Node3D::RenderTransformationProperty);
// Move the current node on the x axis by animating the Translation X property field of the Render Transformation property
// with the keyframeAnimationX keyframe animation.
timeline->addEntry(PropertyFieldTranslationX, keyframeAnimationX);
// Move the current node on the y axis by animating the Translation Y property field of the Render Transformation property
// with the keyframeAnimationY keyframe animation.
timeline->addEntry(PropertyFieldTranslationY, keyframeAnimationY);

```


To play an animation regardless of the timeline type:

```
// Create the playback context and the timeline playback for the node defined in the item2d.
SceneGraphTimelinePlaybackContext context(*item2d);
// Create the playback for the timeline defined in the propertyFieldTimeline.
TimelinePlaybackSharedPtr playback = propertyFieldTimeline->createPlayback(context);
// Start the animation.
domain->getRootTimelineClock()->addTimelinePlayback(playback);

```


For details, see the `KeyframeAnimation` class.
## Creating property timelines using the Kanzi Engine API


Property timeline applies an animation to a property of an object. For example, to change the layout size of an Image node, use the property timeline to animate the Layout Width and Layout Height properties of the node.

To create a property timeline:

```
// Create a property timeline and apply the linearAnimation animation to the Layout Width property
// to animate the width of the current node.
PropertyAnimationTimelineSharedPtr propertyTimeline = PropertyAnimationTimeline::create(domain, ".", Node::WidthProperty, linearAnimation);

```


To play an animation regardless of the timeline type:

```
// Create the playback context and the timeline playback for the node defined in the item2d.
SceneGraphTimelinePlaybackContext context(*item2d);
// Create the playback for the timeline defined in the propertyFieldTimeline.
TimelinePlaybackSharedPtr playback = propertyFieldTimeline->createPlayback(context);
// Start the animation.
domain->getRootTimelineClock()->addTimelinePlayback(playback);

```


For details, see the `PropertyAnimationTimeline` class.
## Creating property field timelines using the Kanzi Engine API


Property field timeline applies an animation to one or more fields of a property of an object. For example, you can use a separate animation for each color channel to change the color of the text in a Text Block node.

To create a property field timeline:

```
// Create a property field timeline and apply it to the Render Transformation property of the current node.
PropertyFieldAnimationTimelineSharedPtr propertyFieldTimeline = PropertyFieldAnimationTimeline::create(domain, ".", Node2D::RenderTransformationProperty);
// Scale the current node on the x axis by animating the Scale X property field of the Render Transformation property
// with the linearAnimation animation.
propertyFieldTimeline->addEntry(PropertyFieldScaleX, linearAnimation);

```


To play an animation regardless of the timeline type:

```
// Create the playback context and the timeline playback for the node defined in the item2d.
SceneGraphTimelinePlaybackContext context(*item2d);
// Create the playback for the timeline defined in the propertyFieldTimeline.
TimelinePlaybackSharedPtr playback = propertyFieldTimeline->createPlayback(context);
// Start the animation.
domain->getRootTimelineClock()->addTimelinePlayback(playback);

```


For details, see the `PropertyFieldAnimationTimeline` class.
## Creating parallel timelines using the Kanzi Engine API


Parallel timeline allows you to group timelines which Kanzi plays at the same time. A parallel timeline ends when the animations in the last child timeline end. Use this timeline to organize collections of timelines and create a composition of timelines.

When you add to a parallel timeline child timelines, the union of the child timelines forms the content of the parallel timeline. This means that all playback properties of the parallel timeline are applied to its child timelines.

To create a parallel timeline:

```
// Create a parallel timeline.
ParallelTimelineSharedPtr parallelTimeline = ParallelTimeline::create(domain);
// Add propertyTimeline and propertyFieldTimeline timelines to the parallel timeline. Parallel timeline plays
// both timelines at the same time.
parallelTimeline->addChild(propertyTimeline);
parallelTimeline->addChild(propertyFieldTimeline);

```


To play an animation regardless of the timeline type:

```
// Create the playback context and the timeline playback for the node defined in the item2d.
SceneGraphTimelinePlaybackContext context(*item2d);
// Create the playback for the timeline defined in the propertyFieldTimeline.
TimelinePlaybackSharedPtr playback = propertyFieldTimeline->createPlayback(context);
// Start the animation.
domain->getRootTimelineClock()->addTimelinePlayback(playback);

```


For details, see the `ParallelTimeline` class.
## Configuring timelines using the Kanzi Engine API


A timeline consists of a series of iterations played successively, starting at a specified start time. Each iteration is a continuous portion of timeline content which Kanzi plays in a specific manner. Timeline content can consist of one or more animations, or child timelines.

Timeline playback properties allow you to define how Kanzi plays timeline content. For example, you can set the speed, number of repetitions and playback direction of animations. Kanzi applies timeline properties in this order:

1.

Clipping properties set the portion of timeline content played in an iteration:

  - Clip start time sets the length of time the timeline content skips from the beginning.
  - Clip duration sets the duration of the timeline content.

2.

Duration scale sets how long the (clipped) timeline content takes to play.

For example, if you set duration scale to 2, the timeline content takes twice as long to play as it is defined in the timeline content.

The clipped and duration-scaled timeline content represents the content of an iteration.
3.

Direction behavior sets in which direction the iteration content plays. Set direction behavior to:

  - Normal to make the iteration content play normally
  - Reverse to make the iteration content play in reverse direction
  - PingPong to make the iteration content play normally until the end and then in reverse direction back to the beginning

4.

Repeat count sets how many times the iteration content is repeated. Set repeat count to 0 to make the iteration repeat indefinitely or until it is stopped.
5.

Start time sets when the first iteration of the timeline starts to play. Set start time to:

  - Zero to make the first iteration start to play immediately. This is the default value for start time.
  - Positive value to make the first iteration start to play after the length of time set by start time.
  - Negative value to make Kanzi clip the beginning of the timeline by the length of time set by start time. This makes the timeline act as if it started at some time in the past.


A timeline applies its content only after its global time exceeds the start time property of the timeline. After Kanzi has played the timeline until the end, the timeline applies its content from the end indefinitely until it is removed. If you have a parallel timeline with repeat count set to multiple repeats, and you add to it a timeline with a non-zero positive start time, the child timeline starts playing in the beginning of each iteration of the parallel timeline only after its global time exceeds its start time.

Note that not all combinations of timeline playback properties are valid. For example, if you set the repeat count of a timeline to infinite and add the timeline to a parallel timeline as a child timeline, the content duration of the parallel timeline becomes infinite. In this case it is not allowed to set the direction behavior of the parallel timeline to reverse, because it does not make sense to revert infinite content. If you do set the direction behavior to reverse, Kanzi Engine internally reverts it to normal and prints a warning message to the log.

To start the playback of a timeline:

```
// Create playback context.
SceneGraphTimelinePlaybackContext context(*nodeToAnimate);

// Create playback for timeline.
TimelinePlaybackSharedPtr timelinePlayback = timeline->createPlayback(context);

// Add playback to the clock.
timelineClock->addTimelinePlayback(timelinePlayback);

```


To stop the playback of a timeline:

```
// Remove playback from the clock.
timelineClock->removeTimelinePlayback(*timelinePlayback);

```


To get the start time of a timeline:

```
// Get start time of timeline.
chrono::milliseconds startTime = timeline->getStartTime();

```


To set the start time of a timeline:

```
// Set start time of timeline to 100 milliseconds.
// Playback of timeline will start to perform its first iteration after its global time reaches 100 milliseconds.
timeline->setStartTime(chrono::milliseconds(100));

```


To get the clipping of a timeline:

```
// Get clip start time of timeline.
chrono::milliseconds clipStartTime = timeline->getClipStartTime();

// Get clip duration of timeline.
optional<chrono::milliseconds> clipDuration = timeline->getClipDuration();

```


To set the clipping of a timeline:

```
// Set clip start time of timeline to 100 milliseconds.
// Playback of timeline will perform playback of timeline content starting from 100 milliseconds in each iteration.
timeline->setClipStartTime(chrono::milliseconds(100));

// Set clip duration of timeline to 200 milliseconds.
// Playback of timeline will perform playback of timeline content for 200 milliseconds in each iteration.
timeline->setClipDuration(chrono::milliseconds(200));

```


To get the amount of repeat times of a timeline:

```
// Get repeat count of timeline.
unsigned int repeatCount = timeline->getRepeatCount();

```


To set the amount of repeat times of a timeline:

```
// Set repeat count of Timeline to 10.
// Playback of timeline will perform 10 iterations of timeline content.
timeline->setRepeatCount(10);

// Set repeat count of Timeline to 0.
// Playback of timeline will perform infinite amount of iterations.
timeline->setRepeatCount(0);

```


To get the duration scale of a timeline:

```
// Get duration scale of timeline.
float durationScale = timeline->getDurationScale();

```


To set the duration scale of a timeline:

```
// Set scale of timeline to 4.
// Playback of timeline will be 4 times slower compared to default playback speed and each iteration
// will be 4 times longer compared to iteration duration with default scale.
timeline->setDurationScale(4.0f);

```


To get the direction of a timeline playback:

```
// Get direction behavior of timeline.
enum Timeline::DirectionBehavior directionBehavior = timeline->getDirectionBehavior();

```


To set the direction of a timeline playback:

```
// Set direction behavior of timeline to pingpong.
// Each odd iteration of timeline will play its content normally
// and each even iteration will play it in reverse manner.
timeline->setDirectionBehavior(Timeline::DirectionBehaviorPingPong);

```


For details, see the `Timeline` class.
