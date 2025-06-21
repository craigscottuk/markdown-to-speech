Now let’s take a look at how we can make edits using the **Project Manager Tool**.

To open an offer, simply tick the checkbox next to the project ID and name. Since Google Sheets doesn’t support real buttons inside cells, this checkbox acts as a lightweight workaround to launch the selected offer in the Project Manager.

Ticking it triggers a script that opens the Project Manager spreadsheet — a dedicated template — and pulls in the corresponding offer from the main system.

The Project Manager displays the same offer, but in a vertical layout, with information grouped into tabbed sections: **Status**, **Price**, **Dates**, **Configuration**, **Design**, and **Customer**.

Editable fields are shown with a light-shaded background. Let’s go to the **Design** tab and update the paint colour from blue to yellow — and change the price from 100 zł to 500 zł.

We’ll also jump to the **Configuration** tab and switch the front chainring from a 48T to a 50T model using the dropdown.

Now, if we return to the main **Offer & Production Management** spreadsheet, we’ll see the changes have been applied. Opening the configuration dropdown confirms the update — the chainring now shows the 50T model.

All of this is handled by Google Apps Script, which keeps both spreadsheets synced automatically.

The Project Manager offers a faster, more focused way to work — allowing users to concentrate on one project at a time and navigate via tabs, rather than scrolling across dozens of columns while looking at a single row.

Error checking is also built in. If we enter a typo in the configuration, conditional formatting highlights the issue immediately. Because the Project Manager imports the **PARTS INDEX** from the **Parts & Inventory** spreadsheet, it can detect unrecognised items in the same way as the main system.

Switching back to the main spreadsheet, we’ll also see the part flagged there — and the pricing fields highlighted again.

So, edits made in either tool are always synced to the **Offer & Production Management** spreadsheet — keeping everything up to date and consistent.

The Project Manager can also be used later in the process, once a project has moved into production. At that stage, the **Status** tab provides a detailed overview of progress as the build moves through each phase.

We’ll cover that in a future video — but next, we’ll look at how to generate customer-facing PDFs that summarise an offer or project for sharing with the customer.
