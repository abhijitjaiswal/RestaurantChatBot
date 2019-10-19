## Generated Story 7607686653584715151
* greet
    - utter_greet
* information{"place": "bangalore"}
    - slot{"place": "bangalore"}
    - utter_cuisine
* information{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_budget
* information{"budget": "less than 300"}
    - slot{"budget": "less than 300"}
    - action_restaurant
    - slot{"place": "bangalore"}
    - utter_email
* yes
    - utter_type_email
    - utter_type_email
* yes{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - utter_goodbye
    - export

## Generated Story 5563148809421920207
* greet
    - utter_greet
* information{"place": "pune"}
    - slot{"place": "pune"}
    - utter_cuisine
* information{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_budget
* information{"budget": "300 to 700"}
    - slot{"budget": "300 to 700"}
    - action_restaurant
    - slot{"place": "pune"}
    - utter_email
* no
    - utter_goodbye
    - export

