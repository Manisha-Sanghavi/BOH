Feature: Mobile App Feature

  Scenario: [Customer-1] Verify the User can login successfully with valid credentials
    Given User is on BOH FPU homepage
    When User enters username as "harish.ekal@spurqlabs.com"
    And User enters password as "Test123!BOH"
    And User taps on "Sign In" button
    Then User verifies "Customer Management" page is displayed

  Scenario Outline: [Customer-2] Verify the User can not login with In-valid credentials
    Given User is on BOH FPU homepage
    When User login with <username> and <password>
    Then User verifies "<message>" is displayed
    Examples:
      | username                  | password    | message                     |
      | harish.ekalspurqlabs.com  | Test123!BOH | Incorrect username/password |
      | harish.ekal@spurqlabs.com | test123     | Incorrect username/password |
      |                           |             | Incorrect username/password |
      |                           | test123     | Incorrect username/password |
      |harish.ekal@spurqlabs.com  |             | Incorrect username/password |


  Scenario: [Customer-3] Verify the Headers and Tabs displayed on Customer Management Page.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    Then User verifies following options are displayed on page
      | Customer Management | Customers | REs       |Opportunities       | Sort By   | Filter By |

#  Scenario: [NAT-4] Verify after clicking on the profile, the user can see Sign-Out Option
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Adminastrator" option
#    Then User can see "Sign Out" option

  Scenario: [Customer-4] Verify user can update Profile picture from Profile menu
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Adminastrator" option
    And User taps on "Update Profile Picture" option
    Then user verifies profile picture updated successfully

#  Scenario: [NAT-6] Verify after clicking on "Update Profile Picture", user should see two options 1) Take Picture 2) Upload File
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Adminastrator" option
#    And User taps on "Update Profile Picture" option
#    Then User updated profile picture successfully


  Scenario: [Customer-5] Verify user can sign out successfully from app
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Administrator" option
    And User taps on "Sign Out" button
    Then User verfies "Homepage" is displayed

  Scenario: [Customer-6] Verify user can sort customers by Date option in ascending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Sort By" option
    And User select "Date" option
    Then User verifies customer list is sorted in ascending order

    Scenario: [Customer-7] Verify user can sort customers by Date option in descending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Sort By" option
    And User select "Date" option
    Then User verifies customer list is sorted in descending order

  Scenario: [Customer-8] Verify user can filter customer by Active option
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "filter By" option
    And User select "Active" option
    Then User verifies Customer with only Active status are displayed

  Scenario: [Customer-9] Verify that the user can find an existing customer using the Search (Q) option.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "search" option
    And User search for customer "newCust"
    Then User verifies "newCust" displyed on page


  Scenario: [Customer-10] Verify the Headers and Tabs displayed under Activity Tab
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User navigeated to "Activity" page
    Then User verifies Customer details page with following information is displayed
      | INFO | ACTIVITY | REs | Note | Phone | Email | In-Person | Voicemail |

  Scenario: [Customer-11] Verify after tapping '+' symbol in Customer tab, user can see Add Touchbase, Add Opportunity, Add RE and 'x' symbol
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User is navigated to "customer management" page
    And User taps on '+' option
    Then User verifies following options are displayed
      | Add Touchbase | Add Opportunity | Add RE |X|

#    Low Priority.
#  Scenario Outline: [NAT-13] Verify User can select different option from Direct in dropdown list
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on '+' option
#    And User taps on "Add Touchbase" options
#    And User select <region> from list
#    Then User verifies selected "region" displayed on page
#    Examples:
#      | region                  |
#      | Americas (Excluding US) |
#      | Central                 |
#      | East                    |
#      | Europe/Africa           |
#      | Middle East             |
#      | Pacific West            |

  Scenario: [Customer-12] Verify that the "forgot password" link works
    Given User is on BOH FPU homepage
    When User taps on "Forgot Password" option
    And User navigated to "Forgot your password?" page
    And User enters email "harish.ekal@spurqlabs.com" in type your BOH email field
    Then User verifies meassage "A recovery email has been sent to your account" is displayed

  Scenario: [Customer-13] Verify Details added during Customer Creation are displayed in Info Tab in customer detail page of that customer
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "INFO" option
    Then User verifies following options are displayed
      | Sales Rep | Location | Contacts | Delete |

  Scenario: [Customer-14] Verify user can switch from Active to Inactive mode
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And user navigated to "abcd" page
    And "Change State" popup is displayed
    And User taps on "Set Customer to Inactive" option
    And User verifies status changed to “Inactive”
    And User taps on "Set Customer to Active" option
    Then User verifies status changed to “Active”

