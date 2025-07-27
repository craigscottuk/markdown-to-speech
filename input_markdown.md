We’re now back in the **PAINTING & PARTS** sheet of the **Offer & Production Management** spreadsheet. Returning to our example project — **Donaldson** — we can see that it’s still missing three components.

If we expand the dropdown in the **Missing** column, we get a list of the items that are currently unavailable, along with the required quantities.

We can also view this information from inside the **Project Manager**. Let’s open it by ticking the checkbox next to the project.

Inside the **Status** tab — where we land by default — we see a summary of the project’s health, including the number of missing items and their total net cost. Scrolling further down reveals the full configuration for this build, with the three missing items highlighted in red. Each is listed alongside the quantity still needed.

The **Project Manager** also pulls live data from the **Parts & Inventory Management** spreadsheet.

Let’s take a look at how the production and inventory spreadsheets work together. Imagine we’ve just received a delivery containing exactly the three missing components for this project.

We’ll start by copying the item codes for these missing items, and then head over to the **STOCK IN** sheet, located in the **Parts & Inventory Management** spreadsheet.

We can jump to the bottom of the sheet using the keyboard shortcut **Cmd + ↓** (or **Ctrl + ↓** on Windows), and then paste in the item codes.

The remaining columns auto-fill based on the data stored in the **PARTS INDEX** sheet, and today’s **Date** is automatically added in column B. We’ll now enter a quantity of **1** for each, since we’ve received a single unit of each part.

Once entered, these items are now officially part of our available stock.

If we switch back to the **Project Manager**, we’ll see the status has updated in real time — all items are now in stock for **Donaldson**.

Closing the **Project Manager** and returning to the **PAINTING & PARTS** sheet, we can now see that **Donaldson** has **26 out of 26 parts available**, and both the **Availability** and **Percentage** columns are highlighted in green — indicating the project is ready to move forward.

However, if we look at the **Missing** column, it still shows a value of **3**. Clicking into it, we’ll notice that the dropdown appears empty and a validation warning is displayed.

This means the system recognises that the current value no longer matches the dropdown options — because there are no longer any missing parts to display.

A quick refresh of the spreadsheet will clear this up, and the **Missing** column will update to reflect the current status.

This live link between the inventory system and production sheets is what keeps everything in sync — helping the team stay up to date on part availability and project readiness in real time.
