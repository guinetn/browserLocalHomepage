# WebHooks

Lightweight pub/sub HTTP pattern for wiring Web APIs and SaaS services.
When an event happens in a service, a notification is sent in the form of an HTTP POST request to registered subscribers. The POST request contains information about the event which makes it possible for the receiver to act accordingly.

SERVICES EXPOSING 
    WEBHOOKS
    Dropbox   ....
    GitHub    ....
    Bitbucket ....
    MailChimp .........> RECEIVERS ......> HANDLERS (user code processing the WebHook)
    PayPal    ....
    Slack     ....
    Stripe    ....
    Trello    ....
    …
    
For example, a WebHook can indicate that a file has changed in Dropbox, or a code change has been committed in GitHub, or a payment has been initiated in PayPal, or a card has been created in Trello. 


HTTP POST request contains a JSON object or HTML form data determined by the WebHook sender including information about the event causing the WebHook to trigger. 


## More

- https://docs.microsoft.com/en-us/aspnet/webhooks/