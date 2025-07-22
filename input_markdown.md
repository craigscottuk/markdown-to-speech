The **STOCK OUT** sheet is used to log parts that have been sold or removed from inventory — typically surplus items sold through the online shop.  
This doesn’t include parts used for builds, which are managed separately by the system.

Just like in the **STOCK IN** sheet, each row here represents a single stock entry.

To record an item, we take the same approach — by entering or selecting the **Item ID** from the dropdown in column C.  
In this example, let’s paste in the item code for the part we entered earlier in **STOCK IN**, and hit Enter.

Next, we manually enter:

- The number of units sold — let’s enter 999 to deduct 999 units.
- And the **Gross Price**, in PLN, including VAT — the unit price the item was sold for.

The **Gross Value** is calculated automatically by multiplying the quantity by the unit price.

This sheet also feeds into the **STOCK LEVELS** sheet, where it reduces the **Total Stock** and updates the **Available** count.

If we search for this item in **STOCK LEVELS**, we can see that 999 units have been deducted from the original 1,000 — leaving just 1 unit in both **Total Stock** and **Available Stock**.

Let’s move over to the **STOCK OFFSET** sheet to see how we can remove this last remaining unit.