#  Scenario: [NAT-17] Verify user can check all options after tapping on the plus symbol in activity details [ Add Touchbase, Add contact, Add RE]
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User select "abcd" customer
#    And User taps on '+' option
#    Then Following options are displayed
#      | Add Touchbase | Add contact | Add RE |

  Scenario: [Customer-15] Verify Details added during customer Creation are displyed in Info Tab of customer
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User taps on "Info" option
    And User selects "RE #" RE
    Then User verifies following options are displayed
      |Sales Rep  | Ron P         |                    |                   |              |
      |Location   |29 palm        |Arlington, VA       |Florida            |JBER, AK      |
      |Contacts   |Bradford Kasper|Jesus Amsdell       |Behanzin Luzunaris |Gretta Sevilla|

#  Scenario: [NAT-19] Verify that users can see all details after tapping on contacts in the info tab of any customer.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User select "abcd" customer
#    And User taps on "INFO" option
#    And User taps on "Bradford Kasper" option
#    Then Following options are displayed
#      | hello@clearbluedesign.com |  | 000                     |
#      | Edit Contact              |  | Touchbase with bradford |

#  Scenario: [NAT-20] Verify that users can edit contact after tapping on contacts in the info tab of any customer
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User select "abcd" customer
#    And User taps on "INFO" option
#    And User taps on "Contact" option
#    And User taps on "Edit Contact" option
#    Then User can see "Edit Contact" page


#  Scenario: [NAT-21] Verify that users can edit contact successfully in the info tab of any customer
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User select "abcd" customer
#    And User taps on "INFO" option
#    And User taps on "Bradford Kasper" option
#    And User make changes in their respective fields
#    And User taps on "Save Changes" option
#    Then User can see "Edit Contact" page

  Scenario: [Customer-16] Verify that the customer summary shows all details.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    Then User verifies following summary of "abcd" customer displayed on page
      | abcd          | Ron P    |
      | 29 Palm       | Active   |
      | Arlington, VA | Validate |
      | Florida       | Active   |
      | JBER, AK      | Active   |

#  Scenario: [NAT-23] Verify any customer's options, such as notes, phone, email, in-person, and voicemail, are visible to the user.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User select "abcd" customer
#    And User can see "ACTIVITY" page
#    Then Following options are displayed
#      | Note | Phone | Email | In-Person | Voicemail |

  Scenario: [Customer-17] Verify user can add a note successfully from Activity Tab in Customer Details page
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User enter "Test note" in input field at bottom of the page
    And User taps on "Post" option
    Then User verifies "Test note" is displayed in Activity list.

  Scenario: [Customer-18] Verify user can edit posted note from Activity tab.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User select "abcd" customer
    And User enters "test1" in post a message field and send it
    And User selects "test1" to edit
    And User edits to "test2"
    Then USer verifies note text is updated to "test2" in Activity list

  Scenario: [Customer-19] Verify user can delete posted note text successfully
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User selects "test2" to delete
    And User taps on "delete" option
    And "Delete Note" popup is displayed
    Then User verfies "test2" is deleted successfully

