The **STOCK OUT** sheet is used to log parts that have been sold or removed from inventory.  
This typically applies to surplus parts sold via the online shop — not parts used for builds, which are managed separately by the system.

Just like in the **STOCK IN** sheet, each row here represents a single stock entry — in this case, something leaving the system.

To record an item, we start by entering or selecting the **Item ID** from the dropdown in column C.  
In this example, let’s paste in the item code for the part we entered earlier in **STOCK IN**, then hit Enter.

The **Date** in column B is also filled in automatically — just like in **STOCK IN**.

Next, we manually enter:

- **Quantity (QTY)** — the number of units sold or removed. Let’s enter 999 to deduct 999 units.
- And the **Gross Price**, in PLN, including VAT — the unit price the item was sold for.

The **Gross Value** is calculated automatically by multiplying the quantity by the unit price.

This gives us a clear picture of what’s been sold or removed — helping track surplus sales separately from production-related stock movement.

This sheet also feeds into the **STOCK LEVELS** sheet, where it reduces the **Total Stock** and updates the **Available** count.

If we search for this item in **STOCK LEVELS**, we can see that 999 units have been deducted from the original 1,000 — leaving just 1 unit in both **Total Stock** and **Available Stock**.
