Feature: Mobile App Feature

  Scenario: [NAT-1] Verify the User can login successfully with valid credentials
    Given User is on boh fpu homepage
    When User enters username as "harish.ekal@spurqlabs.com"
    And User enters password as "Test123!BOH"
    And User taps on "Sign In" option
    Then User can see "Customer Management" page

  Scenario Outline: [NAT-2] Verify the User can not login with In-valid credentials
    Given User is on boh fpu homepage
    When User login with <username> and <password>
    Then User verifies "<message>"
    Examples:
      | username                  | password    | message                     |
      | harish.ekalspurqlabs.com  | Test123!BOH | Incorrect username/password |
      | harish.ekal@spurqlabs.com | test123     | Incorrect username/password |
      |                           |             | Incorrect username/password |

  Scenario: [NAT-3] Verify that the user is on the customer management page after signing in.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    Then Following options are displayed on homepage
      | Customer Management | Customers | REs       |
      | Opportunities       | Sort By   | Filter By |

  Scenario: [NAT-4] Verify after clicking on the profile, the user can see Sign-Out Option
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    Then User can see "Sign Out" option

  Scenario: [NAT-5] Verify after clicking on profile, user can able to see Update Profile Picture option
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    Then User can see "Update Profile Picture" option

  Scenario: [NAT-6] Verify after clicking on "Update Profile Picture", user should see two options 1) Take Picture 2) Upload File
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    And User taps on "Update Profile Picture" option
    Then Following options are displayed
      | Take Picture |
      | Upload File  |

  Scenario: [NAT-7] Verify user can sign out after tapping on SignOut
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Administrator" option
    Then User taps on "Sign Out" option

  Scenario Outline: [NAT-8] Verify user can sort out customers by choosing different option [Date, CSM, Value, Name]
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Sort By" option
    And User select <sort by> option
    Then "Customers" list is displayed
    Examples:
      | sort by |
      | Date    |
      | CSM     |
      | Value   |
      | Name    |

  Scenario Outline: [NAT-9] Verify user can filter out customer by selecting different options [All, Active, Inactive]
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "filter By" option
    And User select <filter By> option
    Then "Customers" list is displayed
    Examples:
      | filter By |
      | All       |
      | Active    |
      | Inactive  |

  Scenario: [NAT-10] Verify user can search out exixting customer by tapping on Search (Q) option
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "search" option
    And User search for customer "newCust"
    Then "newCust" details are displayed


  Scenario: [NAT-11] Verify User can see Activity details after selecting existing customer
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    Then "abcd" details are displayed

  Scenario: [NAT-12] Verify User can able to see add Touchbase, Opportunity & RE by tapping on '+' symbol
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on '+' option
    Then Following options are displayed
      | Add Touchbase   |
      | Add Opportunity |
      | Add RE          |

  Scenario Outline: [NAT-13] Verify User can select different option from Direct in dropdown list
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on '+' option
    And User taps on "Add Touchbase" options
    Then User select <region> from list
    Examples:
      | region                  |
      | Americas (Excluding US) |
      | Central                 |
      | East                    |
      | Europe/Africa           |
      | Middle East             |
      | Pacific West            |

  Scenario: [NAT-14] Verify that the "forgot password" link works
    Given User is on boh fpu homepage
    When User taps on "Forgot Password" option
    Then User can see "Forgot your password?" page

  Scenario: [NAT-15] Verify user can able to see all details after tapping on Info tab [Sales Rep, Location, Contacts, Delete]
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    Then Following options are displayed
      | Sales Rep | Location | Contacts | Delete |

  Scenario: [NAT-16] Verify user can switch from Active to Inactive mode and vice versa.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And user can see "ACTIVITY" page
    And User taps on "ACTIVE" option
    And User can see "Change State" page
    Then User taps on "Set Customer to Inactive" option

  Scenario: [NAT-17] Verify user can check all options after tapping on the plus symbol in activity details [ Add Touchbase, Add contact, Add RE]
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on '+' option
    Then Following options are displayed
      | Add Touchbase | Add contact | Add RE |

  Scenario: [NAT-18] Verify that the user can edit location details and add a new location in the info tab of any customer.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    And User taps on "location" option
    Then "new location" details are displayed

  Scenario: [NAT-19] Verify that users can see all details after tapping on contacts in the info tab of any customer.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    And User taps on "Bradford Kasper" option
    Then Following options are displayed
      | hello@clearbluedesign.com |  | 000                     |
      | Edit Contact              |  | Touchbase with bradford |

  Scenario: [NAT-20] Verify that users can edit contact after tapping on contacts in the info tab of any customer
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    And User taps on "Contact" option
    And User taps on "Edit Contact" option
    Then User can see "Edit Contact" page


  Scenario: [NAT-21] Verify that users can edit contact successfully in the info tab of any customer
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    And User taps on "Bradford Kasper" option
    And User make changes in their respective fields
    And User taps on "Save Changes" option
    Then User can see "Edit Contact" page

  Scenario: [NAT-22] Verify that the customer summary shows all details.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    Then Following options are displayed
      | abcd          | Ron P    |
      | 29 Palm       | Active   |
      | Arlington, VA | Validate |
      | Florida       | Active   |
      | JBER, AK      | Active   |

  Scenario: [NAT-23] Verify any customer's options, such as notes, phone, email, in-person, and voicemail, are visible to the user.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    Then Following options are displayed
      | Note | Phone | Email | In-Person | Voicemail |

  Scenario: [NAT-24] Verify that after selecting the Notes option, the user can post a message.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User enters a message in a message field and sends it.
    Then User verifies message

  Scenario: [NAT-25] Verify whether the posted message through notes is editable or not.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User taps on "3 dots" option
    And User taps on "edit" option
    And User can see "Edit Note" pop-up
    Then User validated "edited message" on page

  Scenario: [NAT-26] Verify whether the posted message through notes is deleteable or not.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User taps on "3 dots" option
    And User taps on "delete" option
    And User can see "Delete Note" pop-up
    Then User validated "deleted" Note

  Scenario: [NAT-27] Verify that the posted message shows two options: edit or delete after tapping on three dots.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User taps on "3 dots" option
    Then Following options are displayed
      | Edit | Delete |

  Scenario: [NAT-28] Verify that the user can add a touchbase note through the phone option.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User enter note in Note fields
    And User taps on "phone" option
    And User taps on "Create Touchbase" option
    Then User validated "Touchbase" on page

  Scenario: [NAT-29] Verify that the user can add a touchbase note through the Email option.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User enter note in Note fields
    And User taps on "Email" option
    And User taps on "Create Touchbase" option
    Then User validated "Touchbase" on page

  Scenario: [NAT-30] Verify that the user can add a touchbase note through the In-Person option.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User enter note in Note fields
    And User taps on "In-Person" option
    And User taps on "Create Touchbase" option
    Then User validated "Touchbase" on page

  Scenario: [NAT-30] Verify that the user can add a touchbase note through the Voicemail option.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User enter note in Note fields
    And User taps on "Voicemail" option
    And User taps on "Create Touchbase" option
    Then User validated "Touchbase" on page

  Scenario: [NAT-31] Verify that the user can delete created touchbase
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User enter note in Note fields
    And User taps on "Voicemail" option
    And User taps on "Create Touchbase" option
    And User select touchbase and delete it by tapping delete option
    Then User validated on page

  Scenario: [NAT-32] Verify that after tapping on Add touchbase from the symbol (+), the user is able to create a touchbase successfully.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User fills all reuired data into their respective field
    And User taps on "Create Touchbase" option
    Then user validated "touchbase" on page

  Scenario: [NAT-33] Verify that after tapping on Add touchbase from the symbol (+), the user is able to see following details(Customer Info, Direct/Program,Contact, Touchbase Info, Contact method)
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    Then Following options are displayed
      | Customer Info | Direct/Program | Contact | Touchbase Info | Contact method |

  Scenario: [NAT-34] Verify that after tapping on Add opportunity from the symbol (+), the user is able to see following details(Capture Lead, Overview, Customer )
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    Then Following options are displayed
      | Capture Lead | Overview | Customer Contact | Win Probability | Value Breakdown |

  Scenario: [NAT-35] Verify that after tapping on Add RE from the symbol (+), the user is able to see following details.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add RE" option
    Then Following options are displayed
      | Sales Rep | Estimated Order Date(Optional) | Estimate Sub-Title | opportunity | Customer Info | Primary Contact | Metrics and Color |

  Scenario: [NAT-36] Verify that after tapping on Add opportunity from the symbol (+), the user is able to create a opportunity successfully.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User fills all reuired data into their respective field for opportnity
    And User taps on "Create Opportunity" option
    Then user validated "Opportunity" on page

  Scenario: [NAT-37] Verify that after tapping on Add RE from the symbol (+), the user is able to create a REs successfully.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add RE" option
    And User fills all reuired data into their respective field for RE
    And User taps on "Create Requirement Estimate" option
    Then user validated "RE" on page

  Scenario: [NAT-38] Verify that the user can able to delete customer from info tab of Customer details
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User can see "ACTIVITY" page
    And User taps on "INFO" option
    And User taps on "Delete abcd" option
    Then User validted "Customer" on page

  Scenario: [NAT-39] Verify that if there are no REs in the RE tab, then the user should be able to see the message
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "RE" option
    Then user can see "Tap the + to add the first RE" page

  Scenario: [NAT-40] Verify that user can able to update existing contact in info tab of contacts
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    And User taps on "Bradford Kasper" option
    And User taps on "Edit Contact" option
    And User taps on "Contact Phone" and make changes
    And User taps on "Save Changes" option
    Then User validated "contact" on page

  Scenario: [NAT-41] Verify that the push button is working to check the default button functionality.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    And User taps on "Bradford Kasper" option
    And User taps on "Edit Contact" option
    Then User taps on "Push" button to check pushBtn functionality

  Scenario: [NAT-42] Verify that user can upload profile picture through upload a file functionality
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    And User taps on "Upload Profile Picture" option
    And User taps on "Upload file" option
    Then User validated "File" on page

  Scenario: [NAT-43] Verify that user can upload profile picture through Take a picture functionality
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    And User taps on "Upload Profile Picture" option
    And User taps on "Take a Picture" option
    Then User validated "picture" on page

  Scenario: [NAT-44] Verify User can add Touchbase, Opportunity & RE by tapping on '+' symbol
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User taps on '+' symbol
    Then Following options are displayed
      | Add Touchbase | Add Opportunity | Add RE |

  Scenario: [NAT-45]Verify that the user can see the summary part on display which includes the total, quoted, and remaining
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    Then Folllowing options are displayed
      | Opportnity #60      | Est Order Date |
      | 115th BSB SSA 1ABCT | 7/2022         |
      | Fort Hood, TX       | $7K            |
      | $0.00               | $7K            |
      | Total               | Quoted         |
      | Remaining           |                |

  Scenario: [NAT-46] Verify that the user is on the info page after tapping on any opportunity.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    Then User can see "INFO" on page

  Scenario: [NAT-47] Verify that If the user has the ability to edit the Sales Rep.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User select "Jerry Boggess" from list
    Then User validated "Jerry Boggess" on page

  Scenario: [NAT-48] Verify that after tapping on "no affiliation", the choose type pop-up should appear.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "no affiliation" option
    And User can see "Choose Type" pop-up
    Then Following options are displayed
      | Direct | Program |

  Scenario: [NAT-49] Verify that if the user can edit the order month and select any month from the list.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "order month" option
    And User select "April" from list
    Then User validated "April" on page

  Scenario: [NAT-50] Verify that after tapping on order month, the pop-up should appear that includes a list of months.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "order month" option
    Then following options are displayed
      | January | February | March     | April   | May      | June     |
      | July    | August   | September | October | November | December |

  Scenario: [NAT-51] Verify that the Total Amount is editable and that the user can enter values in that field.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "Total Amount" option
    Then User validated "$000" on page

  Scenario: [NAT-52] Verify that the user can edit contact details in the info tab.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "Customer Contact" option
    Then User validated "(123)(456)(7890)" on page

  Scenario: [NAT-53] Verify whether the fields are editable after tapping on contact details.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "Customer Contact" option
    And User check following fields are editable
      | Rank or Title | First name | Last name | Contact Email | Contact Phone |
    Then User verifies the details on Info page

  Scenario: [NAT-54] Verify whether the user can delete the opportunity from the info tab.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User can see "INFO" page
    And User taps on "Delete Opportunity" option
    Then User verified on "Opportunities" page

  Scenario: [NAT-55] Verify that after tapping on REs, the user can see the list of REs.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "REs" option
    Then User verified "Res list" on page

  Scenario: [NAT-56] Verify that after tapping on REs, if there are no REs, then it should display the message No requirement estimates for opportunity.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "REs" option
    Then User verifies "No requirement Estimates for opportunity #60" on page

  Scenario: [NAT-57] Verify that the user can see the win probability and their respective responses on screen.
    Given User is on boh fpu homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User taps on "Win Probability" option
    Then Following options are displayed
      | 10%  | Providing Information-No Known Requirements                  |
      | 20%  | Customer Requested Survey-No Known Funding Source            |
      | 50%  | Customer Wants It-CurrentlySeeking Funding,                  |
      | 75%  | Customer Wants It-Funding Identified-Awaiting Authorization, |
      | 100% | Customer has Provided Document Numbers or Confirmed Purchase |