#  Scenario: [NAT-27] Verify that the posted message shows two options: edit or delete after tapping on three dots.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User select "abcd" customer
#    And User can see "ACTIVITY" page
#    And User taps on "3 dots" option
#    Then Following options are displayed
#      | Edit | Delete |

  Scenario Outline: [Customer-20] Verify user can create a Touchbase with selected contact option from Activity tab.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User navigated to "ACTIVITY" page
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User enter "<note>" in Note fields
    And User taps on "<Contact Method>" option
    And User taps on "Create Touchbase" option
    Then User verifies "note" is displayed on page
    Examples:
    |Contact Method|note                     |
    |Phone         |1234567890               |
    |Email         |xyz@example.com          |
    |In-Person     |text in In-Person        |
    |Voicemail     |message through voicemail|
#
#  Scenario: [NAT-29] Verify that the user can add a touchbase note through the Email option.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User select "abcd" customer
#    And User can see "ACTIVITY" page
#    And User taps on "+" option
#    And User taps on "Add Touchbase" option
#    And User enter note in Note fields
#    And User taps on "Email" option
#    And User taps on "Create Touchbase" option
#    Then User validated "Touchbase" on page
#
#  Scenario: [NAT-30] Verify that the user can add a touchbase note through the In-Person option.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User select "abcd" customer
#    And User can see "ACTIVITY" page
#    And User taps on "+" option
#    And User taps on "Add Touchbase" option
#    And User enter note in Note fields
#    And User taps on "In-Person" option
#    And User taps on "Create Touchbase" option
#    Then User validated "Touchbase" on page
#
#  Scenario: [NAT-31] Verify that the user can add a touchbase note through the Voicemail option.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User select "abcd" customer
#    And User can see "ACTIVITY" page
#    And User taps on "+" option
#    And User taps on "Add Touchbase" option
#    And User enter note in Note fields
#    And User taps on "Voicemail" option
#    And User taps on "Create Touchbase" option
#    Then User validated "Touchbase" on page

  Scenario: [Customer-21] Verify that the user can delete created touchbase from Activity details
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User navigated to "Activity" page
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User enter "note" in Note fields
    And User taps on "email" option
    And User taps on "Create Touchbase" option
    And User select recently created touchbase and delete it
    Then User verifies "Touchbase" is deleted successfully

  Scenario: [Customer-22] Verify that the user can create a new touchbase successfully.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User fills all required data into their respective field
        |Customer          |Location         |Direct/Program|Contact      |Existing/New/None|Rank or Title (optional)|                   |
        |Contact First Name|Contact Last Name|Contact Email |Contact Phone|Date of Contacts |Note                    |Contact Method     |
    And User taps on "Create Touchbase" option
    Then user verifies "touchbase" is displayed on page

#  Scenario: [NAT-34] Verify that after tapping on Add touchbase from the symbol (+), the user is able to see following details(Customer Info, Direct/Program,Contact, Touchbase Info, Contact method)
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "+" option
#    And User taps on "Add Touchbase" option
#    Then Following options are displayed
#      | Customer Info | Direct/Program | Contact | Touchbase Info | Contact method |

#  Scenario: [NAT-35] Verify that after tapping on Add opportunity from the symbol (+), the user is able to see following details(Capture Lead, Overview, Customer )
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "+" option
#    And User taps on "Add Opportunity" option
#    Then Following options are displayed
#      | Capture Lead | Overview | Customer Contact | Win Probability | Value Breakdown |

#  Scenario: [NAT-36] Verify that after tapping on Add RE from the symbol (+), the user is able to see following details.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "+" option
#    And User taps on "Add RE" option
#    Then Following options are displayed
#      | Sales Rep | Estimated Order Date(Optional) | Estimate Sub-Title | opportunity | Customer Info | Primary Contact | Metrics and Color |

  Scenario: [Customer-23] Verify that the user can create a new opportunity successfully.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User fills all required data into their respective field for opportnity
        |Affiliation|Customer Location|BOH Role|Customer Contact(New/Existing)|Rank or Title|Contact First Name|Contact Last Name|Contact Email|Contact Phone|Win Probability|Value Breakdown|
    And User taps on "Create Opportunity" option
    And User taps on "Opportunity" option
    Then user verifies "Opportunity #" is displayed on page

