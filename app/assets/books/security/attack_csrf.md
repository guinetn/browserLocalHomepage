### CSRF Attacks

CROSS-SITE REQUEST FORGERY

For every HTTP request to a domain, the browser attaches any HTTP cookies associated with that domain. This is especially useful for authentication, and setting sessions. For instance, it’s feasible that you would sign into a web app like facebook-clone.com. In this case, your browser would store a relevant session cookie for the facebook-clone.com domain:

Facebook-clone.com -------------------> Facebook-clone.com/api
                    session_id=fb0021
This is great! Session cookie gets stored → every visit to facebook-clone.com you don’t have to sign in again because API will recognize the stored session cookie upon further HTTP requests.

Trouble is that the browser automatically includes any relevant cookies stored for a domain when another request is made to that exact domain. Therefore, a scenario like this can happen. Say you clicked on a particularly trick popup add, opening evil-site.com.

Evil-site.com -------------------> Facebook-clone.com/api
               session_id=fb0021
               
The evil site also has the ability send a request to facebook-clone.com/api. Since the request is going to the facebook-clone.com domain, the browser includes the relevant cookies. Evil-site sends the session cookie, and gains authenticated access to facebook-clone. Your account has been successfully hacked with a cross-site request forgery attack.  

