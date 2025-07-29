Before we wrap up this section, let’s take a look at how **Available Stock** and **Allocated Stock** work at this stage — and how they respond to project movements across the system.

To make this as clear and easy to follow as possible, we’ll start by clearing out the current inventory.

We’ll open the **STOCK IN** sheet inside the **Parts & Inventory Management** spreadsheet and delete all the entries — removing all existing stock. If we jump to the **STOCK LEVELS** sheet, you’ll notice it now reflects this change: every item shows **0** in **Total Stock**, **Available Stock**, and **Allocated to Assembly**.

Now, if we return to the **PAINTING & PARTS** sheet, we can see the impact across all projects. As expected, the **Parts Availability** and **Percentage** columns now show **0** across the board and are highlighted in red, indicating that no components are currently in stock.

The dropdowns in the **Missing** column, however, are still showing stale values from before the stock reset — but if we click into **Donaldson’s** row, we can see that all 26 missing components are listed. This simply means the dropdowns haven’t refreshed yet. Reloading the sheet will update these values across all projects.

If we open **Donaldson** in the **Project Manager**, we’ll also see that every component is still registered as missing and highlighted in red.

To demonstrate how **Available Stock** works in the system, let’s add the full list of components required for **Donaldson**’s build back into the inventory. This will allow us to track the movement of a single project and clearly show how the inventory and production spreadsheets interact with each other.
