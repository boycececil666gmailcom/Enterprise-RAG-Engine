---
title: Setting transitions between Page nodes
source: https://docs.kanzi.com/4.1.0/en/working-with/pages/using-page-transitions.html
---

# Setting transitions between Page nodes
**Note:** The Page and Page Host nodes are deprecated. Use the Activity and Activity Host nodes to build navigable UIs for your application. See Activities.
Kanzi by default uses the Push transition for transitions between Page and Page Host nodes. You can create your own transitions using:
- Transition Presets to set to and from transitions between Page and Page Host nodes.
- Animations to set or customize transitions between Page and Page Host nodes.

In Kanzi transitions are resources you can reuse. You can see transitions in a Kanzi Studio project in the Library > Page Transitions.
## Setting transitions between Page and Page Host nodes

To set the transitions between Page and Page Host nodes:

1.

Create a user interface structure using Page and Page Host nodes. See Using the Page and Page Host nodes.
2.

In the Pages click Transitions to show the Transitions editor in the Pages.
3.

In the Pages click any Page or Page Host node to select it and in the Transitions editor click  to create a transition.

The Transitions editor shows the transitions used by the Page or Page Host node you select either in the Pages or the Node Tree. When you create a transition, Kanzi Studio by default uses the Push transition.
4.

In the Transitions editor drag from the Transition Presets a transition and drop it below the Default transition.

That way you add a transition to the Default transition between this and any other Page or Page Host node.

For example, drag the Flip transition from the Transition Presets and drop it below the Default transition in the Transitions editor.

In the Preview when you start a transition either from or to the Page node for which you set the transition type, Kanzi uses the transition you set.

Carousel

Cube

Fade

Flip

Hinge

Push

Rotate

Scale

Slide

Swivel
5.

To configure the transition, in the Transitions editor click  and in the popup window set:

  - Duration to the length of the transition in milliseconds.
  - From to the Page or Page Host node to which you want to apply this transition when you navigate from that node.
  - To to the Page or Page Host node to which you want to apply this transition when you navigate to that node.
  - Direction to whether the transition applies to the transition from the node you set in the From property to the node you set in the To property, or to the transitions from both nodes:

    - Bidirectional applies the transition to the transition from the node in the From property to the node in the To property, and from the node in the To property to the node in the From property.
    - Unidirectional applies the transition only to the node in the From property to the node in the To property.

## Creating transition animations

Use transition animations to set transitions between Page and Page Host nodes, or to customize transitions.

To create a transition animation:

1.

In the Library > Page Transitions press Alt and right-click the transition to which you want to add a transition animation and select Page Transition Animation.
2.

In the Library select the transition animation you created in the previous step and in the Properties set:

  - Animation Target to:

    - Page In to use the animation when navigating to the set Page or Page Host node
    - Page Out to use the animation when navigating from the set Page or Page Host node

  - Transition Property to the property you want to animate.
  - Start Value to the value of the Transition Property when the transition animation starts.
  - End Value to the value of the Transition Property when the transition animation ends.

3.

To set a Page or Page Host to use the transition animation you created, in the Node Tree select that Page or Page Host node, and in the Properties set the Transitions property to the transition which uses the animation.

## Adding transition animations to transitions

To customize a transition you can add a transition animation to an existing transition.

To add a transition animation to a transition:

1.

In the Pages click Transitions to show the Transitions editor in the Pages.
2.

In the Pages select the Page or Page Host node to which you want to add a transition animation and in the Transitions editor from the Animations drag an animation to the transition you want to customize.

For example, drag the Scale animation to the Default transition to add scale animation to the Default transition.
3.

(Optional) To customize a transition animation, in the Library > Page Transitions expand the transition which uses that animation, select the transition animation, and in the Properties set:

  - Start Value to the value of the Transition Property when the animation starts.
  - End Value to the value of the Transition Property when the animation ends.

## Starting transitions between Page nodes in your application

When you click a Page or a Page Host node in the Pages, in the Preview you can see the transition. However, to transition between the nodes in your application you need to use a trigger with one of the Navigate to actions.

To start a transition between Page nodes in your application:

1.

Create a user interface structure using Page and Page Host nodes. See Using the Page and Page Host nodes.
2.

In the Node Tree create a control that you want to use to navigate between Page and Page Host nodes.

For example, in the Page Host node RootPage create a Button 2D node. See Using the Button nodes.
3.

In the Node Tree select the control you created in the previous step, in the Node Components > Triggers section press Alt and right-click the trigger type that you want to use for the navigation, and select an action:

  - Page: Navigate to Page goes to the node you set in this action.
  - Page Host: Navigate to Next goes to the sibling node which is on the right side of the current node as shown in the Pages.
  - Page Host: Navigate to Previous goes to the sibling node which is on the left side of the current node as shown in the Pages.
  - Page: Navigate to Parent goes to the node that is the parent node of the node you select in this action.

For example, select the Page Host: Navigate to Next action and set the action to the RootPage node.
4.

In the action settings, set:

  - Target Item to the node on which you want to execute the action. To set the target node for the action with a property, set the Define Target with Property property to enabled and set:

    - Target Item to the node that contains the property which you want to use to set the target node
    - Property to the property that you want to use to set the target Page Host node. When you use a custom property type, in that property type set:

      - Data Type to Project Item
      - Editor to Page selector

See Creating property types.

  - (Optional) To make the transition without a transition animation, set the Immediate property to enabled.

In the Preview click the control you created to navigate between Page and Page Host nodes. Every time you click the control you advance one page to the right: Home to Music, Music to Car, Car to Home, and so on.
## Using page transitions in the API

For details, see the `PageTransitionCollection` class.
