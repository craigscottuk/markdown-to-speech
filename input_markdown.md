Let’s take a look at how we can make edits to an offer.

Offers often change while the customer is still deciding on the setup or design — so the system is built to allow flexibility at this stage.

There are two main ways the team can make updates: either directly in the **OFFERS** sheet, or through a more structured interface using a secondary spreadsheet — a template I’ve called the **Project Manager Tool**.

Let’s start with the **OFFERS** sheet.

Each row here remains fully editable until the offer is marked as **PAID** and moved into one of the production tabs. This means sales team members can update components, delivery dates, or customer details directly in the row — just like working in any other spreadsheet.

To access the full offer data, we expand the grouped columns on the far right side of the sheet. This reveals the configuration details and other editable fields that make up the offer.

Each column in this section represents a **specific component category** used in a bike build — like **Bottom Bracket**, **Crankset**, **Front Chainring**, or **Brake Lever**. To help users make updates quickly and accurately, each cell includes a dropdown menu with a **predefined list of valid options**. This limits inputs to a curated list, prevents typos or inconsistent naming, and helps users select parts without needing to memorise model numbers.

It’s important that part names match exactly with those stored in the system — because the entries here are checked against the **PARTS INDEX** sheet, which is part of the Inventory & Parts Management spreadsheet.

If a part is mistyped or missing from the **PARTS INDEX**, a Google Sheets data validation rule will flag the cell — shown by a small red triangle in the top right corner — and display a warning.

That same invalid item is also flagged in the **Unknown Items** column under the red **COST OF CONFIG & CHECK** headers. Conditional formatting draws attention to the issue — a red background with yellow text appears in the affected row. Clicking the highlighted cell shows a dropdown listing the unrecognised part and its quantity.

You’ll also notice that both the **System Price** and **Offer Price** cells turn red — because the system can’t calculate a proper price without knowing the cost of every component.

To resolve this, either fix the typo — or if it’s a real part — add it to the **PARTS INDEX**. Once that’s done, the system will recognise the part, and the error will disappear.

There are other validation checks in place too — for example, duplicated IDs are flagged to avoid repeated entries. The cleaner the data is at this early stage, the smoother everything runs later on.
