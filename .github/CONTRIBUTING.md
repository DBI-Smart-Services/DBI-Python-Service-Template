# Workflow for contributing to the project

## Getting Tasks

- [ ] Get a task from the Sprint Planing and have a Ticket Via JIRA

## Create a Branch

For Creating a Branch, you have to follow the following naming convention:

`<KindOfTask>/<TicketNumber>_<NameOfTicket>`

Example: `feature/BER-1234_AddingNewFeature`

To get the name automated you cna use the following JavaScript Snippet

```javascript
javascript:(function(){const el=document.createElement("textarea");el.value=((document.querySelectorAll("div[data-test-id='issue.views.issue-base.foundation.breadcrumbs.breadcrumb-current-issue-container']")[0].getElementsByTagName("img")[0]).getAttribute("alt") === "Bug" ?%20%22bugfix%22%20:%20%22feature%22)+%22/%22+(window.location.href.split(%22/%22).pop()).split(%27?%27)[0]+%22_%22+document.querySelectorAll(%22h1[data-test-id=%27issue.views.issue-base.foundation.summary.heading%27]%22)[0].innerText.replace(/[^a-zA-Z0-9]/g,%22_%22).replace(/\_+/g,%27_%27),document.body.appendChild(el),el.select(),document.execCommand(%22copy%22),document.body.removeChild(el);})();
```

## Work on the Task

- Work on the task based on the Ticket Specification

## Create a Pull Request

Create a Pull Request and use the given Pull Request Template. Name the Pull Request like the Branch Name.

