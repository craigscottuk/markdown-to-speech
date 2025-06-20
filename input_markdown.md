Each column in this section represents a **specific component category** used in a bike build — like **Bottom Bracket**, **Crankset**, **Front Chainring**, or **Brake / Shift Lever**.

---

If a part is mistyped or missing from the **PARTS INDEX**, a Google Sheets data validation rule will flag the cell and display a warning.

That same invalid item is also flagged in the _Unknown Items_ column, under the _COST OF CONFIG & CHECK_ section. Conditional formatting highlights the issue with a red background and yellow text. Clicking the highlighted cell opens a dropdown listing the unrecognised part and its quantity.

You’ll also notice that both the **System Price** and **Offer Price** cells turn red — because the system can’t calculate a proper price without knowing the cost of every component.

To resolve this, we can either fix the typo — or, if it’s a valid part, add it to the **PARTS INDEX**. In this case, we’ll add it to the index. We’ll open the **Inventory & Parts Management** spreadsheet, create a new row, and enter the part’s details. Once that’s done, refreshing the **Offer & Production Management** spreadsheet will update the system — the part will be recognised, and the error will disappear.

There are other validation checks in place too — for example, duplicated IDs are flagged to avoid repeated entries. The cleaner the data is at this early stage, the smoother everything runs later on.