#  Scenario: [Customer-23] Verify that the user is able to create a REs successfully.
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "+" option
#    And User taps on "Add RE" option
#    And User fills all reuired data into their respective field for RE
#    And User taps on "Create Requirement Estimate" option
#    And User navigated to "Config" page
#    Then user verifies RE # is displayed at left corner of a page

  Scenario: [Customer-24] Verify user can delete Customer from Touchbase info tab
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Touchbase" option
    And User fills all required data into their respective field
        |Customer          |Location         |Direct/Program|Contact      |Existing/New/None|Rank or Title (optional)|                   |
        |Contact First Name|Contact Last Name|Contact Email |Contact Phone|Date of Contacts |Note                    |Contact Method     |
    And User taps on "Create Touchbase" option
    And User click on created touchbase
    And User taps on "INFO" option
    And User taps on "Delete" option
    Then User verifies "Customer" is deleted successfully.

#    Low Priority.
  Scenario: [Customer-25] Verify that if there are no REs in the RE tab, then the user should able to see the message
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User taps on "RE" option
    Then user verifies "Tap the + to add the first RE" is displayed on page

  Scenario: [Customer-26] Verify that user can update existing contact details in info tab of customer
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User taps on "INFO" option
    And User taps on "Bradford Kasper" option
    And User taps on "Edit Contact" option
    And User enter "1234567890" in contct phone
    And User taps on "Save Changes" option
    And User taps on "Back" option
    And User taps on "Edit Contact" option
    Then User verifies "1234567890" is displayed on page

  Scenario: [Customer-27] Verify that the push button functionality works.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User selects "abcd" customer
    And User taps on "INFO" option
    And User taps on "Jesus Amsdell" option
    And User taps on "Edit Contact" option
    And User navigated to "Edit Contact" page
    And User taps on "Push" button
    Then user verifies "Save Changes" is displayed on page

#  Scenario: [Customer-28] Verify that user can upload profile picture
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Adminastrator" option
#    And User taps on "Upload Profile Picture" option
#    And User taps on "Upload file" option
#    Then User verifies Picture is uploaded successfully

#  Scenario: [NAT-43] Verify that user can upload profile picture through Take a picture functionality
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Adminastrator" option
#    And User taps on "Upload Profile Picture" option
#    And User taps on "Take a Picture" option
#    Then User validated "picture" on page

#  Scenario: [NAT-44] Verify User can add Touchbase, Opportunity & RE by tapping on '+' symbol
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Opportunities" option
#    And User taps on '+' symbol
#    Then Following options are displayed
#      | Add Touchbase | Add Opportunity | Add RE |

  Scenario: [Opportunity-1]Verify that the user can see the opportunities summary part displayed on the page.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    Then User verifies folllowing options are displayed
      | Opportnity #60      | Est Order Date |115th BSB SSA 1ABCT |
      |7/2022               |Fort Hood, TX   |                    |
      |$7K                  |$0.00           |$7K                 |
      |Total                |Quoted          |Remaining           |

#  Scenario: [Opportunity-2] Verify that the user should be on the info page after selecting any opportunity.
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Opportunities" option
#    And User selects "opportunity #60" opportunity
#    Then User verifies that it navigated to the "INFO" page.

#  Scenario: [NAT-47] Verify that If the user has the ability to edit the Sales Rep.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Opportunities" option
#    And User select "opportunity #60" option
#    And User select "Jerry Boggess" from list
#    Then User validated "Jerry Boggess" on page

#  its covers while creating opportunity
#  Scenario: [Opportunity-3] Verify that after selecting "no affiliation", the choose type pop-up should appear.
#    Given User is on BOH FPU homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Opportunities" option
#    And User selects "opportunity #60" opportunity
#    And User taps on "no affiliation" option
#    And "Choose type" popup is displayed
#    Then User verifies following options are displayed
#      | Direct | Program |

