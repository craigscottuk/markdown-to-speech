The **FOCUS** sheet provides a detailed overview of what’s missing and the potential return from completing the selected project.

The layout is divided into two parts:

- On the **left**, we have a project summary for each selected build.
- On the **right**, we see a live mini-inventory showing the missing parts and their net cost.

Let’s start with the summary. In this case, we’re only analysing one project — **Donaldson**. So, we see only one project here.

The first five columns show basic production and project data: its **deadline window**, **priority score**, **project ID**, **name**, and **bike type/drivetrain**.

To the right, we move into the financials:

- The **Estimated Net Cost** shows how much we need to spend to complete the bike.
- Next, we see a **Paid in Full** column — marked as **false** in this case, because only a 50% deposit has been paid so far.
- Then, there’s the **Outstanding Balance**, which shows that **2,804 zł** is still due. This final payment will be collected when the customer picks up their completed bike.
- Lastly, the **Difference** column shows the potential return on this project — calculated as the **Outstanding Balance** minus the **Cost of Missing Items**.

So while there’s still some spending required to finish the build, we can also expect a return once it’s done.

At the top of the sheet, we can see this clearly — the **Estimated Return** for completing all selected projects is **2,482 zł**.

---

Now, over on the right-hand side, we have the **Missing Items** panel — the core of the **FOCUS** sheet.

This section provides a clear breakdown of all the parts still needed to complete the selected project or projects. It functions like a mini-inventory, filtered specifically to show only the missing components for the focused builds. Each row represents a missing item and includes:

- **Item Code** and **Item Name**
- **Manufacturer** and **Item Category**

Next, we have a group of columns that display **live inventory data** from the **Parts & Inventory Management** spreadsheet for each of these items. Let’s go over what each column means:

- **Allocated to Assembly** shows how many units of a part are already booked for bikes currently in the assembly stage.  
   For example:
  - The rear sprocket shows **0**, meaning it hasn’t yet been allocated to any builds.
  - The black grips show **3**, indicating three pairs are already booked for other bikes.
  - The PRO 70mm stem shows **5**, meaning five units are currently assigned.
- **Available Stock** shows how many units are unallocated and ready for immediate use. In this case, each item shows **0**, meaning we have none available — either for this project or for any new builds.
- **Total Stock** refers to the full number of units physically onsite — including those in storage, booked for other builds, or already installed on completed bikes awaiting pickup.  
   For example:
  - We have **3** pairs of grips and **5** PRO stems onsite.
  - However, as they’re all already allocated, **Available Stock** remains **0**.
  This figure helps provide a complete view of inventory for insurance, reporting, and valuation purposes.
- **Project Demand** shows how many units are needed for the current build. In this case, it’s **1** of each — one sprocket, one pair of grips, and one stem.
- **Missing** shows how many units still need to be sourced. It’s calculated as:  
   **Project Demand – Available Stock**  
   Since **Available Stock** is zero across the board, each part appears as **1 missing**, highlighted in red.
- **Value of Missing Items (NET)** displays the net cost of each missing item. The total comes to **322 zł**, shown in the top-right corner of the panel.

What makes this tool especially powerful is its ability to analyse multiple projects at once.

Let’s jump back to the **PARTS & PAINTING** sheet and select a few additional projects using the checkboxes to include them in the **FOCUS** sheet.

Back in the **FOCUS** sheet, the summary now includes **five projects**, and the **Missing Items** panel reflects a broader range of components still needed. We also see an updated total cost for the parts required to complete these group of builds.

This gives us a clear, at-a-glance view of what needs to be ordered — supporting better planning, smarter purchasing, and more efficient use of resources.

In the next video, we’ll take a closer look at the **Parts & Inventory Management** spreadsheet — the system’s central hub for maintaining part prices, tracking stock levels, and calculating real-time availability across all active builds. We’ll explore how it connects with the **Offers & Production Management** spreadsheet to keep everything in sync.
