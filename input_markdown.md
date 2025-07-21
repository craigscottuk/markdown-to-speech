This sheet provides a real-time overview of current inventory and parts demand across all active projects.

This sheet is **dynamically generated**, pulling in live data from other sheets within this file — as well as from the production management environment. Because of this, it can’t be edited directly.

Each row represents a unique part from our inventory — whether it's in stock, already allocated to a build, or still needed for an upcoming project. The system combines data from multiple sources to calculate these values automatically:

- **Stock-In, Stock-Out, and Stock-Offset** sheets provide the actual movement of parts into and out of the system.
- The **Parts & Painting** sheet feeds in production demand from projects that are in pre-assembly.
- The **Assembly & Testing** sheet shows how many units are already allocated to builds in progress.
- The **Completed Projects** sheet helps remove parts from stock once bikes are finished.

This all comes together here to give us an up-to-date view of stock on hand, future demand, and any gaps we need to fill.

Each row shows a unique inventory item, identified by:

- **Item Code** – the product or internal reference number
- **Item Name** – the item’s full name
- **Manufacturer** – the brand or supplier
- **Item Category** – category or type (e.g. tyre, headset)

Then we move into the dynamic stock and demand columns:

- **Allocated to Assembly** – the number of units currently assigned to builds in the Assembly & Testing stage
- **Available Stock** – parts physically on-site and ready to be used for upcoming builds
- **Total Stock** – the current on-site inventory, based on all stock movements: added via **Stock-In**, removed via **Stock-Out** and **Completed Projects**, with adjustments from **Stock-Offset**
- **Production Demand** – number of units needed to fulfil current project requirements, based on the Painting & Parts sheet
- **Missing** – any shortfall between the total stock and what’s required for active projects
- **Surplus** – any excess quantity beyond current production needs

Finally, we have the **financial overview**:

- **Net Item Price** – the part’s unit net price net
- **Net Value of Items in Stock** – calculated by multiplying the total stock by the unit price

At the top right, we can see the **estimated net value of all stock** currently on-site — a useful metric for procurement, planning, and insurance purposes.