#  Scenario: [NAT-49] Verify that if the user can edit the order month and select any month from the list.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Opportunities" option
#    And User select "opportunity #60" option
#    And User taps on "order month" option
#    And User select "April" from list
#    Then User validated "April" on page

  Scenario: [Opportunity-4] Verify that after selecting an order month, the month pop-up should appear.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User selects "opportunity #60" opportunity
    And User taps on "order month" option
    Then User verifies following options are displayed
      | January | February | March     | April   | May      | June     |
      | July    | August   | September | October | November | December |

#  Scenario: [NAT-51] Verify that the Total Amount is editable and that the user can enter values in that field.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Opportunities" option
#    And User select "opportunity #60" option
#    And User taps on "Total Amount" option
#    Then User validated "$000" on page

#  Scenario: [NAT-52] Verify that the user can edit contact details in the info tab.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Opportunities" option
#    And User select "opportunity #60" option
#    And User taps on "Customer Contact" option
#    Then User validated "(123)(456)(7890)" on page

#  Scenario: [NAT-53] Verify whether the fields are editable after tapping on contact details.
#    Given User is on boh fpu homepage
#    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
#    And User taps on "Opportunities" option
#    And User select "opportunity #60" option
#    And User taps on "Customer Contact" option
#    And User check following fields are editable
#      | Rank or Title | First name | Last name | Contact Email | Contact Phone |
#    Then User verifies the details on Info page

  Scenario: [Opportunity-5] Verify that the user can delete the opportunity from the info tab.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User fills all required data into their respective field for opportunity
        |Affiliation|Customer Location|BOH Role|Customer Contact(New/Existing)|Rank or Title|Contact First Name|Contact Last Name|Contact Email|Contact Phone|Win Probability|Value Breakdown|
    And User taps on "Create Touchbase" option
    And User click on created opportunity
    And User taps on "INFO" option
    And User taps on "Delete" option
    Then User verifies meassage "Removed Opportunity #" is displayed

  Scenario: [Opportunity-6] Verify that after selecting REs, the user can see the list of REs.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User selects "opportunity #60" option
    And User taps on "REs" option
    Then User verifies "REs list" is displayed on page

  Scenario: [Opportunity-7] Verify that if there are no REs, then it should display the message.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "Opportunities" option
    And User select "opportunity #60" option
    And User taps on "REs" option
    Then User verifies "No requirement Estimates for opportunity #60" is displayed on page

  Scenario Outline: [Opportunity-8] Verify that the user can see the win probability and their respective responses on screen.
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User taps on "+" option
    And User taps on "Add Opportunity" option
    And User taps on "<Win Probability>" option
    Then User verifies "<Message>" is displayed on page
    Examples:
      |Win Probability|Message                                                       |
      |      10%      | Providing Information-No Known Requirements                  |
      |      20%      | Customer Requested Survey-No Known Funding Source            |
      |      50%      | Customer Wants It-CurrentlySeeking Funding,                  |
      |      75%      | Customer Wants It-Funding Identified-Awaiting Authorization, |
      |     100%      | Customer has Provided Document Numbers or Confirmed Purchase |

  Scenario: [Customer-29] Verify that selecting "Remember me", user should able to see security page after closing an application.
    Given User is on BOH FPU homepage
    When User enters username as "harish.ekal@spurqlabs.com"
    And User enters password as "Test123!BOH"
    And User taps on "Remember me" option
    And User taps on "Sign in" option
    And User close the application & re-open it
    Then User verifies "Welcome back" is displayed on page

  Scenario: [Customer-30] Verify User can sort customers in descending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User navigated to "Customer Management" page
    And User taps on "Upside arrow" option
    Then User verifies "customer list" is displayed in descending order

  Scenario: [Customer-31] Verify User can sort customers in ascending order
    Given User is on BOH FPU homepage
    When User login with username "harish.ekal@spurqlabs.com" and password "Test123!BOH"
    And User navigated to "Customer Management" page
    And User taps on "downside arrow" option
    Then User verifies "customer list" is displayed in ascending order