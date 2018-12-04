Feature: Do Something
  A sample run of a Pytest-BDD integration


  Scenario: Admin user is taken to the dashboard after logging in
    Given an admin user is on the login page
    When the user logs into Clinic Wise
    Then the user is taken to the dashboard page

  Scenario:  Admin user can search for a client by last name
    Given an admin user is on the Clients page
    When the user searches by last Name
    Then a client match should be returned

  Scenario:  Admin can view a client's details
    Given the user has a client in view
    When the selects a client
    Then the client details page is returned

