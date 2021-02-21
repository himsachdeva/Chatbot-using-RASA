## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search
    - action_validate_price
    - action_search_restaurants
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

##     
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart


## location, cuisine and price specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "more than 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "more than 700"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## complete path where send mail denied
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "more than 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "more than 700"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
### Invalid parameter stories
## interactive_story_1 
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mirzapur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mirzapur"}
    - action_validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
    
## interactive_story_1   
* greet
    - utter_greet
* restaurant_search{"location": "wasseypur"}
    - slot{"location": "wasseypur"}
    - action_validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "wasseypur"}
    - slot{"location": "wasseypur"}
    - action_validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Invalid Cuisine
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - action_validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "moroccan", "location": "Mumbai"}
    - slot{"cuisine": "moroccan"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - action_validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - action_validate_cuisine
    - slot{"csn_avl": "0"}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
    
#### Invalid price
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Kochi", "price": "200 to 600"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kochi"}
    - slot{"price": "200 to 600"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - action_validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - action_validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "less than 300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - action_validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
## interactive_story_1  
* greet
    - utter_greet
* restaurant_search{"cuisine": "egyptian"}
    - slot{"cuisine": "egyptian"}
    - action_validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "more than 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart    


## interactive_story_1
* restaurant_search{"location": " Chennai"}
    - slot{"location": " Chennai"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than 300"}
    - slot{"price": "Less than 300"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": " Chennai"}
    - slot{"cuisine": "American"}
    - slot{"price": "Less than 300"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "trichur"}
    - slot{"location": "trichur"}
    - action_validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* restaurant_search{"location": "vellure", "cuisine": "chinese"}
    - slot{"location": "vellure"}
    - slot{"cuisine": "chinese"}
    - action_validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* restaurant_search{"cuisine": "chinese", "location": " Mumbai"}
    - slot{"location": " Mumbai"}
    - slot{"cuisine": "chinese"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than 300"}
    - slot{"price": "Less than 300"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": " Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Less than 300"}
    - utter_ask_sendmail
* email
    - action_get_mail
    - slot{"emailid": "123"}
    - action_validate_emailid
    - slot{"email_avl": "0"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": " Ahmedabad"}
    - slot{"location": " Ahmedabad"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"cuisine": "4"}
    - slot{"cuisine": "4"}
    - action_validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "5"}
    - slot{"price": "5"}
    - action_validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "Less than 300"}
    - slot{"price": "Less than 300"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": " Ahmedabad"}
    - slot{"cuisine": "American"}
    - slot{"price": "Less than 300"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - action_get_mail
    - slot{"emailid": "dhanwantichoudhary@gmail.com"}
    - action_validate_emailid
    - slot{"email_avl": "1"}
    - action_send_mail
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Thrissur"}
    - slot{"location": "Thrissur"}
    - action_validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "to 700"}
    - slot{"price": "to 700"}
    - action_validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "to 700"}
    - slot{"price": "to 700"}
    - action_validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Thrissur"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
