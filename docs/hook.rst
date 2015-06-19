========
Web hook
========

Synopsis
========

``/gs-group-groups.json``? :option:`token` =<t> & :option:`get`

Description
===========

The hook, ``gs-group-groups.json`` in the *site* context, lists
all the groups on a site.

.. warning::
   The hook returns *all* groups, including the secret ones, and
   the *existence* of some groups may be controversial. That is
   why **secret** group-privacy exists. Be cautious about
   disclosing the list of all groups.

Required arguments
==================

.. option:: token=<token>

  The authentication token [#token]_.

.. option:: get

   The "form" action (no value needs to be set, but the argument
   must be present).

Returns
=======

A list of JSON_ objects is returned. Each object within the list
represents a group, and has the following fields set.


.. js:class:: GroupsReturn()

   .. js:attribute:: id

      The unique identifier for the group.

   .. js:attribute:: name

      The name of the group (the title).

   .. js:attribute:: url

      The URL for the group.

   .. js:attribute:: email

      The email address for the group,

   .. js:attribute:: type

      The type of group.

   .. js:attribute:: privacy

      The group privacy.

Example
=======

Get a list of groups on ``groups.example.com`` using
:program:`wget`:

.. code-block:: console

   $ wget --post-data="token=Fake&get" \
     http://groups.example.com/gs-group-groups.json

The return-value for `GroupServer.org`_:

.. code-block:: json

    [
        {
            "id": "groupserver_announcements", 
            "name": "GroupServer Announcements", 
            "url": "http://groupserver.org/groups/groupserver_announcements", 
            "email": "groupserver_announcements@groupserver.org", 
            "type": "Announcement group", 
            "privacy": "public"
        }, 
        {
            "id": "groupserver_team", 
            "name": "GroupServer Team", 
            "url": "http://groupserver.org/groups/groupserver_team", 
            "email": "groupserver_team@groupserver.org", 
            "type": "Discussion group", 
            "privacy": "private"
        }, 
        {
            "id": "development", 
            "name": "GroupServer Development", 
            "url": "http://groupserver.org/groups/development", 
            "email": "development@groupserver.org", 
            "type": "Discussion group", 
            "privacy": "public"
        }, 
    ]

.. _JSON: http://json.org/

.. [#token] See ``gs.auth.token`` for more information
   <https://github.com/groupserver/gs.auth.token>

.. _GroupServer.org: http://groupserver.org/
