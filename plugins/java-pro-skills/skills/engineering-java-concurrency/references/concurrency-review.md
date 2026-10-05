# Concurrency review questions

- Publication: how does another thread see new state?
- Atomicity: can two callers pass the same check?
- Ordering: what happens-before edge exists?
- Lifetime: can close/reload race with in-flight use?
- Cancellation: who cancels and how does the task observe it?
- Failure: can an exception leave state permanently “in progress”?
- Boundedness: are executor queues, retries, histories, caches bounded?
- Affinity: must completion run on UI/event-loop/entity/region thread?
- Blocking: can any call transitively perform I/O or wait?
- Backpressure: what happens when producers outrun consumers?
