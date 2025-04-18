# Alerting System

The alert mechanism is designed to notify department managers whenever an item's inventory falls below a defined critical threshold. This check is performed during the update operation specifically, when an item's `inventory_count` is changed via the `/items/<id>` PUT endpoint.

If the new inventory count is **less than the configured** `alert_threshold`, an alert should be triggered immediately. This ensures that restocking actions can be taken proactively.

Furthermore alerts can be handled in a variety of ways, depending on the system's integration and scale:
* **Email or SMS**: Notify department heads directly through predefined contact methods.
* **Dashboard Logging**: Display flagged items within an internal admin portal for daily review.
* **Webhooks or Event Queues**: Push alert events to external systems (e.g., PagerDuty, Slack, Kafka) for asynchronous processing or escalation workflows.

In a production environment, this alert logic could either be:
* Embedded in the same logic handling item updates (synchronous triggering), or
* Delegated to a background task queue like Celery to decouple alerting from the request lifecycle allowing for retries, throttling or batching alerts when needed.

# Assumptions I made

* Each item name is unique within a department but may exist in multiple departments, e.g. "T-shirt" in both Clothing and Sportswear.
* Inventory is maintained at the item name level and product variations such as SKU, size or color are not tracked here.
* Departments like Clothing, Home Goods, etc. are treated as separate entities and new departments can be added as needed through the database for now.
* The system focuses on inventory tracking and reporting without handling pricing, supplier info or order management at this stage.