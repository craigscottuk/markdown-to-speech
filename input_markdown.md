The **STOCK IN** sheet is where we enter newly purchased parts into the system. Each row represents a single inventory entry — usually copied over from a supplier invoice or delivery note.

To log a new item, we start by entering or selecting the **Item Code** from the dropdown in column C. You can scroll through the full list or start typing to quickly filter results. These codes match the **Item Codes** listed in the **PARTS INDEX**, keeping everything consistent across the system. If you're working from a digital invoice, you can also copy and paste the code straight in for quicker entry.

Once the code is selected, the rest of the product details — like the **Name**, **Manufacturer**, and **Item Category** — are automatically filled in using data from the **PARTS INDEX**. This built-in lookup acts as a safeguard, helping confirm that we’re logging the correct item.

After the item code is added, the **Date** in column B is automatically populated with today’s date – though it can be manually adjusted to match the actual delivery or invoice date.

Next, we manually enter:

- **Quantity (QTY)** — the number of units received
- **Net Price (PLN)** — the unit price listed on the invoice

The **Net Value** is then worked out automatically by multiplying the quantity by the unit price.

The data in this sheet is counted and dynamically fed into the **STOCK LEVELS** sheet, where it contributes to the **Total Stock** and **Available** stock calculations.
