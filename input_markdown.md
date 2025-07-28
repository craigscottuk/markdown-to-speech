Before we wrap up this section, let's take a look at how **Available Stock** and **Allocated Stock** work in the system – and how they respond to project movements across the system.

To keep things simple for this demonstration, let’s start by resetting the current inventory.

We’ll open the **STOCK IN** sheet inside the **Parts & Inventory Management** spreadsheet and delete all the entries — clearing out the existing stock. You’ll notice that the **STOCK LEVELS** sheet now reflects this change: every item shows **0** in **Total Stock**, **Available Stock**, and **Allocated to Assembly**.

Now, if we return to the **PAINTING & PARTS** sheet, we can see the impact across all projects. The **Parts Availability** and **Percentage** columns are all red — and if we scroll down to **Donaldson**, it’s dropped back to **0 out of 26 parts available**, with **0% readiness**.

The dropdowns in the **Missing** column are still showing the stale values from before the stock reset — but if we click inside, they’re empty. Refreshing the sheet will update these values across all projects.

To show how **Available Stock** works at this stage, let’s add the full list of components required for **Donaldson**'s build.

We’ll open the **STOCK IN** sheet again, and paste in the **Item Codes** for each of the missing parts. The product data auto-fills, and we’ll enter a quantity of **1** for each — except for **inner tubes** and **tyres**, where we’ll enter **2 units**.

Let’s take a quick look at the **STOCK LEVELS** sheet to see how things look now.

We’ll tick this checkbox in the header to filter the list to only show items that are currently in stock. Here, we can see the full list of parts for Donaldson that we just added — all marked as **Available**, and none yet **Allocated**. This means every component is ready for use in any eligible project in the **PAINTING & PARTS** stage.

Jumping back to the **PAINTING & PARTS** stage, we can now see that **Donaldson** has **26 out of 26 parts available**, and the percentage column is once again green — showing 100% readiness.

At the same time, we can see that other projects have partially recovered — some now show **10%**, **20%**, or **40%** availability. That’s because some of the parts we just added are compatible with multiple builds, and since they haven’t yet been allocated to a specific project, they remain available for others.

This demonstrates how **Available Stock** represents what’s physically on hand — and how that availability can be shared across multiple projects depending on demand.

Since **Donaldson** is now at 100%, it makes sense to allocate these parts and move the project into the next stage.

Let’s do that now and see what happens in the inventory.

We’ll scroll to the right-hand side of the **PAINTING & PARTS** sheet. First, we’ll update the status to **PARTS READY** — meaning all required components have been collected from storage and packed for this build.

Then we’ll tick the checkbox for **Donaldson** in the **Send** column and click the **Send** label at the top. This triggers a script that moves the project into the **ASSEMBLY & TESTING** stage. A confirmation prompt appears — we’ll click **Yes**.

Now, let’s jump back to the **STOCK LEVELS** sheet and take a look at what’s going to change.

Keep an eye on the **Allocated to Assembly** column. You’ll see that it’s now populated with the values that were previously in the **Available Stock** column — and **Available Stock** is now **0** for those parts.

This means all the components for **Donaldson** have been booked — and are no longer available to other projects. However, the **Total Stock** remains unchanged, since the items are still physically onsite and tracked within the system.

This clearly shows how the system distinguishes between:

- what’s in the building (**Total Stock**),
- what’s still up for grabs (**Available Stock**),
- and what’s already been booked for upcoming builds (**Allocated to Assembly**).

Back in the **Offer & Production Management** spreadsheet, we can see that the transfer is complete. We’ll click **OK** to dismiss the prompt.

Looking at the **PAINTING & PARTS** sheet, **Donaldson** has now been removed, and if we check the **Parts Preparation** section, all projects are showing **0 parts available** and **0% readiness** — with red conditional formatting applied once again.

And if we switch over to the **ASSEMBLY & TESTING** sheet, we can now see **Donaldson** listed there — ready for the next phase of production, which we’ll cover in the next video.
