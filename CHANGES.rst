
Version History
===============

Many thanks to everyone who submits pull requests.  We'll merge in most changes that are unit tested and well thought out.

0.4.1
-----
 - nicpottier: include formID in ODK form list, this won't fix issues with more than one form on ODK collect 1.1.7, but if they accept our patch then it will fix the single form issue.  see: http://code.google.com/p/opendatakit/issues/detail?id=324

0.4.0
-----
 - nicpottier: paginate submissions, about time
 - nicpottier: add security framework for authentication either SMS or XForms submissions, see docs (added django_digest dependency)

0.3.6
-----
 - nicpottier: added ability to submit photos, sounds and videos from ODK clients

0.3.5
-----
 - nicpottier: fix performance issue when listing submissions either via CSV or through web interface (thanks jaredalexander for bug)

0.3.4
-----
 - nicpottier: nail down version for django-uniform and django
 - nicpottier: fix bug with new version of django-uniform

0.3.3
-----
 - daveycrockett: for string fields which are last in an SMS, use all values, not just the first word
 - daveycrockett: add fix for optional string fields not failing when no value provided, ie: +epi ma
 - daveycrockett: add fix for duplicate optional fields not causing errors, ie: +epi ma 10 ma 12
 - nicpottier: add CHANGES.rst

0.3.2
-----
 - nicpottier: fix bug where messages containing only the keyword were not matching forms
