Now that the payment has been logged, a yellow checkbox appears next to the amount. Ticking this checkbox flags the project for transfer to production.

We can mark multiple projects as **PAID** — entering each payment, confirming the details, and ticking the checkbox — to batch-transfer several projects at once. This allows the sales team to log payments as they come in, and move projects into production in bulk when ready.

For now, we’ll just send **Donaldson**, so we’ll untick the other project for **Scott** and move only one offer forward.

With our paid project selected, we open the **Send** menu and choose **Send to next stage**. A confirmation window appears, listing the selected projects. In this case, only **Donaldson** is selected, so the process will apply to that project alone.

This triggers a script that gathers all key project data and copies it to two places:

**1. The PRODUCTION sheet**  
**2. The PARTS & PAINTING sheet**

Once the transfer is complete, a prompt appears confirming that the transfer was successful, and the original offer row is moved from the **OFFERS** sheet to the **OFFERS ARCHIVE** — preserving a full historical record of the offer in its pre-production state.

At this point, the offer has transitioned into a project and is officially live — now in the hands of the production team.

Let’s take a look at the areas of the system that the production team are involved with. We’ll start with the main **PRODUCTION** sheet, which provides a general overview of all active projects.

---

### 1. The **PRODUCTION** sheet

The **PRODUCTION** sheet acts as a central overview of all active projects in the production lifecycle. It gives the team a high-level snapshot — showing how each project is progressing, what stage it’s in, and highlighting any delays or issues that might need attention.

At the centre of the sheet, we see three distinct, **colour-coded columns** representing the main stages of production: blue for **Painting & Parts**, turquoise for **Assembly & Testing**, and yellow for **Dispatch & Pick-Up**. Each column displays the project’s latest status within that stage.”

Each of these columns shows the project’s current status in that stage. These updates are pulled directly from the individual stage sheets, and completion dates are added automatically by script as the project moves forward.

If we scroll down, we can find **Donaldson** — the project we just moved into production. It’s currently in the first stage — **Painting & Parts** — with a status of **Not Started**, meaning no action has been taken since it entered this stage.

Now let’s take a quick look at the rest of the sheet.

On the left-hand side, we have the **production acceptance date**, the **deadline**, and a countdown showing the number of **days left**. There’s also a calculated **Priority** score — based on the deadline, project cost, and parts availability — which helps the team focus on the most time-sensitive builds.

Next to that are the usual project details: the **project ID**, the **surname or project name** — clicking the link in this cell opens the latest document for **Donaldson** — as well as the **assigned owner**, and a dropdown showing the bike’s drivetrain configuration at a glance.

There’s also a checkbox that opens the project in the **PROJECT MANAGER**, where we can edit the order or view a more detailed status summary. At the top, we can see that the current stage is **PAINTING & PARTS** and that the project is currently marked as **NOT STARTED**. Below that, we have a bar chart that visualises the number of days spent in each production stage, along with the overall deadline. This gives the team a quick overview of progress and helps track how much time remains.

This isn’t the most exciting example to look at — the project is only on day one of production. So, let’s take a look at another project that’s further along in the process to get a clearer picture.

Let's check out this project here for **Pawłowski**, which is currently in the final stage of production. Like in the previous example, we can see that the current stage is **DISPATCH & PICK-UP**, and the status is marked as **IN PROGRESS**, meaning the bike is likely being packed or prepared for collection.

If we scroll down, the chart now shows a more complete production timeline. This project has already spent a substantial amount of time in the system: 18 days in **PAINTING & PARTS**, 22 days in **ASSEMBLY & TESTING**, and now 3 days in **DISPATCH & PICK-UP**. The grey line above shows the overall project deadline. Altogether, the stacked bar provides a quick visual summary of the time spent — 43 days out of a 53-day timeline — helping the team spot delays and assess whether the project is on track.

Scrolling down a little further, we can see the financial summary for the project: the total price, how much has been paid, and any outstanding balance.

Let’s go back to the **Production** sheet.

On the right-hand side, the **Payments** section tracks key financials — including the currency, VAT rate, **gross bike price**, **amount paid**, and any **remaining balance**. If we scroll back down to the bottom, we can see that Donaldson’s deposit of **3,400 PLN**, which we entered earlier, has been automatically carried over — along with the remaining amount still to be paid.

Finally, this sheet includes the option to **cancel a project**. Selecting **Cancel** from the menu opens a confirmation prompt. If confirmed, the project is removed from its current production stage and from all relevant sheets across the system. In this case, we want to keep it, so we’ll click **No**.

Let’s move on and take a closer look at the first stage of production.

---

### 2. The **PARTS & PAINTING** sheet

This is a dedicated area for the first stage of production. It covers the preparation and painting of the frame and fork, as well as gathering all the necessary parts for assembly.

In the next video, we’ll take a closer look at this stage — how it connects to the **Parts & Inventory Management** spreadsheet, and the key features that help the production team spot and order any missing parts.
