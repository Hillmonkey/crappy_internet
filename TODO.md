TASK LIST FOR CRAPPY INTERNET APP

* Before Initial Presentation
  * Research Domain Name
   * ConnectTest?
   * ServiceReport?
   * InternetServiceReport?
   * Pingdom synonym

  * MVP 0.1
   * cron job + bash script -> populates log file
   * generate text based stats from log file
    * connectivity percentage
    * histogram

  * MVP 0.2 (this MVP goal might be considered optional)
   * There is a python package that turns your program into a CLI command

  * Research: Easy to use time-seriesd database
   * Graphite
   * InfluxDb
   * QUESTION: How hard is it to a proprietary AWS database?

  * Research: Easy to use Queue System
   * Celery
   * RQ (Redis Queue)
   * QUESTION: How hard is it to a proprietary AWS Queue?

  * Research: How to make it easy to install connectivity monitor
   * Python packaging?
   * Create bash installation script
   * Run it in a webpage (this seems subpar)

  * MVP 0.3 (make the service run locally)
   * Locally running database
   * Locally served webpage with statistics
   * Question: How hard is it to transition to proprietary AWS products?
